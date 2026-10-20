# Worked example: heart failure readmission risk score (illustrative)

Every file used here is illustrative, typed for this build (`examples/sample-data/`); no real patient, site or organization is shown. Run on 20 October 2026. The library connector was unavailable during the build, so no library call was made; the scripts did all the computation on the illustrative files. Library behaviors for the optional steps are in `references/tools.md` from outputs saved on 19 October 2026.

Scenario: a digital health company runs a heart failure remote monitoring program in the US and wants a 30-day readmission risk score to rank patients for nurse outreach calls. Index time: the discharge date. No owner, version or fairness criterion was given.

## A1 Cohort, features and data handoff

Request: "Here are our cohort steps, feature dictionary and split. What do we hand to the modeling team?"

```
$ python3 scripts/prep_check.py cohort --steps examples/sample-data/cohort_steps_illustrative.csv
| Step | Rule (your words) | Remaining | Excluded at this step | Share of start excluded | Flags |
|---|---|---|---|---|---|
| S0 | Adults with a heart failure discharge, 1 January 2024 to 30 June 2026, sites A to D | 18420 |  |  | none |
| S1 | Enrolled in remote monitoring within 7 days of discharge | 6310 | 12110 | 65.7% | none |
| S2 | Excluded: discharged to hospice or died in hospital | 6025 | 285 | 1.5% | none |
| S3 | Excluded: fewer than 30 days of follow-up in the observation period | 5730 | 295 | 1.6% | none |
| S4 | Excluded: duplicate person records after linkage | 5790 | -60 | -0.3% | C1 count rises after an exclusion |
| S5 | not given | 5512 | 278 | 1.5% | C2 rule not given |

Start 18420; final 5512; 70.1% of the start excluded in all.
Whether the cohort fits the intended use is the person's call.

$ python3 scripts/prep_check.py features --dict examples/sample-data/feature_dictionary_illustrative.csv
| Feature | Source field | Window (days from index) | Missing code | Flags |
|---|---|---|---|---|
| prior_admissions_12m | encounter.admit_date | -365 to 0 | 0 | none |
| nt_probnp_last | lab.loinc_33762-6 | -30 to 0 | blank | none |
| daily_weight_trend_7d | rpm.weight_kg | -7 to 0 | not given | F4 missing-value code not given |
| age_at_index | person.birth_date | 0 to 0 | not applicable | F6 input measures a characteristic named in 45 CFR 92.210 |
| race_category | person.race_concept_id | 0 to 0 | unknown | F6 input measures a characteristic named in 45 CFR 92.210 |
| discharge_disposition_code | encounter.discharge_disposition | 0 to 2 | not given | F3 window ends after the index time, F4 missing-value code not given, F5 availability at decision time not given |
| days_to_first_nurse_call | outreach.call_date | 0 to 14 | none | F3 window ends after the index time, F5 availability at decision time no |
| readmit_flag_any_30d | encounter.readmit_30d | 0 to 30 | not given | F3 window ends after the index time, F4 missing-value code not given, F5 availability at decision time no, F7 derived from the outcome |
| insurance_type | not given | not given | unknown | F1 source field not given, F2 window not given |

Candidates to refuse (F3, F5 'no' or F7; the person decides): discharge_disposition_code, days_to_first_nurse_call, readmit_flag_any_30d.
Inputs a covered entity must identify and mitigate under 45 CFR 92.210 (F6): age_at_index, race_category.

$ python3 scripts/prep_check.py split --file examples/sample-data/split_illustrative.csv
| Subset | Rows | Patients | Sites |
|---|---|---|---|
| test | 12 | 12 | A, B, C, D |
| train | 24 | 24 | A, B, C |
| tune | 6 | 6 | A, C |

S1 patients in more than one subset: 2 (P005, P012)
S2 sites in both development and test subsets: A, B, C
Whether the split is acceptable for the intended use is the person's call.
```

Short-mode answer (`python3 scripts/prep_check.py words`: 379 words, within the short-mode cap):

> **Answer.** Your cohort runs from 18420 heart failure discharges to 5512 encounters; the remote monitoring enrollment step removes the most (12110, 65.7% of the start). Three features are candidates to refuse for leakage (discharge_disposition_code, days_to_first_nurse_call, readmit_flag_any_30d), two inputs carry a 45 CFR 92.210 duty (age_at_index, race_category), two patients sit in both training and test, and the handoff has no version yet.
> 
> **Cohort rule (yours).** Adults with a heart failure discharge, 1 January 2024 to 30 June 2026, sites A to D; enrolled within 7 days; exclusions as listed; unit of row: encounter. Step S4 (duplicate person records after linkage) shows the count rising from 5730 to 5790 (C1); OMOP expects linkage before the person table is written (OHDSI CDM v5.4 page, community standard, DA-106). Step S5 has no rule (C2). Operational definitions for heart failure and readmission: not given; the FDA RWD guidance on EHR and claims data (July 2024) asks for both a conceptual and an operational definition (CV80).
> 
> **Features.**
> 
> | Feature | Window from index (days) | Missing code | Flags |
> |---|---|---|---|
> | discharge_disposition_code | 0 to 2 | not given | F3, F4, F5 |
> | days_to_first_nurse_call | 0 to 14 | none | F3, F5 no |
> | readmit_flag_any_30d | 0 to 30 | not given | F3, F5 no, F7 |
> | age_at_index, race_category | 0 to 0 | as given | F6 |
> | insurance_type | not given | unknown | F1, F2 |
> 
> Refusals are yours to confirm. For F6 inputs, a covered entity must make reasonable efforts to identify and mitigate discrimination risk from such tools (45 CFR 92.210, PE-113); whether that applies to you is for your legal owner, owner not named.
> 
> **Split.** Train 24, tune 6, test 12 patients. P005 and P012 appear in train and test (S1); sites A, B and C appear in development and test (S2). The FDA AI-enabled device software functions draft of January 2025 proposes independent test data, generally from different sites (DA-39, DA-41, draft).
> 
> **Handoff.** Version: not given (no dataset is handed over without one). Remaining missingness: not given. Who may change the cohort rule: not given; ask.
> 
> **Calls made.** None; the library connector was unavailable on 20 October 2026 and no call was needed. Scripts: prep_check.py cohort, features, split on your files.
> 
> A full version (definitions table, handoff record, EU Article 10 items) is available on request.
> 
> **Record.** Data preparation draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## A2 Statistical and causal analysis plan (uncertainty step)

Request: "In our pilot 42 of 120 enrolled patients met the weight-logging goal. We continue if the probability that the true rate exceeds 0.30 is above 0.8. Our prior is flat; our earlier pilot suggests Beta(6, 24). Does the decision hold?" The numbers, the prior and the rule are the person's.

```
$ python3 scripts/prep_check.py bayes --successes 42 --n 120 --prior 1 1 --alt-prior 6 24 --threshold 0.30 --decision-prob 0.8
Data: 42 of 120 (0.350). Priors are the person's; this run computes, it does not choose.
| Prior | Beta(a, b) | Posterior mean | 95% interval | Pr(rate > 0.3) | Meets your rule Pr > 0.8 |
|---|---|---|---|---|---|
| your prior | Beta(1, 1) | 0.352 | 0.270 to 0.439 | 0.890 | yes |
| alternative 1 | Beta(6, 24) | 0.320 | 0.248 to 0.397 | 0.695 | no |

Your rule gives different answers under the priors listed: keep both results and say which prior reverses it.
```

Reading: under the flat prior the probability is 0.890 and the rule is met; under the earlier-pilot prior it is 0.695 and the rule is not met. Both results are kept, and the earlier-pilot prior reverses the decision (old task DH-05.01.1.3.3). The pilot is not randomized, so the rate is an observed proportion, not an effect of the program. This is not a device or drug trial; the FDA Bayesian documents (device final 2010, DA-127; drug draft January 2026, DA-130, draft) are named only as context.

## B1 Prediction choices (holdout step)

Request: "Check our score on the test set. We use 0.25 as the outreach threshold."

```
$ python3 scripts/prep_check.py holdout --file examples/sample-data/predictions_illustrative.csv --group-col group --threshold 0.25
H1 100 rows are not in a held-out subset (external_test, holdout, internal_test, test) and are left out of every figure below.
| Group | n | Events | Observed rate | Mean predicted | AUROC | Sensitivity | Specificity | PPV | NPV |
|---|---|---|---|---|---|---|---|---|---|
| all | 200 | 51 | 0.255 | 0.238 | 0.801 | 0.784 | 0.671 | 0.449 | 0.901 |
| group=Group 2 | 78 | 27 | 0.346 | 0.286 | 0.737 | 0.815 | 0.510 | 0.468 | 0.839 |
| group=Group 1 | 122 | 24 | 0.197 | 0.208 | 0.831 | 0.750 | 0.755 | 0.429 | 0.925 |
H4 outcome rates differ between groups: a calibrated model cannot have equal sensitivity and specificity at one threshold for both (Paulus and Kent 2020, DA-119, DOI 10.1038/s41746-020-0304-9). Which criterion fits the decision is the person's.
Whether this performance is acceptable is the person's call.
```

Short-mode answer (`python3 scripts/prep_check.py words`: 300 words, within the short-mode cap):

> **Answer.** On the 200 held-out encounters your readmission score has AUROC 0.801 overall, 0.831 in Group 1 and 0.737 in Group 2, where readmissions are more frequent (0.346 against 0.197) and the mean predicted rate sits below the observed rate (0.286 against 0.346). At your threshold of 0.25 the score finds 0.815 of Group 2 readmissions at a specificity of 0.510; your fairness criterion and the reviewer before outreach are still open.
> 
> **Application.** A 30-day readmission risk score that ranks heart failure patients for nurse outreach calls; it allocates a scarce resource, the kind of polar decision where fairness criteria apply (Paulus and Kent 2020, DA-116, DOI 10.1038/s41746-020-0304-9).
> 
> **Held-out result** (script, 100 training rows left out, H1).
> 
> | Group | n | Events | Observed | Mean predicted | AUROC | Sensitivity | Specificity | PPV |
> |---|---|---|---|---|---|---|---|---|
> | All | 200 | 51 | 0.255 | 0.238 | 0.801 | 0.784 | 0.671 | 0.449 |
> | Group 1 | 122 | 24 | 0.197 | 0.208 | 0.831 | 0.750 | 0.755 | 0.429 |
> | Group 2 | 78 | 27 | 0.346 | 0.286 | 0.737 | 0.815 | 0.510 | 0.468 |
> 
> **Your choices.** Threshold 0.25: yours. Fairness criterion: not given. Because the groups' readmission rates differ, a calibrated score cannot have equal sensitivity and specificity in both groups at one threshold (DA-119); choose which criterion fits outreach (equal opportunity, equalized odds or predictive parity; Rajkomar et al. 2018, DA-114, DOI 10.7326/M18-1990). TRIPOD+AI asks for the threshold rationale and the fairness approach to be reported (CV127, DOI 10.1136/bmj-2023-078378). Use limit: not given. Reviewer before a score triggers a call: owner not named.
> 
> **Open items.** Fairness criterion (owner not named, date not given); use limit and reviewer (owner not named, date not given); the split overlap from A1 (P005, P012) before these figures are final.
> 
> **Calls made.** None; scripts: prep_check.py holdout on your file with --group-col group, then with --threshold 0.25.
> 
> A full version (reporting items, choices record) is available on request.
> 
> **Record.** Model choices record draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## B1 Forecasting step

Request: "Does our monthly heart failure admissions forecast beat a naive one?"

```
$ python3 scripts/prep_check.py forecast --file examples/sample-data/forecast_illustrative.csv
| Period | Actual | Forecast | Naive baseline | Interval | Inside |
|---|---|---|---|---|---|
| M13 | 131.0 | 127.0 | 135.0 | 117 to 137 | yes |
| M14 | 126.0 | 130.0 | 135.0 | 120 to 140 | yes |
| M15 | 138.0 | 140.0 | 135.0 | 130 to 150 | yes |
| M16 | 140.0 | 143.0 | 135.0 | 133 to 153 | yes |
| M17 | 133.0 | 122.0 | 135.0 | 112 to 132 | no |
| M18 | 129.0 | 127.0 | 135.0 | 117 to 137 | yes |

Holdout periods 6; history periods 12.
MAE forecast 4.33; MAE naive baseline (last history value) 4.83.
Interval coverage on holdout: 5 of 6 (83.3%); the nominal level is the person's to state.
Whether the forecast is fit for the decision is the person's call.

$ python3 scripts/prep_check.py forecast --file examples/sample-data/forecast_illustrative.csv --season 12
| Period | Actual | Forecast | Naive baseline | Interval | Inside |
|---|---|---|---|---|---|
| M13 | 131.0 | 127.0 | 112.0 | 117 to 137 | yes |
| M14 | 126.0 | 130.0 | 118.0 | 120 to 140 | yes |
| M15 | 138.0 | 140.0 | 121.0 | 130 to 150 | yes |
| M16 | 140.0 | 143.0 | 109.0 | 133 to 153 | yes |
| M17 | 133.0 | 122.0 | 115.0 | 112 to 132 | no |
| M18 | 129.0 | 127.0 | 124.0 | 117 to 137 | yes |

Holdout periods 6; history periods 12.
MAE forecast 4.33; MAE naive baseline (seasonal, lag 12) 16.33.
Interval coverage on holdout: 5 of 6 (83.3%); the nominal level is the person's to state.
Whether the forecast is fit for the decision is the person's call.
```

Reading: on six holdout months the forecast's MAE is 4.33 against 4.83 for the last-value baseline and 16.33 for the seasonal baseline; five of six actuals fall inside the interval. The nominal interval level and whether this is good enough for staffing are the person's.
