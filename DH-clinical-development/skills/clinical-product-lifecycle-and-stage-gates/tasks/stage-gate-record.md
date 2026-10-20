# B1 Stage gate record

Framework task: DH-01.01.1.1, Part B, task B1. Replaces the earlier "Stage gate record" section (DH-01.01.1.1.3).

## What this task delivers

A gate record draft: each of the person's gate criteria read against the work products they shared, marked present, missing or not measurable, with the fact and reference behind each; the decision the person states (go, hold, recycle, stop), the date and the person who decided; the attendees as named; open items with the owner the person names and what each blocks. It answers "did we pass by our own criteria, and who carries what is missing?"

Why it matters: a gate decided from a roadmap color or because the date arrived (the old rules) leaves no trace anyone reading the record later can follow. FDA expects design reviews at major decision points (PL5), and the records needed to show design compliance sit in the design and development file (PL9, QS24). The record written here is the product team's draft; the formal design review record belongs to `dh-regulatory-and-quality` design-controls-and-risk-management.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Product Manager (`digital-health-product-manager`) |
| Skill | DH-01.01.1.1 Part B, Stage gate record |
| Workflow | The steps below |
| Knowledge | A2 output; `references/gate-evidence-rules.md` sections 1 and 3; rows PL1, PL2, PL4, PL5, PL9, PL66, PL67, TM3, TM13, TM14, QS23, QS24 (DOI 10.1136/bmj.n2061) |
| Tools | None |
| Prompt | This guide |
| Template | `assets/stage-gate-record-output.md` |
| Input | The request and its context: the gate name, the person's criteria, the work products shared (ids, versions), the decision, date, decider and attendees as the person states them |
| Governance | `references/governance.md`; the person sets criteria and makes the decision |
| Catalogue job | none |

## The rule that shapes this task: people decide

The person writes the gate criteria, in their own words, and makes the decision. The model checks the material against those criteria and writes down what the person decided. It never sets a criterion, never decides that the gate passed, and never names a decider, attendee or owner the person has not named. If asked to propose criteria, it may, each marked "proposed" with the row behind it (for example TM14 progression criteria, PL4 design review elements), and applies none until the person confirms.

## Workflow

### Step 1. Confirm the criteria

Write the person's criteria back, numbered, verbatim. If none were given, say "Gate criteria not stated `[GAP]`", offer the source-named elements from A2 as "proposed", and stop before marking anything.

### Step 2. Read the material against each criterion

Follow `references/gate-evidence-rules.md` section 3: present (with reference), missing, or not measurable `[GAP]`. A status word with no work product is not present. Where a criterion depends on a source element, cite the row.

### Step 3. Record the decision as stated

Write the decision, date and decider exactly as the person gives them. If the decision is go while a criterion is missing, write both facts side by side and the person's stated reason; do not judge it. Note TM3 (repeat rather than progress automatically while uncertainties remain) only as a sourced reference point, not as a verdict.

### Step 4. Attendees

List attendees as named. If the person asks whether attendance meets ISO 13485 7.3.5, state PL1 and PL6 and that the design review record itself belongs to `dh-regulatory-and-quality` design-controls-and-risk-management; do not certify it. Independence: PL2, QS23, PL66, PL67.

### Step 5. Open items, owners and blocks

For each missing item: the owner the person named (or owner not named), what it blocks by dependency, and the date the person set to read the gate again (or "reread date not given"; ask). The old rule holds: do not unblock the next stage while the item is missing, unless the person decides so and the record says it.

## Build the output

Follow `assets/stage-gate-record-output.md`. Answer first: criteria present, missing and not measurable (counts of the person's criteria), the decision as stated, and the item that blocks most. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every criterion, the decision, the decider, attendees and owners are the person's, and the record says so.
- Every "present" carries a work product reference.
- No general verdict ("passed", "ready"); only per-criterion facts and the decision as the person stated it.
- The record is labeled "gate record draft for OWNER".
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The design review record in the QMS and its signature: `dh-regulatory-and-quality` design-controls-and-risk-management and document-and-change-control.
- Stage health across gates over time, days open, repair: `lifecycle-quality-monitoring` (this pack).
- Any external wording about the gate (board, investor, FDA, notified body): stops for the owner.
