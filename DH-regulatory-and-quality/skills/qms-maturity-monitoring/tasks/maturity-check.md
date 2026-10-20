# A1 Maturity check

Framework task: DH-03.02.3.2, Part A, task A1. Replaces the earlier "QMS maturity check" and "QMS score" sections.

## What this task delivers

A process-by-process view of the evidence that the QMS runs, against the A1 process map of the design skill: for each process, the criteria the evidence can be checked against (with their sources), the evidence the person showed or described, and what is missing. If the person has a maturity scale, it is applied as they wrote it. If not, the output presents criteria and evidence without any level or score. It answers "what evidence do we have that each process runs, and where is it thin?"

Why it matters: a procedure shows a process was designed, not that it runs. Since 2 February 2026 FDA can read management review and audit reports (QS15) and inspects through areas and elements it names (QS30, QS33). Evidence gaps are cheaper to find in a self-check than in an inspection.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Quality & Software Lifecycle Director (`quality-systems-director-software`) |
| Skill | DH-03.02.3.2 Part A, Maturity check |
| Workflow | The steps below |
| Knowledge | `references/maturity-criteria.md`; `references/process-map-requirements.md` (the A1 map from the design skill); `references/quality-systems-research.md` |
| Tools | None from the library. `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/maturity-check-output.md` |
| Input | The request and its context: the process map (from the design skill or the person's list), the period to check, the evidence the person supplies or describes, their maturity scale if any |
| Governance | `references/governance.md`; findings and evidence only; the scale and any level are the person's |

## The rule that shapes this task: findings and evidence only

The model reads evidence against criteria. It does not assign a level, score, color or average unless the person's own scale defines it, and it never declares a process mature or effective. The register's starter rule (owner, record from the last period, review of that record) is offered as an option and applied only if the person adopts it (`references/maturity-criteria.md`).

## Read the request

- **Process list.** Use the design skill's A1 map if it is in the conversation. Otherwise use P1 to P16 in `references/process-map-requirements.md`, or the person's own process list, and say which.
- **Period.** Ask which period the evidence should come from (for example "since the last management review"). Without a period, records cannot be called current.
- **Scale.** Ask whether they have a maturity scale. Take it verbatim if they do.
- **Evidence.** What they can show or describe: records, logs, minutes, audit reports. Aggregates and descriptions are enough; do not ask for patient data.
- **Mode.** Short for a direct question; full for a self-assessment document.

## Workflow

### Step 1. Fix the frame

Write back: processes in scope, the period, the scale (theirs, the adopted starter rule, or "no scale: criteria and evidence only"). Confirm before checking.

### Step 2. Criteria per process

For each process, list the criteria from `references/maturity-criteria.md` with row ids. Add the person's own criteria if their scale has them. Do not add criteria from memory; ISO 13485 clause text is not in the sources (`[GAP]`).

### Step 3. Read the evidence

For each criterion, record one of: evidence seen (what it is, its date), evidence described but not seen, no evidence, not applicable per the person. Quote dates and identifiers from the person's material. A procedure alone is "designed, no record seen for the period".

Points to check where they apply, from the rows:

- Management review and internal audit reports exist for the period and are written as records an investigator can read (QS15, BX14).
- Complaint records carry the seven US items where the US applies (QS11).
- MDR event files record the reportability deliberation (VG21); non-reported corrections carry a justification reviewed by a designated person (VG24).
- Closed CAPA show effectiveness verification (EU4) and depth proportionate to risk (QS18).
- Changes were assessed for risk and impact before implementation (QS34).
- Records from before 2 February 2026 may be reviewed by FDA; note if the person has done a comparative analysis (QS26), without judging whether they should.

### Step 4. Apply the person's scale (only if given or adopted)

Apply their level definitions process by process. Where a definition does not decide the level from the evidence, say "the scale does not decide this; your call" rather than choosing. Never average across processes.

### Step 5. Findings

List findings as factual statements: "No management review record for the period" or "Three of five closed CAPA show no effectiveness verification in the records shown". Each finding names the process, the criterion, the row and the evidence. No cause, no severity, no grade unless the person's scale sets it.

## Build the output

Follow `assets/maturity-check-output.md`. Answer first: the processes with the least evidence for the period, and the one or two findings that matter most for the criteria the rows tie to inspection (QS15, QS33). Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every criterion has a row id or is the person's own.
- Every evidence line says seen, described, none or not applicable.
- No level, score or average unless the person's scale or adopted rule defines it.
- No statement that the QMS or a process is mature, effective, compliant or inspection-ready.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- A self-check on evidence the person supplies; not an audit and not a certification readiness opinion.
- Indicators over time are A2; what to repair and who owns it is B1.
- Drugs, biologics and wellness apps are out of scope.
