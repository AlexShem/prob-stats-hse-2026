---
name: slides
description: Stage 2 of a teaching unit. Build the reveal.js deck slides/LNN-<slug>.qmd from the finished, committed lecture chapter, in a fresh context, and check every slide visually.
argument-hint: "LNN [extra instructions]"
disable-model-invocation: true
context: fork
background: false
---

You are making the reveal.js slides for lecture **$0** of the course in this repository. Extra instructions from Alexander, if any: $ARGUMENTS

You start with no conversation history. Everything you need is in this repo and below.

## 0. Preconditions (stop and report if any fails)

- Invoke the `quarto-authoring` skill first.
- Read `CLAUDE.md` in full. The "Writing style" rules apply to slides too.
- `git branch --show-current` is `unit/$0-…`, and `book/lectures/$0-*.qmd` exists and has no uncommitted changes (`git status --short book/lectures`). The chapter is final: you do not edit it. If you find an error in the chapter, list it in your report.

## 1. Read

- The whole chapter `book/lectures/$0-<slug>.qmd`.
- `make book`, then `make labels L=$0-<slug>`. This prints the chapter's numbers (Definition 1.3, Example 1.2, Figure 1.1, …). Use these numbers in the slide tags and never guess them.
- `templates/slides.qmd`: the pattern deck. Render it once to see the look: `cp templates/slides.qmd slides/L99-pattern.qmd && make snapshot L=L99-pattern`, then look at the sheet image and delete `slides/L99-pattern.qmd` afterwards.

## 2. What these slides are for

Students get the slides as a study aid next to the book, and Alexander may project them in class. A student flipping through the PDF the night before the seminar should be able to follow the lecture from the slides alone. The slides don't replace the chapter, but each one should be complete enough to read on its own.

## 3. Plan first (write the plan as an HTML comment at the top of the deck)

One line per slide: `NN | title | pattern | chapter item`. Patterns:

- **hook**: the opening business case, with a figure or a number.
- **item**: a definition or theorem in a `.box-def` / `.box-thm` box, plus one or two lines on how to use it.
- **worked**: a worked example, shown step by step with `. . .` pauses and ending in an `.answer`. Use 2–4 steps. If it needs more, split it over two slides ("… (cont.)").
- **picture**: a figure or table, with at most one sentence.
- **compare**: two columns (`:::: {.columns}`), e.g. permutations against combinations.
- **your turn**: a short question for the room (`## Your turn {.yourturn}`), with the answer after a pause. Use 2–4 per deck, taken from the chapter's exercises or simple variants.
- **break**: exactly one, at the midpoint (the chapter's break cue).

Budget: 28–40 slides for a lecture day. At least a third of the slides should have a figure, table, diagram or boxed result. Every chapter example appears, either as a full **worked** slide or, if it's minor, merged into another slide.

## 4. Slide rules

- **Content per slide: one complete idea, 25–70 words.** That's not a stub ("Event (Def 1.2)" + two bullets) and not a wall of text. If a slide would be mostly empty, merge it with its neighbour. If it overflows, split it.
- Titles say what the slide shows: "Complement rule", "At least one defective box". The chapter number goes in a tag after the title: `## Complement rule [Thm 1.2]{.tag}`.
- No `#` section-divider slides, except for at most one slide marking the second half after the break.
- Show the working: worked examples go step by step with pauses, not just a table of answers. Students can't see the board in the PDF.
- Math: display formulas for anything that matters, inline only for short symbols. Use the course macros (`\Prob`, `\E`, `\Var` …).
- Figures: reuse the chapter's figure code (same seed, same data), resized for the slide. In two-column layouts use `fig-width: 5`, `fig-height: 3.6`. Full width is about `fig-width: 9`, `fig-height: 4.6`. Label the axes in words. A figure shown in a column must fit next to its text, so check this in the snapshot.
- Bullets only for real lists. Prefer short sentences that flow from one to the next.
- Speaker notes (`::: {.notes}`) carry the board cues from the chapter's `::: lecturer` blocks that matter when projecting.
- Writing style: everything in CLAUDE.md applies. No "Key takeaways", no "Summary" slide, no rhetorical Q&A, no emoji, and roughly one em dash in the whole deck.

## 5. Build, look, fix (repeat until clean, at most 4 rounds)

1. `make snapshot L=$0-<slug>`. It prints the page/slide counts and the sheet images.
2. **Look at every sheet image** (Read the PNGs). For any slide in doubt, open the single page `slides/_output/snap/<stem>/p-NN.png`. Check for:
   - content cut off at the bottom, or an extra page (the script warns)
   - slides more than about half empty
   - figures that are too small, or labels you can't read
   - formulas that didn't render (raw `\Prob`)
   - two slides in a row with the same shape
   - a column layout where one column is much longer than the other
3. Fix the issues and run the snapshot again.

## 6. Finish

- `make book` (the chapter must now show "Slides (PDF)" links) and `make lint`.
- Commit: `$0: slides`.
- Report back:
  - slide count and pages
  - the plan table
  - what you fixed during the visual rounds
  - problems you found in the chapter (don't fix them)
  - anything left for Alexander
