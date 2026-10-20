# A2 Process ownership and governance cadence

Framework task: DH-03.02.3.1, Part A, task A2. Replaces the earlier "Process owner" and "Governance cadence" sections.

## What this task delivers

A governance design for the QMS: for each process on the A1 map, the owner the person names, the record the process produces, and the forum that reads it; for each forum (management review, internal audit program, any other the person runs), its inputs, the decisions it may take, its attendees as the person names them, and its cadence as the person sets it. It shows which of these records FDA can now inspect and which external audit clocks the cadence has to fit around. It answers "who owns what, what gets reviewed, and how will an investigator see it?"

Why it matters: the QMSR removed the old shield on management review, internal audit and supplier audit reports (QS15). FDA calls these programs fundamental to the culture of quality it expects (QS16). The records are now evidence in their own right.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Quality & Software Lifecycle Director (`quality-systems-director-software`) |
| Skill | DH-03.02.3.1 Part A, Process ownership and governance cadence |
| Workflow | The steps below |
| Knowledge | `references/governance-records.md`; the A1 map; `references/qms-requirements-additions.md` |
| Tools | None from the library. `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/ownership-and-cadence-output.md` |
| Input | The request and its context: the A1 process map (or the person's process list), owners as the person names them, existing forums and their cadence, markets (for the external clocks) |
| Governance | `references/governance.md`; the person names owners and sets cadence |

## The rule that shapes this task: the person names owners

The person names every owner, attendee and cadence. Use the owner or role the person names, in their words. Only if they named none for a process, write "owner not named" and ask. Never suggest a job title, a role name or a person, even as an example. The model lists what each process must produce and which forum should read it, from the sourced rows.

## Read the request

- **Process list.** Use the A1 map from the conversation. Without one, run A1 in short mode first or take the person's list and say the requirement links were not checked.
- **Owners.** Ask for one owner per process in a single question. Accept names, teams or roles in the person's words.
- **Forums.** Which forums exist today, what they read, what they may decide, who attends, how often.
- **Mode.** Short for a direct question; full for a governance charter draft.

## Workflow

### Step 1. Owner, record and reader per process

For each process on the map write one row: process, owner (the person's, or "owner not named"), the record the process produces, the forum that reads that record. Take the record from the process's sourced basis, for example complaint records with the seven US items (QS11), the justification for not investigating (QS12), MDR event files with the reportability deliberation (VG21), the justification for non-reported corrections reviewed by a designated person (VG24). Where a process has no sourced record in the rows, write "record named by the person".

Flag any process with no owner and any record with no reader. Those are the two design gaps this step exists to find.

### Step 2. Inputs per forum

For management review, list the inputs from the "Inputs a governance forum can read" table in `references/governance-records.md`, each with its row. Ask the person which they will bring and at what level of detail. Do not list ISO 13485 clause 5.6.2 inputs from memory: the clause text is not in the sources (`[GAP]`, free read-only copy per ST13).

For the internal audit program, record the audit scope by process (map P1 to P16) and the person's planned coverage. Say that audit reports are now inspectable (QS15) and that FDA expects audits and reviews against aligned requirements, not separate QSR and ISO 13485 exercises (BX15).

### Step 3. Decisions each forum may take

Ask the person what each forum may decide (for example resources, holding a release, accepting a residual risk, opening a CAPA). Record their list. Where a decision is legally assigned, say so from the rows: release conformity checks are a PRRC duty in the EU (EU10); risk acceptability is weighed against benefit under Annex I (EU12). Never decide on the person's behalf which forum holds which authority.

### Step 4. Cadence against external clocks

Write the person's cadence for each forum. Beside it, list the external clocks that apply to their markets from `references/governance-records.md`: notified body audits at least every 12 months and unannounced audits at least once every five years (EU25); MDSAP three-year cycle (QS42) and its report deadlines (QS48, QS49); FDA inspections risk-scheduled (QS41). These are facts to plan around, not targets. If the person has set no cadence, leave it blank and ask.

### Step 5. What an investigator can see

List the records from Steps 1 to 4 that FDA can now inspect (management review, internal audit, supplier audit: QS15), plus the point that records made before 2 February 2026 may be reviewed and a comparative analysis may help (QS26). Whether to do that analysis is the person's decision.

### Step 6. Roles the law names

Record the person's arrangement for each role a row names: PRRC (EU8 to EU11, including written split of responsibilities and protection from disadvantage), top management (BX13, QS36), the designated reviewer for non-reported corrections (VG24). The skill checks the arrangement against the row; it never proposes who.

## Build the output

Follow `assets/ownership-and-cadence-output.md`. Answer first: processes with no owner, records with no reader, and which records are inspectable. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections, then table rows that the person's facts do not touch (list them by P number in one line); count every table cell except the Rows column; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every owner, attendee and cadence is the person's, and the output says so. No job title appears that the person did not write.
- Every record and input carries its row id or "named by the person".
- External clocks are labeled as facts, not targets.
- No statement that governance is effective or inspection-ready.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Design of ownership and cadence only. Whether governance works in practice is the monitoring skill (DH-03.02.3.2).
- No HR or organization design: the skill does not propose reporting lines or headcount.
- Drugs, biologics and wellness apps are out of scope.
