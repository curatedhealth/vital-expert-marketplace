# A1 Intended use and validation plan

Framework task: DH-01.04.3.1, Part A, task A1. Carries the old tasks "DH-01.04.3.1.1 Clinical model intended use" and "DH-01.04.3.1.2 Validation dataset".

## What this task delivers

The model's intended use written from the person's facts (user, input, output, the decision it may support, the decision it must not make, population), the data plan checked against the sourced rules (split, independence of the test set, reference standard, subgroups, sample size reasoning, missing data), the metrics the person names before the run, and every gap. With the person's dataset manifest, `scripts/model_check.py split` checks for patients in both development and test data, site or time overlap against the claim, and populations absent from the test set. It answers "what exactly is this model for, and is our test data fit to show it?"

Why it matters: the FDA draft guidance warns that leakage between development and test data "can create uncertainty regarding the true performance" (FDA AI-enabled device software functions draft, January 2025, DA-39). A model validated on rows it was trained on, or for "clinical decision support" with no decision named, has no result that means anything.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `clinical-algorithm-validator` (old DH-01.04.3.1.1 and .2). Work as a clinical model validation analyst who checks the plan against sourced rules |
| Skill | DH-01.04.3.1 Part A, Intended use and validation plan |
| Workflow | The steps below |
| Knowledge | `references/validation-rules.md` sections 1 to 8; rows DA-06, DA-10 to DA-13, DA-26, DA-35 to DA-43, DA-47 to DA-53, DA-67, DA-72 to DA-74, DA-76 to DA-86, DA-113 to DA-120, CV124 to CV128; `references/gap-rules.md`; `references/governance.md` |
| Tools | `regulatory-dh.search_devices` only to read the person's own or a named comparable authorization; `scripts/model_check.py split`, `words` |
| Prompt | This guide |
| Template | `assets/intended-use-and-validation-plan-output.md` |
| Input | The request and its context: model purpose, users, inputs, output, the decision, the population, markets, development and test data description or a manifest (record_id, patient_id, site, date, split, subgroup columns), the claim for the test set (external by site, temporal, internal), the reference standard, the metrics the person names and the date named |
| Governance | `references/governance.md`; the person decides adequacy |
| Catalogue job | none (no saved `list_jobs` entry for model validation; needs a live check) |

## The rule that shapes this task: say what the data can show

The model never declares a test set adequate and never supplies a metric value to aim for. It writes back what the person said, checks it against the rows, runs the split check on their manifest, and names each gap. Adequacy, the metrics and their values are the person's.

## Workflow

### Step 1. Intended use back (old "Clinical model intended use")

Write the user, the input, the output, the decision the output may support, the decision it must not make, and the population, each in the person's words or "not given". If the stated use is "clinical decision support" with no decision named, write "decision not named `[GAP]`; the model cannot be validated against it" (old task DH-01.04.3.1.1). Check against NIST MAP 1.1 and MAP 2.2 (DA-10, DA-11; voluntary) and TRIPOD+AI items 3b and 3c (Collins et al. 2024, DOI 10.1136/bmj-2023-078378, CV125). If the person names an authorized product, call `regulatory-dh.search_devices {query: "NAME", jurisdiction: "all", limit: 10}` and quote the record (number, decision, date, product code, "library, retrieved DATE"); the record holds no AI flag, validation data or intended-use text, so never infer them. Device status questions route to `dh-regulatory-and-quality` regulatory-pathway-and-classification.

### Step 2. The words for the data subsets

Name each subset as training, tuning, internal test, external test (site) or external test (time). "Validation" is used differently by NIST, EMA, CLAIM 2024 and the FDA draft (DA conflicts 5; CLAIM 2024, DOI 10.1148/ryai.240300, DA-86).

### Step 3. The data plan against the rows (old "Validation dataset")

Lay out the plan in a table: source, inclusion rule and count (old task), split description (DA-40, draft), independence and sequestration of the test set (DA-39, draft), sites (DA-41, draft), early split before aggregate processing (DA-74, EMA, medicines), single use of the test set (DA-73, EMA), prospective data for high-impact uses (DA-72, EMA), reference standard and its uncertainty (DA-42, draft), sample size reasoning and missing data (TRIPOD+AI items 10 and 11, CV126), differences between development and evaluation data (item 16, CV128). For a product in the EU, add Article 10(2) to 10(4) of the AI Act with the date it applies to AI in Annex I devices, 2 August 2028 as amended by Regulation (EU) 2026/1744 (DA-47 to DA-50, DA-67). Each cell is the person's fact or "not given".

### Step 4. Run the split check on the manifest

With code execution: `python3 scripts/model_check.py split --manifest MANIFEST.csv --claim external|temporal|internal --groups COL1,COL2`. Report the split table and each flag: S0 no test label, S1 patients in test and development, S2 shared site under an external claim, S3 test dates not after development dates under a temporal claim, S4 internal testing only, S5 a group present in development and absent from the test set ("not validated `[GAP]`"). The flags are facts about the manifest; whether the set is adequate is the person's call. Without a manifest, list the checks the person can run.

### Step 5. Subgroups and the fairness question

List the subgroups the intended use names and the counts per split. Subgroup evaluation (DA-38, DA-43, draft). Ask which fairness criterion fits the decision (equal sensitivity, equalized odds, predictive parity, calibration within groups; DA-114, DA-117, DA-118); state the impossibility row when two criteria are asked at once (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-119). The tolerance is the person's.

### Step 6. Metrics named before the run

Write back the metrics the person names, the date named, and the operating threshold with its rationale (TRIPOD+AI items 12e and 15, CV127): discrimination, calibration, clinical utility. Values to aim for are "not given" unless the person gives them; no source sets them. Name the appraisal and reporting checklists that fit (PROBAST+AI, DOI 10.1136/bmj-2024-082505, DA-76 to DA-79; DECIDE-AI for early live evaluation, DOI 10.1136/bmj-2022-070904, DA-80; CLAIM 2024 for imaging, DA-85).

## Build the output

Follow `assets/intended-use-and-validation-plan-output.md`. Answer first: the intended use in one line (or what is missing from it), the split check flags that matter most, the populations not validated, and the inputs still needed from the person. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/model_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Intended use, metrics, thresholds and adequacy are the person's, and the plan says so.
- Every draft guidance is labeled draft with its date; EU AI Act dates carry the act that set them.
- Every split flag comes from the script output or the person's stated facts, not from estimation.
- Each absent population is written "not validated `[GAP]`".
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry the DOI.
- `python3 scripts/model_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Cohort rules, feature engineering and data quality checks: `data-preparation-and-analytics-methods` and `data-quality-monitoring` (this pack).
- Whether the product is a device and its pathway: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- A clinical study of the model: `dh-clinical-development` study-protocol-and-endpoint-design.
