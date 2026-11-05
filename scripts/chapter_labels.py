"""List the numbered items of a rendered chapter: label, number and title.

Usage: uv run python scripts/chapter_labels.py L01-probability-basics
       make labels L=L01-probability-basics
Reads book/_output/book/lectures/<stem>.html (run `make book` first). The slides use these
numbers in their tags, e.g. `## Complement rule [Thm 1.2]{.tag}`.
"""
import html
import re
import sys
from pathlib import Path

stem = sys.argv[1].removesuffix(".qmd").split("/")[-1]
page = Path("book/_output/book/lectures") / f"{stem}.html"
if not page.exists():
    sys.exit(f"{page} not found. Run `make book` first.")
text = page.read_text(encoding="utf-8")

rows = []
for m in re.finditer(r'<div id="((?:def|thm|lem|cor|prp|exm|exr)-[^"]+)"[^>]*>\s*<p><span class="theorem-title"><strong>(.*?)</strong>', text, re.S):
    rows.append((m.start(), m.group(1), m.group(2)))
for m in re.finditer(r'id="((?:fig|tbl)-[^"]+?)-caption-[^"]*">\s*(.*?)</figcaption>', text, re.S):
    cap = re.sub(r"<[^>]+>", "", m.group(2))
    rows.append((m.start(), m.group(1), cap.split(":")[0] + ": " + ":".join(cap.split(":")[1:])[:70].strip()))
for m in re.finditer(r'<h([23])[^>]*data-number="([\d.]+)"[^>]*class="anchored"[^>]*>(?:<span class="header-section-number">[\d.]+</span>\s*)?(.*?)</h\1>', text, re.S):
    rows.append((m.start(), "sec", f"Section {m.group(2)} {re.sub(r'<[^>]+>', '', m.group(3)).strip()}"))

for _, label, title in sorted(rows):
    print(f"{label:28s} {html.unescape(title).replace(chr(160), ' ')}")
