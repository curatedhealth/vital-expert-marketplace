# A1 CAPA effectiveness check

Framework task: DH-03.02.4.2, Part A, task A1. Replaces the earlier "CAPA effectiveness check" section.

## What this task delivers

For one CAPA (or a short list), each effectiveness criterion the person set, the evidence read against it, and a status per criterion: met, not met, evidence missing, or not yet due. It answers "did this CAPA work, on the test we set?" The verdict "effective" is the person's.

Why it matters: the MDR requires CAPA effectiveness to be verified (EU4), and MDSAP treats a repeat nonconformity as a sign a corrective action was not adequately taken (QS47). A CAPA closed on time can still have failed.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | QA Manager, Software (V&V) |
| Skill | DH-03.02.4.2 Part A, CAPA effectiveness check |
| Workflow | The steps below |
| Knowledge | `references/effectiveness-and-trends.md` sections 1 and 2; rows EU3, EU4, QS17, QS18, QS47, R3, R8 |
| Tools | None required; `scripts/complaint_trends.py` when the criterion is complaint recurrence |
| Prompt | This guide |
| Template | `assets/effectiveness-check-output.md` |
| Input | The request and its context: the CAPA plan with its effectiveness criteria (record, measure, window, pass condition, owner), and the evidence records |
| Governance | `references/governance.md`; the effectiveness verdict and closure are the person's |

## Read the request

- **The criteria.** Take them from the CAPA plan (the sibling skill's B1 output, or the person's CAPA record). If the plan has none, say the CAPA cannot be checked and route back to the sibling skill's B1 to set them. Do not invent a criterion. If the person asks for a proposal, give one labeled "proposed" and do not apply it until confirmed.
- **The evidence.** The records the criteria name: complaint log extract, audit result, defect tracker, test record. Ask for what is missing.
- **Mode.** "Did CAPA-031 work?" gets short mode. A CAPA board pack gets full mode.

## Workflow

### Step 1. Restate each criterion

Write each criterion back in the person's words: action, record read, measure, window, pass condition, owner. Confirm before checking.

### Step 2. Check the window

Is the window over as of today? If not, the criterion is "not yet due", with the end date. An interim reading may be shown, labeled interim.

### Step 3. Read the evidence

For each criterion, state what the evidence shows, with record ids and dates. For a complaint-recurrence criterion, run `scripts/complaint_trends.py` on the person's log with the CAPA row and its window, and list each later complaint with the same code. A later complaint with the same code is a candidate recurrence; whether it has the same cause is the person's call. Note the version each recurrence was on. If a candidate recurrence has no reportability decision recorded, say so and route it to DH-03.02.4.1 A2. For software, harm from a decision based on incorrect output is indirect harm (VG14).

### Step 4. Status per criterion

- **Met:** the evidence meets the pass condition within the window.
- **Not met:** the evidence shows the pass condition was missed.
- **Evidence missing:** the criterion exists but the record was not supplied. Not a pass.
- **No check performed:** the window ended and nobody read the record. Under the register rule this counts as a fail; say so and leave the verdict to the person.
- **Not yet due.**

Closed on time is never a criterion (register rule).

### Step 5. What the statuses point to

Without a verdict: if any criterion is not met or no check was performed, say the register rule is to open a new action rather than reopen the old one, and that the finding stays open while the new action runs. Route to the sibling skill (DH-03.02.4.1, B1). If an audit is near, note that MDSAP may issue a nonconformity for an ineffective corrective action system when new occurrences show actions are not effective (R3).

## Build the output

Follow `assets/effectiveness-check-output.md`. Answer first: per CAPA, the count of criteria met, not met, missing, not yet due, and the decision the person faces.

## Before you hand it over

- Every criterion is the person's and is quoted in their words, or labeled "proposed".
- Every status cites its evidence, or says what is missing.
- No "effective" verdict and no closure in the model's voice.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Checks against set criteria only; does not judge whether the criteria were good enough (that is a CAPA plan question).
- Does not close a CAPA or a finding.
