"""Split a rendered book PDF into one PDF per lecture/seminar chapter.

Usage: uv run python scripts/split_book_pdf.py <book.pdf> <out_dir>
Matches PDF bookmarks to the `# ` titles of book/lectures/*.qmd and book/seminars/*.qmd
and writes <out_dir>/<stem>.pdf (e.g. L01-probability-basics.pdf). Called by `make book`
and `make print`.
"""
import re
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

src, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
out_dir.mkdir(parents=True, exist_ok=True)
reader = PdfReader(src)

titles = {}
for qmd in sorted(Path("book").glob("[ls]e*/[LS][0-9][0-9]*.qmd")):
    m = re.search(r"^# (.+?)\s*(\{.*\})?\s*$", qmd.read_text(encoding="utf-8"), re.M)
    if m:
        titles[m.group(1).strip()] = qmd.stem

# Parts, chapters and appendices: bookmark depth 0 and 1.
# A depth-0 item followed by a list of children is a part ("Lectures", "Seminars").
marks, part_pages = [], set()
outline = reader.outline
for i, item in enumerate(outline):
    if isinstance(item, list):
        marks += [(o.title, reader.get_destination_page_number(o)) for o in item if not isinstance(o, list)]
        continue
    page = reader.get_destination_page_number(item)
    marks.append((item.title, page))
    if i + 1 < len(outline) and isinstance(outline[i + 1], list):
        part_pages.add(page)
marks.sort(key=lambda t: t[1])
marks.append(("END", len(reader.pages)))

found = 0
for (title, a), (_, b) in zip(marks, marks[1:]):
    name = titles.get(re.sub(r"^[\dA-Z]+(\.\d+)*\s+", "", title).strip()) or titles.get(title.strip())
    if a in part_pages:  # unnumbered chapters get bookmarked on the part page before them
        a += 1
    if not name or b <= a:
        continue
    w = PdfWriter()
    for i in range(a, b):
        w.add_page(reader.pages[i])
    w.write(out_dir / f"{name}.pdf")
    found += 1
    print(f"{out_dir / name}.pdf  pages {a + 1}-{b}")
missing = set(titles.values()) - {p.stem for p in out_dir.glob("*.pdf")}
if missing:
    print("WARNING: no bookmark matched for", ", ".join(sorted(missing)))
