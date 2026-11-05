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
- **Branch:** if `git branch --show-current` is `main`, create `unit/$0-slides` (`git switch -c unit/$0-slides`) and work there. Otherwise it should be `unit/$0-…`.
- **Existing deck:** if `slides/$0-*.qmd` already exists, rebuild it from scratch unless the instructions say "update" (git keeps the old version). With "update", diff the chapter against the deck, then redo only the slides whose chapter content changed and keep the rest.
- **Chapter:** `book/lectures/$0-*.qmd` exists and has no uncommitted changes (`git status --short book/lectures`). The chapter is final: you do not edit it. If you find an error in the chapter, list it in your report.

## 1. Read

- The whole chapter `book/lectures/$0-<slug>.qmd`.
- `make book`, then `make labels L=$0-<slug>`. This prints the chapter's numbers (Definition 1.3, Example 1.2, Figure 1.1, …). Use these numbers in the slide tags and never guess them.
- `templates/slides.qmd`: the pattern deck. Render it once to see the look: `cp templates/slides.qmd slides/L99-pattern.qmd && make snapshot L=L99-pattern`, then look at the sheet image and delete `slides/L99-pattern.qmd` afterwards.

## 2. What these slides are for

The deck is **the chapter, retold visually**. Students study from it, and many will open the slides before the book. Alexander may project them in class.

- **Keep the main content of the chapter**: every definition, theorem, worked example, key explanation and warning about a common mistake. Keep the chapter's order and its numbers.
- **Format it so it is pleasant to look at**: boxed definitions and results, two-column layouts that pair text with a picture, highlighted answers, step-by-step reveals, and generous spacing. Write short sentences, never a pasted paragraph.
- **Add visualizations** wherever a picture helps more than words: Venn diagrams, tree diagrams, sample-space grids, number lines and intervals, bar charts of a distribution, a shaded area under a density, a table that builds up row by row. You may draw new figures that the chapter doesn't have, as long as they only illustrate what the chapter says (no new facts, numbers or examples).
- **Cut only the most cumbersome parts**:
  - Long proofs become the statement plus one line of idea and "Proof: see the book, Section N.k".
  - Long algebra becomes its 2–3 key steps.
  - Side remarks become a footnote or are dropped.
  - Lecturer cues go into speaker notes.
  Everything else stays.

## 3. Plan first (write the plan as an HTML comment at the top of the deck)

Go through the chapter section by section. Write one line per slide: `NN | title | pattern | chapter item | visual`. Patterns:

- **hook**: the opening business case, with a figure or a striking number.
- **item**: a definition or theorem in a `.box-def` / `.box-thm` box, plus how to read or use it. Where possible, a small visual goes next to it in a column.
- **explain**: the chapter's explanation of why something works or how to think about it, as 2–4 short formatted sentences, ideally next to a diagram.
- **worked**: a worked example shown step by step with `. . .` pauses, ending in an `.answer`. Use 2–4 steps per slide. If it needs more, continue on a second slide ("… (cont.)").
- **picture**: a figure, diagram or table that carries the idea, with at most two sentences.
- **compare**: two columns, e.g. permutations against combinations, or with against without replacement.
- **pitfall**: a common mistake from the chapter, showing wrong against right.
- **your turn**: a short question for the room (`## Your turn {.yourturn}`), with the answer after a pause. Use 3–5 per deck, from the chapter's exercises or simple variants.
- **break**: exactly one, at the chapter's break cue.

Budget: 35–55 slides for a lecture day. **At least half of the slides have a visual** (figure, diagram, table, or a boxed result next to a picture). Before writing, check the plan against the chapter: every numbered item and every example is in it. List what you are cutting and why. The list should be short.

## 4. Slide rules

- **Each slide holds one complete idea, 30–90 words.** Don't write stubs (a title plus two bullets) and don't write walls of text. A mostly empty slide gets merged with its neighbour or given a visual. An overflowing slide gets split.
- **Visual hierarchy:** the title, then the key statement (boxed or large), then the supporting text, then a small `.muted` note if needed. Use **bold** for the term being defined and `.answer` for results. Use the theme classes (`.box-def`, `.box-thm`, `.box-ex`, `.answer`, `.muted`, `.small`, `{.yourturn}`) instead of ad-hoc styling.
- **Layout:** use columns whenever there is a picture (text on the left, about 45–55%; figure on the right). Vary the layouts. Don't put four text-only slides in a row.
- **Titles** say what the slide shows: "Complement rule", "At least one defective box". The chapter number goes in a tag after the title: `## Complement rule [Thm 1.2]{.tag}`.
- No `#` section-divider slides, except for at most one slide marking the second half after the break.
- **Show the working.** Worked examples go step by step with pauses, not just a table of answers. Students can't see the board in the PDF.
- **Math:** display formulas for anything that matters, inline only for short symbols. Use the course macros (`\Prob`, `\E`, `\Var` …).
- **Figures:**
  - Reuse the chapter's figure code (same seed, same data), resized for the slide.
  - New illustrative figures are welcome, made with matplotlib in a hidden code cell (code is hidden on slides by default).
  - In two-column layouts use `fig-width: 5`, `fig-height: 3.6`. Full width is about `fig-width: 9`, `fig-height: 4.6`.
  - Label the axes in words and keep fonts large enough to read on the snapshot.
  - Use the theme colours: blue `#1f5c99` / light `#9bb8d6` for the main data, orange `#b4542a` to highlight.
- **Bullets** only for real lists. Prefer short sentences that flow from one to the next.
- **Speaker notes** (`::: {.notes}`) carry the chapter's `::: lecturer` cues that matter when projecting.
- **Writing style:** everything in CLAUDE.md applies. No "Key takeaways", no "Summary" slide, no rhetorical Q&A, no emoji, and roughly one em dash in the whole deck.

## 5. Build, look, fix (repeat until clean, at most 4 rounds)

1. `make snapshot L=$0-<slug>`. It prints the page/slide counts and the sheet images.
2. **Look at every sheet image** (Read the PNGs). For any slide in doubt, open the single page `slides/_output/snap/<stem>/p-NN.png`. Check for:
   - content cut off at the bottom, or an extra page (the script warns)
   - slides more than about half empty
   - figures that are too small, or labels you can't read
   - formulas that didn't render (raw `\Prob`)
   - two slides in a row with the same shape, or four text-only slides in a row
   - fewer than half the slides with a visual
   - a column layout where one column is much longer than the other
3. Fix the issues and run the snapshot again.

## 6. Finish

- `make book` (the chapter must now show "Slides (PDF)" links) and `make lint`.
- Commit: `$0: slides`.
- Report back:
  - slide count and pages
  - the plan table
  - what was cut from the chapter and why
  - what you fixed during the visual rounds
  - problems you found in the chapter (don't fix them)
  - anything left for Alexander
