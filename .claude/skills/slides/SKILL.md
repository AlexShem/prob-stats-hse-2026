---
name: slides
description: Build or update the reveal.js deck for a lecture (slides/LNN-*.qmd) from its chapter, with visual checks. Use for a new deck, a full rebuild, or any change to existing slides.
argument-hint: "LNN [update: what to change]"
context: fork
agent: slide-designer
background: false
allowed-tools: Bash(git branch *) Bash(git status *) Bash(ls *)
---

Lecture: **$0**. Instructions from Aleksandr: $ARGUMENTS

Repo state at invocation:
- Branch: !`git branch --show-current`
- Uncommitted changes: !`git status --short`
- Decks and chapters: !`ls slides book/lectures`

Mode:
- **update** if the instructions contain "update" or name specific slides, figures or changes. Change only what they ask for, plus anything that follows from it (tags, numbering, neighbouring slides that would now be unbalanced).
- **update (chapter sync)** if the instructions say the chapter changed. Diff the chapter since the deck's last commit and redo the affected slides.
- **build** otherwise: a new deck, or a rebuild from scratch if one exists.

Follow your agent instructions: branch, numbers, rules, visual rounds, commit, report.
