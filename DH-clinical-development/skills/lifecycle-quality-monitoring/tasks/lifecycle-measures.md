# A1 Lifecycle measures

Framework task: DH-01.01.1.2, Part A, task A1. Replaces the earlier "Lifecycle measure" section (DH-01.01.1.2.1).

## What this task delivers

A short set of lifecycle measures written with the person: for each pair of stages they compare, what counts as a healthy move, the evidence the measure requires (the accepted work product and the decision record), and the moves that do not count. Each measure says which source it leans on, or that it is the person's own. The output is the rulebook A2 reads the log against and B1 reviews misses against.

Why it matters: without written measures, stage health is read from a roadmap color (the old rule forbids scoring a stage that way). The sources give the anchors: criteria set before the gate (TM14), no automatic progression (TM3), decisions at major decision points (PL5), records that show them (PL9).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Product Manager (`digital-health-product-manager`) |
| Skill | DH-01.01.1.2 Part A, Lifecycle measures |
| Workflow | The steps below |
| Knowledge | `references/lifecycle-measures.md` sections 1 and 2; `references/lifecycle-stages.md`; rows TM3, TM4, TM13, TM14, PL1, PL2, PL4, PL5, PL9, QS23, QS24 (DOI 10.1136/bmj.n2061) |
| Tools | None |
| Prompt | This guide |
| Template | `assets/lifecycle-measures-output.md` |
| Input | The request and its context: the person's stage model, the stage pairs they want measured, any measures they already use, their gate log fields |
| Governance | `references/governance.md`; the person writes and confirms every measure |
| Catalogue job | none |

## Read the request

- **Stage pairs.** Which moves does the person want measured (for example Concept to Feasibility)? Take their stage names.
- **Existing measures.** Verbatim. Keep them; map each to a source or mark it "your own".
- **Log fields.** Can the log show what the measure needs (evidence reference, decider, decision date)? If not, the measure is not measurable until the field exists.

## Workflow

### Step 1. Write each measure in the person's words

One line per stage pair: "A move from X to Y counts when ...". If the person asks for proposals, offer from `references/lifecycle-measures.md` section 1, each labeled "proposed" with its row (for example "predefined progression criteria met and recorded, TM14").

### Step 2. Name the evidence each measure requires

For each measure: the work product that must be accepted, the decision record (decider, date), and where it lives (the person's log field or document). A measure whose evidence the log cannot hold is marked "not measurable with the current log `[GAP]`" and names the missing field.

### Step 3. Name the moves that do not count

From section 1: a status with no work product; a stage advanced by date; an item marked in progress and then passed with no decision. Add the person's own. Label the source-free ones "proposed".

### Step 4. Map to the countable flags

Show which `scripts/gate_log_check.py` count or flag (section 2) reads each measure, so A2 can run it. A measure that needs judgment beyond a count stays with the person in B1.

### Step 5. Confirm

Write the measures back for confirmation. Nothing is applied until the person confirms. Never set a numeric threshold (days open, percent present); if the person wants one, it is theirs, and no benchmark exists in the sources `[GAP]`.

## Build the output

Follow `assets/lifecycle-measures-output.md`. Answer first: the measures in one table, each with its evidence and source. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every measure is the person's or labeled "proposed"; no threshold was invented.
- Every proposed measure carries its row; [PAPER] rows carry the DOI.
- No measure scores a team or a person.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Gate criteria for one specific gate: `clinical-product-lifecycle-and-stage-gates` (this pack) A2 and B1.
- QMS process metrics: `dh-regulatory-and-quality` capa-effectiveness-monitoring (CAPA effectiveness) and `dh-regulatory-and-quality` design-control-and-risk-monitoring (design control completeness).
