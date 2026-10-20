# A1 Data quality rules

Framework task: DH-01.04.4.2 Data Quality Assessment & Feature Engineering Effectiveness Monitoring, Part A, task A1. Carries the old one-line task "DH-01.04.4.2.1 Data quality rule" ("Define the checks this dataset must pass").

## What this task delivers

The person's rules for one dataset, written before any run: the dataset and its version, the unit of row, each check in its Kahn category (value, relational or computational conformance; completeness; uniqueness, atemporal or temporal plausibility) and context (verification or validation), the leak check against the index time, the row count against the cohort rule, the limit for each check as the person sets it, and who wrote the rules and when. It answers "what must this dataset pass before anyone trains or reports on it?"

Why it matters: a check judged against a limit written after the results is a story, not a check. The old task warns against one completeness percentage standing in for quality; Kahn's categories (DA-94 to DA-98, DOI 10.13063/2327-9214.1244) give the rest of the list.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `data-engineering-manager-health` (old DH-01.04.4.2.1). Work as a data quality analyst who writes the person's rules down |
| Skill | DH-01.04.4.2 Part A, Data quality rules |
| Workflow | The steps below |
| Knowledge | `references/data-quality-requirements.md` sections 1 to 4; rows DA-47 to DA-50, DA-67, DA-94 to DA-98, DA-102 to DA-106, CV79 to CV83 |
| Tools | `scripts/dq_check.py rules` (flags only; no limit is set); `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/data-quality-rules-output.md` |
| Input | The request and its context: dataset, version, unit of row, fields and their allowed values or ranges, reference files, index time, expected row count from the cohort rule, limits, who writes the rules and when |
| Governance | `references/governance.md`; every check and limit is the person's |
| Catalogue job | none (`list_jobs_2026-10-19.json` lists no data quality job) |

## Read the request

- **Dataset and version.** Name and version as the person gives them. Without a version, write "version not given" and ask; rules cannot be tied to data otherwise.
- **Intended use.** What the data feed (training, a measure, a report). Relevance (CV79) and the EU dataset qualities (DA-49, DA-50) are read against it.
- **What the person has.** Existing checks, allowed values, ranges, limits: keep them verbatim.
- **What is missing.** Limits, the index time, the expected row count: "not given"; ask. Never fill.

## Workflow

### Step 1. Unit of row and keys

The unit of row (patient, encounter, device-day) and its key fields. A uniqueness check on the key (DA-98) comes first; in OMOP data, person linkage is expected before loading (DA-106, community standard).

### Step 2. Checks by category

Write each check the person names in its category, with the script's fields (`references/data-quality-requirements.md` section 1): value conformance with allowed values, type or pattern (DA-96); relational conformance with the reference file and field; computational conformance with the formula and the person's tolerance; completeness for each decision-time feature, with the missing-value codes the person uses (DA-97; in OMOP, inside the observation period, DA-105); atemporal plausibility with the person's range; temporal plausibility with the two date fields; the leak check (feature date after the index time); the row count against the cohort rule. Mark each as verification or validation (DA-94). If the person asks which checks to add, list the categories they have not covered, each check "proposed" and without a limit.

### Step 3. Limits

Write the person's limit for each check in the form "share failing at most <your figure>". A check without a limit is kept and reported but never marked pass or fail. No source in this skill sets a limit; if asked for one, say so and ask. For RWD used in a regulatory context, lay beside the rules the reliability and relevance elements (accuracy, completeness, traceability; key variables and representative patients, CV79; drug guidance, context for devices) and, for an EU high-risk system, the Article 10(3) and 10(4) qualities with the amended application date (DA-49, DA-50, DA-67).

### Step 4. Who wrote the rules, and when

Record the author the person names and the date written. A run can show the rules came first only if this date precedes the read date.

### Step 5. Validate the rules file

With code execution, save the rules as JSON and run `python3 scripts/dq_check.py rules --rules RULES.json`. Report flags Q1 to Q6 as what is still missing before the first run.

## Build the output

Follow `assets/data-quality-rules-output.md`. Answer first: how many checks in which categories, how many have a limit, whether a leak check and a version exist, and what is missing most. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/dq_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every check, limit, version and author is the person's or "not given"; proposed checks carry no limit and are labeled "proposed".
- Kahn categories cite DA-94 to DA-98 with the DOI; EU rows carry the amended date; drug guidance is labeled context.
- No limit supplied, no "acceptable".
- `python3 scripts/dq_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Choosing the features and refusing leaking ones at design: `data-preparation-and-analytics-methods` (this pack).
- FHIR conformance rules for an interface: `integration-quality-monitoring` (this pack).
