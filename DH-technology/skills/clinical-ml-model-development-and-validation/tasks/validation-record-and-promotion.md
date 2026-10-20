# B1 Validation record and promotion

Framework task: DH-01.04.3.1 and DH-01.04.2.1, Part B, task B1. Carries the old tasks "DH-01.04.3.1.3 Validation record", "DH-01.04.2.1.1 Model promotion rule", "DH-01.04.2.1.2 Pipeline run" and "DH-01.04.2.1.3 Drift watch".

## What this task delivers

The validation record: the metrics the person named before the run, computed on their locked test set (`scripts/model_check.py evaluate`), overall and per subgroup, each read against the person's acceptance criteria as met or not met (or "criteria not given"); the fairness reading on the criterion they chose, with the impossibility row where criteria conflict; the model version and the person who accepts the record. Then the promotion rule, the run record and the drift watch written in the person's words, with every threshold theirs. It answers "what did our model do on our locked test set against what we said in advance, who accepts it, and how does it get promoted and pulled back?"

Why it matters: the old task was plain: "Do not add a metric after the run to improve the story." A record that reports only the metric that looks good, or a promotion with no run id and no pull-back signal, cannot be defended later.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `clinical-algorithm-validator` (old DH-01.04.3.1.3, DH-01.04.2.1.1 to .3). Work as a clinical model validation analyst who computes on the person's data and records their decisions |
| Skill | DH-01.04.3.1 and DH-01.04.2.1 Part B, Validation record and promotion |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/validation-rules.md` sections 5, 6, 8 and 9; rows DA-08, DA-13, DA-14, DA-16, DA-37, DA-43 to DA-46, DA-54 to DA-57, DA-62, DA-65 to DA-67, DA-70, DA-71, DA-87 to DA-92, DA-113 to DA-120, CV127, US-03 to US-13, US-37, US-38, UK-10; `references/governance.md` |
| Tools | `scripts/model_check.py evaluate`, `words`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/validation-record-and-promotion-output.md` |
| Input | The request and its context: the locked test predictions (CSV: id, y, p, subgroup columns), the criteria file the person wrote (operating threshold, acceptance criteria with the date written, fairness criterion), the run date, model version, code and data versions, run id, approver, the promotion stages and who may promote, the drift signal, threshold and action |
| Governance | `references/governance.md`; the person accepts or rejects |
| Catalogue job | none (no saved `list_jobs` entry; needs a live check) |

## The rule that shapes this task: people decide acceptance

Acceptance criteria, the operating threshold, the fairness criterion, the drift threshold and the release decision are the person's. The model computes and compares; it never supplies a value to compare against, never marks a result against proposed criteria, and never calls a model validated, fair or ready to release.

## Workflow

### Step 1. Confirm what was named before the run

Write back each metric, operating threshold and acceptance criterion with the date the person wrote it, and the run date. A metric named after the run is flagged as a fact (old task DH-01.04.3.1.3; the script prints E1). Criteria labeled proposed are not applied. If no criteria were given, write "acceptance criteria not given; values reported, nothing marked met or not met".

### Step 2. Compute on the locked test set

With code execution: `python3 scripts/model_check.py evaluate --predictions PRED.csv --criteria CRITERIA.json --groups COL1,COL2`. Report n, events, event rate, AUROC with interval, observed to expected ratio, calibration intercept and slope, Brier score, and at the person's threshold sensitivity, specificity, PPV and NPV with intervals, overall and per group. These cover discrimination and calibration (TRIPOD+AI item 12e, Collins et al. 2024, DOI 10.1136/bmj-2023-078378, CV127); clinical utility needs the person's decision model and is "not computed" unless they give it. Say the interval methods are computation methods, not sourced rules, and give each group's event and non-event counts beside its values so the reader sees how wide the intervals are.

### Step 3. Read against the person's criteria

For each criterion: observed value, met or not met, "your criterion, written DATE". Populations absent from the test set (A1 flag S5) are "not validated `[GAP]`" (old task DH-01.04.3.1.2). Good overall performance can mask poor subgroup performance (FDA draft, January 2025, DA-43).

### Step 4. Fairness on the criterion the person chose

Report the subgroup values for the criterion the person named. Where outcome rates differ between groups and the person asks for calibration and equal error rates together, state: "for any single threshold, a well-calibrated prediction model will never have the same sensitivity and specificity for two groups with different outcome rates" (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-119), and ask which criterion fits the decision. The tolerance is the person's; none is sourced.

### Step 5. The record (old "Validation record")

Metric, dataset version, model version, run id, the result against each criterion, populations not validated, and the person who accepts the record, as the person names them ("not given" otherwise). The acceptance decision is the person's; this is a draft for that person.

### Step 6. Promotion rule and run record (old "Model promotion rule", "Pipeline run")

Write the stages (experiment, validation, production), the record each stage requires (dataset version, metric, approver), who can promote and who cannot, in the person's words; never from a notebook path. The run record: code version, data version, holdout metric, approver or "not approved", run id; a previous run's metric is never overwritten (old tasks DH-01.04.2.1.1 and .2). NIST MEASURE 2.1 asks that test sets, metrics and tools be documented (DA-13; voluntary). The release pipeline and IEC 62304 records are `medical-software-lifecycle-and-delivery` (this pack).

### Step 7. Drift watch (old "Drift watch")

Write the input or outcome watched (a metric the product logs), the threshold the person sets, who is paged, and what they may do: retrain, roll back, or stop the decision (old task DH-01.04.2.1.3). Context from the rows: data drift and performance change (FDA draft, DA-37, DA-44, DA-45); calibration drift and when recalibration fits (Davis et al. 2017, DOI 10.1093/jamia/ocx030, DA-91, DA-92); EU AI Act logging and post-market monitoring (Articles 12 and 72, DA-54, DA-55, DA-65, DA-66). A watch threshold is "not given" until the person gives it. Whether a retrain needs a new submission or fits a PCCP is `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.

## Build the output

Follow `assets/validation-record-and-promotion-output.md`. Answer first: the result on each of the person's criteria (or "criteria not given"), the subgroup or population that limits the record, the fairness reading on their criterion, who accepts (or "not given"), and the promotion and watch elements still missing. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/model_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every number comes from the script output on the person's file.
- Every criterion and threshold is the person's, with the date they wrote it; none supplied, none proposed applied.
- No "validated", "fair", "safe" or "ready to release".
- Populations not validated are listed.
- The impossibility row is stated where fairness criteria conflict.
- `python3 scripts/model_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Watching the released model: `model-performance-and-drift-monitoring` (this pack).
- Governance controls and bias questions beyond the metrics: `responsible-ai-governance` (this pack).
- PCCP, retraining under an authorization, submissions: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Any model card, labeling or external wording: stops for the owner the person names.
