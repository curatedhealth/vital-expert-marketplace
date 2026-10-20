# A2 Complaint and recurrence trends

Framework task: DH-03.02.4.2, Part A, task A2. Replaces the earlier "CAPA score" step that listed complaints with missing reportability decisions.

## What this task delivers

From the person's complaint log (and CAPA log): which complaint codes came back after a CAPA closed, which open complaints are ageing against the limit the person set, whether each reportability decision and report met its clock, and counts by code and month. FDA 483 citation data for FY 2025 is added as context, labeled pre-QMSR. It answers "is our complaint handling under control?"

Why it matters: complaint procedures were the second most cited device area on FDA 483s in FY 2025 (211 citations of 820.198(a), QS53), behind CAPA procedures (279). Recurrence after closure is the plainest sign a CAPA did not work, and a late reportability decision has to be recorded as late.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | QA Manager, Software (V&V) |
| Skill | DH-03.02.4.2 Part A, Complaint and recurrence trends |
| Workflow | The steps below |
| Knowledge | `references/effectiveness-and-trends.md`; `references/vigilance-clocks.md`; rows VG4 to VG28, QS47, QS51 to QS54 |
| Tools | `scripts/complaint_trends.py`; optional `regulatory-dh.search_safety_events` (one or two calls) |
| Prompt | This guide |
| Template | `assets/trends-output.md` |
| Input | The request and its context: complaint log (CSV or table), CAPA log, the person's limits (ageing, window), the period |
| Governance | `references/governance.md`; limits and verdicts are the person's |

## Read the request

- **The log.** Ask for the columns listed in `scripts/complaint_trends.py`. If the person pastes a table, map it to those columns and say which are missing. Never send log contents to the library.
- **Limits.** The ageing limit and each CAPA's window are the person's. Without them, show days open and later complaints with no verdict.
- **Period and as-of date.**
- **Mode.** "Which complaints are overdue?" gets short mode. A quarterly quality review gets full mode.

## Workflow

### Step 1. Run the helper

`python3 scripts/complaint_trends.py complaints.csv --capas capas.csv --rules rules.json --as-of <date>`. Federal holidays are excluded by default from `scripts/us_federal_holidays.txt` (OPM, 2026 and 2027, R14); pass `--holidays` with the person's list if the period runs outside those years, otherwise the output warns that a work-day date may be later. Without code execution, do the same steps by hand and show the counts.

### Step 2. Recurrence after CAPA closure

For each closed CAPA, list later complaints with the same code inside the person's window, with days after closure and version. Mark them "candidate recurrence"; same cause is the person's call. Note when a recurrence is on a version released after the fix, because that is the stronger signal; say it as a fact, not a verdict.

### Step 3. Ageing

List open complaints by days open. Against the person's limit, flag over or within. No limit, no flag.

### Step 4. Reporting timeliness

For each complaint row with an event type, show the due date (from the awareness date), the decision, and the status: submitted on time, submitted late (days), decided reportable and not submitted, undecided with the due date passed or not, decided not reportable after the due date (record that the date was missed, register rule). Note the GB counting `[GAP]` and whether holidays were excluded. Missing awareness dates are listed as a record gap; the US event file needs the deliberation (VG21).

For each undecided EU or GB serious-incident row, also give the 10-day and 2-day dates (VG5, VG6, VG28), because severity is part of the undecided decision. A shorter date that has passed or falls today is stated as such, as a fact, with no urgency wording.

US work-day counts exclude Federal holidays (R9; the helper names any holiday it excluded, from the OPM list for 2026 and 2027, R14). A US 5-day row counts from the date a manager or supervisor over regulatory, scientific or technical staff learned that remedial action is needed (VG19), not from first receipt; if the log holds only first receipt, say so and do not call the 5-day date passed.

### Step 5. Counts and trend context

Show counts by code and month. State that whether a rise is statistically significant is decided by the method in the person's PMS plan (VG9); the model does not run a significance test it was not given.

### Step 6. FDA 483 context (optional, one paragraph)

Add the FY 2025 device citations from `effectiveness-and-trends.md` section 4, labeled: FDA FY 2025, inspections ending 30 September 2025, pre-QMSR (QS regulation sections), not a complete list, not a benchmark.

### Step 7. Public comparables (only if asked)

If the person asks whether comparable products had repeated problems, call `regulatory-dh.search_safety_events` with a manufacturer or one product word. Report what the records state. Two recalls of the same product are a recurrence only if the records state the same defect; the Dexcom G7 iOS app example in `effectiveness-and-trends.md` shows two different defects.

## Build the output

Follow `assets/trends-output.md`. Answer first: the candidate recurrences, the clocks passed without a decision or report, and the complaints over the person's limit.

## Before you hand it over

- Every limit and window is the person's, or the output says none was set.
- Recurrences are "candidate", with ids and versions.
- Every late or undecided item shows its due date and rule.
- 483 data is labeled pre-QMSR and context only.
- No log data went into a library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No new reportability decision: a new or undecided complaint goes to the sibling skill (DH-03.02.4.1, A2).
- No statistical significance claim without the person's PMS method.
