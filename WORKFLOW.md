# Workflow: preparing a week of teaching

This is a quick reference for Aleksandr. The rules the agents follow are in `CLAUDE.md` (see "Routing"). The agents are in `.claude/agents/`, and the commands in `.claude/skills/`.

## Just say what you want

Open a new Claude Code session in this repo and describe the task in plain words. The main session works out what kind of request it is, hands the work to the right agent (each with its own model), checks the result, and reports back:

| You say | Who does it |
|---|---|
| "prepare lecture 2" | source-scout (sonnet) gathers material, and you approve an outline. Then chapter-writer (opus) writes the chapter, and math-checker (sonnet) and build-checker (haiku) check it. |
| "add the notation $A\setminus B$ to lecture 1 and make sure the slides show it" | chapter-writer, then slide-designer (opus) updates the affected slides, seminar-writer adjusts seminars if needed, then the checks. |
| "slide 12 of lecture 1 is cramped, split it" | slide-designer, then build-checker. |
| "make the slides for lecture 2" | slide-designer builds the deck in a fresh session and looks at every slide as an image. |
| "prepare seminar 2" | source-scout, then you approve a problem list. Then seminar-writer (opus) writes it, and the checks run. |
| "check the numbers in seminar 1" | math-checker. |
| "is unit 2 ready?" | math-checker, unit-reviewer and build-checker in parallel, then one numbered list of findings. |
| "fix 1, 3 and 4" | each finding goes to the agent that owns the file, then the checks run again. |
| "typo in Example 1.3: 'recieve'" | the main session fixes it directly in the chapter and the slides, then runs build-checker. |
| "merge it" | merges the branch into `main` and rebuilds. |
| "release S02 solutions" | after all three groups have had the seminar. Students then see the solutions. |

Each request ends with a short report: what changed (files, slide numbers), which branch, and whether the builds pass. Nothing is merged or pushed until you say so.

## The weekly cycle, step by step

A *unit* is one lecture and the seminar(s) after it (`admin/course-plan.md` maps them). The commands are the same steps in explicit form. Use them when you want to be sure which step runs.

| # | Say, or type | What you do |
|---|---|---|
| 1 | "prepare lecture 2" or `/chapter L02` | Approve or change the outline. |
| 2 | *(continues)* | Read `book/_output/lecturer/L02-*.pdf` and ask for fixes in plain words. |
| 3 | "make the slides for lecture 2" or `/slides L02` | Look at `slides/_output/L02-*.pdf`. |
| 4 | "prepare seminar 2" or `/seminar S02` | Approve the problem list, then read `book/_output/lecturer/S02-*.pdf`. |
| 5 | "is unit 2 ready?" or `/review-unit L02 S02` | Pick the findings to fix ("fix 1–4"). |
| 6 | "merge it" | Publish (see below). |
| 7 | "release S02 solutions" | Publish again. |

You can add a few words to any of these, for example `/chapter L03 start from the insurance example, skip geometric probability`.

## Changing things later

- **Slides:** "lecture 2 slides: slide 12 too dense, add a tree diagram for Example 2.3". Only the affected slides are redone.
- **A lecture's content:** "add … to lecture 2". The slides and seminars that depend on it are updated in the same go.
- **Start the slides over:** "rebuild the lecture 2 slides from scratch". Git keeps the old version.
- **A mistake in published material:** just say it. The fix goes on a `fix/…` branch and is merged when you say so.

## The content tracker

`admin/content-tracker.md` is a short record of what each lecture, deck and seminar contains and how it is presented. The agents read it before a new unit and update it when they finish, so later units stay consistent with earlier ones. You can read or correct it at any time; it is plain text.

## Guardrails

These are hooks in `.claude/settings.json`, which apply to every agent:
- **No pushing.** You push yourself.
- **Never rename `main`.**
- **No commits straight to `main`**, except releasing solutions and refreshing the schedule.
- **`sources/` is read-only.**
- **A style check runs after every `.qmd` edit.**

To see the hooks, type `/hooks`.

## Building and publishing

| Command | Gives you |
|---|---|
| `make book` | The student site in `book/_output/book/`: HTML, the full PDF, a PDF of each chapter, and slides in HTML and PDF. **This folder is what you publish.** |
| `make print` | Your print copies, one PDF per lecture and seminar with board cues and all solutions, in `book/_output/lecturer/`. |
| `make snapshot L=L02-<slug>` | One deck as a PDF plus contact-sheet images in `slides/_output/snap/`. |
| `make check` | Checks that no board cue or unreleased solution reached the student files, that all references resolve, and that the page and slide counts are in range. |
| `make lint` | A quick check for AI-sounding wording. |
| `make schedule` | Refreshes the schedule after you drop a new RUZ `.xls` into `admin/raw/`. |

After publishing, tag the version students saw: `git tag pub/2026-11-21` (then `git push --tags`).

## Branches (the agents handle them, this is just so you know)

- `main` always builds and is what you publish.
- `unit/LNN-…` holds one week's lecture, slides and seminar, and is merged when you're happy.
- `fix/…` is for corrections to merged material, `infra/…` for tooling, and `exam/midterm` / `exam/final` / `exam/quiz-2-1` etc. for exams and quizzes (which are never published).
- Agents never push, never merge without your OK, and never commit straight to `main` (enforced by the hooks). The exceptions are releasing solutions and refreshing the schedule, when you ask.

## Exams

There's no command for exams. Ask in plain words, for example "draft the midterm on L1–L7, 90 minutes, two variants". The agent works on `exam/midterm` in `assessment/`. Then `make assessment` builds the papers and `make assessment-keys` the marking keys. Quizzes work the same way ("draft quiz 2-1 on L1–L2, 15 minutes, 5 multiple-choice questions"), in `assessment/quizzes/`, and you upload them to the LMS. None of this goes into the book.

## If something looks wrong

- **The commands or agents don't show up** (`/` menu, `/agents`): start a new Claude Code session in the repo. They load when a session starts.
- **A hook blocked something you do want** (e.g. a push): run it yourself with `! git push`.
- **An agent is on the wrong branch, or two agents share the checkout:** stop one of them. For tooling work, ask for a separate worktree (see CLAUDE.md, "Git workflow").
- **Slides look cramped or empty:** `/slides LNN update: …` with the slide numbers from the PDF.
- **A solution shows up for students too early:** check `solutions-released` in `book/_quarto.yml`, then `make book`.


**Slide PDFs.** They are printed by `scripts/slides_to_pdf.mjs` (needs `node` and `npm`). The first run downloads MathJax and the Source Sans font into `~/.cache/prob-stats-*`, so the PDF does not depend on the network. If a PDF ever comes out as one blank page, run `make snapshot L=<stem>` and read the message.
