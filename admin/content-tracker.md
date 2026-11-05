# Content tracker

What each lecture, deck and seminar actually contains and how it is presented. Writers read this **before** starting a new unit so the course stays consistent, and update their unit's entry **before** reporting done. It records what exists in the files, not what is planned: the plan is `course-plan.md`.

Keep entries short. Numbers (Def 1.4, Ex 1.7) are the book's numbers, taken from `make labels L=<stem>`. After a renumbering, fix them here.

## Course-wide conventions (as established so far)

**Notation.** Events $A, B, A^c$ (not $\bar A$); $\cap, \cup, \varnothing$; $\Omega$; $\Prob$, $\binom{n}{k}$. "Mutually exclusive" is the main term for events that cannot both happen. Keep it distinct from "independent".

**Recurring devices in chapters.**
- Open with one concrete business case, no "in this lecture" preview.
- Numbered boxes for definitions, theorems, examples. Examples are worked in full.
- A "common mistake" is named where it occurs and reused as the lesson in a lecturer cue.
- `::: lecturer` cues: timing in the first cue, a question for the room, what to draw on the board, one break at the midpoint.
- Chapter ends with `## Exercises {.unnumbered}`: 5 items, then one paragraph of answers, then a pointer to the seminar.

**Recurring devices in slides.** Opening hook slide, `[Def 1.2]{.tag}` chapter-number tags, "Your turn" slides, one `## Break` slide at the midpoint, a pitfall slide for each common mistake.

**Recurring devices in seminars.** Problems numbered by hand, easy to hard, solution by hand in `::: sol`, Python check at the end.

**Contexts and names already used** (vary them, do not repeat without a reason): Ilya's croissant stand at Paveletskaya, promo code and mobile app store, coffee/dessert café chain, discounted items and instalments, yoghurt and expired packs, Wi-Fi passwords and PINs, sales managers and analysts, robots on a grid, courier in a 2-hour window, two people meeting in a café, birthdays. Names: Ilya, Priya, Kemal.

## L01: Events, probability and counting

Files: `book/lectures/L01-probability-basics.qmd`, `slides/L01-probability-basics.qmd` (49 slides), `book/seminars/S01-counting.qmd` (10 problems).
Status: merged (PR #1, counting terminology). Permutation, arrangement and combination are separate definitions; the numbers below are the current ones.

**Chapter.** Opens with Ilya's croissants ("will he sell at least 25?"). Order of sections:

| Section | Items |
|---|---|
| 1.1 Experiments and outcomes | Def 1.1 experiment and sample space; Ex 1.1 four sample spaces |
| 1.2 Events and set operations | Def 1.2 event; Table 1.1 operations; Fig 1.1 Venn; Ex 1.2 promo code and app; Def 1.3 mutually exclusive, partition; Thm 1.1 De Morgan |
| 1.3 Axioms | Def 1.4 probability (three axioms); Thm 1.2 consequences (empty set, complement, monotonicity, union); Eq 1.1 inclusion-exclusion for three events; Ex 1.3 promo/app with numbers |
| 1.4 Classical probability | Def 1.5; Ex 1.4 two dice (Fig 1.2) |
| 1.5 Counting | Thm 1.3 product rule; Ex 1.5 PIN codes; Def 1.6 permutation; Def 1.7 arrangement ($k$ of $n$, ordered); Def 1.8 combination ($0\le k\le n$, $\binom nk$); Thm 1.4 orderings and selections; Eq 1.2 binomial coefficient; Ex 1.6 6-from-45 lottery; Ex 1.7 expired packs |
| 1.6 Geometric probability | Def 1.9; Ex 1.8 courier; Ex 1.9 meeting in a café (Fig 1.3) |

**Facts L02 and later can use.** The promo/app store: $\Prob(\text{promo})=0.40$, $\Prob(\text{app})=0.55$, both $0.20$ (Ex 1.3). A partition $H_1,\dots,H_n$ is defined in Def 1.3, and the text promises its use in the law of total probability (Lecture 2). The complement rule is presented as the tool for "at least one" questions. Probability zero is not the same as impossible (geometric probability).

**Counting vocabulary.** Permutation = ordering of all $n$; arrangement = ordered selection of $k$ from $n$ (also called $k$-permutation or variation, $A_n^k$); combination = unordered selection, $\binom nk$ (also $C_n^k$). The chapter warns that English books use "arrangement" loosely. Test used throughout: swap two chosen items, is it a different outcome?

**Slides.** Break after classical probability. Tags give chapter numbers. Pitfall slides: forgetting the overlap, too coarse an $\Omega$, "at least one is 1 minus none", unequal sums of two dice.

**Seminar S01.** Problems on events, counting, classical and geometric probability. Problem 9 is birthdays (leads into products of conditional probabilities). Problem 10 is a meeting problem that uses "independently" informally, so L02 defines independence formally.

## L02: Conditional probability and Bayes' theorem

Status: in preparation on `unit/L02-conditional-probability`. Planned outline only; the writer replaces this entry with what the chapter actually contains.

Planned: opening with the L01 store ($\Prob(\text{promo}\mid\text{app})$); conditional probability, multiplication rule with a tree, independence (gambler's fallacy), total probability, Bayes. Break after independence.

## Template for a new entry

```
## LNN: <title>
Files: chapter, deck (slide count), seminar (problem count).
Status: branch / merged.
**Chapter.** Opening case. Table of sections and numbered items.
**Facts later units can use.** Numbers, examples, definitions that the next lectures will build on, and promises made to later lectures.
**Slides.** Break position, notable patterns, pitfall slides.
**Seminar.** Problems by theme, anything that depends on or anticipates other units.
```
