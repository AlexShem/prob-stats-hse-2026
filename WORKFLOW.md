# Workflow: preparing a week of teaching

This is a quick reference for Alexander. The rules the agents follow are in `CLAUDE.md`. The commands themselves are in `.claude/skills/`.

A *unit* is one lecture and the seminar(s) after it (see `admin/course-plan.md` for which seminar goes with which lecture). Each unit is made in stages, and you look at each stage before starting the next.

## The weekly cycle

| # | You type (in Claude Code, in this repo) | What happens | What you do |
|---|---|---|---|
| 1 | `/chapter L02` | Proposes an outline (sections, opening case, definitions, examples, break point). | Approve it or change it. |
| 2 | *(continues)* | Writes `book/lectures/L02-….qmd` on the branch `unit/L02-…`, builds, commits, reports the page count. | Read `book/_output/lecturer/L02-*.pdf` and ask for fixes in plain words. |
| 3 | `/slides L02` | A fresh agent builds the deck from the approved chapter, renders every slide to an image, fixes layout problems and commits. | Look at `slides/_output/L02-*.pdf`. |
| 4 | `/seminar S02` | Proposes 6–9 problems with type and timing. After your OK, it writes problems and solutions with Python checks and verifies every answer. | Approve the list, then read `book/_output/lecturer/S02-*.pdf`. |
| 5 | `/review-unit L02 S02` | A fresh agent checks everything read-only: maths, leaks, numbering, slides, style. | Decide which findings to fix ("fix findings 1–4"). |
| 6 | "merge the L02 unit into main" | Merges the branch and rebuilds. | Publish (see below). |
| 7 | after all three groups had the seminar: "release S02 solutions" | Adds S02 to `solutions-released` and rebuilds. | Publish again. |

You can add a few words after any command, for example `/chapter L03 start from the insurance example, skip geometric probability` or `/seminar S04 include one problem on the Poisson approximation`.

## Changing things later

- **Slides, after feedback:** `/slides L02 update: slide 12 is too dense, add a tree diagram for Example 2.3`. Only the affected slides are redone.
- **Chapter changed after the slides were made:** edit the chapter (or ask for it), then run `/slides L02 update to the revised chapter`.
- **Start the slides over:** `/slides L02`. Without "update", the agent rebuilds from scratch, and git keeps the old version.
- **A mistake in material that is already published:** "fix the typo in L02 Example 2.4". The agent uses a `fix/…` branch and merges after you check.

## Building and publishing

| Command | Gives you |
|---|---|
| `make book` | The student site in `book/_output/book/`: HTML, the full PDF, a PDF of each chapter, and slides in HTML and PDF. **This folder is what you publish.** |
| `make print` | Your print copies, one PDF per lecture and seminar with board cues and all solutions, in `book/_output/lecturer/`. |
| `make snapshot L=L02-<slug>` | One deck as a PDF plus contact-sheet images in `slides/_output/snap/`. |
| `make lint` | A quick check for AI-sounding wording. |
| `make schedule` | Refreshes the schedule after you drop a new RUZ `.xls` into `admin/raw/`. |

After publishing, tag the version students saw: `git tag pub/2026-11-21` (then `git push --tags`).

## Branches (the agents handle them, this is just so you know)

- `main` always builds and is what you publish.
- `unit/LNN-…` holds one week's lecture, slides and seminar, and is merged when you're happy.
- `fix/…` is for corrections to merged material, `infra/…` for tooling, and `exam/midterm` / `exam/final` for exams (which are never published).
- Agents never push, never merge without your OK, and never commit straight to `main`. The exceptions are releasing solutions and refreshing the schedule, when you ask.

## Exams

There's no command for exams. Ask in plain words, for example "draft the midterm on L1–L7, 90 minutes, two variants". The agent works on `exam/midterm` in `assessment/`. Then `make assessment` builds the papers and `make assessment-keys` the marking keys. None of this goes into the book.

## If something looks wrong

- **The commands don't show up after `/`:** start a new Claude Code session in the repo. Commands load when a session starts.
- **An agent is on the wrong branch, or two agents share the checkout:** stop one of them. For tooling work, ask for a separate worktree (see CLAUDE.md, "Git workflow").
- **Slides look cramped or empty:** `/slides LNN update: …` with the slide numbers from the PDF.
- **A solution shows up for students too early:** check `solutions-released` in `book/_quarto.yml`, then `make book`.
