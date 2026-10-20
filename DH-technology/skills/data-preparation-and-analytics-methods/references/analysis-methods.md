# Analysis methods: estimands, causal design, Bayesian rules, prediction, personalization and forecasting

Interpretive reference for A2 and B1. Every rule carries its row in `data-and-ai-research.md` (DA), `clinical-study-and-rwe-research.md` (CV) or `therapeutic-mechanism-research.md` (TM). Market tags: [US], [EU], [INTL]. [PAPER] rows carry their own DOI in the Rows cell. No row sets an alpha, a sample size, a prior, a posterior probability for success, an AUROC, a calibration tolerance, a fairness tolerance or a forecast accuracy target (`data-and-ai-research.md`, Not sourced); every such number is the person's.

## 1. The question before the method (estimands)

| Rule | Source and date | Rows |
|---|---|---|
| Intercurrent events occur after treatment starts and affect the interpretation or existence of measurements (for example stopping treatment, rescue therapy) | ICH E9(R1), adopted 20 November 2019 [INTL] | CV31, CV32 |
| An estimand has five attributes: treatment condition and comparator, target population, variable (endpoint), handling of remaining intercurrent events, population-level summary | ICH E9(R1) A.3.3 [INTL] | CV33, CV34 |
| Strategies for intercurrent events: treatment policy, hypothetical, composite variable, while on treatment, principal stratum | ICH E9(R1) A.3.2 [INTL] | CV35 to CV39 |
| The protocol and analysis plan prespecify the main estimator aligned with the primary estimand and a sensitivity analysis | ICH E9(R1) A.6 [INTL] | CV40 |
| Missing data are defined relative to a specific estimand | ICH E9(R1) [INTL] | CV41 |
| Write the causal question (treatment, outcome, population, the decision it changes, a confounder that can be seen and one that cannot) before choosing a method | Old task DH-05.01.1.1.1 (method, not a source row) | none |

ICH E9(R1) is written for clinical trials; for an observational analytics question it is used as a checklist and labeled so.

## 2. A design the data can support

| Rule | Source and date | Rows |
|---|---|---|
| A non-interventional (observational) study uses the product in routine practice without protocol-assigned intervention | FDA RWE considerations guidance, August 2023 (drugs and biologics) [US] | CV73, CV74 |
| The protocol and analysis plan are finalized before prespecified analyses; FDA must be confident that data sources or analyses were not chosen to favor a conclusion | Same guidance [US] | CV75 |
| Device RWD sources include EHRs, claims, registries and DHT data; RWD can support randomized, single-arm, observational and hybrid designs | FDA CDRH RWE device guidance, final, 18 December 2025 [US] | CV88, CV89 |
| State whether there is an experiment, a natural experiment or only observational rows; name the method that fits that fact; refuse a causal claim the design cannot support and say what is estimated instead | Old task DH-05.01.1.1.2 (method, not a source row) | none |
| Report the estimate, the interval and the sample; the assumption that, if wrong, reverses the decision; the code and data version | Old task DH-05.01.1.1.3 (method, not a source row) | none |

`[GAP]`: no source row in this skill gives the assumptions of difference-in-differences, matching, instrumental variables or regression discontinuity. The method named stays the person's or their statistician's choice; the skill records it and the assumption the person names.

## 3. Covariate adjustment

| Rule | Source and date | Rows |
|---|---|---|
| Final guidance, May 2023, for randomized trials of drugs and biological products | FDA covariate adjustment guidance [US; context for devices and analytics] | DA-121 |
| An unadjusted primary analysis is acceptable; adjustment generally narrows confidence intervals | Same | DA-122 |
| Prespecify the covariate-adjusted analysis before any unblinding | Same | DA-123 |
| Adjust for covariates expected to be most strongly associated with the outcome; include randomization strata variables | Same | DA-124, DA-125 |

## 4. Bayesian analysis and priors

| Rule | Source and date | Rows |
|---|---|---|
| Devices: final guidance issued 5 February 2010; no device-specific update found in this pass | FDA Bayesian statistics in medical device trials [US] | DA-126 |
| Devices: the prior information and the model are prespecified and agreed; meet FDA early | Same | DA-127 |
| Devices: evaluate operating characteristics, including type I and type II error rates, in planning | Same | DA-128 |
| Drugs and biologics: draft guidance, January 2026, docket FDA-2025-D-3217; not for devices | FDA Bayesian methodology draft [US] | DA-129 |
| Drug draft: success is most often a posterior probability that the effect exceeds a threshold, Pr(d > a) > c | Same draft | DA-130 |
| Drug draft: the default frequentist criterion may not fit with borrowing; calibration to type I error is one option | Same draft | DA-131 |
| Use no prior that cannot be cited; refit with a stated alternative prior or none; keep both results; do not hide a result that reverses the decision | Old tasks DH-05.01.1.3.1 and DH-05.01.1.3.3 (method, not source rows) | none |

The two FDA Bayesian documents are not cross-applied (`data-and-ai-research.md`, Changes and conflicts item 11). The script `bayes` computes the beta-binomial posterior for a rate under the person's prior and every alternative they name, and whether the person's rule (their a and c) gives the same answer under each.

## 5. Regression and prediction models

| Rule | Source and date | Rows |
|---|---|---|
| TRIPOD+AI: 27 main items (52 subitems) for prediction models using regression or machine learning; supersedes TRIPOD 2015 | Collins et al. 2024 [PAPER] [INTL] | CV124, DOI 10.1136/bmj-2023-078378 |
| State the target population, intended purpose in the care pathway and intended users; describe known health inequalities | TRIPOD+AI items 3b, 3c | CV125, DOI 10.1136/bmj-2023-078378 |
| Justify study size separately for development and evaluation; describe missing-data handling | TRIPOD+AI items 10, 11 | CV126, DOI 10.1136/bmj-2023-078378 |
| Specify performance measures and plots with rationale (discrimination, calibration, clinical utility), fairness approaches, and the model output with threshold rationale | TRIPOD+AI items 12e, 14, 15 | CV127, DOI 10.1136/bmj-2023-078378 |
| PROBAST+AI: four domains (participants and data sources, predictors, outcome, analysis), 34 signalling questions and six applicability items; supersedes PROBAST-2019; yes or probably yes means low concern | Moons et al. 2025 [PAPER] [INTL] | DA-76 to DA-79, DOI 10.1136/bmj-2024-082505 |
| CLAIM 2024: each item answered Yes, No or Not Applicable (imaging AI) | Tejani et al. 2024 [PAPER] [INTL] | DA-85, DOI 10.1148/ryai.240300 |
| Metrics chosen starting with the most significant risks; risks that will not or cannot be measured are documented; test sets, metrics and tools documented | NIST AI RMF 1.0, January 2023, voluntary [US] | DA-12, DA-13 |
| The draft proposes describing the reference standard and its uncertainty | FDA AI-enabled device software functions draft, January 2025 [US] | DA-42 |
| For high-impact uses such as a primary endpoint, test on prospectively generated data from a representative setting; transparent models preferred, black-box models acceptable when interpretable ones perform unsatisfactorily | EMA reflection paper, 2024 [EU, medicinal products] | DA-72, DA-75 |
| Specifications say how to build and calculate a measure; describe scoring direction; descriptive statistics show data are available but are not evidence of reliability or validity | CMS Measures Management System Hub [US, quality measures; context elsewhere] | DA-132, DA-137, DA-139 |
| Name the outcome, unit of row, predictors used and not used, and the use (description or prediction); fit on a stated sample with a stated holdout; choose the metric before training; report the group harmed by a miss; write where the model must not be used and who may promote it | Old tasks DH-05.01.1.2.1 to .3 and DH-05.01.2.1.1 to .3 (method, not source rows) | none |

## 6. Fairness and subgroups

| Rule | Source and date | Rows |
|---|---|---|
| Three fairness axes: equal outcomes, equal performance, equal allocation; equal performance types are equal sensitivity (equal opportunity), equal sensitivity and specificity (equalized odds), equal PPV (predictive parity) | Rajkomar et al. 2018 [PAPER] [INTL] | DA-113, DA-114, DOI 10.7326/M18-1990 |
| Fairness concerns apply to polar decisions such as allocating scarce resources; criteria are mutually incompatible | Paulus and Kent 2020 [PAPER] [INTL] | DA-116, DOI 10.1038/s41746-020-0304-9 |
| Statistical parity is the least rigorous notion; equalized odds conditions on the outcome | Same paper | DA-117, DA-118, DOI 10.1038/s41746-020-0304-9 |
| For any single threshold, a well-calibrated model will never have the same sensitivity and specificity for two groups with different outcome rates | Same paper | DA-119, DOI 10.1038/s41746-020-0304-9 |
| The draft proposes evaluating performance across subgroups, because good overall performance can mask poor subgroup performance | FDA AI-enabled device software functions draft, January 2025 [US] | DA-38, DA-43 |
| Instructions for use give performance for specific persons or groups when appropriate | EU AI Act Article 13(3)(b)(v) [EU; from 2 December 2027 or 2 August 2028, DA-67] | DA-57 |
| Measure developers always consider stratifying by social, economic and geographic characteristics | CMS Measures Management System Hub [US, context] | DA-136 |

When the person asks for more than one fairness criterion and the groups' outcome rates differ, state DA-119 and ask which criterion fits the decision; the script `holdout` prints flag H4 when the rates differ.

## 7. Recommendation and personalization

| Rule | Source and date | Rows |
|---|---|---|
| Adaptive interventions have four components: decision points, intervention options, tailoring variables and decision rules; proximal and distal outcomes guide their design | Nahum-Shani et al. 2018 [PAPER] [INTL] | TM77 to TM84, DOI 10.1007/s12160-016-9830-8 |
| Decision rules specify which option to offer, for whom and when; this is what a rule engine implements | Same paper | TM82, DOI 10.1007/s12160-016-9830-8 |
| Include proximal outcomes for engagement and intervention fatigue; receptivity is the transient ability or willingness to use support | Same paper | TM86, TM87, DOI 10.1007/s12160-016-9830-8 |
| Unreliable tailoring variables make a rule little better than random; plan the rule's behavior when tailoring data are missing | Same paper | TM88, TM89, DOI 10.1007/s12160-016-9830-8 |
| A micro-randomized trial randomizes options at many decision points to estimate causal effects on proximal outcomes | Same paper | TM90, DOI 10.1007/s12160-016-9830-8 |
| Planned personalization, titration or adaptation is described (what, why, when, how) | TIDieR item 9 (EQUATOR checklist file) [INTL] | TM30 |
| MOST sets an optimization objective in preparation, an operational definition of the best intervention under resource constraints (for example "Most effective for under $400 per person"); EASE balances effectiveness against affordability, scalability and efficiency | Collins, Kugler and Gwadz 2016; Guastaferro and Collins 2021 [PAPER] [INTL] | TM66 to TM69, DOI 10.1007/s10461-015-1145-4; TM74, TM75, DOI 10.1177/26334895211054363 |
| Overseers can disregard, override or reverse output; they stay aware of automation bias, especially for recommendations | EU AI Act Article 14(4)(b), (d), (e) [EU; dates DA-67] | DA-60, DA-61 |
| Systems that keep learning after release reduce biased outputs feeding future inputs (feedback loops) | EU AI Act Article 15(4) [EU] | DA-63 |
| High-risk systems allow automatic event logs over their lifetime, supporting post-market monitoring | EU AI Act Article 12(1), 12(2) [EU] | DA-54, DA-55 |
| Report user agreement with the AI and reasons users varied from its recommendations | DECIDE-AI (Vasey et al. 2022) [PAPER] [INTL] | DA-82, DOI 10.1136/bmj-2022-070904 |
| Name the user, the item and the objective (a completed task, not a click); state the inputs the policy may use, the rule or model version and how a person refuses; log role, item, policy version, time and accept, dismiss or no action | Old tasks DH-05.01.2.2.1 to .3 (method, not source rows) | none |

A therapeutic decision rule inside a DTx (dose, intervention options for a clinical outcome) routes to `dh-clinical-development` therapeutic-mechanism-and-intervention-design; this skill covers analytics personalization (content, outreach, next step) and records the policy.

## 8. Forecasting and optimization

| Rule | Source and date | Rows |
|---|---|---|
| Name the quantity, grain, horizon, the decision that uses it and the baseline to beat (last period, seasonal naive); fit on a stated history; report the point and interval on a holdout horizon against the same baseline; never report accuracy on the history fitted | Old tasks DH-05.01.2.3.1 and .2 (method, not source rows) | none |
| Name the decision variables, the constraint (capacity, safety stock, fairness, budget) and who may relax it; never return an optimum that breaks a safety constraint | Old task DH-05.01.2.3.3 (method, not a source row) | none |

`[GAP]`: no source row in this skill gives forecasting methods, interval methods or optimization solvers. The script `forecast` computes MAE of the person's forecast and of a last-value or seasonal naive baseline on the person's holdout periods, and interval coverage; the nominal coverage and any accuracy target are the person's.
