# B1 Conformance gaps and go-live scope

Framework tasks: DH-04.01.1.1, DH-04.01.3.1 and DH-04.01.4.1, Part B, task B1. Carries the old tasks "DH-04.01.1.1.3 Conformance gap record", "DH-04.01.3.1.3 Unmatched code hold" and "DH-04.01.4.1.3 Adoption measure".

## What this task delivers

A gap record tied to the guide version the person chose: each payload miss as element path, the rule from the person's check sheet, and whether it blocks go-live (the person's flag). An unmatched-code hold list kept out of the production map, with the steward the person names and the steward's promotion rule. One adoption definition for the replaced step (who, which action, over what period), all in the person's words. Then the decisions for the owner: what is in scope for go-live, which gaps are accepted and by whom. It answers "against our chosen guide, what does not conform, what is held back, and what must we decide before go-live?"

Why it matters: an empty gap list is only meaningful after every element on the sheet was checked (old task output), and a gap accepted without a named person is a gap hidden.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `fhir-integration-specialist` (old DH-04.01.1.1.3); `data-engineering-manager-health` (old DH-04.01.3.1.3); `clinical-informatics-lead` (old DH-04.01.4.1.3). Work as an integration lead who records gaps against the person's rules |
| Skill | DH-04.01.1.1 Part B, Conformance gaps and go-live scope |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/interop-rules.md`; `references/governance.md` |
| Tools | `scripts/fhir_check.py resources` and `map`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/conformance-gaps-and-go-live-scope-output.md` |
| Input | The request and its context: the guide and version chosen, the person's check sheet, one sandbox payload per profile, the map file, the steward and rule, the adoption definition, owners |
| Governance | `references/governance.md`; go-live and acceptance are the person's |
| Catalogue job | none |

## The rule that shapes this task: people decide

The person chose the guide, wrote the check sheet, flags which misses block go-live, names the steward, defines adoption and decides go-live. The model runs the checks and writes down the result. It never calls an integration ready, certified or compliant, never marks a payload conformant because it parses, and never reclassifies a miss as accepted without the person who accepted it.

## Workflow

### Step 1. Confirm the guide and the sheet

Write back the guide and version (from A1) and the sheet's source. If the sheet was not built from that version's StructureDefinitions, say so: a payload is never scored against a version that was not the one selected. No sheet: "check sheet not given `[GAP]`"; nothing is marked conformant.

### Step 2. Gap record (old "Conformance gap record")

Take one sandbox payload per profile (old task method step 1). Run `python3 scripts/fhir_check.py resources --sheet SHEET.json PAYLOAD.json`. Quote the gap table: payload, resource, element path, result, blocks go-live (the person's flag, or "not given"). Resource types with no sheet entry are "not checked", never conformant. An empty list is allowed only after every element on the sheet was checked for every profile in scope.

### Step 3. Unmatched code hold (old "Unmatched code hold")

From the A2 map run: count unmatched codes by source system, confirm they sit in the hold set and not in production (flag K1 if not), and record the steward the person names and their promotion rule in the person's words ("steward not named" otherwise). Unmatched codes are never dropped from the source feed (old task "Do not").

### Step 4. Adoption definition (old "Adoption measure")

Who counts (role, site), which action counts (the new screen used, the old retype stopped) and the counting period, all from the person. A login is never the adoption event. No adoption target or benchmark is supplied: none is sourced. Tracking adoption after go-live routes to `dh-technology` integration-quality-monitoring (step level) or `dh-go-to-market` adoption-monitoring (organization level).

### Step 5. What the person must decide

Each gap marked "blocks go-live: not given" (ask), each accepted gap with the person who accepted it, the go-live scope, the hold list owner, and the rules the legal or regulatory owner must read (A1 step 4). Propose nothing unless asked; label any proposal "proposed". Go-live is the person's.

## Build the output

Follow `assets/conformance-gaps-and-go-live-scope-output.md`. Answer first: checks run and misses found by profile, how many the person flagged as blocking, unmatched codes held, and the item that most limits the record (for example "no sheet entry for MedicationRequest"). Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/fhir_check.py words ANSWER.md`; without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- No "ready", "certified", "compliant" or "conformant" verdict.
- Every miss is tied to the guide version and the sheet line.
- Unchecked resource types and missing blocking flags are visible.
- Steward, adoption definition and owners are the person's, in their words, or "not named".
- The record is labeled "gap record draft for the owner".
- The record line is the very last line; the calls list and the offer of the full version come before it.

## Boundaries

- Go-live wording for a customer or EHR vendor stops for the owner the person names.
- Release go or no-go of the software: `dh-technology` medical-software-lifecycle-and-delivery.
- Interface hazards in the risk file: `dh-regulatory-and-quality` design-controls-and-risk-management.
