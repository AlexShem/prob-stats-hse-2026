---
name: seminar
description: Stage 3 of a teaching unit. Write the seminar sheet book/seminars/SNN-<slug>.qmd (problems + solutions with Python checks) for an approved lecture chapter.
argument-hint: "SNN [notes]"
disable-model-invocation: true
---

Write seminar **$0** (stage 3 of the unit workflow in CLAUDE.md). Extra instructions from Alexander, if any: $ARGUMENTS

1. Invoke the `quarto-authoring` skill before editing any Quarto file.
2. Git: if the lecture this seminar follows is still on its unit branch (`admin/course-plan.md` maps seminars to lectures), work there. If you're on `main` (the lecture is already merged), create `unit/$0-<slug>` with `git switch -c`. Never commit to `main`.
3. Read CLAUDE.md, the seminar's row in `admin/course-plan.md`, the lecture chapter(s) it covers (they are final, so cite their numbered items with `@def-…`, `@thm-…`, `@exm-…`), and the reusable problems listed in `sources/Модули_1_2_новые.summary.md`.
4. Propose the problem list to Alexander first: about 6–9 problems for 80 minutes, each with a one-line gist, its type and an estimated time. Mix the types (a quick drill, standard problems, one longer business case, one "find the mistake", one with a one-word answer). Order them from easy to hard. Wait for his OK.
5. Write from `templates/seminar.qmd`. Every solution goes in `::: sol`. Work it by hand first, then add a short Python check (see CLAUDE.md, "Python in seminar solutions"). Recast problems adapted from `sources/` in a business context with new numbers, and note the origin in a comment.
6. Verify every numeric answer by running the Python cells, and check the by-hand result matches.
7. `make book`, `make print`, `make lint`. Check for leaks: a phrase from a solution must not appear in `book/_output/book/seminars/$0-*.html` or in `pdftotext book/_output/book/pdf/$0-*.pdf` (unless $0 is in `solutions-released`).
8. Commit (`$0: problems and solutions`) and report: the problem list with answers, the print PDF page count, and open TODOs.
