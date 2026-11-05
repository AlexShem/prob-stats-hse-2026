# Probability Theory and Mathematical Statistics, HSE 2026/27

Course materials for the 2nd-year International Business programme at the HSE Higher School of
Business (lecturer: Alexander Shemendyuk). Everything students see is one Quarto book (lectures and
seminars), with a PDF of each chapter and reveal.js slides for each lecture linked from it.

## Setup

Install [Quarto](https://quarto.org) (≥ 1.9), [uv](https://docs.astral.sh/uv/) and a TeX distribution with xelatex, then run `uv sync`.

## Build

| Command | Output |
|---|---|
| `make book` | `book/_output/book/`: the site to publish (HTML, full PDF, `pdf/` per chapter, `slides/`) |
| `make print` | `book/_output/lecturer/`: lecturer print copy, one PDF per lecture/seminar, with board cues and all solutions |
| `make assessment`, `make assessment-keys` | midterm and exam papers and marking keys (private) |
| `make schedule` | refresh the schedule from the RUZ export in `admin/raw/` |
| `make lint` | style check for AI-sounding wording |

`make snapshot L=<deck>` renders one slide deck to PDF and PNG contact sheets for checking it by eye.

Each teaching unit is made in stages with the project commands in Claude Code: `/chapter L02` → review →
`/slides L02` → `/seminar S02` → `/review-unit L02 S02` → merge. See "Making a teaching unit" in CLAUDE.md.

`uv run quarto preview book` gives a live preview while writing. How the pieces fit together, the
conventions and the writing rules are in [CLAUDE.md](CLAUDE.md).
