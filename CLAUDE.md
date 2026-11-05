# CLAUDE.md

Course materials for **Probability Theory and Mathematical Statistics** (RUZ: «Теория вероятностей и математическая статистика (анг)»), HSE University, Higher School of Business, International Business programme, 2nd year bachelor, taught in English, Nov 2026 – Mar 2027 (modules 2–3). Lecturer and seminar teacher for all three groups: Alexander Shemendyuk.

Alexander's how-to for the stage commands: `WORKFLOW.md`. Keep it in sync when commands change. Facts, grading and policies: `admin/course-info.md`. Dates and rooms: `admin/schedule.md`. Topic for each lecture and seminar: `admin/course-plan.md`.

## Required skills

- **`quarto-authoring`**: invoke it with the Skill tool before creating or editing any `.qmd` file, `_quarto.yml`, profile or Lua filter. This is not optional. If you spawn a subagent that will touch Quarto files, say in its prompt: "Before editing any Quarto file, invoke the `quarto-authoring` skill."
- **Project commands** (`.claude/skills/`): `/chapter`, `/slides`, `/seminar`, `/review-unit`. These are the stages of a teaching unit, and Alexander triggers each one (see "Making a teaching unit"). Don't run a later stage on your own initiative.
- **`anti-ai`**: the user invokes this skill by name and agents should not load it on their own. Its rules for this course are written out below under "Writing style", and they apply to every piece of text.

## Audience and scope

- Business students, not mathematicians. Practice-oriented: every concept arrives with a business situation (pricing, demand, inventory, insurance, credit risk, quality control, A/B tests, surveys, HR, marketing funnels).
- Most are not native English speakers. Write in plain English, keep the vocabulary simple and the terminology consistent.
- It is a paid ("premium") programme, so the materials have to look carefully made: consistent notation, no typos in formulas, figures with labelled axes.
- It is a classic university course: probability in module 2, statistics including regression in module 3. There is no programming or software-tools layer.
- Python only appears at the end of seminar solutions, to show how the problem is solved numerically. We don't teach Python. Students should be able to read the code, run it and change a number.
- No quizzes for now.

## What students get

**One Quarto book holds everything.** A student opens the published site and finds:

- **Lectures** part: one chapter per lecture day (`book/lectures/LNN-*.qmd`). Chapter number = lecture number.
- **Seminars** part: one unnumbered chapter per seminar (`book/seminars/SNN-*.qmd`), with problems and, once released, solutions with a Python check.
- **Appendix**: the schedule (generated from RUZ).
- Under every lecture and seminar title, a download line: **PDF** of that chapter, plus **Slides** (reveal.js) and **Slides PDF** for lectures. The filter adds it automatically, so don't write it by hand.
- A download icon for the PDF of the whole book.

Alexander also gets a **print copy** (`make print`): the same chapters with board cues and *all* solutions, A4, 12 pt and a 5.5 cm right margin for handwriting, one PDF per lecture or seminar. He teaches at the whiteboard from it. Each lecture day is 2 × 80 minutes.

## Layout

```
book/                Quarto BOOK project, the published site
  _quarto.yml        chapters list, `solutions-released`, formats
  _quarto-lecturer.yml   profile for the print copy (lecturer-copy: true)
  index.qmd          front page ("About this book")
  lectures/LNN-<slug>.qmd
  seminars/SNN-<slug>.qmd
  schedule.qmd       includes _schedule-tables.md (generated, don't edit)
slides/              reveal.js project, slides/LNN-<slug>.qmd, same stem as the lecture
assessment/          midterm/, exam/: separate PRIVATE project, never published
_shared/             _macros.qmd + preamble.tex (math), _setup.qmd (plot style), course.lua
                     (filter), book.css, slides.scss, data/
templates/           lecture.qmd, seminar.qmd, slides.qmd (a pattern deck), exam.qmd. Copy these, don't render them in place
admin/               course facts, plan, generated schedule; raw RUZ exports in admin/raw/
sources/             inherited materials (read-only input, see "Working with sources")
scripts/             schedule_from_xls.py, split_book_pdf.py, style_check.py,
                     slides_snapshot.py (deck → PDF + PNG contact sheets), chapter_labels.py
.claude/skills/      project commands: chapter, slides, seminar, review-unit
```

There is no root `_quarto.yml`. Don't add one. Each project writes to `<project>/_output/` (gitignored). Keep `output-dir` inside the project, because Quarto misbehaves when it points outside. Slides cannot live inside the book project, since Quarto renders them next to their source. That's why they are a separate project, and `make book` copies them in.

## Build

Run everything from the repo root through `make`, which calls `uv run quarto …` so Quarto finds the project's Python.

```
make book             # student site → book/_output/book/ (HTML, full PDF, pdf/LNN-*.pdf, pdf/SNN-*.pdf, slides/)
make print            # lecturer copy → book/_output/lecturer/LNN-*.pdf, SNN-*.pdf
make slides           # slides only (make book already runs this)
make snapshot L=<stem>   # one deck → slides/_output/<stem>.pdf + PNG contact sheets in slides/_output/snap/<stem>/
make labels L=<stem>     # numbers of definitions/theorems/examples/figures in a rendered chapter
make assessment       # private papers → assessment/_output/papers
make assessment-keys  # with marking keys → assessment/_output/solutions
make lint             # style tripwire (see "Writing style")
make schedule         # regenerate admin/schedule.md + book/_schedule-tables.md from the newest admin/raw/*.xls
uv run quarto preview book   # live preview while writing (no per-chapter PDFs or slides in preview)
```

- `quarto render book` on its own gives the HTML and the full PDF but not the per-chapter PDFs or the slides. Use `make book` for anything you'll publish.
- The per-chapter PDFs come from splitting the book PDF at its bookmarks (`scripts/split_book_pdf.py`). That's why the numbering and cross-references in a chapter PDF match the book. The split matches each bookmark to the `# ` title line of the `.qmd` file, so keep that title on a single line. The script warns if a chapter isn't found.
- `execute: freeze: auto`: code only re-runs when its file changes. Commit `_freeze/`. After changing `_shared/_setup.qmd`, delete the `_freeze/` folders.
- Python packages: `uv add <pkg>` (`--dev` for build-only tools). Never `pip install`. Student-facing code may only use numpy, scipy, pandas, matplotlib and statsmodels.

## Book mechanics (`_shared/course.lua`)

| Write | Student book | Print copy |
|---|---|---|
| `::: lecturer` … `:::` | removed | shown as a "Board" box |
| `::: sol` … `:::` (in seminars) | shown only if the seminar is in `solutions-released` | always shown |
| `::: proof` … `:::` | inline, "Proof." and an end square | same |
| `::: proof-fold` … `:::` | closed "Proof" dropdown in HTML; in PDF printed in full, with the end square | printed in full |

- **Releasing solutions:** after a seminar has run for all three groups, add its prefix to `book/_quarto.yml` (`solutions-released: [S01, S02]`), then `make book`. Until then the chapter says "Solutions appear here after the seminar."
- Use `sol` and not `solution`, which is a built-in Quarto class that bypasses the filter and would leak the solution. Don't put solutions in any other kind of block.
- The download line and the "solutions appear" note only appear for files named `LNN-*.qmd` / `SNN-*.qmd`.
- After any change to a seminar, check the student output: `grep` a phrase from a solution in `book/_output/book/seminars/SNN-*.html` and in `pdf/SNN-*.pdf` (via `pdftotext`). It must not be there unless the seminar is released.

## Git workflow

Material is prepared one teaching unit at a time, a few days before it is taught, so we use **one short-lived branch per unit** off `main`.

- **`main`** always builds (`make book` and `make print` pass) and is what gets published. Nothing half-written lands there.
- **Unit branch** `unit/LNN-<slug>`, e.g. `unit/L01-probability-basics`. It holds lecture N's chapter, its slides and the seminar(s) that follow it in `admin/course-plan.md` (for example L04 with S04 and S05). One branch is one week of teaching, and it is reviewed and merged as a whole.
- **Seminar-only work** (a seminar prepared separately from its lecture, or reworked later): `unit/SNN-<slug>`.
- **Fixes to material already merged** (a typo in L02 found during L03 week): `fix/<what>`, e.g. `fix/L02-bayes-example`. Keep these off unit branches, so a fix can go out without waiting for the next unit.
- **Infrastructure** (filter, templates, Makefile, CLAUDE.md, scripts): `infra/<what>`.
- **Assessment**: `exam/midterm`, `exam/final`. The repo is private, but still never merge exam content into `book/` or `slides/`.
- **One-line operational changes** go straight to `main` as single commits, and only when Alexander asks: releasing solutions (`solutions-released`), a schedule refresh (`make schedule`). Commit message, for example: `Release S01 solutions`.

Rules for agents:

1. Before editing, check the branch (`git branch --show-current`). If you are on `main`, create the right branch with `git switch -c unit/...`. **Never rename `main`** (`git branch -m`). Don't start a new unit on top of an unmerged one: branch from `main`.
1a. Another agent may be working in the same checkout. For infrastructure work, use a separate worktree (`git worktree add ../prob-stats-hse-2026-infra -b infra/<what> main`) instead of switching branches under it.
2. Commit in small steps with the unit as the prefix: `L01: first draft of chapter`, `L01: slides`, `S01: problems 1–6`, `S01: solutions`, `infra: split script handles appendices`. Don't commit `_output/`. Do commit `_freeze/`.
3. Merge only after `/review-unit` has no open findings for mathematics, leaks or consistency, **and** Alexander has looked at the unit. Merge with `git merge --no-ff unit/...` so the unit stays one visible block in the history, then delete the branch.
4. Don't push, merge into `main` or delete branches unless Alexander asks. He reviews the branch first.
5. After publishing, tag what students saw: `git tag pub/2026-11-07`. That makes "which version did they have before the midterm?" easy to answer.

## Making a teaching unit

A unit is one lecture and the seminar(s) after it. It is made in **stages, in this order**, and Alexander reviews each stage before the next one starts. The book chapter comes first and is finished before anything is derived from it.

| Stage | Command | Runs | Output |
|---|---|---|---|
| 1. Chapter | `/chapter LNN` | in the session, with an outline to approve first | `book/lectures/LNN-*.qmd` |
| — | Alexander reads the print copy, edits, approves | | commit |
| 2. Slides | `/slides LNN` | fresh subagent; reads only the committed chapter | `slides/LNN-*.qmd`, visually checked |
| 3. Seminar | `/seminar SNN` | in the session, with a problem list to approve first | `book/seminars/SNN-*.qmd` |
| 4. Review | `/review-unit LNN SNN` | fresh subagent, read-only | findings report |
| — | fixes, then merge (`git merge --no-ff`) | | `main` |

Why the stages are separate: slides written in the same pass as the chapter turn into a thin outline of it. Making the slides as their own task, from a finished chapter and with every slide looked at as an image, gives a deck students can study from.

If the chapter changes after the slides exist, rerun `/slides LNN` with "update to the revised chapter". It will compare the chapter with the deck and redo the slides that changed.

The full instructions for each stage are in `.claude/skills/<stage>/SKILL.md`. The essentials:

### The lecture chapter is the master

- Write content and fix mistakes in the chapter first. The slides and seminar follow it.
- Complete enough for a student who missed the lecture: definitions, results, every worked example in full and the figures. Every theorem has a proof. Proofs of important results (those that teach a method or that later chapters lean on) go in `::: proof`, always visible. Proofs of lesser results go in `::: proof-fold`, a dropdown in HTML. Keep each proof short, and give the idea when the full argument is long.
- About 8–12 pages in the print copy per lecture day. That fits 160 minutes at the board with examples worked live.
- Number everything that will be referred to: `#def-`, `#thm-`, `#exm-`, `#fig-`, `#eq-`, `{#sec-}`. Seminars cite them with `@thm-…`, and the reference resolves across the book.
- `::: lecturer` cues are for the board layout, timing, the question to ask the room, when to show a slide, and the break (once per lecture day, after the first 80 minutes). Keep them short, because they are notes to self.

### Slides

- The chapter retold visually. Students study from it, and Alexander may project it.
- It keeps the chapter's main content (every definition, theorem, example, key explanation and common mistake) in well-formatted text: boxes, columns, highlighted answers, step-by-step reveals.
- It adds visualizations wherever a picture helps: diagrams, trees, grids, plots, tables. New figures are fine if they only illustrate what the chapter says.
- It cuts only the most cumbersome parts. Long proofs become a statement plus one line of idea and a pointer to the book, and long algebra shrinks to its key steps.
- Built from the patterns in `templates/slides.qmd` (`.box-def`/`.box-thm`/`.box-ex`, `.answer`, `.muted`, `{.yourturn}`, columns) and the theme `_shared/slides.scss` (16:9, 1280×720).
- Chapter numbers go in a tag: `## Complement rule [Thm 1.2]{.tag}`. Get the numbers from `make labels`, never by guessing.
- 35–55 slides per lecture day, at least half of them with a visual. One `## Break` at the midpoint.
- Every deck is checked by eye: `make snapshot` and then the contact-sheet images. A deck isn't done until no slide overflows and no slide is half empty.
- The full instructions are in `.claude/skills/slides/SKILL.md`.

### Seminars

- File names follow the S-numbers in `admin/schedule.md`. All three groups get the same sheet.
- Problems are `## Problem N {.unnumbered}`, numbered by hand. About 6–9 problems per 80-minute seminar, from easy to hard.
- Seminar files set `execute: echo: true` in their front matter (already in the template), so the Python is visible. Lecture chapters hide code by default and show only the figures.

## Conventions

### Math

- Use the macros `\E`, `\Var`, `\Cov`, `\Corr`, `\Prob`, `\R`. They are defined twice, in `_shared/_macros.qmd` (HTML/MathJax) and in `_shared/preamble.tex` (PDF). A new macro goes into both files.
- Notation is fixed for the whole course: CDF $F(x)=\Prob(X\le x)$, $\Phi$ the standard normal CDF, $\binom{n}{k}$, $X, Y$ random variables, $x$ values, $\mu, \sigma^2$ population, $\bar x, s^2$ sample, $\hat\theta$ estimators, $\alpha$ significance level, $H_0/H_1$. Ask before introducing an alternative.
- Include paths: chapters in `book/lectures/` and `book/seminars/` use `../../_shared/`, and slides use `../_shared/`.

### Python in seminar solutions

- Each solution is worked by hand first. The Python cell comes after it, as a check or a simulation, never as a replacement.
- Code has to run as-is when pasted into Colab or Jupyter: imports in the cell and no course helpers. The hidden `_setup.qmd` only styles the plots, and nothing may depend on it.
- Short cells (≤15 lines) with one idea each. Use variable names from the problem (`p_default`, `n_customers`), not `x1`, `tmp`.
- Seed the randomness: `rng = np.random.default_rng(2026)`.
- Print results the way a person would state them, e.g. `print(f"P(X > 3) = {p:.3f}")`, never a bare `np.float64(0.16596)`.
- Prefer `scipy.stats` distribution objects (`stats.binom(n, p).pmf(k)`) to hand-coded formulas.
- Data files go in `_shared/data/` with a line in `_shared/data/README.md` (source, licence, what the columns mean). Never invent "real" data. Either cite a real source or label the data as simulated.

### Confidentiality

- Midterm and exam content lives only in `assessment/` (its own project with a `solutions` profile for marking keys). It must never appear in `book/` or `slides/`, or in anything published. Keep the repository private.
- Exams use `::: {.content-visible when-profile="solutions"}` for keys. The `sol`/`lecturer` filter is only active in the book.

## Writing style (anti-AI rules)

The materials must read as written by this lecturer, not generated. These rules come from the anti-AI skill (reader mode). They target human readers. They do not promise anything about AI detectors. Run `make lint` before calling a document done. It catches the mechanical tells, and the rest has to be checked by reading.

**Voice**
- One recognisable voice: a lecturer talking to students. First person is fine ("I like this example because…", "we will need this in Lecture 6"). Contractions are fine in chapters and slides and not in exams.
- Commit to a view. "The normal approximation is bad here, n = 12 is too small" beats "it may be important to consider whether the approximation is appropriate". At most one hedge per page.
- Let some friction show. Say where students usually go wrong, where a method is annoying, which textbook formula you don't like and why.
- If Alexander gives his own wording or a rough draft, keep his sentences verbatim, including any oddities. Add material between them instead of rewriting them. Tell him which parts are new.

**Structure**
- No preview openers ("In this lecture we will…") and no recap closers ("In summary…", "Key takeaways"). Start a chapter with a concrete case, a number or a question students would ask. End on the last useful point or on an exercise.
- No fractal summaries. Say each thing once, in the place where it does the most work.
- Vary sentence and paragraph length on purpose: some very short sentences, a few long ones, and paragraphs of uneven size. Chapters are prose. Bullets are for lists of discrete items, not for arguments.
- Avoid the intro → three points → conclusion template, for sections and for slides alike. Don't group things in threes by reflex. Two or four is fine.
- Callout boxes (other than `lecturer`/`sol`) only when they matter: no more than about two per chapter, and never a "Key takeaway" box.

**Sentences**
- Banned constructions: "It's not X, it's Y" / "not just X but Y"; rhetorical Q&A ("The result? …"); "serves as", "stands as" (say "is"); participial tails ("…, highlighting the importance of…"); vague authority ("studies show", "experts agree"), so name the source or cut it; false suspense ("here's the kicker"); grand claims ("a pivotal concept that revolutionized…").
- Banned words (the lint list): delve, leverage, utilize, harness, foster, facilitate, streamline, showcase, unlock, empower, optimize (outside the math sense), crucial, pivotal, robust (outside "robust estimator"), seamless, comprehensive (in clusters), landscape, realm, tapestry, journey, myriad, plethora, testament, furthermore, moreover, "it is worth noting", "plays a key role", "when it comes to", "let's dive into". Use the plain word: use, show, help, important, many, also.
- Soft adverbs such as genuinely, truly, quietly, basically or actually (as a pivot): at most one per page.

**Formatting**
- Em dashes: about one per page at most. Use a comma, a colon, parentheses or a full stop.
- No bold-first bullets ("**Variance:** …"), no emoji, no decorative arrows. Headings in sentence case and specific ("Why the sample mean wobbles", not "Understanding Sampling Distributions: A Comprehensive Overview").
- Bold is for a term the first time it is defined, nothing else.

**Examples and exercises**
- Specific beats generic: "a Moscow coffee chain sells 340 cups a day on average", not "a company sells products". Use rubles, local places and a mix of Russian and international names (Ilya, Zarina, Kemal, Priya, Oksana, not Emily and Sarah every time). Don't invent real-world statistics. If a number is made up, it belongs to an obviously hypothetical firm.
- Vary how problems are framed. Not every problem should start "A company…". Mix in short drills, one long case, a "find the mistake in this solution" item, and a question with a one-word answer.
- Real stories are a bit untidy. One irrelevant-but-true detail is better than an example that serves the point too perfectly.

**Never leave in:** "Certainly!", "I hope this helps", "Great question", placeholder text other than explicit `[TODO: …]`, or any sentence that tells the reader what the previous sentence meant.

## Working with sources

`sources/` holds the old materials Alexander builds on. Use them for coverage and problem ideas, but rewrite in this course's notation and voice instead of copying their wording. When adapting a problem, change the context and the numbers and note the origin in a comment: `<!-- adapted from sources/xxx.md, task 3.14 -->`. Keep `sources/README.md` up to date.

- `Модули_1_2_новые.md` (4,700 lines): read `sources/Модули_1_2_новые.summary.md` first, then only the line ranges you need. It uses ξ, M (mean), D (variance), $F(x)=P(\xi<x)$ and $C_n^k$. Convert these to our notation. Its contexts are ML/IT (servers, classifiers, hashes), so recast them as business situations. It has known answer-key errors, which are listed in the summary.

## Open items

- Module 3 timetable (Jan–Mar 2027) is missing. Add it with `make schedule` when it arrives.
- Grading formula and ECTS: TODO in `admin/course-info.md` and in the table on `book/index.qmd`.
- Midterm date: S10 or a separate session in the week of 21–27 Dec, not confirmed.
- Where the book is published (HSE LMS, GitHub Pages, Quarto Pub): not decided. Publish the folder `book/_output/book/`.
- The welcome text in `book/index.qmd` is for Alexander to write.
