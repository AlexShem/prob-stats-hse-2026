---
name: chapter
description: Prepare a new lecture chapter (book/lectures/LNN-*.qmd) or make a substantial change to one, and carry the change through to slides and seminars. Use when Aleksandr asks to write, prepare or rework a lecture.
argument-hint: "LNN [notes, outline or the change to make]"
allowed-tools: Bash(git branch *) Bash(git status *) Bash(ls *)
---

Lecture **$0**. Aleksandr's instructions: $ARGUMENTS

Repo state at invocation:
- Branch: !`git branch --show-current`
- Uncommitted changes: !`git status --short`
- Existing files: !`ls book/lectures book/seminars slides`

You are the main session and you coordinate. Delegate the work to the project agents in `.claude/agents/`. Their models are set in their files, so don't override them. Follow CLAUDE.md, "Routing".

**New chapter** (no `book/lectures/$0-*.qmd` yet):
1. Spawn **source-scout**: "Brief for lecture $0: plan row, source material, reusable examples, what earlier chapters define."
2. From the brief and `admin/course-plan.md`, draft an outline: sections, the opening business case, each definition, theorem and example with a one-line purpose, figures, and the break point. **Show it to Aleksandr and wait for his OK.** Skip this only if he gave an outline.
3. Spawn **chapter-writer** with the approved outline and the scout's brief.
4. Spawn **math-checker** (the chapter) and **build-checker** in parallel. If math-checker finds errors, send them back to chapter-writer (SendMessage to the same agent) and check again.
5. Report: page count, numbered items, open TODOs, and the next step (`/slides $0` once Aleksandr has read the print copy `book/_output/lecturer/$0-*.pdf`).

**Revision** (the chapter exists):
1. If the change is substantial (a new section, a restructure, several new items), show Aleksandr a short plan of the change first. For a single addition (a notation, a remark, an example), go straight on.
2. Spawn **chapter-writer** with the change.
3. **Propagate:**
   - If its report lists slide impact or renumbering and `slides/$0-*.qmd` exists, spawn **slide-designer** in update mode. Pass on the slide-impact list, the renumbering and Aleksandr's wording.
   - If seminars cite renumbered or changed items (`grep -l '@<label>' book/seminars/`), spawn **seminar-writer** to bring them in line.
4. Spawn **math-checker** on the changed files and **build-checker**, in parallel.
5. Report what changed where (chapter, slides by number, seminars), the branch, and that it is ready to merge when Aleksandr agrees.
