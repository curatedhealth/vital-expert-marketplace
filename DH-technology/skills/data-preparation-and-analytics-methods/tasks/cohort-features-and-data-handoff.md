# A1 Cohort, features and data handoff

Framework task: DH-01.04.4.1 Clinical Data Preparation & Feature Engineering Execution, Part A, task A1. Carries the old tasks "DH-01.04.4.1.1 Cohort rule", "DH-01.04.4.1.2 Feature definition" and "DH-01.04.4.1.3 Data handoff".

## What this task delivers

From the person's intended use and data: the cohort rule (population, time window, care setting, exclusions, unit of row) with conceptual and operational definitions and an attrition table; a feature dictionary in which every feature can be rebuilt (source field, window relative to the index time, missing-value code, availability at decision time), with the candidates to refuse for leakage and the inputs that carry a 45 CFR 92.210 duty; a check of the data split; and a versioned handoff to the model owner with the missingness that remains and who may change the cohort rule. It answers "who is in the data, what does each feature mean, and what are we handing over?"

Why it matters: a feature known only after the outcome makes a model look better than it will be; a patient in both training and test data does the same (DA-39, draft). A dataset handed over without a version cannot be traced when a check later fails.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `data-engineering-manager-health` (old DH-01.04.4.1.1 to .3). Work as a clinical data scientist who writes definitions so they can be rebuilt |
| Skill | DH-01.04.4.1 in this competency, Part A, Cohort, features and data handoff |
| Workflow | The steps below |
| Knowledge | `references/data-requirements.md` sections 1 to 4; rows CV78 to CV87, CV109, CV126, CV128, DA-39 to DA-41, DA-47 to DA-53, DA-67, DA-71, DA-73, DA-74, DA-86, DA-99 to DA-112, DA-115, DA-120, DA-133, DA-134, PE-113 to PE-115, TM89 |
| Tools | `scripts/prep_check.py cohort`, `features`, `split`; optional `literature.search_literature` and `literature.get_record` for a published validation of an operational definition; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/cohort-features-and-data-handoff-output.md` |
| Input | The request and its context: intended use and the decision served, data source and version, cohort steps, feature dictionary, split file, index time definition, who may change the cohort rule |
| Governance | `references/governance.md`; every definition, refusal and version is the person's |
| Catalogue job | none (`list_jobs_2026-10-19.json` lists no data preparation job) |

## Read the request

- **Intended use.** The decision the data serves and who acts on it. If not given, write "intended use: not given" and ask; relevance (CV79) cannot be read without it.
- **Index time.** The moment a prediction or estimate is made (for example "discharge date and time"). Feature windows are read against it. If not given, ask; never assume one.
- **Files.** Use the person's files as given; never edit a value. Missing columns: "not given".
- **Market.** US, EU or both: it decides which rows apply (FDA and 45 CFR 92.210; EU AI Act and EMA). Rows from another market are labeled context.

## Workflow

### Step 1. Cohort rule (old "Cohort rule")

Write the population, time window, care setting, exclusions and unit of row in the person's words. For each key variable (population, exposure, outcome, covariates), the conceptual definition and the operational definition the person uses, or "not given" (CV80). Run `python3 scripts/prep_check.py cohort --steps STEPS.csv` and report the attrition table with flags C1 to C3. A count that rises after a linkage step is a fact; OMOP expects person linkage before the person table is written (DA-106, OHDSI community standard). For claims data, ask how continuity of coverage is handled (CV83). Describe the denominator in words, not codes (DA-134, CMS, context outside quality measures).

### Step 2. Operational definition accuracy (optional, library)

If the person asks whether a code algorithm is accurate, the measures are sensitivity, specificity, PPV and NPV against a reference standard (CV81). If they have a validation, report its figures as theirs. If they ask for a published one, call `literature.search_literature {query: "<condition> <data source> algorithm validation positive predictive value", limit: 10}` (needs a live check for this query type), then `literature.get_record {doi}` for a candidate, and quote a figure only from a passage read in the paper, in the same direction (register N3). Never supply an accuracy figure from memory.

### Step 3. Feature definitions (old "Feature definition")

Run `python3 scripts/prep_check.py features --dict FEATURES.csv`. Report per feature: source field, window relative to the index time, missing-value code, availability at decision time, flags F1 to F7. List the candidates to refuse (F3 window ends after the index time, F5 not available at decision time, F7 derived from the outcome) and ask the person to confirm each refusal; the old task requires at least one feature named and refused when one leaks. For inputs flagged F6, state the 45 CFR 92.210 duty for a covered entity to identify and mitigate (PE-113, compliance date PE-115) and route the covered-entity question to the owner the person names for legal matters, or owner not named. Where the outcome may be ascertained differently across groups, name label bias (DA-115, DA-120). For an EU high-risk system, list the Article 10(2) preparation operations the person documents (DA-47), with the amended application date (DA-67).

### Step 4. Split check

Run `python3 scripts/prep_check.py split --file SPLIT.csv` (name the person's test subsets with `--test-names`). Report counts per subset and flags S1 (patients in more than one subset) and S2 (sites in both development and test). Lay beside them the sourced rules: the FDA draft proposes independent, sequestered test data, generally from different sites (DA-39, DA-41, draft); EMA encourages an early split before aggregate processing and a test set used once (DA-74, DA-73, medicinal products, context for devices); name subsets as internal or external testing (DA-86). Whether the split fits is the person's.

### Step 5. Data handoff (old "Data handoff")

Write the handoff record: dataset version (or "not given"; a dataset is not handed over without one), cohort rule, feature list with refused features, split counts and flags, the missingness that remains per feature (from the person's figures or the sibling skill `data-quality-monitoring` run), provenance and license (FAIR R1.1 and R1.2, DA-100, a guide, not a standard, DA-101), transformations made to conform to a standard and their impact (CV87, drug submissions, context), and who may change the cohort rule (the person named, or owner not named). Where the data use a common model or exchange standard, state its version facts dated and apart: OMOP CDM v5.5 named current by OHDSI, rules quoted from v5.4 (DA-103); USCDI v3 adopted for certification, v7 published 23 July 2026 and not a certification requirement until adopted (DA-108, DA-111).

## Build the output

Follow `assets/cohort-features-and-data-handoff-output.md`. Answer first: the cohort count from start to final with the step that removes most, the features to refuse and the 92.210 inputs, the split flags, and whether the handoff has a version. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/prep_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Counts and flags come from the script output, not from estimates.
- Every refusal, definition, version and owner is the person's or "not given"; proposals are labeled "proposed".
- Draft rows say "draft"; EU AI Act rows carry the amended application date; USCDI and OMOP versions are dated and apart.
- No threshold, no "fit for purpose", no "compliant".
- `python3 scripts/prep_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry their DOI.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Running data quality checks on the dataset: `data-quality-monitoring` (this pack).
- FHIR and USCDI exchange design: `interoperability-and-ehr-integration` (this pack).
- De-identification and access controls: `cybersecurity-and-privacy-by-design` (this pack).
- A trial's data management plan: `dh-clinical-development` study-protocol-and-endpoint-design.
