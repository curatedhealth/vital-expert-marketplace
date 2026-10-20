# Worked run: deterioration model and sleep-program rules (ILLUSTRATIVE)

ILLUSTRATIVE. The person's files in `sample-data/` are invented for this example (a deterioration model for adult inpatients, its manifest, locked test predictions and the criteria the team wrote on 1 October 2025; a sleep-program rule table). No real patient, site or model. Rules come from `references/`; script outputs are saved beside the inputs (`split_output.txt`, `rules_output.txt`, `evaluate_output.txt`). The connector was not connected when this example was written; no library call was needed for A2 and B1, and A1 names no authorized product.

Request: "Our deterioration model DET-1 2.1.0 flags adult inpatients for nurse review within an hour. Training at Site A and Site B, external test at Site C. Check the split, check our three sleep-program rules, then tell us whether the model passed the criteria we wrote on 1 October 2025."

---

## A1 answer (short mode)

**Answer.** Your intended use names the decision and the population, but not the user, the inputs or the decision it must not support. The manifest does not support an external claim as it stands: 40 test records come from Site B, a development site, 3 patients sit in both test and training, and patients aged 85 and over are absent from the test set, so that group is not validated `[GAP]`.

**Intended use (yours).** User: not given. Input: not given. Output: a flag (threshold 0.25 in your criteria file). Decision supported: nurse review within 1 hour. Decision excluded: not given. Population: adult inpatients.

**Split check (your manifest, `model_check.py split`).**

| Split | Records | Patients | Sites | Dates |
|---|---|---|---|---|
| train | 1,200 | 1,200 | Site A, Site B | 1 January 2023 to 29 December 2024 |
| tune | 200 | 200 | Site B | 1 July 2024 to 30 December 2024 |
| test | 603 | 603 | Site B, Site C | 3 November 2024 to 30 September 2025 |

- S1: 3 patients appear in test and training. Leakage "can create uncertainty regarding the true performance" (FDA AI-enabled device software functions draft guidance, January 2025, draft, DA-39).
- S2: the external test shares Site B with development; the draft says test data should generally come from sites different from those used to develop the model (DA-41).
- S5: age 85+: 454 development records, 0 test records: not validated `[GAP]`.

**Data plan against the rows.** Reference standard and its uncertainty: not given (DA-42, draft). Sample size reasoning: not given (TRIPOD+AI item 10, Collins et al. 2024, DOI 10.1136/bmj-2023-078378, CV126). Differences between development and test data: Site C added; outcome definition not given (item 16, CV128).

**Needed from you.** The user, the inputs and the decision the flag must not support; the reference standard; whether to rebuild the test set without Site B and the 3 patients, or report it as internal testing. That choice is yours.

**Calls made.** None (connector not connected; no named authorization). `model_check.py split`, 20 October 2026. Full version on request.

**Record.** Validation plan draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

## A2 answer (short mode)

**Answer.** Of three decision points, one is fully specified; DP2 has no rule for missing sleep data and can shorten the window by 30 minutes, which is outside your allowed options, and DP3 has no tailoring variable or proximal outcome. No bound on prompt frequency and no test design were given.

**Rule table (your file, `model_check.py rules`).**

| Decision point | On missing data | Flags |
|---|---|---|
| DP1 daily 21:00 | no prompt | none |
| DP2 weekly sleep window | not given | R1 no missing-data rule; R3 no engagement or fatigue outcome; R6 "shorten window 30 minutes" outside the allowed options |
| DP3 morning check-in | check-in card | R0 no tailoring variable; R2 no proximal outcome; R4 measurement validity not stated |

Each flag is a gap against the adaptive-intervention components (Nahum-Shani et al. 2018, DOI 10.1007/s12160-016-9830-8, TM79, TM84, TM87 to TM89), not a safety verdict. DP1's wearable sleep-onset validity is "not given" in your table; unreliable tailoring variables make a rule little better than random (TM88).

**Bounds you set.** Options never delivered: not given. Maximum prompts per day: not given. Who may change a rule: not given.

**How each rule is tested.** Not given. A micro-randomized trial estimates causal effects of options on proximal outcomes (TM90); comparisons from a deployed log are descriptive.

**Calls made.** None. `model_check.py rules`, 20 October 2026. Full version on request.

**Record.** Personalization specification draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

## B1 answer (short mode)

**Answer.** On the test set as supplied, all three of your criteria are met (AUROC 0.809 against 0.75; sensitivity 0.810 overall and 0.814 for women against 0.70), but the set includes the Site B records and the 3 leaked patients from A1, and patients aged 85+ are not validated. Who accepts the record is not given.

**Your criteria (written 1 October 2025; run 3 November 2025).**

| Criterion | Observed | Result |
|---|---|---|
| AUROC at least 0.75, all | 0.809 (0.761 to 0.857) | met |
| Sensitivity at least 0.70 at 0.25, all | 0.810 (0.732 to 0.869) | met |
| Sensitivity at least 0.70, women | 0.814 (0.696 to 0.893) | met |

**Values not covered by a criterion.** Observed to expected ratio 0.77 and calibration slope 1.25 overall; specificity 0.577 for men and 0.723 for women at 0.25. Calibration was named in TRIPOD+AI item 12e (CV127) but is not among your criteria.

**Fairness on your criterion (equal sensitivity by sex).** Women 0.814, men 0.806. Outcome rates differ (0.203, 0.214); a well-calibrated model will never have the same sensitivity and specificity for two groups with different outcome rates (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-119), so equal specificity cannot be asked as well without giving up calibration. Your choice stands as written.

**Promotion and drift watch.** Stages, who may promote and the watch threshold: not given.

**Calls made.** None. `model_check.py evaluate`, 20 October 2026. Full version on request.

**Record.** Validation record draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
