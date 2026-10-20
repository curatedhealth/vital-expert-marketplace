# B1 Prediction, personalization and forecasting choices

Framework task: DH-05.01.2 Machine Learning Applications, Part B, task B1. Carries the old tasks "DH-05.01.2.1.1 Prediction target", "DH-05.01.2.1.2 Train and holdout", "DH-05.01.2.1.3 Score limit", "DH-05.01.2.2.1 Recommendation unit", "DH-05.01.2.2.2 Policy", "DH-05.01.2.2.3 Recommendation log", "DH-05.01.2.3.1 Forecast target", "DH-05.01.2.3.2 Forecast and interval" and "DH-05.01.2.3.3 Optimization constraint".

## What this task delivers

A record of the person's choices for one machine learning application, with the facts behind each: for a prediction or classification model, the label rule and exclusions, the holdout result computed on held-out rows only (overall and for the group harmed by a miss) at the person's threshold, the fairness criterion they choose, and the use limit with the reviewer who must look before a score triggers an action; for recommendation and personalization, the unit, the objective, the policy (inputs, rule or model version, how a person refuses) and the log; for forecasting and optimization, the target, horizon, baseline, the holdout comparison and the constraint with who may relax it. It answers "what will this model do, how did it do on data it never saw, and where must it stop?"

Why it matters: training-set performance reported as the result, an average that hides the group a miss harms, or a score wired to a clinical action with no reviewer each turn a model into a risk the team did not choose.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `clinical-algorithm-validator` (old DH-05.01.2.1.1 to DH-05.01.2.3.3). Work as a model reviewer who records the person's choices against sourced requirements |
| Skill | DH-05.01.2 in this competency, Part B, Prediction, personalization and forecasting choices |
| Workflow | The steps below |
| Knowledge | A1 output; `references/analysis-methods.md` sections 5 to 8; `references/data-requirements.md` section 3; rows CV124 to CV128, DA-12, DA-13, DA-38, DA-42, DA-43, DA-54, DA-55, DA-57, DA-60 to DA-63, DA-72, DA-75 to DA-86, DA-113 to DA-120, TM30, TM66 to TM69, TM74, TM75, TM77 to TM90 |
| Tools | `scripts/prep_check.py holdout`, `forecast`, `split`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/prediction-personalization-and-forecasting-choices-output.md` |
| Input | The request and its context: the application type, A1 handoff, the person's predictions or forecast file, the threshold, fairness criterion, use limit, reviewer, policy, constraint and who may relax it |
| Governance | `references/governance.md`; every choice is the person's; no deployment verdict |
| Catalogue job | none |

## The rule that shapes this task: people choose

The person chooses the label, the metric, the threshold, the fairness criterion, the use limit, the reviewer, the recommendation objective and the constraint. The model lays out what the sources require, computes on the person's held-out data and writes the choices down. It never sets a threshold, never calls performance acceptable and never connects a score to an action without the reviewer the person names. Where two readings are possible, it shows both and writes "your call".

## Workflow

### Step 1. Which application, and is it a device?

Name the type (prediction or classification, recommendation or personalization, forecasting or optimization) and the action it drives. If the output informs diagnosis or treatment of a patient, the device question routes to `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control and model validation to `clinical-ml-model-development-and-validation` (this pack); this task still records the person's choices.

### Step 2. Prediction and classification (old "Prediction target", "Train and holdout", "Score limit")

- **Label rule.** Event, time window, unit; written so two people would label a row the same way; excluded rows (insufficient follow-up, wrong population). A proxy label names what it is a proxy for; name label bias where outcome ascertainment differs by group (DA-115, DA-120).
- **Holdout.** Confirm the split from A1 (`split` flags S1, S2). Run `python3 scripts/prep_check.py holdout --file PRED.csv --group-col GROUP [--threshold T]`. Report AUROC and observed versus mean predicted rate per group on held-out rows only (H1 says how many rows were left out); sensitivity, specificity, PPV and NPV only at the person's threshold (H2 if none). Report the group a miss harms, not only the average (old task; DA-43, draft). Lay the TRIPOD+AI items beside the result: intended purpose and users, sample size rationale, missing data, discrimination, calibration and clinical utility, fairness approach, threshold rationale, development versus evaluation differences (CV125 to CV128, DOI 10.1136/bmj-2023-078378).
- **Fairness.** Ask which criterion fits the decision (equal opportunity, equalized odds, predictive parity, calibration; DA-113, DA-114). If the groups' outcome rates differ (H4), state that a calibrated model cannot equalize sensitivity and specificity at one threshold (DA-119, DOI 10.1038/s41746-020-0304-9) and that the choice is the person's.
- **Score limit.** Who may see the score and what action it may trigger; the population outside the training support; the reviewer the person names before any action (or owner not named). For the EU, human oversight lets users disregard or override output and keep automation bias in view (DA-60, DA-61; applies from 2 December 2027 or 2 August 2028, DA-67).

### Step 3. Recommendation and personalization (old "Recommendation unit", "Policy", "Recommendation log")

Write the user, the item and the objective (a completed task, not a click) and one recommendation the system will not make. Write the policy in the adaptive-intervention terms: decision points, options, tailoring variables, decision rules, proximal and distal outcomes (TM77 to TM84, DOI 10.1007/s12160-016-9830-8); the rule's behavior when a tailoring variable is missing (TM89); proximal outcomes for engagement and fatigue (TM87); the inputs the policy may use and whether users were told about them; the rule or model version; how a person refuses. If the person wants to learn which options work, name the micro-randomized trial (TM90) or MOST with an optimization objective they set (TM69, TM74, TM75) as options, not recommendations. The log: user role, item, policy version, time, accept, dismiss or no action, kept long enough to review a complaint (old task; DECIDE-AI user agreement item, DA-82; EU logging duty for high-risk systems, DA-54, DA-55). A system that keeps learning from its own outputs names the feedback-loop risk (DA-63).

### Step 4. Forecasting and optimization (old "Forecast target", "Forecast and interval", "Optimization constraint")

Quantity, grain, horizon, the decision that uses it and the baseline (last period or seasonal naive). Run `python3 scripts/prep_check.py forecast --file FC.csv [--season K]`: MAE of the forecast and of the naive baseline on holdout periods, interval coverage, flags FC1 to FC3. Accuracy on fitted history is never the result. For optimization: decision variables, the constraint (capacity, safety stock, fairness, budget) and who may relax it, the person named or owner not named; an optimum that breaks a safety constraint is not reported as a solution. No source row in this skill gives forecasting or solver methods (`[GAP]`).

### Step 5. The choices record

One table of the person's choices with the facts behind each, the open items (each with the owner the person names or owner not named, and a date or "not given"), and the decisions still to make. Propose nothing unless asked; label any proposal "proposed".

## Build the output

Follow `assets/prediction-personalization-and-forecasting-choices-output.md`. Answer first: the application and the action it drives, the holdout or forecast figures computed on held-out data with the group a miss harms, and the choices still open (threshold, fairness criterion, reviewer, constraint owner). Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/prep_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every figure is from the script on held-out rows or periods; training rows and fitted history are left out.
- No threshold, no fairness tolerance, no "acceptable", no deployment verdict.
- The fairness impossibility row is stated when the groups' outcome rates differ.
- Each choice is labeled as the person's; proposals are labeled "proposed".
- `python3 scripts/prep_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry their DOI.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Device-grade validation, PCCP and submissions: `clinical-ml-model-development-and-validation` (this pack); `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Performance and drift once deployed: `model-performance-and-drift-monitoring` (this pack).
- Decision support products and their adoption: `analytics-products-and-decision-support` (this pack).
- Therapeutic decision rules for a DTx: `dh-clinical-development` therapeutic-mechanism-and-intervention-design.
