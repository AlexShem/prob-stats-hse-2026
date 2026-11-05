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

Files: `book/lectures/L02-conditional-probability.qmd` (12 print pages), `slides/L02-conditional-probability.qmd` (50 slides + title). S02 not yet written.
Status: chapter drafted on `unit/L02-conditional-probability`, under review.

**Chapter.** Opens with the L01 store: $\Prob(\text{promo}\mid\text{app})=0.20/0.55\approx0.36$, not $0.40$.

| Section | Items |
|---|---|
| 2.1 Conditional probability | Def 2.1; Fig 2.1 reduced sample space (conditioning panels); Ex 2.1 promo given app, $\Prob(A\mid B)\ne\Prob(B\mid A)$; Thm 2.1 $\Prob(\cdot\mid B)$ satisfies the axioms (proof-fold) |
| 2.2 Multiplication rule | Thm 2.2 with chain rule (Eq 2.1); Ex 2.2 birthdays as a chain (team of 10, 0.883, ties to S01 Problem 9); Ex 2.3 two faulty bulbs out of 12, tree (Fig 2.2), checked by counting |
| 2.3 Independence | Def 2.2; Thm 2.3 complements; Def 2.3 mutual independence (pairwise is not enough, counterexample); Ex 2.4 gambler's fallacy, six tosses and the loan-officer version. **Break after this section.** |
| 2.4 Total probability | Thm 2.4 (Eq 2.2), uses the partition from L01 Def 1.3; Ex 2.5 two phone-case factories (0.024); Ex 2.6 funnel by segment, overall rate 5.6% to 7.1% only because the mix changed |
| 2.5 Bayes | Thm 2.5 (Eq 2.3); Ex 2.7 which factory made the defective case (0.75); Ex 2.8 fraud alerts, 100,000 payments, 0.2% fraud, 1% false alarms (198 / 2 / 998 / 98,802), Table 2.1; prior and posterior; prosecutor's fallacy |

Ends with 5 exercises and the pointer to Seminar 2.

**Facts later units can use.** Notation $\Prob(A\mid B)$, no new macros. Terms introduced: conditional probability, probability tree, independent, mutually independent, gambler's fallacy, prior, posterior. Contexts used: phone-case factories, customer funnel with segments (new, returning, referred), fraud alerts, loan officer, team birthdays. Real cases named: Gigerenzer's tests of doctors, Sally Clark (prosecutor's fallacy). Mistakes named: swapping $\Prob(A\mid B)$ and $\Prob(B\mid A)$; $\Prob(A\mid B^c)\ne1-\Prob(A\mid B)$; independent taken as mutually exclusive; pairwise taken as mutual independence; the gambler's fallacy and its mirror; a change in mix read as a change in rates. Open thread: the chapter points to Bayes for "one firm rejected five times", which no section works out, so S02 can pick it up.

**Slides.** 50 slides, 44 with a visual. Break at slide 31, after the loan-officer slide that closes Sec 2.3. Reuses Fig 2.1 (conditioning panels), Fig 2.2 (bulb tree) and Table 2.1. New pictures: the B-rescaled-to-1 bar (Def 2.1), the red-die-shows-6 grid, the 66-pair grid checking Ex 2.3, the unit-square area picture for Def 2.2 and Thm 2.3, all 64 six-toss sequences with runs marked, sequence strips for Ex 2.4, a partition picture for Thm 2.4, a 1000-case grid for Ex 2.5, width = share mosaics for Ex 2.6, prior/posterior bars for Ex 2.7 and Ex 2.8. A shared `tree()` helper in the hidden first cell draws every probability tree (Ex 2.3, Ex 2.5, Ex 2.8, Exercise 4). Pitfall slides: swapping $\Prob(A\mid B)$ and $\Prob(B\mid A)$; complement behind the bar; independent vs mutually exclusive (with Exercise 3 as a quick check); pairwise vs mutual independence; mix moved, not the rates; "99% accurate" with the prosecutor's fallacy and Sally Clark. Your turn: Exercises 1, 2, 4, 5 and the "write six random tosses" room activity. Lecturer cues are in speaker notes.

**Seminar.** Not yet written.

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
