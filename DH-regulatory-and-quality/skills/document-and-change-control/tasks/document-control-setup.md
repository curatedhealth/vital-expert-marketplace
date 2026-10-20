# A1 Document control setup

Framework task: DH-03.02.2.1, Part A, task A1. Replaces the earlier "Controlled document" and "Obsolete copy" sections.

## What this task delivers

A sourced statement of what document and record control has to do for the person's device and markets, and a controlled document lifecycle that produces those records: who owns each document, who approves, where the current version lives, how obsolete copies leave use, and how long each record is kept. It answers "what must our document control do, and how do we run it?"

Why it matters: since 2 February 2026 FDA inspects against the QMSR, and management review, internal audit and supplier audit reports are no longer shielded from inspection (QS15). A procedure written for the old QS regulation can now be out of step on the records an investigator asks for first.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | QA Manager, Software (`quality-assurance-manager-software`) |
| Skill | DH-03.02.2.1 Part A, Document control setup |
| Workflow | The steps below |
| Knowledge | `references/document-and-record-control.md`; `references/QUALITY_SYSTEMS.md` (QS, EU, VG, ST rows); `references/supplementary-rows.md` (QX1 to QX9) |
| Tools | None needed. `regulatory-dh.list_jurisdictions` only if the person asks what public data exists for a market |
| Prompt | This guide |
| Template | `assets/document-control-setup-output.md` |
| Input | The request and its context: device, class, markets (US, EU, other), current procedure or document list if the person shares one, named owners |
| Governance | `references/governance.md` |

## Read the request

- **Markets and class.** US only, EU only, or both. Class II or III, or class I with software, brings design and development records into scope (QS9). If unknown, ask.
- **What they have.** A current procedure, a document list, or nothing. With a procedure, the output is a gap view against the sourced rules; without one, it is a setup.
- **Scope.** A direct question ("how long do we keep records", "can FDA read our management review") gets short mode on that point only. "Set up our document control" gets full mode.

## Workflow

### Step 1. Fix the frame

State which rules apply, each with its row: QMSR in force since 2 February 2026 with ISO 13485:2016 incorporated by reference (QS1, QS3, QS4); US law controls on conflict (QS5); for the EU, Article 10(9) and, if a notified body is involved, Annex IX (EU3, EU22, EU23). Say once that ISO 13485 clause text is not in the sourced references and can be read free through the ANSI IBR portal or ISO OBP (ST13).

### Step 2. Documents versus records

Explain the split FDA restates (QX1): documents controlled under Clause 4.2.4, records under 4.2.5. Then list the US record content the QMSR adds (QS11, QS12, QX3 to QX6). Say that the DMR, DHF and DHR names are retired and their content sits in ISO 13485 Clause 4.2 and Clause 7 records, the DHF mapping to the design and development file (QX7, QS24). For EU, name the Article 10(9) element on managing modifications (EU3) and the timely-update duty (EU2).

### Step 3. The inspectability change

State it plainly: management review, internal audit and supplier audit reports are inspectable under the QMSR (QS15), expected to be readily available (QX8), and records from before 2 February 2026 may be reviewed, with a comparative analysis suggested (QS26). Close with the consequence for the person, without rules the sources do not set: those reports should be written as records an investigator may read.

### Step 4. Retention

Build the retention table from `document-and-record-control.md` section 4: EU technical documentation 10 years after the last device, 15 for implantables (EU6); US MDR event files (VG21); US unreported corrections (VG24). For general QMS records under Clause 4.2.5, write `[GAP]` and point to the clause. Never fill a period from memory.

### Step 5. The lifecycle

Lay out the controlled document lifecycle (`document-and-record-control.md` section 7) filled with the person's names and locations. Each stage shows what is recorded. Approver, owner and storage location come from the person; where missing, "owner not named" and ask. Mark this lifecycle as the pack's working method, not a quotation of the standard.

### Step 6. Where an inspector or auditor looks

One short paragraph: CP 7382.850's Change Control area and its purpose (QS34), and that MDSAP treats clauses 4.1 to 6.3 as indirect impact except 4.2.3 (QS46). Grades are the auditor's; the model does not predict one.

## Build the output

Follow `assets/document-control-setup-output.md`. Answer first: the two or three things the person must do differently, then the tables. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

## Before you hand it over

- Every rule has its row id; no ISO clause text appears that a row does not state.
- Retention periods appear only where a row states them; the rest say `[GAP]`.
- Owners and approvers are the person's, or "owner not named".
- The lifecycle is labeled the pack's method.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Sets up document and record control. Checking an existing document set against it is DH-03.02.2.2. Change significance is A2.
- Does not write the full QMS or its other procedures (CAPA, complaints, audit).
- Does not state that a procedure "complies"; the person's quality owner decides that.
