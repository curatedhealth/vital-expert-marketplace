# A2 Data quality read

Framework task: DH-01.04.4.2 Part A, task A2. Carries the old one-line task "DH-01.04.4.2.2 Data quality score" ("Run the checks").

## What this task delivers

For one dataset version and a read date the person gives: each check run with the rows checked, the count and share failing, the person's limit and the result (pass, fail, "limit not given" or "not run" with the reason); the features with rows dated after the index time named; a field-by-field comparison with the previous version (row counts, missing shares, means, medians, category shares); and the flags that limit the read (rules written for another version, no version, no limit). It answers "what does this version of the data actually show against our rules, and what changed?"

Why it matters: the old task says "Do not drop a failed feature quietly and report a pass." A read that drops a failing feature, or reports a share without the version it came from, cannot be repeated.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `data-engineering-manager-health` (old DH-01.04.4.2.2). Work as a data quality analyst who runs the person's rules on the person's data |
| Skill | DH-01.04.4.2 Part A, Data quality read |
| Workflow | The steps below |
| Knowledge | `references/data-quality-requirements.md` sections 1, 2, 4 and 5; rows DA-12 to DA-14, DA-35, DA-37, DA-44, DA-87, DA-88, DA-94 to DA-98, DA-105, DA-139, CV79, CV87 |
| Tools | `scripts/dq_check.py run`, `compare`; optional `literature.get_record` for a method paper the person names; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/data-quality-read-output.md` |
| Input | The request and its context: the rules (A1 or the person's file), the data file and its version, reference files, the previous version, the read date |
| Governance | `references/governance.md`; no fit-for-use verdict |
| Catalogue job | none |

## Read the request

- **Read date.** The person's. If not given, write "read date: not given" and ask; never assume today.
- **Version.** The version label of the data read. If the rules were written for another version, the run still reads against the rules as written and says so (V1).
- **Files.** Use them as given; never edit a value. A field named in a rule but absent from the data is "not run", with the reason.

## Workflow

### Step 1. Run the checks

Run `python3 scripts/dq_check.py run --data DATA.csv --rules RULES.json --version V [--ref NAME=FILE] --json RESULTS.json`. Report per check: Kahn category, field, rows checked, failing, share, the person's limit, result. Counts: pass, fail, limit not given, not run. Name each feature with rows dated after the index time; it is reported, never dropped.

### Step 2. Read order and denominators

Report uniqueness and relational failures first: duplicated keys or orphan ids change every other denominator. Completeness is the share of rows with a value present (DA-97); in OMOP data it is read inside the observation period (DA-105, community standard). A share with its denominator, always ("6 of 90").

### Step 3. Compare with the previous version

Run `python3 scripts/dq_check.py compare --old OLD.csv --new NEW.csv --fields F1,F2,...` on the fields the person names (or those in the rules). Report row counts and per-field missing share, mean and median or category shares, old against new. A difference is a fact about the data. An input shift between development data and later data is what the literature calls covariate shift (Sahiner et al. 2023, DA-88, DOI 10.1259/bjr.20220878); the FDA draft names data drift as a postmarket performance risk (DA-37, draft). No row gives a drift threshold; what it means for the model routes to `model-performance-and-drift-monitoring` (this pack).

### Step 4. What the read does not show

Descriptive counts show data exist; they are not evidence of reliability or validity (DA-139; CMS, context). A verification run does not test accuracy against an external reference: that is a validation check (DA-94) with the person's reference standard (CV81). Risks the person chose not to measure are listed (NIST MEASURE 1.1, DA-12, voluntary).

### Step 5. Published method (optional, library)

If the person names a data quality method paper, call `literature.get_record {doi: "<doi>"}` (needs a live check for this use) and quote only what a passage states, in the same direction (register N3).

## Build the output

Follow `assets/data-quality-read-output.md`. Answer first: as of the read date and for the version read, counts of checks that pass, fail, have no limit or were not run against the person's limits; the failed checks by name with their counts; the leak features; and the largest change from the previous version as a fact. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/dq_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every count comes from the script output with its denominator and version.
- No check is marked pass or fail without the person's limit; no failing feature is dropped.
- No "fit for use", no drift verdict.
- `python3 scripts/dq_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry their DOI.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Model performance consequences of a data shift: `model-performance-and-drift-monitoring` (this pack).
- Data checks inside a running clinical trial: `dh-clinical-development` trial-operations-monitoring.
