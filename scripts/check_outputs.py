"""Mechanical checks on the rendered book (run after `make book` and `make print`).

Usage: make check   (or: uv run python scripts/check_outputs.py)

Checks
  leaks     text from `::: lecturer` blocks must not reach the student HTML/PDF;
            text from `::: sol` blocks of unreleased seminars must not either
  refs      no unresolved cross-references (`?@`) in the student HTML
  sizes     lecturer print PDF per lecture 8–12 pages; decks 35–55 slides
Prints one PASS/FAIL/WARN line per check and exits 1 if anything FAILs.
"""
import re
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader

BOOK = Path("book/_output/book")
LECT = Path("book/_output/lecturer")
fails = 0


def report(status, msg):
    global fails
    fails += status == "FAIL"
    print(f"{status:4s}  {msg}")


def norm(text):
    return re.sub(r"\s+", " ", text).strip().lower()


def html_text(path):
    t = path.read_text(encoding="utf-8")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S)
    return norm(re.sub(r"<[^>]+>", " ", t).replace("&nbsp;", " "))


def pdf_text(path):
    r = subprocess.run(["pdftotext", str(path), "-"], capture_output=True, text=True)
    return norm(r.stdout)


def blocks(qmd, cls):
    """Text of each `::: cls` div (handles nested divs and code fences)."""
    out, cur, depth, target_depth, in_code = [], None, 0, None, False
    for line in qmd.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^\s*(:{3,})\s*(.*)$", line)
        if m:
            if m.group(2):  # opening fence
                depth += 1
                opener = m.group(2)
                if cur is None and re.match(rf"^(\{{\s*\.)?{cls}\b", opener):
                    cur, target_depth = [], depth
            else:  # closing fence
                if cur is not None and depth == target_depth:
                    out.append(" ".join(cur))
                    cur, target_depth = None, None
                depth -= 1
            continue
        if cur is not None:
            cur.append(line)
    return out


def phrases(text, k=3):
    """Up to k runs of 5 plain words (no math, markup or code) to search for."""
    text = re.sub(r"\$[^$]*\$|`[^`]*`|\[[^\]]*\]\{[^}]*\}|@\S+|[*_#>|]", " ", text)
    words = [w for w in re.findall(r"[A-Za-z][A-Za-z'’-]*", text)]
    runs = [" ".join(words[i:i + 5]) for i in range(0, max(len(words) - 4, 0), 7)]
    return [norm(r) for r in runs if len(r) > 20][:k]


def released():
    cfg = Path("book/_quarto.yml").read_text(encoding="utf-8")
    m = re.search(r"^solutions-released:\s*\[(.*?)\]", cfg, re.M)
    return {x.strip() for x in m.group(1).split(",") if x.strip()} if m else set()


if not BOOK.exists():
    sys.exit("book/_output/book missing: run `make book` first.")

# leaks: lecturer cues
for qmd in sorted(Path("book/lectures").glob("L[0-9][0-9]*.qmd")):
    outs = [p for p in (BOOK / "lectures" / f"{qmd.stem}.html", BOOK / "pdf" / f"{qmd.stem}.pdf") if p.exists()]
    texts = [html_text(p) if p.suffix == ".html" else pdf_text(p) for p in outs]
    leaked = [ph for b in blocks(qmd, "lecturer") for ph in phrases(b) if any(ph in t for t in texts)]
    report("FAIL" if leaked else "PASS", f"lecturer cues stay out of {qmd.stem}" + (f": found '{leaked[0]}'" if leaked else ""))

# leaks: unreleased solutions
rel = released()
for qmd in sorted(Path("book/seminars").glob("S[0-9][0-9]*.qmd")):
    outs = [p for p in (BOOK / "seminars" / f"{qmd.stem}.html", BOOK / "pdf" / f"{qmd.stem}.pdf") if p.exists()]
    if qmd.stem in rel or qmd.stem[:3] in rel:
        # Released: the solutions must be in every student output, the PDF included.
        # Lenient on purpose (PDF line breaks split some phrases): one phrase found is enough.
        sol_phrases = [ph for b in blocks(qmd, "sol") for ph in phrases(b)]
        missing = [p.name for p in outs if not any(ph in (html_text(p) if p.suffix == ".html" else pdf_text(p)) for ph in sol_phrases)]
        report("FAIL" if missing else "PASS", f"{qmd.stem} solutions released and shown" + (f": missing from {', '.join(missing)}" if missing else ""))
        continue
    texts = [html_text(p) if p.suffix == ".html" else pdf_text(p) for p in outs]
    sols = blocks(qmd, "sol")
    leaked = [ph for b in sols for ph in phrases(b) if any(ph in t for t in texts)]
    if not sols:
        report("WARN", f"{qmd.stem}: no `::: sol` blocks found")
    else:
        report("FAIL" if leaked else "PASS", f"{qmd.stem} solutions hidden ({len(sols)} blocks)" + (f": found '{leaked[0]}'" if leaked else ""))

# unresolved references
bad = [str(p) for p in BOOK.rglob("*.html") if "slides" not in p.parts and "?@" in p.read_text(encoding="utf-8")]
report("FAIL" if bad else "PASS", "cross-references resolve" + (f": ?@ in {', '.join(bad)}" if bad else ""))

# sizes
for pdf in sorted(LECT.glob("L[0-9][0-9]*.pdf")):
    n = len(PdfReader(pdf).pages)
    report("PASS" if 8 <= n <= 12 else "WARN", f"{pdf.stem} print copy {n} pages (target 8–12)")
for html in sorted(Path("slides/_output").glob("L[0-9][0-9]*.html")):
    t = html.read_text(encoding="utf-8")
    n = len(re.findall(r'<section[^>]*class="[^"]*\bslide\b', t)) + t.count('id="title-slide"')
    report("PASS" if 35 <= n <= 55 else "WARN", f"{html.stem} deck {n} slides (target 35–55)")

print("ALL PASS" if not fails else f"{fails} FAIL")
sys.exit(1 if fails else 0)
