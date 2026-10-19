# A2 Session record and coverage

Framework task: DH-02.02.4.1, Part A, task A2. Replaces register task CF-12.02.02.4.1.2 "Session record".

## What this task delivers

A session record per site and role: who was in the role, who attended, who did the task on the task card once, who attended without completing, whose completion was not recorded, who in the role did not attend, and who is designated to train others. It answers "who was trained on the task, who can do it, and who in the role was missed?"

Why it matters: attendance is not completion (register CF-12.02.02.4.1.2), and a gap between the two is the first sign that the training, the task or the workflow is wrong. Train-the-trainer and champion strategies (CS45, CS46) only work if the designated people themselves completed the task.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.4.1 Part A, Session record and coverage |
| Workflow | The steps below |
| Knowledge | `references/enablement-strategies.md` (CS8, CS45, CS46); `references/training-rules.md` section 1 |
| Tools | `scripts/session_coverage.py` (local, optional). No library call: the person's log never goes to the connector |
| Prompt | This guide |
| Template | `assets/session-record-and-coverage-output.md` |
| Input | The request and its context: the task card (A1), the person's training log (one row per person in the role), the as-of date |
| Governance | `references/governance.md`; roles and pseudonymous ids only; any staff-identifying report stops for the owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Task card.** Completion means the task on the card. If there is no card, run A1 first or ask the person to state the task in one line.
- **Log.** Ask for one row per person in the role at the site, in the columns `scripts/session_coverage.py` reads: `user_id, role, site, session_date, completed_task_once, trains_others`. A table in the message is fine. If the log names people, replace names with ids before computing and say so.
- **Denominator.** "In the role" is the person's list of who should be able to do the task. If they only have the attendance sheet, coverage cannot be computed: `[GAP]` the roster.
- **As-of date.** Default to the date of the conversation and say so.
- **Mode.** Short for a direct question; full for a site record.

## Workflow

### Step 1. Take the log

Check it: a completion with no session date (trained elsewhere, or an error); a session date after the as-of date; a role missing. Blank completion is "not recorded", never "done".

### Step 2. Compute coverage

With code execution, run `python3 scripts/session_coverage.py LOG.csv --by site,role --as-of YYYY-MM-DD`. Without it, count by hand. Report per group, each with its denominator (in role): attended; completed once; attended but not completed; not recorded; not attended; designated trainers.

### Step 3. Trainers and champions

If the person runs train-the-trainer or champions (CS45, CS46, CS8): list per site the number of designated trainers and whether each completed the task once. A designated trainer who has not completed the task is a finding. No row gives a trainer-to-user ratio; do not propose one.

### Step 4. Who was missed

List, by role and site (not by name), the people in the role who did not attend, and those who attended but did not complete. These feed B1 and the sibling adoption-monitoring skill. Do not rank individuals.

### Step 5. What it means for the person

Two or three consequences from the numbers and rows, stated conditionally. For example: "At South, 2 of 12 nurses attended without completion being recorded; until it is recorded, they are not counted as able to do the task." "Care coordinators at South have no session yet; the task card for that role cannot be checked in production."

## Build the output

Follow `assets/session-record-and-coverage-output.md`. Answer first: the coverage per site and role with denominators, then who was missed. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rate has its numerator and denominator.
- Attendance and completion are separate columns; "not recorded" is never counted as done.
- No names; roles and ids only.
- No verdict: no row sets a coverage share. If the person set one, mark met or missed against it.
- The log went into no library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Training coverage only. Whether the trained task is done in production, over time, is the sibling skill adoption-monitoring (DH-02.02.4.2).
- Workforce training the customer owes under HIPAA (CS82, CS83) is not tracked here.
