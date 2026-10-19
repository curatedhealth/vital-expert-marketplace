# A1 Usability results by task

Framework task: DH-02.04.4.2, Part A, task A1. Replaces the earlier "Usability task score" section.

## What this task delivers

A summary of the person's usability test: per task, the participants, outcomes as the person coded them, use errors, participants who returned to the old step, and the severity the person assigned; per user group, the participant count; flags for rows without severity, employees and think-aloud sessions; SUS if collected, with published benchmarks as labeled context; and a check of the test against the conditions for its kind (formative or validation). It answers "what happened in our test, task by task?"

Why it matters: FDA reads validation results qualitatively and sets no numeric error-rate acceptance (UX-US-43), so a single success percentage hides what matters: which critical task failed, how, and for whom. A test that broke a validation condition (employees, think-aloud, too few per group) cannot carry the weight the team may want to put on it (UX-US-34 to UX-US-41).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Service Design Director (`service-design-director`) |
| Skill | DH-02.04.4.2 Part A, Usability results by task |
| Workflow | The steps below |
| Knowledge | `references/test-results-and-validity.md`; `references/ux-usability-research.md` |
| Tools | `scripts/usability_log.py`; `verify.qualify_source` and `verify.check_claim` (counted, optional, for a benchmark quoted outside the conversation); `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/results-by-task-output.md` |
| Input | The request and its context: the log (CSV or summary), test kind, test dates, user groups, the person's severity scale, critical-task list (from the design skill's A2 or the person) |
| Governance | `references/governance.md`; counts describe, the person judges |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## The rule that shapes this task: count what is in the log; never assign severity or a verdict

The script and the model count. Severity and criticality are taken from the log as the person assigned them; a row without severity is flagged, not filled. No pass, fail, score or grade unless the person's rule defines it (that is B1). The designer or any employee as a participant is flagged (old register rule; UX-US-38 for validation).

## Read the request

- **The log.** Ideally one row per participant per task with: participant_id, user_group, task_id, task_name, critical, severity, outcome, returned_to_old_step, and optionally employee, think_aloud, note. A summary table is enough if no file is available.
- **Test kind.** Formative or validation. Ask; it decides which conditions apply.
- **Outcome codes.** The person's labels (for example success, difficulty, use_error, not_completed). Ask which label means success.
- **User groups.** Distinct populations as the person defines them; FDA treats professionals and lay users, and adults and children, as distinct (UX-US-36).
- **SUS.** If collected, ten item answers per participant.
- **Mode.** Short or full.

## Workflow

### Step 1. Fix the frame

Write back: product, build version tested, test kind, test dates, user groups, tasks and which are critical (the person's), the success label. Confirm.

### Step 2. Summarize the log

With code execution, run:

```
python3 scripts/usability_log.py log FILE.csv [--min-per-group N] [--outcomes-ok success]
```

`--min-per-group` only with the person's number. Without code execution, compute the same tables by hand from the log. Report per task: participants, outcomes, use errors "k of n", returned to old step, severity as assigned. Then non-success rows grouped by the person's severity, with notes. Then participants per group.

### Step 3. Check the use errors against the definition

For rows coded as use errors, check against FDA's definition (UX-US-27): if the note shows the wrong result was caused solely by a device fault, say it may be a device failure, not a use error, and leave the recoding to the person. Users may not know they made a use error (UX-UK-15); ask whether outcomes were observed or self-reported.

### Step 4. Check the test against its kind

Formative: note what it can and cannot show (UX-US-29, UX-M-04).

Validation: check each condition and mark met, not met, or not stated: representative users, all critical tasks performed, final UI, realistic conditions (UX-US-34); at least 15 per distinct population (UX-US-35); condition-related limits represented (UX-US-37); no employees (UX-US-38); US residence for US use (UX-US-39); no think-aloud (UX-US-40); training matching real use and not immediately before testing (UX-US-41, CS80). If design flaws appeared and no formative work preceded, say FDA treats such a test as formative (UX-M-06).

### Step 5. SUS (if collected)

Run `python3 scripts/usability_log.py sus FILE.csv`. Report mean, SD, min and max per group and overall, scored as Hyzy et al. 2022 restate Brooke (UX-M-07). Give context, labeled: general benchmark mean 68 (SD 12.5) (UX-M-08); digital health apps mean 76.64 (SD 15.12) across 117 scores, 68.05 (SD 14.05) excluding physical-activity apps (UX-M-09). These are not targets, and SUS does not measure use error.

If the benchmark leaves the conversation, check it: `verify.qualify_source {doi: "10.2196/37290", question: "<the person's question>"}`, then `verify.check_claim` with the claim, the passage quoted from row UX-M-09 with its locator, and `source` set to the full record `qualify_source` returned (a minimal `{source_id, doi}` failed with 502 in testing; `references/tools.md`). Read the passage yourself: the tool decides on word overlap (register N3).

### Step 6. Findings

List findings as facts: "2 of 14 participants made a use error on T2 (critical, your severity: serious): entered mg instead of mg/kg". Each names the task, the count, the person's severity and the row of any condition missed. No cause, no verdict.

## Build the output

Follow `assets/results-by-task-output.md`. Answer first: the critical tasks with use errors, counts and the person's severity, and any validation condition the test did not meet. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every count traces to the log or the script output; every severity is the person's.
- Rows without severity are flagged; none is treated as minor.
- Test conditions are marked met, not met or not stated, each with its row.
- SUS benchmarks are labeled context, with their source limits.
- No statement that the product is usable, validated or safe.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Reads results the person supplies; does not run or redesign the study.
- Controls in the build and field signals are A2; acceptance and shipping are B1.
- Whether the test is sufficient for a submission is the regulatory owner's (dh-regulatory-strategy).
