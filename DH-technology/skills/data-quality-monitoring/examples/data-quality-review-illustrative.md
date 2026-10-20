# Worked example: data quality review of a readmission training set (illustrative)

Every file used here is illustrative, generated for this build (`examples/sample-data/`); no real patient, site or organization is shown, and the people named in the files are invented. Run on 20 October 2026. The library connector was unavailable during the build, so no library call was made; the script did all the computation.

Scenario: a heart failure readmission training set exists as version v3 (80 encounters) and a refreshed version v4 (90 encounters). The person's rules were written for v3 on 1 September 2026. The read date the person gives is 20 October 2026.

## A1 Data quality rules

```
$ python3 scripts/dq_check.py rules --rules examples/sample-data/dq_rules_illustrative.json
Dataset: HF readmission training set (illustrative); rules for version v3; unit of row encounter (one heart failure discharge); written 1 September 2026 by Data engineering lead, Dana Ortiz (illustrative).
| Check | Kahn category | Field(s) | Context | Your limit | Flags |
|---|---|---|---|---|---|
| DQ1 | Conformance (value) | sex | verification | 0 | none |
| DQ2 | Conformance (relational) | patient_id | verification | 0 | none |
| DQ3 | Conformance (computational) | bmi | verification | 0 | none |
| DQ4 | Completeness | nt_probnp | verification | 0.15 | none |
| DQ5 | Plausibility (uniqueness) | encounter_id | verification | 0 | none |
| DQ6 | Plausibility (atemporal) | age | verification | 0 | none |
| DQ7 | Plausibility (temporal) | admit_date on or before discharge_date | verification | not given | Q3 limit not given |
| DQ8 | Leak check (feature dated after the index time; the person's rule, outside Kahn) | nt_probnp_date | verification | 0 | none |
| DQ9 | Row count against the cohort (the person's rule, outside Kahn) | all rows | not given | 0 | none |

Limits, categories and the version are the person's; this check sets none.
```

Reading: nine checks cover all seven Kahn subcategories plus the person's leak and row-count rules; DQ7 (admission on or before discharge) has no limit (Q3) and will be reported but never marked. The limits are the person's; the skill set none.

## A2 Data quality read

```
$ python3 scripts/dq_check.py run --data examples/sample-data/encounters_v3_illustrative.csv --rules examples/sample-data/dq_rules_illustrative.json --version v3 --ref patients=examples/sample-data/patients_illustrative.csv
Data file examples/sample-data/encounters_v3_illustrative.csv: 80 rows, labeled version v3; rules written for version v3 on 1 September 2026.
| Check | Kahn category | Field | Rows checked | Failing | Share failing | Your limit | Result | Note |
|---|---|---|---|---|---|---|---|---|
| DQ1 | Conformance (value) | sex | 80 | 1 | 1.2% | 0 | fail | blank values are left to completeness |
| DQ2 | Conformance (relational) | patient_id | 80 | 1 | 1.2% | 0 | fail |  |
| DQ3 | Conformance (computational) | bmi | 80 | 1 | 1.2% | 0 | fail | recomputed as weight_kg / height_m ** 2, tolerance 0.2 (yours) |
| DQ4 | Completeness | nt_probnp | 80 | 7 | 8.8% | 0.15 | pass | decision-time feature |
| DQ5 | Plausibility (uniqueness) | encounter_id | 80 | 2 | 2.5% | 0 | fail | rows sharing a key with another row |
| DQ6 | Plausibility (atemporal) | age | 80 | 1 | 1.2% | 0 | fail | range 18 to 110 (yours) |
| DQ7 | Plausibility (temporal) | admit_date on or before discharge_date | 80 | 1 | 1.2% | not given | limit not given | admit_date on or before discharge_date |
| DQ8 | Leak check (feature dated after the index time; the person's rule, outside Kahn) | nt_probnp_date | 80 | 1 | 1.2% | 0 | fail | nt_probnp_date dated after index_time |
| DQ9 | Row count against the cohort (the person's rule, outside Kahn) | all rows | 80 | 0 |  | 0 | pass | 80 rows against 80 expected from your cohort rule |

Against your limits: 2 pass, 6 fail, 1 with no limit given, 0 not run.
Features with rows dated after the index time: nt_probnp_date.
Whether the dataset is fit for its use is the person's call; a failed check stays open until the person closes it with evidence.

$ python3 scripts/dq_check.py run --data examples/sample-data/encounters_v4_illustrative.csv --rules examples/sample-data/dq_rules_illustrative.json --version v4 --ref patients=examples/sample-data/patients_illustrative.csv --json examples/sample-data/results_v4_illustrative.json
Data file examples/sample-data/encounters_v4_illustrative.csv: 90 rows, labeled version v4; rules written for version v3 on 1 September 2026.
V1 the rules were written for version v3; this run reads version v4. Results are reported against the rules as written.
| Check | Kahn category | Field | Rows checked | Failing | Share failing | Your limit | Result | Note |
|---|---|---|---|---|---|---|---|---|
| DQ1 | Conformance (value) | sex | 90 | 3 | 3.3% | 0 | fail | blank values are left to completeness |
| DQ2 | Conformance (relational) | patient_id | 90 | 1 | 1.1% | 0 | fail |  |
| DQ3 | Conformance (computational) | bmi | 90 | 1 | 1.1% | 0 | fail | recomputed as weight_kg / height_m ** 2, tolerance 0.2 (yours) |
| DQ4 | Completeness | nt_probnp | 90 | 8 | 8.9% | 0.15 | pass | decision-time feature |
| DQ5 | Plausibility (uniqueness) | encounter_id | 90 | 2 | 2.2% | 0 | fail | rows sharing a key with another row |
| DQ6 | Plausibility (atemporal) | age | 90 | 1 | 1.1% | 0 | fail | range 18 to 110 (yours) |
| DQ7 | Plausibility (temporal) | admit_date on or before discharge_date | 90 | 1 | 1.1% | not given | limit not given | admit_date on or before discharge_date |
| DQ8 | Leak check (feature dated after the index time; the person's rule, outside Kahn) | nt_probnp_date | 90 | 6 | 6.7% | 0 | fail | nt_probnp_date dated after index_time |
| DQ9 | Row count against the cohort (the person's rule, outside Kahn) | all rows | 90 | 10 |  | 0 | fail | 90 rows against 80 expected from your cohort rule |

Against your limits: 1 pass, 7 fail, 1 with no limit given, 0 not run.
Features with rows dated after the index time: nt_probnp_date.
Whether the dataset is fit for its use is the person's call; a failed check stays open until the person closes it with evidence.

$ python3 scripts/dq_check.py compare --old examples/sample-data/encounters_v3_illustrative.csv --new examples/sample-data/encounters_v4_illustrative.csv --fields sex,age,nt_probnp,bmi
Rows: 80 in examples/sample-data/encounters_v3_illustrative.csv; 90 in examples/sample-data/encounters_v4_illustrative.csv.
| Field | Missing share old | Missing share new | Old summary | New summary |
|---|---|---|---|---|
| sex | 0.0% | 0.0% | F 50%; M 49%; 2 1% | M 50%; F 47%; 2 1%; unknown 1% |
| age | 0.0% | 0.0% | mean 67.65, median 66.00, n 80 | mean 70.01, median 71.00, n 90 |
| nt_probnp | 8.8% | 8.9% | mean 4445.56, median 4665.00, n 73 | mean 4196.22, median 4247.00, n 82 |
| bmi | 0.0% | 0.0% | mean 28.58, median 27.20, n 80 | mean 30.52, median 31.20, n 90 |

Differences are facts about the two files, not a verdict and not a drift threshold. What they mean for a model's performance goes to model-performance-and-drift-monitoring (this pack).
```

Short-mode answer (`python3 scripts/dq_check.py words`: 313 words, within the short-mode cap):

> **Answer.** On version v4, read 20 October 2026 against your rules written for v3 on 1 September 2026, 1 check passes, 7 fail and 1 has no limit: the failures are sex codes (3 of 90), orphan patient ids (1 of 90), BMI recomputation (1 of 90), duplicate encounter ids (2 of 90), age range (1 of 90), NT-proBNP results dated after the index time (6 of 90) and the row count (90 against 80 expected). Compared with v3, v4 has 10 more rows and the leak count rose from 1 to 6.
> 
> **Results** (script, uniqueness and relational first).
> 
> | Check | Category | Failing | Your limit | Result |
> |---|---|---|---|---|
> | DQ5 | Plausibility (uniqueness) | 2 of 90 | 0 | fail |
> | DQ2 | Conformance (relational) | 1 of 90 | 0 | fail |
> | DQ8 | Leak check (yours) | 6 of 90 | 0 | fail |
> | DQ1 | Conformance (value) | 3 of 90 | 0 | fail |
> | DQ4 | Completeness, nt_probnp | 8 of 90 | 0.15 | pass |
> | DQ7 | Plausibility (temporal) | 1 of 90 | not given | not marked |
> 
> Categories follow Kahn et al. 2016 (DA-95 to DA-98, DOI 10.13063/2327-9214.1244). DQ9 counts 90 rows against the 80 your cohort rule expects.
> 
> **Changes from v3.** Rows 80 to 90; sex codes now include "unknown"; mean age 67.65 to 70.01; mean BMI 28.58 to 30.52; NT-proBNP missing share 8.8% to 8.9%. These are facts about the two files, not a drift verdict; what they mean for the model goes to model-performance-and-drift-monitoring (this pack).
> 
> **Limits of this read.** The rules were written for v3 (V1). All checks are verification checks; none compares the data with an external reference (Kahn's validation context, DA-94). Counts show the data exist; they are not evidence of reliability or validity (CMS Measures Management System Hub, read 20 October 2026, DA-139, quality-measure context).
> 
> **Calls made.** None; scripts: dq_check.py run on v3 and v4, compare on sex, age, nt_probnp, bmi. The library connector was unavailable on 20 October 2026; no call was needed.
> 
> A full version (all nine checks, comparison table) is available on request.
> 
> **Record.** Data quality read draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## B1 Data quality review and feature repair

```
$ python3 scripts/dq_check.py review --results examples/sample-data/results_v4_illustrative.json --log examples/sample-data/repair_log_illustrative.csv
Run on version v4: 7 failed checks against your limits.
| Check | Field | Failing | Owner (yours) | Action (yours) | New version | Recheck date | Flags |
|---|---|---|---|---|---|---|---|
| DQ1 | sex | 3 of 90 | owner not named | not given | not given | not given | R1 owner not named, R2 action not given, R5 recheck date not given |
| DQ2 | patient_id | 1 of 90 | owner not named | not given | not given | not given | R1 owner not named, R2 action not given, R5 recheck date not given |
| DQ3 | bmi | 1 of 90 | owner not named | not given | not given | not given | R1 owner not named, R2 action not given, R5 recheck date not given |
| DQ5 | encounter_id | 2 of 90 | owner not named | not given | not given | not given | R1 owner not named, R2 action not given, R5 recheck date not given |
| DQ6 | age | 1 of 90 | owner not named | not given | not given | not given | R1 owner not named, R2 action not given, R5 recheck date not given |
| DQ8 | nt_probnp_date | 6 of 90 | Dana Ortiz (illustrative) | redefined | v5 | 15 November 2026 | none |
| DQ9 | all rows | 10 of 90 | owner not named | not given | not given | not given | R1 owner not named, R2 action not given, R5 recheck date not given |

R6 repair log rows for checks that did not fail in this run: DQ4.
Checks with no limit given (reported, never marked pass or fail): DQ7.
Until a failed check is closed with a new version, the failed version is not used for training (old task: 'Do not train on the failed version'). Owners, actions and dates are the person's.
```

Short-mode answer (`python3 scripts/dq_check.py words`: 327 words, within the short-mode cap):

> **Answer.** Seven checks failed on v4; one (DQ8, NT-proBNP dated after the index time) has an owner, a repair, a new version and a recheck date, and six have none of these. The gap that most limits the review: no owner named for the key failures (duplicate encounter ids and orphan patient ids) that every other count depends on.
> 
> **Your limits.** As written in your rules for v3 on 1 September 2026: share failing at most 0 for DQ1 to DQ3, DQ5, DQ6, DQ8; missing share at most 0.15 for DQ4; row difference at most 0 for DQ9. DQ7 has no limit and is not marked.
> 
> **Failed checks.**
> 
> | Check | Failing | Owner | Repair | New version | Recheck |
> |---|---|---|---|---|---|
> | DQ5 encounter_id | 2 of 90 | owner not named | not given | not given | not given |
> | DQ2 patient_id | 1 of 90 | owner not named | not given | not given | not given |
> | DQ8 nt_probnp_date | 6 of 90 | Dana Ortiz (illustrative) | redefined | v5 | 15 November 2026 |
> | DQ1 sex | 3 of 90 | owner not named | not given | not given | not given |
> | DQ3, DQ6, DQ9 | 1, 1, 10 | owner not named | not given | not given | not given |
> 
> Your log also holds a row for DQ4 ("removed", v4), a check that passed in this run (R6); please confirm what it refers to.
> 
> **Repair order.** DQ5 and DQ2 first, because duplicate and orphan keys change the denominators of every other check; DQ8 before any retraining.
> 
> **For you to decide.** Which version is used for training: not v4 while checks are open (old task DH-01.04.4.2.3). If a model was already evaluated on a test set drawn from v4, whether it needs a new independent test set after the NT-proBNP redefinition (EMA reflection paper, adopted 9 September 2024, DA-73, medicinal-products context). Owners and recheck dates for six checks.
> 
> **Calls made.** None; script: dq_check.py review on the v4 results and your repair log.
> 
> A full version (all flags, limits verbatim) is available on request.
> 
> **Record.** Data quality review draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
