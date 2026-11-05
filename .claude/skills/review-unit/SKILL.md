---
name: review-unit
description: Independent review of a teaching unit (chapter, slides, seminar) against CLAUDE.md, in a fresh context. Reports findings and edits nothing.
argument-hint: "LNN [SNN ...]"
disable-model-invocation: true
context: fork
background: false
---

Review the teaching unit **$ARGUMENTS** in this repository as an independent reviewer. **Do not edit any files and do not commit.** Your output is a report.

You start with no conversation history. Invoke the `quarto-authoring` skill, then read `CLAUDE.md` in full. It defines the audience, the notation, the book mechanics and the writing rules you are checking against.

Files: `book/lectures/LNN-*.qmd`, `slides/LNN-*.qmd`, and the seminars `book/seminars/SNN-*.qmd` that `admin/course-plan.md` links to this lecture.

Build first: `make book`, `make print`, `make labels L=<lecture stem>`, `make snapshot L=<lecture stem>`.

Check, in this order:

1. **Mathematics.** Recompute every numeric result in the chapter, the slides and the solutions (use Python). Check definitions and theorem statements for correctness and for missing conditions (independence, finite Ω, equally likely outcomes, …).
2. **Consistency.**
   - Slide tags (`[Def 1.3]{.tag}`) against the `make labels` output.
   - Slide content against the chapter: no slide says something the chapter doesn't, and every chapter example appears in the slides.
   - Notation is the same everywhere (CLAUDE.md, "Math").
   - Seminar `@` references resolve, with no "?@" in the HTML.
3. **Leaks.**
   - No `::: lecturer` text in `book/_output/book/`.
   - No unreleased `::: sol` text in the student HTML or in `book/_output/book/pdf/`.
   - No exam content anywhere.
4. **Slides visually.** Look at every contact sheet in `slides/_output/snap/<stem>/`. Report overflow, near-empty slides, unreadable figures, raw LaTeX, and runs of same-shaped slides.
5. **Audience fit.** Is it clear for non-native-English business students? Flag jargon that isn't defined, steps that are skipped, and examples that aren't business-like.
6. **Writing style.** Run `make lint`, then read for the tells that lint can't catch (CLAUDE.md, "Writing style"): uniform rhythm, recap paragraphs, rule-of-three lists, sentences that only tell the reader what something meant, generic examples.
7. **Size and coverage.** The print PDF should be 8–12 pages per lecture day, with 35–55 slides (at least half with a visual) and 6–9 seminar problems. Every numbered item and example of the chapter should be on a slide. Only long proofs and long algebra may be cut.

Report findings ranked by severity: wrong mathematics and leaks first, then inconsistencies, then visual problems, then style. Give each finding as `file:line`, what is wrong, and a suggested fix. End with a one-line verdict: ready to merge, or not yet.
