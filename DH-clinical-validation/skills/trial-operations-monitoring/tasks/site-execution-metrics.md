# A1 Site execution metrics

Framework task: DH-01.02.3.2, Part A, task A1 (old DH-01.02.3.2.1 Trial Execution Quality Monitoring).

## What this task delivers

Enrollment, retention, protocol deviations and data completeness for each site and each arm, computed from the person's own export, with the definition of every number stated. It answers "how is each site executing, in numbers, and where is the data thin?"

Why it matters: ICH E6(R3) asks monitoring to find missing data, outliers and deviations and to look at trends within and across sites (CVB6). A trial total can hide a site, and a site total can hide an arm.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.3.2 Part A, Site execution metrics |
| Workflow | The steps below |
| Knowledge | `references/execution-metrics.md`; rows CV41, CV58, CV59, CV67, CV69, CV71, CV110 and CV112 (CONSORT 2025, DOI 10.1136/bmj-2024-081123), CVB2, CVB5, CVB6 |
| Tool | `scripts/trial_ops_metrics.py sites` (with code execution). No library call: the library holds no trial execution data |
| Catalogue job | None |
| Prompt | This guide |
| Template | `assets/site-execution-metrics-output.md` |
| Input | The request and its context: a pseudonymous export (one row per participant or per site), site targets and activation dates if the person has them, the as-of date |
| Governance | `references/governance.md`; the export stays in the conversation |

## Read the request

- **What file and which shape.** Participant-level (site, participant_id, arm, enrolled_on, status, deviations, important_deviations, expected_assessments, received_assessments) or one row per site. Map the person's column names to these; ask only where the meaning is unclear.
- **As-of date.** Every number is "as of" a date. Ask if not given.
- **Mode.** Short for "how are we doing", full for a monitoring report.

## Workflow

### Step 1. Agree the definitions

Show the four formulas from `execution-metrics.md` in one line each and ask the person to confirm or change them (for example, whether "completed" participants count as retained, which they do by default). Say that completeness here is an operational count, not the analysis definition of missing data, which depends on the estimand (CV41).

### Step 2. Check the data

Look for numbers that cannot both be true (received above expected, statuses outside the four, an important-deviation count above the total). Quote and ask; do not correct.

### Step 3. Compute

With code execution: `python3 scripts/trial_ops_metrics.py sites <export.csv> --targets <targets.csv> --as-of <YYYY-MM-DD>`. Without it, compute the same formulas by hand and show the arithmetic for the totals. Targets and activation dates are optional; without them, enrollment shows as a count only.

### Step 4. Look across sites and arms

Name the site with the lowest value on each metric and the largest completeness gap between arms at any site (CV58), even where the trial-level gap is small. If the export has visit type, show completeness by visit type too (CV67, CV69).

### Step 5. Trend

If more than one period is given, show the change per site. Do not extrapolate to a completion date.

### Step 6. Name the next measurements

At most three that would locate a problem: for example, completeness by DHT stream or device version, deviations by category, time from enrollment to first DHT transmission.

## Build the output

Follow `assets/site-execution-metrics-output.md`. Answer first: the site and metric furthest from the rest, with the number. Then the table per site, the arm and modality view, data checks, next measurements, gaps.

## Before you hand it over

- Every number is from the person's file, with its formula and as-of date.
- No verdict: no "failing", "behind" or "on track" without a rule (that is B1).
- No participant-level rows in the output.
- Record line present.

## Boundaries

- Measurement only. Pass or miss is B1, against the person's rules.
- Operational metrics are not the trial's efficacy or safety result.
- Setup and data controls: the decentralized trial operations skill.
