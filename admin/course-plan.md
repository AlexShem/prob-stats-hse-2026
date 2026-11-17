# Course plan (draft for review)

Classic sequence: probability in module 2, statistics in module 3. There is no programming or tools layer: Python only appears as a check at the end of seminar solutions.
Session numbers follow `admin/schedule.md`. Lecture N = one lecture day (usually two 80-minute slots). Seminar N is the same sheet for G1, G2 and G3.
"Ref." points to the colleague's course (`sources/Модули_1_2_новые.summary.md`, line numbers in the source file). A dash means we write it from scratch.

## Module 2: probability (Nov–Dec 2026)

| Lecture | Date | Topic | Ref. |
|---|---|---|---|
| L1 | Sat 7 Nov (2 slots) | Experiments, sample space, events and set operations. Axioms and consequences. Classical probability. Counting: product rule, permutations, combinations. Geometric probability. | – (1.3 for counting) |
| L2 | Wed 11 Nov (2) | Conditional probability, multiplication rule, independence of events (gambler's fallacy). Law of total probability, Bayes' theorem. | 2812–2846 |
| L3 | Wed 18 Nov (2) | Discrete random variables: PMF, CDF, expectation and variance with their properties. Bernoulli, binomial. | 117–427, 429–530 |
| L4 | Wed 25 Nov (2) | Geometric, hypergeometric, Poisson (and the Poisson approximation to the binomial). Continuous random variables: density, CDF, E and Var. Uniform, exponential, memorylessness. | 530–740 |
| L5 | Wed 2 Dec (2) | Normal distribution: standardization, Φ tables, quantiles, the 3σ rule. Linear transformations of a random variable. | 740–1025 |
| L6 | Wed 9 Dec (2) | Joint distributions (discrete tables): marginals, conditionals, independence of random variables. Covariance, correlation, variance of a sum. Two-asset portfolio. | – |
| L7 | Wed 16 Dec (1 slot) | Markov and Chebyshev inequalities, LLN, CLT, normal approximation to the binomial with continuity correction. | 1027–1393 |

| Seminar | Dates (G1/G2/G3) | Problems on | Ref. tasks |
|---|---|---|---|
| S1 | 14 Nov | L1: counting, classical and geometric probability | 1.3 |
| S2 | 21 Nov | L2: conditional probability, total probability, Bayes | – |
| S3 | 27 Nov | L3: discrete random variables, E, Var, binomial | 2.2–2.5, 1.7, 3.3 |
| S4 | 28 Nov | L4 (discrete part): geometric, hypergeometric, Poisson | 1.8, 3.9, 3.11, 6.2, 6.3 |
| S5 | 3 Dec | L4 (continuous part): densities, uniform, exponential | 1.10, 3.12, 3.14 |
| S6 | 5 Dec | L5: normal | 1.9, 3.15, 3.16, bank example 798 |
| S7 | 10 Dec | L6: joint tables, covariance, correlation | – |
| S8 | 12 Dec | L6: variance of sums, portfolio, review of L3–L6 | 6.1 |
| S9 | 17 Dec (G3) / 19 Dec (G1, G2) | L7: Chebyshev, LLN, CLT, normal approximation | 4.1–4.4, 9.2, 9.4 |
| S10 | same day, back-to-back | **Midterm** (likely), or practice if the midterm moves | – |

L7 falls only 1–3 days before S9, so S9 has to use L7 material immediately.

Midterm (not confirmed): most likely in S10 for each group (G3 Thu 17 Dec, G1 and G2 Sat 19 Dec), or as a separate session in the week of 21–27 Dec. Either way it covers L1–L7.

## Module 3: statistics (Jan–Mar 2027, timetable pending)

All eight topics are in. If module 3 has fewer lecture days than topics, items 1 and 2 share a lecture.

| # | Topic | Ref. |
|---|---|---|
| 1 | Data and samples: population against sample, sample mean and variance (n against n−1), empirical CDF, quantiles, histogram, boxplot | 1394–1734 |
| 2 | Sampling distributions: X̄ and its standard error, χ², t and F (definitions and use, no derivations) | (4260 names them) |
| 3 | Point estimation: unbiasedness, consistency, MSE and efficiency. Method of moments. Maximum likelihood (Bernoulli, Poisson, exponential, normal). | 1735–2676 |
| 4 | Confidence intervals: mean with σ known and unknown, proportion, variance; choosing the sample size | – |
| 5 | Hypothesis testing: H₀/H₁, type I/II errors, significance, p-value, power; z- and t-tests for a mean, test for a proportion | – |
| 6 | Two samples: independent and paired t-tests, two proportions (A/B tests), F-test for variances | – |
| 7 | Chi-square tests: goodness of fit, independence in contingency tables | – |
| 8 | Correlation and simple linear regression (OLS, interpreting the slope, t-test on the slope) | (1024 stray) |

## Decisions

- Audience (Nov 2026): first-year students, weaker in maths than planned (CLAUDE.md, "This class"). From L03 on, fewer examples per lecture and every new notation explained. L4 needs a short refresher on integrals before the first density, which makes the L4 row heavy: decide what moves (e.g. hypergeometric to S4 only, or exponential to L5) before writing L4.

- Quizzes: 4 online quizzes in module 2 and 4 in module 3 (5% each block). Dates and topics not fixed yet. Drafted privately in `assessment/quizzes/`.
- No homework.
- Regression is part of module 3.
- Midterm date is open (see above).
