# Content tracker

What each lecture, deck and seminar actually contains and how it is presented. Writers read this **before** starting a new unit so the course stays consistent, and update their unit's entry **before** reporting done. It records what exists in the files, not what is planned: the plan is `course-plan.md`.

Keep entries short. Numbers (Def 1.4, Ex 1.7) are the book's numbers, taken from `make labels L=<stem>`. After a renumbering, fix them here.

## Course-wide conventions (as established so far)

**Notation.** Events $A, B, A^c$ (not $\bar A$); $\cap, \cup, \varnothing$; $\Omega$; $\Prob$, $\binom{n}{k}$. "Mutually exclusive" is the main term for events that cannot both happen. Keep it distinct from "independent".

**This class (from L03 on).** First-year students, weaker in maths than planned; L02 ended 30 minutes early because the room lost track of the examples (data on one slide, used several slides later). Rules in CLAUDE.md, "Audience and scope": few self-contained examples, data restated where used ("Given:" strip on continuation slides), every new notation explained in a "How to read …" callout. L01 and L02 are left as they are.

**Recurring devices in chapters.**
- Open with one concrete business case, no "in this lecture" preview.
- Numbered boxes for definitions, theorems, examples. Examples are worked in full.
- A "common mistake" is named where it occurs and reused as the lesson in a lecturer cue.
- `::: lecturer` cues: timing in the first cue, a question for the room, what to draw on the board, one break at the midpoint.
- Chapter ends with `## Exercises {.unnumbered}`: 5 items, then one paragraph of answers, then a pointer to the seminar.

**Recurring devices in slides.** Opening hook slide, `[Def 1.2]{.tag}` chapter-number tags, "Your turn" slides, one `## Break` slide at the midpoint, a pitfall slide for each common mistake.

**Recurring devices in seminars.** Problems numbered by hand, easy to hard, solution by hand in `::: sol`, Python check at the end.

**Contexts and names already used** (vary them, do not repeat without a reason): Ilya's croissant stand at Paveletskaya, promo code and mobile app store, coffee/dessert café chain, discounted items and instalments, yoghurt and expired packs, Wi-Fi passwords and PINs, sales managers and analysts, robots on a grid, courier in a 2-hour window, two people meeting in a café, birthdays; S01 also uses sushi-bar suppliers, a bank app and salary card, supermarket cashiers, a demo day, a student club, a bakery window, an office shuttle, a loading dock, an ice-cream kiosk. Names: Ilya, Priya, Kemal, Rustam, Lena, Anvar, Sofia. Later: S02 adds Zarina, Gleb, Timur, Aigerim, Diego (HR survey, raffle, furniture delivery, cinema website, flower ads, call centres, loan scoring); L02 has Oksana (lighting wholesaler, Kazan). L03 adds Marat's optician's shop on Bauman Street, Kazan (free eye tests), and in the exercises a guesthouse in Suzdal, a food truck, a car showroom in Kaliningrad.

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

**Seminar S01.** 17 problems in the order of the lecture; 17 print pages with solutions (8 in the student PDF). Not in `solutions-released`. Revised before the first teaching (14 Nov) to match learning outcome 1 of the programme (definitions, axioms and derivations from them, counting): for each subtopic one problem repeats the lecture idea and one expands it (new business setting plus one twist). Intro paragraph and a `::: lecturer` timing cue as in S02: spine Problems 1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14 (about 76 min); 2 and 9 marked *if time allows*; 15, 16, 17\* for a strong group or to take home. A visible "Useful formulas" note (unnumbered section before Problem 1) introduces the factorial ($n!$, $0!=1$, $4!=24$) and tabulates De Morgan, complement, union, classical, product rule, permutations, arrangements, combinations, swap test and geometric probability with their lecture numbers; Problem 9 builds on it.
Figures (unnumbered, `echo: false`, inside `::: sol`, so hidden until release): Problem 1 four two-circle Venn panels (a)–(d); Problem 2 three-circle Venn, "exactly one" and "at least two"; Problem 12 timeline of one 12-minute cycle (first 7 min = wait > 5); Problem 13 square with band $|x-y|\le10$, corners "leg 50"; Problem 14 clash band with lines $y=x+10$, $y=x-20$ and no-clash areas 1250, 800; Problem 15 8×8 grid, robot's row and column (14, "sees") vs 49 safe squares; Problem 16 P(shared birthday) for n = 1…60 with n = 23 and 30 marked. Same colours as L01 (`#4c8cc9`, `#c0392b`, `#b7c4d1`).

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
| 14 | Geometric 2D, expand: one dock, 10 and 20 min unloading, asymmetric band, $\Prob(\text{clash})=31/72\approx0.431$ vs 7/16 for 15+15; labelled figure in the solution | warehouse near Podolsk; Anvar | Def 1.9, Ex 1.9 |
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

**In class (11 Nov).** Too much for this class: the lecture ended 30 minutes early because the room lost track of the examples. The deck is left as it is, but do not copy its pattern of splitting an example over 3–4 slides with the data only on the first: Ex 2.7 ("Which factory made the defective case?") reuses 0.03, 0.60 and 0.024 from about 15 slides earlier; Ex 2.3's counting check and "the second bulb" use 3/12, 2/11 and 66 from the set-up slide; Ex 2.6 and its pitfall slide rely on the 50/35/15 shares, 2/8/12% rates and 5.6% from earlier slides; the two fraud-alert slides rely on 0.2%, 99% and 1% from the problem slide.

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

## L03: Discrete random variables

Files: `book/lectures/L03-discrete-random-variables.qmd` (12 print pages, 17 in the student PDF; the brief asked for 7–10, the eight How-to-read callouts take about 2 pages). Deck and seminar S03 not made yet.
Status: chapter drafted on `unit/L03-discrete-random-variables`, under review.

**Chapter.** First chapter written for "This class". Opens with Marat's optician's shop on Bauman Street, Kazan: 3 customers come for a free eye test on Saturday, each orders glasses with probability 0.4, independently; 2,000 rubles per pair, 500 rubles per free test. Question: how many pairs to expect, and how much that swings. One running example (Marat) carries the whole chapter; there is no second worked example (the planned Bin(10, 0.9) pharmacy example was cut for length, so S03 must do the first larger-$n$ binomial calculation itself); every example box opens with a "*Given:*" line restating the data (the PMF as $p(0)=0.216$, $p(1)=0.432$, $p(2)=0.288$, $p(3)=0.064$). Rubles are written as the word "rubles" (the PDF font has no ₽ sign).

| Section | Items |
|---|---|
| 3.1 Random variables | Def 3.1 random variable (a number for each outcome, function on $\Omega$); Ex 3.1 Marat's 8 outcomes OOO…NNN mapped to $X\in\{0,1,2,3\}$; Fig 3.1 three-level tree with leaf probabilities, the $X=2$ leaves in red |
| 3.2 PMF | Def 3.2 discrete, PMF $p(x)=\Prob(X=x)$; Ex 3.2 Marat's PMF 0.216/0.432/0.288/0.064 (table); Fig 3.2 bar chart; Thm 3.1 $p\ge0$, $\sum_i p(x_i)=1$ (proof via partition, Def 1.3) |
| 3.3 CDF | Def 3.3 $F(x)=\Prob(X\le x)$; Ex 3.3 Marat's CDF 0.216/0.648/0.936/1, $F(1.5)=0.648$, piecewise formula; Fig 3.3 staircase (filled dot on top), dashed reading of $F(1.5)$; Eq 3.1 $\Prob(a<X\le b)=F(b)-F(a)$ with $\Prob(1<X\le3)=0.352$; pitfall $\Prob(1\le X\le3)=0.784$. **Break after this section.** |
| 3.4 Expected value | Def 3.4 $\E[X]=\sum_i x_ip(x_i)$, $\mu$; Ex 3.4 $\E[X]=1.2$; weighted average (plain average 1.5) and 1,000 Saturdays (1,200 pairs) |
| 3.5 Variance and SD | Eq 3.2 $\E[g(X)]=\sum_i g(x_i)p(x_i)$ (stated in words, before the variance); Def 3.5 $\Var(X)=\E[(X-\mu)^2]$, $\sigma=\operatorname{SD}(X)$; Thm 3.2 shortcut $\E[X^2]-\mu^2$ (proof-fold); Ex 3.5 by definition (five-column table, 0.31104+0.01728+0.18432+0.20736) and by shortcut ($\E[X^2]=2.16$), $\Var=0.72$, $\sigma\approx0.85$; pitfall $\E[X^2]\ne(\E X)^2$ |
| 3.6 Changing units: $aX+b$ | Thm 3.3 $\E[aX+b]$, $\Var(aX+b)=a^2\Var X$, $\operatorname{SD}=|a|\operatorname{SD}$ (E proof visible, Var/SD proof-fold); Ex 3.6 profit $Y=2000X-1500$: 900, 2,880,000 rubles², SD ≈ 1,697 rubles; pitfalls: $b$ vanishes from Var, $\Var(-X)=\Var(X)$ |
| 3.7 Bernoulli and binomial | Def 3.6 Bernoulli($p$), parameter, success/failure; mean $p$, variance $p(1-p)$ worked in prose (not a numbered result); Def 3.7 binomial, four conditions, Eq 3.3 PMF; why $\binom nk$ (Marat's 3 paths to $X=1$); Thm 3.4 $np$, $np(1-p)$ (proof-fold: sum of Bernoullis, relies on Lecture 6); check on Marat 1.2 and 0.72. No Example 3.7. |

"How to read" callouts (8): $X$, $x$, $\{X=2\}$, $\{X\le1\}$; $p(x)$; $\sum$ with index $i$ and $x_1,\dots,x_4$ (written out for Marat, ties back to Eq 2.2); $F(x)$, $\le$ vs $<$; $\E[X]$ and $\mu$; squares, square roots, $\sigma$ and units; $|a|$ (vs $|B|$ for set size in L02); $X\sim\operatorname{Bin}(n,p)$ and $p^k(1-p)^{n-k}$. No other callouts. Ends with 4 exercises (Suzdal guesthouse PMF/CDF/E/Var; food truck $300W-4000$; binomial or not, incl. L02's bulbs and "until the first order"; car showroom in Kaliningrad Bin(5, 0.2)), one paragraph of answers, pointer to Seminar 3.

**Facts later units can use.** Notation now in force: $X$ vs $x$; $p(x)$; $F(x)=\Prob(X\le x)$ (the letter $F$ is the CDF from now on, the chapter says so); $\sum_i$ over all values; $\E[X]$, $\mu$; $\Var(X)$, $\sigma$, $\operatorname{SD}(X)$ (written `\operatorname{SD}`, no macro); $\E[g(X)]$ (Eq 3.2); $X\sim\operatorname{Bin}(n,p)$ (`\operatorname{Bin}`); "parameter", "success/failure". Promises: Lecture 4 continuous random variables (waiting time) and the geometric distribution (Exercise 3c); Lecture 5 uses Thm 3.3 for linear transformations/standardization; Lecture 6 proves $\E$ of a sum and $\Var$ of an independent sum, which completes Thm 3.4's proof. Seminar 3 needs (none of it beyond Marat's $n=3$ is worked in the chapter for the binomial): PMF table → $F$ at a non-jump point, $\E=\sum xp(x)$, $\Var=\E[X^2]-(\E X)^2$, binomial PMF with $\binom{10}{8}0.9^8 0.1^2$, Bernoulli variance, $np$, recognising Bernoulli vs binomial; the source's orders-per-day table (task 2.2) was kept out of the chapter for it.

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
