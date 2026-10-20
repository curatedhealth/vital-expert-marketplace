# Worked example: discharge follow-up worklist (ILLUSTRATIVE)

Everything about the hospital, its people, metrics, data and scores is illustrative, typed or generated for this build (`examples/sample-data/`, see its README). The library calls are real saved outputs from 19 October 2026 (`examples/live/`); the connector was not connected during this build (20 October 2026), so no new call was made. Script runs were made on 20 October 2026.

## The request (A1, A2 and B1 in one conversation)

"I run analytics for a three-hospital system. Care transitions wants a worklist that tells discharge nurses whom to call first. Rank it against two other asks with our RICE scores (attached). Then check our metric cards, because the unit dashboard shows 66% for follow-up calls and nobody trusts it. September data attached. Last month missed calls went up from 51 to 66; draft the commentary for the CNO."

## A1: frame and rank

Frame as the person stated it: decision maker Priya Nair (care transitions); choice "which units get extra discharge nurse capacity next month"; action if yes "move one nurse to the flagged unit", if no "keep the current roster". The worklist bet: discharge nurses call the right patients within 2 days from the worklist instead of the paper census; bet metric "follow-up call within 2 days of discharge" (card M1), comparison June against September, window one month. Discovery evidence: "step not observed" (the person reported interviews only), so the bet is recorded but stopped until the moment is watched (old DH-05.02.3.1.3). Current cost: not given `[GAP]`.

`python3 scripts/metric_check.py rank --input examples/sample-data/use_case_scores_illustrative.json`

| Initiative | RICE score | Note |
|---|---|---|
| discharge-call-worklist | 480.0000 | none |
| sepsis-alert-response-dashboard | 90.0000 | none |
| readmission-risk-score-in-ehr | 1.5000 | confidence given as a fraction: analytics.rice needs a whole percent (80, not 0.8) |

The third score is not comparable until the person restates confidence as a whole percent; recomputed with 50 it would be 150.0000 (1200 x 2 x 0.5 / 8), arithmetic only. Library behavior on the fraction: `rice_percent_confidence.json` and register N5.

## A2: cards and recomputation

`python3 scripts/metric_check.py cards --file examples/sample-data/metric_cards_illustrative.csv`

| Id | Metric | Owner | Status | Version | Flags |
|---|---|---|---|---|---|
| M1 | Follow-up call within 2 days of discharge | Priya Nair (care transitions) | certified | 1.2 | K11 (M2) |
| M2 | Follow-up call rate (unit dashboard) | owner not named | certified | not given | K2, K6, K7, K10 (certifier, certified_on, owner), K11 (M1), K12, K13 |
| M3 | Readmission within 30 days | Priya Nair (care transitions) | draft | 0.9 | K4, K5, K7 |
| M4 | Sepsis alert response time | Dr. Okafor (sepsis program) | certified | 2.0 | K1 |

`python3 scripts/metric_check.py recompute --data examples/sample-data/discharges_illustrative.csv --denominator "disposition=home;age>=18" --numerator "follow_up_call_2d=yes" --reported 0.66 --by unit`

| Group | Denominator | Numerator | Rate |
|---|---|---|---|
| 4 West | 48 | 34 | 0.7083 |
| 5 North | 45 | 22 | 0.4889 |
| 6 South | 46 | 34 | 0.7391 |

Recomputed 90 / 139 = 0.6475; shown 0.6600; difference -0.0125.

## B1: driver

`python3 scripts/metric_check.py driver --file examples/sample-data/missed_calls_by_unit_illustrative.csv` (no rule given): no driver named. With the person's rule `--share 0.5`: 5 North (0.80) accounts for the move; 6 South moved against the total.

## The short answer for A2 (as handed over)

**Answer.** Two of four cards would not pass the elements the checklist names: M2 (the unit dashboard's rate) repeats M1's numerator and denominator with no owner, version, direction or strata, yet is marked certified with no certifier or date; M3 writes its denominator in codes and has no initial population. Recomputed from your September file with M1's rules, the rate is 0.6475 (90 of 139) against 0.66 shown, a difference of -0.0125; whether that matters is your rule, and the certifier decides M2.

**Card flags** (CMS Measures Management System Hub, read 20 October 2026; CMS quality-measure guidance, used here as a checklist):

| Metric | Owner | Flags | Rows |
|---|---|---|---|
| M2 | owner not named | duplicate of M1; no owner, version, direction, strata; every column a filter | DA-134, DA-135, DA-136, DA-137 |
| M3 | Priya Nair | denominator in codes; no initial population; no strata | DA-133, DA-134, DA-136 |
| M4 | Dr. Okafor | no decision named | old DH-05.03.1.1.1 |

**Recomputation.** By unit: 4 West 0.7083, 5 North 0.4889, 6 South 0.7391. Data timestamp of the 0.66: not given, so the gap cannot yet be read as formula versus refresh.

**For the certifier.** Your certification rule: not given. Elements a rule usually names (owner, formula, grain, source, recomputation check) are listed in `metric-governance-rules.md` section 4 as the old method; the rule is yours.

**Calls made.** None: the connector was not connected; scripts run on your files, 20 October 2026. Full version on request.

**Record.** Metric and certification draft for the certifier. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Word count: `python3 scripts/metric_check.py words` on the text from "Answer" to the record line printed "232 words, within the short-mode cap" (20 October 2026).
