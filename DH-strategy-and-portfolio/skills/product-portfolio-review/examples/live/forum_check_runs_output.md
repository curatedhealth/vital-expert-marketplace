Output of scripts/forum_check.py on the illustrative files in examples/sample-data/, run 20 October 2026 (rerun after the fixes of 20 October 2026). Inputs are illustrative, never a person's judgment.

## records
Pass rule applied (confirm it is yours): rule, rank, decision and decider recorded; a continue with no rule fails; a stop with no record fails; a decision only in a slide fails.

| Item | Decision | Rule | Rank | Decider | Date | Record | Result | Why |
|---|---|---|---|---|---|---|---|---|
| Program A: insomnia DTx label expansion | continue | Rule 2026-09 | 1 | Dana Okafor | 2026-07-08 | board minutes 8 July 2026 | pass | all four present |
| Program B: anxiety DTx pivotal study | continue | Rule 2026-09 | 2 | Dana Okafor | 2026-07-08 | board minutes 8 July 2026 | pass | all four present |
| Program C: clinician dashboard add-on | continue | none | none | Dana Okafor | 2026-07-08 | steering deck slide 14 | fail | continue with no rule; no rank; lives only in a slide |
| Program D: pediatric ADHD prototype | stop | Rule 2026-09 | 4 | not named | 2026-07-08 | none | fail | no decider named; stop with no record |

2 of 4 decisions pass the rule as applied. Each decision is reported separately; no average.

Recorded continue items use 15 in the log's capacity unit (compare with the named capacity in the forum score).

## drift
Rule: Rule 2026-09 ; decision rule: {"type": "capacity_in_rank_order", "capacity": 14, "unit": "FTE", "period": "two quarters from 8 July 2026"}

| Item | Recomputed value | Recomputed rank | Recorded rank | Implied by the rule | Recorded decision | Result |
|---|---|---|---|---|---|---|
| Program A: insomnia DTx label expansion | 85.00 | 1 | 1 | continue | continue | match |
| Program B: anxiety DTx pivotal study | 72.50 | 2 | 2 | continue | continue | match |
| Program C: clinician dashboard add-on | 65.00 | 3 | none | not continue (rule does not say stop or delay) | continue | drift: continue beyond the rule |
| Program D: pediatric ADHD prototype | 60.00 | 4 | 4 | not continue (rule does not say stop or delay) | stop | match |

Named capacity 14 ; recorded continue items use 15.0.
Recorded continue item that goes past the named capacity: Program C: clinician dashboard add-on.

Match or drift is read against the person's rule as written; whether the rule or the decision is corrected is the person's call.

## benefits (no rule given)
| Benefit | Item | Owner | Baseline | Target | Actual (date) | Share of planned change | Your rule | Flags |
|---|---|---|---|---|---|---|---|---|
| Prescriptions per month | Program A: insomnia DTx label expansion | Ana Ruiz | 1200 | 1800 | 1500 (2026-09-30) | 50% | no rule given | none |
| Sites activated | Program B: anxiety DTx pivotal study | owner not named | 0 | 12 | 4 (2026-09-30) | 33% | no rule given | owner not given |
| Clinician weekly active users | Program C: clinician dashboard add-on | Sam Patel | not given | 400 | 150 (2026-09-30) | not measurable | no rule given | baseline not given; review date not given |

Baselines, targets, owners and the rule are the person's. A share is arithmetic, not a judgment of the program or its people.

## benefits with the person's rule 0.5 (illustrative)
| Benefit | Item | Owner | Baseline | Target | Actual (date) | Share of planned change | Your rule | Flags |
|---|---|---|---|---|---|---|---|---|
| Prescriptions per month | Program A: insomnia DTx label expansion | Ana Ruiz | 1200 | 1800 | 1500 (2026-09-30) | 50% | met | none |
| Sites activated | Program B: anxiety DTx pivotal study | owner not named | 0 | 12 | 4 (2026-09-30) | 33% | not met | owner not given |
| Clinician weekly active users | Program C: clinician dashboard add-on | Sam Patel | not given | 400 | 150 (2026-09-30) | not measurable | not measurable | baseline not given; review date not given |

Baselines, targets, owners and the rule are the person's. A share is arithmetic, not a judgment of the program or its people.

## records on evals/files/forum_log_eval.csv (rank order and decision check)
Pass rule applied (confirm it is yours): rule, rank, decision and decider recorded; a continue with no rule fails; a stop with no record fails; a decision only in a slide fails.

| Item | Decision | Rule | Rank | Decider | Date | Record | Result | Why |
|---|---|---|---|---|---|---|---|---|
| Cardio remote monitoring v3 | continue | Rule R7 | 1 | Priya Shah | 2026-09-10 | portfolio minutes 10 September 2026 | pass | all four present |
| Diabetes coaching app | continue | Rule R7 | 3 | Priya Shah | 2026-09-10 | portfolio minutes 10 September 2026 | pass | all four present |
| COPD inhaler companion | delay | Rule R7 | 2 | Priya Shah | 2026-09-10 | portfolio minutes 10 September 2026 | pass | all four present |
| Sleep DTx (in-licensed) | continue | none | none | Priya Shah | 2026-09-10 | quarterly review deck | fail | continue with no rule; no rank; lives only in a slide |

3 of 4 decisions pass the rule as applied. Each decision is reported separately; no average.

Rank order and decision (as recorded):
- COPD inhaler companion (rank 2, delay) and Diabetes coaching app (rank 3, continue): rank order and decision differ; reason not in the record. A question for the forum score, not a pass or fail.

Recorded continue items use 14 in the log's capacity unit (compare with the named capacity in the forum score).
