---
name: review-unit
description: Full independent review of a teaching unit (lecture chapter, slides, seminars) before it is merged. Use when Aleksandr asks whether a unit is ready, or before merging a unit branch.
argument-hint: "LNN [SNN ...]"
allowed-tools: Bash(git branch *) Bash(git status *) Bash(ls *)
---

Review the unit **$ARGUMENTS**. Branch: !`git branch --show-current`. Files: !`ls book/lectures book/seminars slides`

You are the main session. Spawn these three agents **in parallel** (one message, three Agent calls). Each gets the lecture and seminar stems:
- **math-checker**: the chapter, the deck and the seminar sheet(s).
- **unit-reviewer**: coverage, consistency, slide visuals, audience fit, style.
- **build-checker**: builds, lint, overflow, leaks, references, sizes.

When all three are back, merge their findings into one list. Remove duplicates and rank them:
1. wrong mathematics and leaks
2. consistency and coverage
3. visual
4. style

Each finding gets a file, line or slide number, and a suggested fix. Number the findings, so Aleksandr can answer "fix 1–5". End with a verdict: ready to merge, or not yet.

When Aleksandr says which to fix, route each finding to the agent that owns the file (CLAUDE.md, "Routing"). Then run math-checker and build-checker once more.
