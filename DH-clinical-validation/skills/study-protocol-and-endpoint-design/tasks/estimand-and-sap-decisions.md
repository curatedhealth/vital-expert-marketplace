# B1 Estimand and statistical analysis plan decisions

Framework task: DH-01.02.1.1, Part B, task B1. Replaces the earlier "Statistical Analysis Plan Development" section.

## What this task delivers

A decision draft for the person and the owner they name for statistics: the primary estimand written out in its five attributes, the intercurrent events the person names with the strategies available for each, and the statistical analysis plan laid out as a list of decisions (analysis populations, missing data, sensitivity analyses, sample size assumptions, interim analyses, design framework), each with the options, the sourced facts that bear on it, and who decides. Nothing is decided here. Where that owner has already decided, the draft records the decision as theirs.

Why it matters: E9(R1) requires the protocol to define a primary estimand and prespecify the matching estimator and a sensitivity analysis (CV40). In digital trials, stopping use of the app is the most common intercurrent event, and how it is handled changes what the result means.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`). The old file bound this task to `cybersecurity-architect-digital-health`, whose remit is security architecture; see BUILD_NOTES. |
| Skill | DH-01.02.1.1 Part B, Estimand and SAP decisions |
| Workflow | The steps below |
| Knowledge | `references/estimand-and-sap-rules.md`; rows CV31 to CV41, CV58, CV59, CV67, CV72, PE-21, SP-19, SP-27a to SP-28b, ES-70, ES-71 |
| Tools | None required. `literature.search_literature` and `verify.*` only if the person or their named owner asks for published assumptions (dropout, variance) from comparables |
| Prompt | This guide |
| Template | `assets/estimand-sap-output.md` |
| Input | The request and its context: primary objective, the A1 endpoint, comparator, design, the intercurrent events the person expects, the named owner's decisions so far, assumptions they hold |
| Governance | `references/governance.md`; the person and the owner they name for statistics decide |
| Catalogue job | none |

## The rule that shapes this task: the person's named owner decides

The model writes out what must be decided and what each option means, using the rows. It never picks a strategy, an estimator, a margin, an alpha or a sample size, and never fills an assumption (effect size, standard deviation, dropout) from memory. If the person asks for a proposal, it may give one, labeled "proposed", with the fact behind it, and it stays out of the SAP until the named owner confirms. There is no statistics expert in the catalogue (`references/tools.md`), so the decider is always the owner the person names for statistics: use the name or role the person gives, in their words, or write "owner not named" and ask.

## Workflow

### Step 1. Write the estimand

Fill the five attributes (CV33, CV34) from the person's facts and A1: treatment and comparator, population, variable (the endpoint with its four elements, SP-16), intercurrent events and their strategies, population-level summary. Anything not given is `[GAP]`.

### Step 2. List the intercurrent events

Ask the person which events they expect (for example stopping app use, starting another treatment, device or connectivity failure). For each, lay out the five strategies (CV35 to CV39) as options, with one line on what the result would then mean for the claim. Do not choose.

### Step 3. Lay out the SAP decisions

One row per decision, with options, the facts and rows that bear on it, and the owner:

| Decision | Facts that bear on it |
|---|---|
| Analysis populations and group assignment | SP-27b; CONSORT 2025 21b will ask the report to define them (CV112) |
| Missing data handling, tied to the estimand | CV41, SP-27c, CV59; reasons for missing COA data collected (PE-21) |
| Main estimator and sensitivity analysis | CV40, SP-27d |
| Design framework (superiority, non-inferiority, equivalence) | SP-12; non-inferiority cautions with DHT measures (CV58, CV72) |
| Sample size and all assumptions | SP-19; the numbers are the named owner's |
| Interim analyses and stopping | SP-28b |
| Assessment modality across arms | Same method in all arms (CV58); modality fixed in the protocol (CV67) |

### Step 4. Assumptions and their sources

If the person or their named owner wants published assumptions (for example dropout seen in comparable app trials), use A1's comparables or search, and report each number with its passage, checked with `verify.qualify_source` then `verify.check_claim` and read in the same direction (N3). The named owner decides whether to adopt it; an adopted number keeps its source.

### Step 5. Bias planning view

Name the five RoB 2 domains a reviewer will later apply to each result (ES-71) and, for each, the protocol items that address it (allocation SP-21a to SP-23, blinding SP-24a, retention SP-25b, prespecification SP-27a to SP-27d). This is a planning aid; it is not a risk-of-bias judgment (ES-70).

### Step 6. Decision log

Record each decision already made, with who made it, in their words. Open decisions are listed by dependency (the estimand before the estimator; the endpoint and estimand before sample size).

## Build the output

Follow `assets/estimand-sap-output.md`. Answer first: the estimand as far as it can be written, and the decisions open for the owner the person names for statistics. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- No strategy, estimator, margin, alpha or sample size is chosen by the model; proposals are labeled.
- Every assumption has a source or is the named owner's, labeled.
- The output is "decision draft for OWNER" (the owner the person names), never a final SAP.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line ends the answer: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Running the analysis or computing the sample size: the owner the person names for statistics, or owner not named. This skill holds no sourced formula.
- Health economic analysis: the Health Economics pack (DH-01.07).
- Risk-of-bias assessment of published results (review method): `dh-clinical-validation` literature-and-real-world-evidence-review (DH-01.02.4.1).
