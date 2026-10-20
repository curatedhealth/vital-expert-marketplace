# B1 Integration review and miss owners

Framework tasks: DH-04.01.1.2, DH-04.01.2.2, DH-04.01.3.2 and DH-04.01.4.2, Part B, task B1. Carries the old tasks "DH-04.01.1.2.3 Nonconformance assignment", "DH-04.01.2.2.3 Failed cell report", "DH-04.01.3.2.3 Map error classes" and "DH-04.01.4.2.3 Step change for the next release" as steps 2 to 5.

## What this task delivers

For every failure from A1 and A2: the failure, the system that must change (sender or receiver, app or EHR configuration) as the person assigns it, the owner the person names, and the release or patch that will close it, or "accepted" with the reason and the person who accepted it. The map error class that blocks the person's threshold, tied to the map version. The one step that must change before the next release, with the change and its owner. Then the decisions the review surfaces, all left to the person. It answers "by our own rules, what failed, who owns each miss, and what do we have to decide?"

Why it matters: the old tasks were clear that a failure is not closed because a ticket exists, a failed cell is not a known limitation until someone named accepts it, and a new map version that leaves the blocking class untouched is not published.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `fhir-integration-specialist` (old DH-04.01.1.2.3, DH-04.01.2.2.3); `data-engineering-manager-health` (old DH-04.01.3.2.3); `clinical-informatics-lead` (old DH-04.01.4.2.3). Work as an integration review lead who records against the person's rules |
| Skill | DH-04.01.1.2 Part B, Integration review and miss owners |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/monitoring-rules.md`; `references/governance.md` |
| Tools | None beyond A1 and A2. `scripts/integration_check.py`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/integration-review-and-miss-owners-output.md` |
| Input | The request and its context: A1 and A2 outputs or the person's files and read date, the pass rules, owners, releases, acceptances and recheck dates the person sets |
| Governance | `references/governance.md`; the person judges and decides |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the rules, assigns each failure to a system, names the owners, sets releases and recheck dates, accepts failures by name and decides what a failure leads to. The model reads the data against the rules and writes down the result. It never calls the integration reliable, conformant or ready, never names an owner the person has not named, never closes a failure on its own, and never supplies a threshold.

## Workflow

### Step 1. Confirm the rules

Write each rule back verbatim, numbered: checks and pass rules (A1 step 1), launch and write-back passes and ceilings (A1 step 3), rate definitions and thresholds (A2 step 1). A unit without a rule: "pass rule not given `[GAP]`"; report its values but mark nothing met or failed.

### Step 2. Nonconformance assignment (old "Nonconformance assignment")

For each failure class from A1 scoring: the system that must change (sender or receiver) as the person says, the owner, and the release or patch that will close it, or "accepted" with the reason and who accepted it. A failure with no known owning team stays "owner not named" and says so. A ticket is not a closure.

### Step 3. Failed cell report (old "Failed cell report")

For each flagged cell from the A1 launch run: the cell, the scope requested, the HTTP status or OperationOutcome as recorded, assigned by the person to the app or to the EHR configuration ("not assigned" otherwise). The cell stays failed until a later run passes it. A cell is never reclassified as a known limitation without the name of the person who accepted it.

### Step 4. Map error classes (old "Map error classes")

From A2: the error classes by map version, and the class the person names as blocking their threshold ("not named" otherwise). If a new map version is planned, list whether it addresses that class; a version that leaves the blocking class untouched is flagged for the person.

### Step 5. Step change for the next release (old "Step change for the next release")

From A2: the step whose workaround the person says blocks the clinical purpose, the change (remove a field, prefill a code, move the exchange) and its owner, all the person's. Polish items are not the blocking step. If the person has not picked one, list the steps with workarounds and their counts, and ask.

### Step 6. What the person must decide

Each open assignment, each acceptance without a name, the blocking class, the blocking step, whether a profile that failed every sample holds go-live or rollout, and recheck dates ("not given" where missing). Propose nothing unless asked; label any proposal "proposed". Go-live, rollback and release are the person's.

## Build the output

Follow `assets/integration-review-and-miss-owners-output.md`. Answer first: counts of units met, failed and not measurable against the person's rules; failures by name; how many have an owner and a release or acceptance; the flag that most limits the review. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/integration_check.py words ANSWER.md`; without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Rules, assignments, owners, releases, acceptances and recheck dates are the person's, and the record says so.
- No overall verdict; no failure closed by the model; acceptances carry a name or say "not accepted".
- Units without a rule are not marked met or failed.
- The review is labeled "integration review draft for the owner".
- The record line is the very last line; the calls list and the offer of the full version come before it.

## Boundaries

- Complaints and CAPA arising from integration failures: `dh-regulatory-and-quality` audit-capa-and-complaints.
- Release go or no-go of the software: `dh-technology` software-quality-and-delivery-monitoring.
- Any wording for a customer or EHR vendor: stops for the owner the person names.
