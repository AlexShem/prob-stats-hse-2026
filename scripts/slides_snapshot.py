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

subprocess.run([
    chrome, "--headless", "--disable-gpu", "--no-sandbox", "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=20000", "--no-pdf-header-footer", f"--print-to-pdf={pdf}",
    f"file://{html.resolve()}?print-pdf",
], check=True, capture_output=True, timeout=180)

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
