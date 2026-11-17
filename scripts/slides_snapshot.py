"""Render a slide deck, export it to PDF and make PNG contact sheets for visual checking.

Usage: uv run python scripts/slides_snapshot.py L01-probability-basics [--no-render] [--pdf-only]
       make snapshot L=L01-probability-basics

Writes
  slides/_output/<stem>.pdf                     one page per slide (fragments collapsed)
  slides/_output/snap/<stem>/p-NN.png           each page, readable size
  slides/_output/snap/<stem>/sheet-N.png        3x3 contact sheets with page numbers
and prints a warning when the PDF has more pages than the deck has slides
(a slide that overflows spills onto an extra page).
"""
import glob
import re
import shutil
import subprocess
import sys
from pathlib import Path

stem = sys.argv[1].removesuffix(".qmd").split("/")[-1]
render = "--no-render" not in sys.argv
pdf_only = "--pdf-only" in sys.argv
deck = Path("slides") / f"{stem}.qmd"
html = Path("slides/_output") / f"{stem}.html"
pdf = Path("slides/_output") / f"{stem}.pdf"
snap = Path("slides/_output/snap") / stem

if render:
    subprocess.run(["uv", "run", "quarto", "render", str(deck)], check=True)

chrome = sorted(glob.glob(str(Path.home() / ".local/share/quarto/chrome-headless-shell/*/chrome-headless-shell")))
chrome = chrome[0] if chrome else shutil.which("chromium") or shutil.which("google-chrome")
if not chrome:
    sys.exit("No headless Chrome found. Run `quarto install chrome-headless-shell`.")

# The chalkboard plugin waits for a drawings file in print mode and never lets reveal lay the
# pages out (result: one blank page). Print from a copy of the deck without the plugin.
printable = html.with_name(f"{stem}.print.html")
src = html.read_text(encoding="utf-8")
src = re.sub(r'<script src="[^"]*reveal-chalkboard/plugin\.js"></script>', "", src)
src = src.replace("RevealChalkboard, ", "")
# Headless Chrome has no network access here, and then the formulas stay as raw TeX. Use a local
# copy of the MathJax version the deck loads (slides/_quarto.yml), fetched once with npm into ~/.cache.
MATHJAX_URL = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js"
mj_dir = Path.home() / ".cache/prob-stats-mathjax2"
mj = mj_dir / "package/MathJax.js"
if not mj.exists() and shutil.which("npm"):
    mj_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(["npm", "pack", "mathjax@2.7.9"], cwd=mj_dir, check=True, capture_output=True)
    subprocess.run("tar xzf mathjax-2.7.9.tgz", shell=True, cwd=mj_dir, check=True)
if MATHJAX_URL not in src:
    sys.exit(f"{html.name} does not load {MATHJAX_URL}. Update MATHJAX_URL to match slides/_quarto.yml.")
if mj.exists():
    src = src.replace(MATHJAX_URL, mj.as_uri())
# Source Sans 3 normally comes from Google Fonts. Without network the text falls back to a wider
# font, slides overflow and drop out of the PDF. Use a local copy through @font-face.
ss_dir = Path.home() / ".cache/prob-stats-fonts"
if not (ss_dir / "package/TTF").exists() and shutil.which("npm"):
    ss_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(["npm", "pack", "source-sans@3"], cwd=ss_dir, check=True, capture_output=True)
    subprocess.run("tar xzf source-sans-*.tgz", shell=True, cwd=ss_dir, check=True)
if (ss_dir / "package/TTF").exists():
    faces = "".join(
        f"@font-face{{font-family:'Source Sans 3';font-weight:{w};font-style:{st};"
        f"src:url('{(ss_dir / 'package/TTF' / f'SourceSans3-{f}.ttf').as_uri()}')}}"
        for f, w, st in [("Regular", 400, "normal"), ("It", 400, "italic"), ("Semibold", 600, "normal"), ("Bold", 700, "normal")])
    src = src.replace("</head>", f"<style>{faces}</style></head>", 1)
printable.write_text(src, encoding="utf-8")
subprocess.run(["node", "scripts/slides_to_pdf.mjs", chrome, f"file://{printable.resolve()}?print-pdf", str(pdf)],
               check=True, timeout=180)
printable.unlink()

if pdf_only:
    print(pdf)
    sys.exit(0)

shutil.rmtree(snap, ignore_errors=True)
snap.mkdir(parents=True)
subprocess.run(["pdftoppm", "-r", "72", "-png", str(pdf), str(snap / "p")], check=True)
pages = sorted(snap.glob("p-*.png"))

for i in range(0, len(pages), 9):
    chunk = pages[i:i + 9]
    subprocess.run(["montage", "-label", "%t", "-pointsize", "18", *map(str, chunk),
                    "-tile", "3x3", "-geometry", "+6+6", "-background", "#d0d4d8",
                    str(snap / f"sheet-{i // 9 + 1}.png")], check=True)

text = html.read_text(encoding="utf-8")
n_slides = len(re.findall(r'<section[^>]*class="[^"]*\bslide\b', text)) + text.count('id="title-slide"')
print(f"{pdf}: {len(pages)} pages, {n_slides} slides")
if len(pages) > n_slides:
    print(f"WARNING: {len(pages) - n_slides} extra page(s). Some slide overflows; look at the sheets.")
for s in sorted(snap.glob("sheet-*.png")):
    print(s)
