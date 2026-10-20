# A2 Subgroup performance test

Framework task: DH-01.04.1.1, Part A, task A2. Carries the old task "DH-01.04.1.1.2 Bias test" (name the dataset and the model version; report the error rate for each group you can see; do not report a group marked [GAP]; do not average the groups into one number and stop).

## What this task delivers

On the person's own scored data, for a named model version, dataset version and decision threshold: per-group counts, outcome rate, sensitivity, specificity, PPV, NPV, false negative and false positive rates, selection rate and calibration-in-the-large (mean score against observed rate), each rate with its count and a 95% interval; differences and ratios against the reference group the person names; the groups the data cannot show, listed as `[GAP]`; and the conflict between fairness criteria when outcome rates differ. It answers "on our data, how does the model perform for each group, and what does that let us say?"

Why it matters: FDA's draft says acceptable performance in some subgroups can mask lower performance in others when only the total population is evaluated (FDA draft, 7 January 2025, DA-43, draft), and the AI Act asks providers to examine data for possible biases and to state, when appropriate, performance for specific groups (AI Act Art 10(2)(f), DA-48; Art 13(3)(b)(v), DA-57; both apply from the Chapter III dates, AI EU-19). A table by group is the evidence; a single overall figure is not.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `ai-ml-governance-director` (old DH-01.04.1.1.2). Work as an AI governance analyst who computes on the person's data |
| Skill | DH-01.04.1.1 Part A, Subgroup performance test |
| Workflow | The steps below |
| Knowledge | `references/responsible-ai-rules.md` section 3; rows DA-12, DA-13, DA-38 to DA-43, DA-48 to DA-53, DA-57, DA-73, DA-74, DA-86, DA-113 to DA-120, CV126 to CV128, EN-108, EN-111, EN-112 |
| Tools | `scripts/subgroup_check.py groups` on the person's file; no library call |
| Prompt | This guide |
| Template | `assets/subgroup-performance-test-output.md` |
| Input | The request and its context: the scored file, the group, outcome and score (or prediction) columns, the model version, the dataset version and data cut, the decision threshold, the reference group, groups the data cannot show |
| Governance | `references/governance.md`; no pass or fail without the person's rule |
| Catalogue job | none |

## Read the request

- **The file.** One row per case: a group column, a 0/1 outcome column, a score (0 to 1) or a 0/1 prediction column. Several group attributes: run once per attribute; intersections only if the person asks and names them.
- **Versions.** Model version and dataset version (with data cut). Missing: "not given"; the result cannot be tied to a release until they are given.
- **Threshold.** The threshold the person uses in practice. Never defaulted: without it the script reports outcome rates and calibration only.
- **Reference group.** The group the person compares against. Not given: no differences are computed; ask.
- **Which data subset.** Name it as the person does, then say which subset it is (development, tuning, internal test, external test from other sites). The word "validation" means different things across sources (research file conflict 5; CLAIM 2024 prefers "internal testing" and "external testing", DA-86, DOI 10.1148/ryai.240300).

## Workflow

### Step 1. Write the test back

Model version, dataset version and data cut, the subset and whether it came from sites other than development (FDA draft, DA-41, draft), threshold, reference group, groups compared, groups unseen. Missing: "not given".

### Step 2. Run the computation

`python3 scripts/subgroup_check.py groups --data FILE --group-col COL --label-col COL --score-col COL --threshold T --reference GROUP --dataset-version V --model-version M --gap-groups "G1,G2"`. Without code execution, compute the same counts by hand from the person's confusion matrix per group and show the arithmetic. Report every group the data holds, the "group not recorded" line, and each `[GAP]` group as not tested.

### Step 3. Read what the numbers can carry

- Give each rate with its count (for example "0.312, 10 of 32") and its interval; a wide interval is stated, never judged against a size the person did not set.
- Differences and ratios against the person's reference group, as the script prints them.
- Calibration-in-the-large: mean score against observed rate per group (O/E). If the scores are not meant as probabilities, say so and do not read O/E.
- Where outcome rates differ between groups, state the impossibility result: a well-calibrated model cannot have equal sensitivity and specificity at one threshold for groups with different outcome rates (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-119). Name the criteria in play: equal opportunity, equalized odds, predictive parity (Rajkomar 2018, DOI 10.7326/M18-1990, DA-114), statistical parity (DA-117). Which fits the decision is the person's (DA-116).
- Possible label bias: if the outcome depends on access to testing or care that differs by group, say the error rates may reflect the label as well as the model (DA-115, DA-120).

### Step 4. What the test does not show

One line each: groups not tested (`[GAP]`); whether the test set was used before (EMA: the hold-out test set is used once, DA-73, medicinal product context); whether development and test data differ in setting, eligibility, outcome or predictors (TRIPOD+AI item 16, CV128); whether the sample size was justified (TRIPOD+AI item 10, CV126). The model never adds a pass or a fail.

### Step 5. Data used to find the groups (EU)

If the group attribute is special-category data (for example ethnicity) and the market is the EU: the AI Act conditions now in Article 4a (other data will not do, pseudonymization, access controls, no transfer, deletion after correction, records of why; DA-51, DA-52), Article 4a's start date an open reading point, and the GDPR DPIA duty (EN-111, EN-112). Whether the processing is lawful: "for your legal owner".

## Build the output

Follow `assets/subgroup-performance-test-output.md`. Answer first: the largest difference against the reference group with its counts, the groups unseen, and whether outcome rates differ (so the criteria conflict). Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/subgroup_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Model version, dataset version, threshold and reference group are the person's, or "not given".
- Every group the data holds is reported, with counts; "group not recorded" has its own line; `[GAP]` groups are listed as not tested.
- No overall figure stands alone; no pass or fail without the person's rule; no "fair" or "biased".
- The impossibility result is stated whenever outcome rates differ.
- `python3 scripts/subgroup_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry their DOI.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Overall discrimination, calibration curves and model validation design: `dh-technology` clinical-ml-model-development-and-validation.
- Performance over time and drift: `dh-technology` model-performance-and-drift-monitoring.
- Data quality of the test set: `dh-technology` data-quality-monitoring.
- What a gap means for release: B1 in this skill.
