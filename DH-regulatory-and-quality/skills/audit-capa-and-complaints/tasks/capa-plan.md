# B1 CAPA plan

Framework task: DH-03.02.4.1, Part B, task B1. Replaces the earlier "CAPA plan" section.

## What this task delivers

A CAPA plan draft for one nonconformity, finding or complaint: the problem, the risk level under the person's procedure, the correction, the cause (or its current state), the corrective and preventive actions, the effectiveness criteria the person sets, the obligations it triggers elsewhere, and the owner. It answers "what do we do about this, and how will we know it worked?"

Why it matters: CAPA procedures were the most cited device area on FDA 483s in FY 2025 (279 citations of 820.100(a), QS53; pre-QMSR data). FDA expects CAPA depth to match the size of the problem and the risk (QS18), and the MDR expects effectiveness to be verified (EU4). A plan without a test of success cannot be checked later.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | QA Manager, Software (V&V) |
| Skill | DH-03.02.4.1 Part B, CAPA plan |
| Workflow | The steps below |
| Knowledge | `references/capa-method.md`; rows QS17 to QS22, QS47, EU4, EU7, EU15, CH9, VG3, VG22 to VG25, R3 |
| Tools | None required. A1 or A2 output if present |
| Prompt | This guide |
| Template | `assets/capa-plan-output.md` |
| Input | The request and its context: the finding or complaint (A1, A2), the person's CAPA procedure (risk levels, root cause method), investigation results so far, owners |
| Governance | `references/governance.md`; the person approves every action and sets every criterion |

## The rule that shapes this task: depth follows risk, and people decide

FDA states the degree of action "shall be appropriate to the magnitude of the problem and commensurate with the risks encountered" (QS18). The person's procedure sets the risk levels and what each level requires. The model applies that procedure, drafts the plan to that depth, and stops at every decision: risk level, cause, actions, criteria, owner, closure.

## Workflow

### Step 1. State the problem

From A1 or A2, or the person's description: what nonconformed, where, which product and versions, how often, since when, with record ids. If neither A1 nor A2 exists and the source is a complaint that might be reportable, run A2 first in short mode; a CAPA does not wait for a reporting decision and does not replace one.

### Step 2. Risk level

Ask for the level under the person's procedure and the risk file entry it rests on. If the event brought new information, note that the risk documentation is reviewed and updated (QS22, EU15). If the person has no levels, say FDA expects procedures that set them (QS18) and offer a proposed scheme, labeled "proposed", not applied until confirmed.

### Step 3. Correction

What fixes this instance (the affected units, versions, records or users). If it touches marketed devices, flag the reporting check: a correction or removal under 806 (VG22 to VG25) or an FSCA under the MDR (VG3, VG8), and route to A2 for the clock. An EU device found non-conforming is corrected, withdrawn or recalled immediately (EU7).

### Step 4. Cause

Use the root cause method the person's procedure names; the sourced rows prescribe none `[GAP]`. Record the cause with its evidence, or "cause not yet established" with the next investigative step. Never state a cause the evidence does not show. If the finding was a repeat (R3), say the earlier CAPA is part of the cause question.

### Step 5. Actions

- **Corrective action:** removes the cause. "Retrain the person" alone only fits when the cause is that the person was not trained (register method rule).
- **Preventive action:** where else the same cause could act (other versions, products, sites, suppliers).
- **Linked changes:** a software fix is a design change (CH9); route the significance question to change control. A risk file update, labeling update or procedure revision is listed with its own owner.

Each action gets an owner the person names, or "owner not named".

### Step 6. Effectiveness criteria, set by the person

For each action, ask the person for: the record to read (complaint code, audit sub-clause, defect tag, test result), the measure, the window, and the pass condition. Offer the shape below, filled with their words. If they ask for a proposal, give one labeled "proposed" with the fact it rests on. A criterion that only checks on-time closure is not an effectiveness criterion (register method rule).

| Action | Record read | Measure | Window | Pass condition (person's words) | Owner |
|---|---|---|---|---|---|

### Step 7. Depth check

Lay the plan against the person's level rule and say where it meets, exceeds or falls short of what the procedure requires for that level. Do not judge whether the procedure itself is adequate.

## Build the output

Follow `assets/capa-plan-output.md`. Answer first: the plan in three lines (correction, cause state, main action) and the decisions the person must make. Then the full plan table, effectiveness criteria, linked obligations and owners.

## Before you hand it over

- Every action, level, criterion and owner is marked as the person's, or "proposed".
- The cause is evidenced or marked "not yet established".
- Each action has an effectiveness criterion or a `[GAP]` asking for one.
- Reporting and change-control links are routed, not decided.
- The plan is a draft; approval and closure stop for the owner. If it leaves the conversation, call `verify.build_record` with the named clearer.

## Boundaries

- No closure decision; that is the person's, after the effectiveness check (the monitoring skill, DH-03.02.4.2).
- No significance or 510(k) decision on a software change.
- No statement that the CAPA "will" prevent recurrence.
