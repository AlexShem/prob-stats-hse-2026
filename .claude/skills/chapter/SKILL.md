---
name: chapter
description: Stage 1 of a teaching unit. Write or revise the lecture chapter book/lectures/LNN-<slug>.qmd (the master copy). Does not touch slides or seminars.
argument-hint: "LNN [notes or outline]"
disable-model-invocation: true
---

Write the lecture chapter for **$0** (stage 1 of the unit workflow in CLAUDE.md). Extra instructions from Alexander, if any: $ARGUMENTS

1. Invoke the `quarto-authoring` skill before editing any Quarto file.
2. Git: `git branch --show-current`. You should be on `unit/$0-<slug>`. If you're on `main`, run `git switch -c unit/$0-<slug>`. Never rename `main`. If another unit branch is checked out with uncommitted work, stop and ask.
3. Read: CLAUDE.md (all of it, especially "Writing style"), the $0 row in `admin/course-plan.md`, and the referenced line ranges of `sources/` via `sources/Модули_1_2_новые.summary.md`. If the chapter already exists, read it and the earlier chapters' last sections, so you don't repeat them and the notation carries through.
4. Before writing, show Alexander a short outline: sections, the opening case, each definition, theorem and example with its one-line purpose, figures, and the break point. Wait for his OK or changes. Skip this only if he gave an outline in the arguments.
5. Write `book/lectures/$0-<slug>.qmd` from `templates/lecture.qmd` and list it in `book/_quarto.yml`. Follow CLAUDE.md, "The lecture chapter is the master". Write prose, label every numbered item, add `::: lecturer` cues, and work every example in full.
6. Build and check: `make book`, `make print`, `make lint`. The print PDF `book/_output/lecturer/$0-*.pdf` should be 8–12 pages. No `lecturer` text may appear in `book/_output/book/`. Read the print PDF text once (`pdftotext`) and fix anything that reads badly or renders wrong.
7. Commit (`$0: chapter …`). **Do not write slides or the seminar.** They come after Alexander approves the chapter, via `/slides $0` and `/seminar SNN`.
8. Report: page count, the list of numbered items (`make labels L=<stem>`), open `[TODO: …]`s, and anything you were unsure about.
