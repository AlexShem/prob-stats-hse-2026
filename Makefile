# Run from the repo root. Everything goes through `uv run` so Quarto finds the project's Python.
Q = uv run quarto render
BOOK_OUT = book/_output/book

.PHONY: all book print slides snapshot labels assessment assessment-keys schedule lint clean

all: book print

# Student book: HTML site + full PDF + per-chapter PDFs + slides (HTML and PDF), all in
# book/_output/book/ (publish this folder)
book: slides
	$(Q) book
	uv run python scripts/split_book_pdf.py $(BOOK_OUT)/*.pdf $(BOOK_OUT)/pdf
	for f in slides/L*.qmd; do [ -e "$$f" ] && uv run python scripts/slides_snapshot.py "$$f" --no-render --pdf-only; done; true
	rm -rf $(BOOK_OUT)/slides && mkdir -p $(BOOK_OUT)/slides && cp -r slides/_output/. $(BOOK_OUT)/slides/ && rm -rf $(BOOK_OUT)/slides/snap

# Lecturer print copy: board cues + all solutions, one PDF per chapter → book/_output/lecturer/
print:
	$(Q) book --profile lecturer --to pdf
	uv run python scripts/split_book_pdf.py book/_output/lecturer/*.pdf book/_output/lecturer

slides:
	$(Q) slides

# Render one deck, export PDF and contact sheets for checking it by eye: make snapshot L=L01-probability-basics
snapshot:
	uv run python scripts/slides_snapshot.py $(L)

# Numbers of definitions/theorems/examples/figures in a rendered chapter: make labels L=L01-probability-basics
labels:
	uv run python scripts/chapter_labels.py $(L)

# Midterm/exam (private, never published) → assessment/_output/{papers,solutions}
assessment:       ; $(Q) assessment
assessment-keys:  ; $(Q) assessment --profile solutions

# Regenerate admin/schedule.md and book/_schedule-tables.md from the newest admin/raw/*.xls
schedule:
	uv run --with xlrd python -W ignore scripts/schedule_from_xls.py $(if $(XLS),"$(XLS)")

# Style tripwire for AI-sounding wording (see CLAUDE.md)
lint:
	uv run python scripts/style_check.py

clean:
	rm -rf book/_output slides/_output assessment/_output
