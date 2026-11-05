---
name: seminar
description: Prepare a new seminar sheet (book/seminars/SNN-*.qmd) or rework one. Use when Alexander asks to write, prepare or change a seminar, its problems or solutions.
argument-hint: "SNN [notes or the change to make]"
allowed-tools: Bash(git branch *) Bash(git status *) Bash(ls *)
---

Seminar **$0**. Alexander's instructions: $ARGUMENTS

Repo state at invocation:
- Branch: !`git branch --show-current`
- Uncommitted changes: !`git status --short`
- Existing files: !`ls book/lectures book/seminars`

You are the main session and you coordinate through the agents in `.claude/agents/`. Their models are set in their files. Follow CLAUDE.md, "Routing".

**New seminar:**
1. Spawn **source-scout**: "Brief for seminar $0: which lecture(s) it follows, the plan row, reusable problems with lines, known errors."
2. Draft the problem list: 6–9 problems for 80 minutes, each with a one-line gist, type and estimated minutes, from easy to hard, with mixed types. **Show it to Alexander and wait for his OK.**
3. Spawn **seminar-writer** with the approved list and the brief.
4. Spawn **math-checker** (the sheet) and **build-checker** in parallel. Send any errors back to seminar-writer and check again.
5. Report the problems with their answers, the print PDF (`book/_output/lecturer/$0-*.pdf`), and a reminder to release the solutions after all three groups have had the seminar.

**Revision:** spawn **seminar-writer** with the change, then **math-checker** on the sheet and **build-checker**. Report what changed.
