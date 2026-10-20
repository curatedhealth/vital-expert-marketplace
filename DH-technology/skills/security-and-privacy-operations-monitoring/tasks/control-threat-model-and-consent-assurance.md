# A1 Control, threat model and consent assurance

Framework task: DH-04.02.1.2, DH-04.02.2.2 and DH-04.02.4.2, Part A, task A1. Carries the old tasks "DH-04.02.1.2.1 Claimed control versus artifact", "DH-04.02.1.2.2 Gap scoring by citation", "DH-04.02.2.2.1 Threat coverage check", "DH-04.02.2.2.3 Model update trigger", "DH-04.02.4.2.1 Consent text versus practice" and "DH-04.02.4.2.2 Withdrawal test".

## What this task delivers

As of the person's read date: each claimed control marked proven as stated, proven (artifact read), unproven or contradicted, with the clause it cites and what that clause requires; the threat register's coverage by hop and whether the model is current against the person's change triggers and design version; and the consent text set against what the system actually does, with the withdrawal test read. It answers "is what we claim actually in place, is our threat model current, and does our consent text match practice?"

Why it matters: the old tasks were blunt: "Do not accept a control whose only evidence is the matrix itself", "Do not treat a tool scan as a threat model", "Do not pass the test because the preference flag flipped". An assurance read that counts matrix rows as controls, or a flag as a withdrawal, tells an auditor what they will find later.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `privacy-engineering-director` (old DH-04.02.1.2.1, .2 and DH-04.02.4.2.1, .2); `security-engineer-digital-health` (old DH-04.02.2.2.1, .3). Work as an assurance analyst who reads artifacts against claims |
| Skill | DH-04.02.1.2 with DH-04.02.2.2 and DH-04.02.4.2, Part A, Control, threat model and consent assurance |
| Workflow | The steps below |
| Knowledge | `references/assurance-and-operations-rules.md` sections 1, 2 and 6; `references/security-and-privacy-requirements.md` sections 3, 4 and 6; rows EN-008, EN-015, EN-022, EN-060, EN-077, EN-097 to EN-105, EN-109, EN-117, EN-123, EN-125, EN-126; CS103 |
| Tools | None from the library. `scripts/secops_check.py controls` and `consent`; the sibling's `threats` check if the person shares a register; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/control-threat-model-and-consent-assurance-output.md` |
| Input | The request and its context: the control matrix with artifacts, the threat register, the person's change triggers and design version, the current consent text (purposes in the product's words), the list of processing the system performs, the withdrawal test log, the read date |
| Governance | `references/governance.md`; proof standards, gap classes and verdicts are the person's |
| Catalogue job | none (`list_jobs_2026-10-19.json` lists no security or privacy job) |

## Read the request

- **Read date.** The person's; "not given" otherwise, and ask.
- **What the person shares.** A matrix, a register, consent text, a processing list, a test log. Read only what is shared; never assume an artifact's content.
- **Short or full.** "Is our control matrix backed up?" is short mode. "Prepare our assurance read" is full mode.

## Workflow

### Step 1. Claimed control versus artifact (old DH-04.02.1.2.1)

With code execution, save the matrix as CSV (control_id, claimed_control, citation, artifact, artifact_type, artifact_date, reviewer_note, owner, due, gap_class) and run `python3 scripts/secops_check.py controls --file CONTROLS.csv`. For each row: proven as stated (artifact named, not opened by the model), proven (artifact read, only when the person shares it and it shows the control), unproven (no artifact, or only the matrix), or contradicted (the artifact or a reviewer note shows otherwise). Report flags C1 to C6.

### Step 2. Gap by citation (old DH-04.02.1.2.2)

For each unproven or contradicted row: the clause it cites, what that clause requires from the rows (for example, required versus addressable under the Security Rule, EN-097 to EN-105), and what the artifact shows. The gap class (blocking or documentation miss) is the person's, printed only where they gave it; "not given" otherwise. Never rank every gap as blocking.

### Step 3. Threat coverage and currency (old DH-04.02.2.2.1 and .3)

If the person shares the threat register, mark each threat covered, accepted or open and count open threats by hop (the sibling skill's `secdesign_check.py threats` does this; or count by hand). A tool scan is not a threat model. Against the person's change triggers (or the old task's examples, labeled "old task rule, proposed": new third party, new write-back, new device) and FDA's list of changes that may impact cybersecurity (EN-060), state whether any change since the model's design version is recorded. Record the last design version the model matches and who watches for triggers, or "not given".

### Step 4. Consent text versus practice (old DH-04.02.4.2.1)

With code execution, save the purposes (purpose, data_class, recipients) and the processing list (step, purpose, data_class, recipient) and run `python3 scripts/secops_check.py consent --purposes PURPOSES.csv --processing PROCESSING.csv`. Each step is described, broader than described, or missing from the text. Lay the rules a broader step may touch beside it, for the person's legal owner, only for the market in the request (EN-109 for the EU; EN-123, EN-125 for Washington; EN-117 for Part 2; CS103 for HIPAA). Whether a step is lawful is not the model's call. A draft text is never read against a future design.

### Step 5. Withdrawal test (old DH-04.02.4.2.2)

With the test log (job, should_stop, ran_after_withdrawal, test_env, test_date), add `--withdrawal WITHDRAWAL.csv` to the consent run. Report jobs that still ran after a withdrawal they should have stopped (W1), tests run in production (W2) and results not recorded (W3). A flipped preference flag is not a pass. For MHMDA, deletion must flow to processors and third parties within 45 days (EN-126).

## Build the output

Follow `assets/control-threat-model-and-consent-assurance-output.md`. Answer first: controls proven as stated, unproven and contradicted; open threats by hop and whether the model is dated; consent steps described, broader and missing; withdrawal jobs that still ran. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/secops_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- No control is "proven" on the matrix alone; "proven as stated" is kept apart from "proven (artifact read)".
- No verdict: no "compliant", "audit-ready" or "secure".
- Gap classes, triggers and design versions are the person's or "not given".
- Consent rows cited only for the market in the request; lawfulness left to the legal owner.
- `python3 scripts/secops_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; [WF] and "(inference)" labels travel with their rows.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Redesigning a control, a consent flow or the threat model: `dh-technology` cybersecurity-and-privacy-by-design.
- App access revocation through a certified FHIR API: `dh-technology` integration-quality-monitoring.
- Quality system documentation compliance: `dh-regulatory-and-quality` documentation-compliance-monitoring.
- Owners and recheck dates for the misses found here: task B1.
