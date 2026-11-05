# Run from the repo root. Everything goes through `uv run` so Quarto finds the project's Python.
Q = uv run quarto render
BOOK_OUT = book/_output/book

.PHONY: all book print slides assessment assessment-keys schedule lint clean

all: book print

# Student book: HTML site + full PDF + per-chapter PDFs + slides, all in book/_output/book/ (publish this folder)
book: slides
	$(Q) book
	uv run python scripts/split_book_pdf.py $(BOOK_OUT)/*.pdf $(BOOK_OUT)/pdf
	rm -rf $(BOOK_OUT)/slides && mkdir -p $(BOOK_OUT)/slides && cp -r slides/_output/. $(BOOK_OUT)/slides/

# Lecturer print copy: board cues + all solutions, one PDF per chapter → book/_output/lecturer/
print:
	$(Q) book --profile lecturer --to pdf
	uv run python scripts/split_book_pdf.py book/_output/lecturer/*.pdf book/_output/lecturer

slides:
	$(Q) slides

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
