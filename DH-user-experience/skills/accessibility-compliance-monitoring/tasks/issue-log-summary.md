# A2 Issue log summary and age

Framework task: DH-02.04.1.2, Part A, task A2. Replaces the earlier "Open barrier age" section.

## What this task delivers

The person's accessibility issue log summarized against the WCAG version and level they target, to a stated as-of date: open issues in the target by the severity they assigned, by W3C level, by screen, with ages; day-one tasks first; issues outside the target listed separately (not deleted); how the log was built (automated, manual, assistive technology, research); and data problems in the log. It answers "what is open against our target, how old is it, and where does it sit?"

Why it matters: a log mixes versions and levels. Against a 2.1 AA target, a 2.2-only criterion is outside scope; against 2.2, 4.1.1 Parsing is gone (UX-STD-07, UX-STD-08). Counting them together misstates both the backlog and the gap.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Health Equity & Digital Access Lead (`health-equity-access-lead`) |
| Skill | DH-02.04.1.2 Part A, Issue log summary and age |
| Workflow | The steps below |
| Knowledge | `references/conformance-sampling.md`; `references/data/wcag_criteria.csv`; `references/wcag-criteria-additions.md` |
| Tools | `scripts/a11y_issue_log.py` (no connector). `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/issue-log-summary-output.md` |
| Input | The request and its context: the issue log (CSV or pasted table), the target version and level, the as-of date, the person's definition of day-one tasks |
| Governance | `references/governance.md`; severity, status and closure are the person's; no conformance statement |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## The rule that shapes this task: count the log, do not judge it

The script counts what the person logged. Severity is their label, counted as logged. An issue is closed when their log says so with a date. A criterion with no issue logged is not a pass. Ages are facts; whether an age is too old is their rule.

## Read the request

- **Log.** Columns: id, screen, task, day_one, criterion, level, severity, status, opened, closed, found_by. Map the person's column names; ask for any of criterion, status or opened that is missing. The log never goes into a library call.
- **Target.** Version and level. Without one, ask; or run 2.1 AA and 2.2 AA side by side, labeled, if the person wants both views.
- **As-of date.** Ask; ages count to it.
- **Day-one tasks.** If the log has no day_one column, ask which tasks are day-one; do not decide.
- **Mode.** Short for a direct question; full for a backlog report.

## Workflow

### Step 1. Fix the frame

Write back: target, as-of date, number of issues, column mapping, day-one definition.

### Step 2. Run the script

With code execution: save the log as CSV and run

`python3 scripts/a11y_issue_log.py LOG.csv --version <2.0|2.1|2.2> --level <A|AA|AAA> --as-of <YYYY-MM-DD>` (add `--json` for the full data).

Without code execution: do the same steps by hand from `references/data/wcag_criteria.csv`: classify each issue as in target, above target, or not in the version; count open in-target issues by the person's severity and by level; age each open one to the as-of date.

### Step 3. Read the result

- Open in target: count, how many on day-one tasks, median and oldest age, by the person's severity.
- Outside the target: list with the reason (for example "2.5.8 Target Size (Minimum), first in 2.2" against a 2.1 target; "4.1.1, removed in 2.2; test and report only if a 2.0 or 2.1 policy applies", UX-STD-08). Where another obligation names an out-of-target criterion (NHS requires the new 2.2 A and AA criteria, UX-UK-23), say so in one line.
- How the log was built: counts by found_by. If most issues come from automated tools, say that automated tests check only part of what needs testing (UX-UK-24) and that criteria with no issue are not passes.
- Data problems: a logged level that differs from the W3C level for the target version, a closed status without a date, dates out of order. List them; do not correct the log.

### Step 4. Findings

Facts only: "4 of 7 open in-target issues are on day-one tasks; the oldest day-one issue (4.1.2, Level A) has been open 111 days to 19 October 2026." No cause, no new severity, no verdict unless the person gives a rule.

## Build the output

Follow `assets/issue-log-summary-output.md`. Answer first: open in-target count, day-one count, oldest age, and the biggest difference the target makes. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The target and as-of date are stated; ages count to it.
- Severity labels are the person's, unchanged.
- Out-of-target issues are listed, not dropped.
- The automated-coverage note is present where the log leans on scans.
- No statement that the product conforms, and no issue closed by the model.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Summarizes the person's log; it does not find issues or test screens.
- Whether to ship is B1. Which criterion one new barrier meets is the sibling skill's A2.
- No benchmark ages or counts: the rows hold none `[GAP]`.
