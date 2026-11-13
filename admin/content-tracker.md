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

**Contexts and names already used** (vary them, do not repeat without a reason): Ilya's croissant stand at Paveletskaya, promo code and mobile app store, coffee/dessert café chain, discounted items and instalments, yoghurt and expired packs, Wi-Fi passwords and PINs, sales managers and analysts, robots on a grid, courier in a 2-hour window, two people meeting in a café, birthdays; S01 also uses sushi-bar suppliers, a bank app and salary card, supermarket cashiers, a demo day, a student club, a bakery window, an office shuttle, a loading dock, an ice-cream kiosk. Names: Ilya, Priya, Kemal, Rustam, Lena, Anvar, Sofia.

## L01: Events, probability and counting

Files: `book/lectures/L01-probability-basics.qmd`, `slides/L01-probability-basics.qmd` (49 slides), `book/seminars/S01-counting.qmd` (17 problems, the last one starred).
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

**Seminar S01.** 17 problems in the order of the lecture; not in `solutions-released`. Revised before the first teaching (14 Nov) to match learning outcome 1 of the programme (definitions, axioms and derivations from them, counting): for each subtopic one problem repeats the lecture idea and one expands it (new business setting plus one twist). Intro paragraph and a `::: lecturer` timing cue as in S02: spine Problems 1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14 (about 76 min); 2 and 9 marked *if time allows*; 15, 16, 17\* for a strong group or to take home. A visible "Useful formulas" note (unnumbered section before Problem 1) introduces the factorial ($n!$, $0!=1$, $4!=24$) and tabulates De Morgan, complement, union, classical, product rule, permutations, arrangements, combinations, swap test and geometric probability with their lecture numbers; Problem 9 builds on it.

| Problem | Theme | Context, names | Cites |
|---|---|---|---|
| 1 | Events, repeat: set expressions for coffee/dessert | café chain | Thm 1.1 |
| 2 | If time allows. Events, expand: three suppliers on time; none vs not all three via De Morgan for three events | sushi bar, Vladivostok | Thm 1.1 |
| 3 | Axioms, repeat: $\Prob(A\cap B)=0.19$, neither 0.22, exactly one 0.59 | online store, discounts and instalments | Thm 1.2 |
| 4 | Axioms, expand: prove $\Prob(A\cap B^c)=\Prob(A)-\Prob(A\cap B)$ and $\Prob(A\cap B)\ge\Prob(A)+\Prob(B)-1$; app 80%, salary card 70%, both between 0.50 and 0.70; mutually exclusive 0.7 and 0.5 impossible (old Problem 2). Mentions $A\setminus B$ as other books' notation for $A\cap B^c$ | regional bank, Yekaterinburg | Def 1.4, Thm 1.2 |
| 5 | Classical, repeat: find the mistake, 11 sums (1/6, 1/36) | dice | Def 1.5 |
| 6 | Classical, expand: 3 customers, 4 cashiers, $4^3=64$; all different 0.375, all same 0.0625, exactly two share 0.5625; Rustam's "three patterns, 1/3 each" is the coarse $\Omega$ | supermarket, Yaroslavl; Rustam | Thm 1.3, Def 1.7, Def 1.5, Sec 1.1 |
| 7 | Counting, repeat: "does order matter?" drill: $6!=720$, $15\cdot14\cdot13=2730$, $\binom{15}3=455$, $26^3=17\,576$ | demo day in Skolkovo, student club, loyalty codes | Defs 1.6–1.8, Thm 1.3, Thm 1.4 |
| 8 | Counting, expand: Wi-Fi password, at least one digit by complement, $\Prob(\text{no digit})\approx0.074$ | Wi-Fi | Thm 1.3 |
| 9 | If time allows. Counting, expand: identical items, $8!/(3!3!2!)=560=\binom83\binom53$ | bakery at Chistye Prudy, Napoleon/medovik/cheesecake | Def 1.6, Thm 1.4, Thm 1.3 |
| 10 | Combinations, repeat: expired packs, 40 shelf, 0.507 vs 0.491 | yoghurt shelf | Ex 1.7 |
| 11 | Combinations, expand: at least 2 analysts by complement, 596/792 ≈ 0.753 | sales department | (none) |
| 12 | Geometric 1D, repeat: shuttle every 12 min, wait > 5 is 7/12; exactly 5 has probability 0 but is not impossible | office shuttle, Rumyantsevo; Lena | Def 1.9, Ex 1.8, Sec 1.6 |
| 13 | Geometric 2D, repeat: meeting with 10 min wait, 11/36 | bus stop; Priya, Kemal | Ex 1.9 |
| 14 | Geometric 2D, expand: one dock, 10 and 20 min unloading, asymmetric band, $\Prob(\text{clash})=31/72\approx0.431$ vs 7/16 for 15+15; figure in the solution (unlabelled) | warehouse near Podolsk; Anvar | Def 1.9, Ex 1.9 |
| 15 | If time allows. Robots on an 8×8 grid, 7/9 | warehouse robots | (none) |
| 16 | If time allows. Birthdays in a team of 30, 0.706 (L02 Ex 2.2 cites it as Problem 16) | team | (none) |
| 17\* | Past the lecture, not examinable: combinations with repetition, 3 scoops of 5 flavours, $5+20+10=35=\binom73$ | ice-cream kiosk, Gorky Park; Sofia | Thm 1.3, Def 1.8 |

New contexts and names: suppliers of a sushi bar, bank app and salary card, supermarket cashiers, startup demo day, student club, loyalty codes, bakery window, office shuttle, loading dock, ice-cream kiosk. Names: Rustam, Lena, Anvar, Sofia. Problems 6, 13 and 14 use independence informally ("whatever the others chose", "independently", "has nothing to do with"); L02 defines it. Problem 12 sets up "probability zero is not impossible" for Lecture 4. Problem 16 (birthdays) leads into products of conditional probabilities in L02. Problem 17\* anticipates nothing examinable.

## L02: Conditional probability and Bayes' theorem

Files: `book/lectures/L02-conditional-probability.qmd` (12 print pages), `slides/L02-conditional-probability.qmd` (50 slides + title), `book/seminars/S02-conditional-probability.qmd` (9 problems, the last one starred).
Status: chapter drafted on `unit/L02-conditional-probability`, under review.

**Chapter.** Opens with the L01 store: $\Prob(\text{promo}\mid\text{app})=0.20/0.55\approx0.36$, not $0.40$.

| Section | Items |
|---|---|
| 2.1 Conditional probability | Def 2.1; Fig 2.1 reduced sample space (conditioning panels); Ex 2.1 promo given app, $\Prob(A\mid B)\ne\Prob(B\mid A)$; Thm 2.1 $\Prob(\cdot\mid B)$ satisfies the axioms (proof-fold) |
| 2.2 Multiplication rule | Thm 2.2 with chain rule (Eq 2.1); Ex 2.2 birthdays as a chain (team of 10, 0.883, ties to S01 Problem 16); Ex 2.3 two faulty bulbs out of 12, tree (Fig 2.2), checked by counting |
| 2.3 Independence | Def 2.2; Thm 2.3 complements; Def 2.3 mutual independence (pairwise is not enough, counterexample); Ex 2.4 gambler's fallacy, six tosses and the loan-officer version. **Break after this section.** |
| 2.4 Total probability | Thm 2.4 (Eq 2.2), uses the partition from L01 Def 1.3; Ex 2.5 two phone-case factories (0.024); Ex 2.6 funnel by segment, overall rate 5.6% to 7.1% only because the mix changed |
| 2.5 Bayes | Thm 2.5 (Eq 2.3); Ex 2.7 which factory made the defective case (0.75); Ex 2.8 fraud alerts, 100,000 payments, 0.2% fraud, 1% false alarms (198 / 2 / 998 / 98,802), Table 2.1; prior and posterior; prosecutor's fallacy |

Ends with 5 exercises and the pointer to Seminar 2.

**Facts later units can use.** Notation $\Prob(A\mid B)$, no new macros. Terms introduced: conditional probability, probability tree, independent, mutually independent, gambler's fallacy, prior, posterior, base rate (Ex 2.8 discussion), prosecutor's fallacy (glossed as $\Prob(\text{evidence}\mid\text{innocent})$ taken for $\Prob(\text{innocent}\mid\text{evidence})$). Contexts used: phone-case factories, customer funnel with segments (new, returning, referred), fraud alerts, loan officer, team birthdays. Real cases named: Gigerenzer's tests of doctors, Sally Clark (prosecutor's fallacy). Mistakes named: swapping $\Prob(A\mid B)$ and $\Prob(B\mid A)$; $\Prob(A\mid B^c)\ne1-\Prob(A\mid B)$; independent taken as mutually exclusive; pairwise taken as mutual independence; the gambler's fallacy and its mirror; a change in mix read as a change in rates. Open thread: the chapter points to Bayes for "one firm rejected five times", which no section works out, so S02 can pick it up.

**Slides.** 50 slides (51 pages with the title), 46 with a visual. Break at slide 31 (page 32), after the loan-officer slide that closes Sec 2.3. Reuses Fig 2.1 (conditioning panels), Fig 2.2 (bulb tree) and Table 2.1. New pictures: the B-rescaled-to-1 bar (Def 2.1), the red-die-shows-6 grid, the 66-pair grid checking Ex 2.3, the unit-square area picture for Def 2.2 and Thm 2.3, all 64 six-toss sequences with runs marked, sequence strips for Ex 2.4, a partition picture for Thm 2.4, a 1000-case grid for Ex 2.5, width = share mosaics for Ex 2.6, prior/posterior bars for Ex 2.7 and Ex 2.8, a shared-cause diagram for "assumed, not computed", an outcome-by-event grid for pairwise vs mutual, overall-vs-segment bars for the mix pitfall, a width = prior, height = likelihood area picture for Thm 2.5, a tree for Exercise 5. A shared `tree()` helper in the hidden first cell draws every probability tree (Ex 2.3, Ex 2.5, Ex 2.8, Exercise 4). Pitfall slides: swapping $\Prob(A\mid B)$ and $\Prob(B\mid A)$; complement behind the bar; independent vs mutually exclusive (with Exercise 3 as a quick check); pairwise vs mutual independence and mix moved, not the rates (both as picture slides, not Wrong/Right boxes); "99% accurate" with the prosecutor's fallacy and Sally Clark. Your turn: Exercises 1, 2, 4, 5 and the "write six random tosses" room activity. Lecturer cues are in speaker notes.

**Seminar S02.** 9 problems, easy to hard; 15 print pages with solutions (7 in the student PDF). Not in `solutions-released`. Revised after the first unit review: reject-rule rubles moved from 8 into 9\*, openings varied (one sheet-level line says the firms and numbers are made up). Revised after the second review: Problems 1, 3, 4 and parts 3(c), 5(d) marked "if time allows"; a `::: lecturer` timing cue at the top (the spine is 2, 5, 6, 7, 8 at 10–12 min each; 9\* for a strong group or homework, the first lecturer cue in a seminar); 8(b) no longer asks the same question twice; renamed Oksana → Diego and Priya → Timur; Problem 3 moved from a bank to furniture delivery and Problem 4 from an online shop to a cinema chain; idioms replaced; solutions end on the last number or step, not on a moral.

| Problem | Theme | Context, names | Cites |
|---|---|---|---|
| 1 | If time allows. Drill: $\Prob(S\mid R)$ vs $\Prob(R\mid S)$ from a 500-answer two-way table; one-word independence check (0.80, 0.491, $\Prob(S)=0.684$) | HR survey, IT outsourcing firm, Nizhny Novgorod | Def 2.1, Ex 2.1, Def 2.2 |
| 2 | Chain rule and tree, checked by counting: 3 of 40 raffle tickets, 4 prizes (357/494, 63/247) | Zarina, New Year raffle, Tyumen | Eq 2.1, Ex 2.3, Def 1.8 |
| 3 | If time allows. Independent ($0.10\cdot0.20=0.02$) vs mutually exclusive with the same marginals (union 0.28 vs 0.30); (c) optional | damaged item ($D$, 0.10) and late delivery ($L$, 0.20), furniture delivery firm in Samara; second firm cancels deliveries of damaged items | Def 2.2, Thm 2.3, Thm 1.2 |
| 4 | If time allows. Find the mistake: divides instead of multiplying, unstated independence (0.0025); shared power supply pushes it up | Gleb, two servers behind the ticket website of a cinema chain in Tver | Def 2.1, Thm 2.2, Thm 1.2 |
| 5 | Gambler's fallacy with conversions: next click still 0.30, $0.3^6$, complement; (d) optional: streak as a reason to doubt the model | Timur, flower delivery ads before 8 March, Moscow | Def 2.3, Ex 2.4 |
| 6 | Short drill, total probability: three call centres take 50/30/20% of calls, complaint rates 1/2/4% (0.019; 50/60/80 per 10,000); "probation" and "weighted average" glossed | support line of an online electronics shop; Kazan, Ufa, Izhevsk | Thm 2.4, Eq 2.2 |
| 7 | Bayes reverse of 6: which centre took the complaint call (5/19, 6/19, 8/19, start with Izhevsk); shares 70/20/10 flip it to Kazan (0.467) because the prior matters | Aigerim, quality manager, same shop | Eq 2.3 |
| 8 | Long case, 4 parts: scoring model, 5% default, flags 80% / 10%; natural-frequency table, $\Prob(D\mid F)\approx0.296$ by Bayes and checked in the table, not flagged 0.012, recession 10% gives 0.471 | Diego, credit-risk team, consumer-loan bank in Krasnoyarsk | Eq 2.3, Ex 2.1, Ex 2.8 |
| 9* | Beyond the lecture, not examinable: sequential Bayes (posterior becomes prior), conditional independence in plain words; second check gives 28/47, flag + clean report 3/22; conditional independence is not independence; rubles: Rule 1 "reject every flagged" net gain 51.5 mln vs Rule 2 "reject flagged with a bad report" 50.3 mln per 10,000 applicants (break-even default rate 0.130 < 3/22; at 32,000 interest it is 0.138 and Rule 2 wins); the "firm rejected by five banks" case left open in Sec 2.3 (0.200 to 0.560, sixth bank rejects 0.790) | same bank; small-business loans | Eq 2.3, Eq 2.2, Sec 2.3 |

New contexts and names: HR survey, raffle, furniture delivery (damaged and late), cinema tickets website and servers, flower ads, call centres and complaints, loan scoring and credit bureau. Names: Zarina, Gleb, Timur, Aigerim, Diego. Online shops on the sheet: only Problems 6–7 (electronics). Bank items: Problems 8 and 9\* only. Relies on L01 (Def 1.8, Thm 1.2) and on the L02 loan officer's 30% approval rate (Problem 9 is built to match it). Anticipates: a test of independence for a two-way table (module 3, mentioned unnamed in Problem 1), expected value (L03; Problem 9\*(c) works in totals per 10,000 applicants and a break-even rate, no $\E$), and the idea of updating a belief from data. Problem 9 introduces "conditionally independent" informally; nothing in the lectures defines it yet.

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
