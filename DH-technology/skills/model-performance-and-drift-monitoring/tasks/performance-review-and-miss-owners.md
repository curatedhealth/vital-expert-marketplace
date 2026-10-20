# B1 Performance review and miss owners

Framework task: DH-01.04.3.2, DH-01.04.2.2 and DH-01.06.1.2, Part B, task B1. Carries the old tasks "DH-01.04.3.2.3 Validation miss", "DH-01.04.2.2.3 Drift response", "DH-01.06.1.2.2 personalisation pass rule" and "DH-01.06.1.2.3 personalisation miss owner" as steps 1, 3 and 4.

## What this task delivers

For each failed record element (A1), each threshold crossed and each fired watch (A2), and each personalization rule that failed the person's pass rule: the facts, the owner the person names, the action the person chooses (retrain, recalibrate, roll back, stop the decision, keep running), the replacement version or the time the decision stays stopped, whether the model may influence the named decision meanwhile, and the recheck date. Then the decisions the review surfaces, each with its facts and route, all left to the person. It answers "by our own rules, what failed, who owns each miss, what do we do about it, and when do we look again?"

Why it matters: the old tasks said "Do not leave a fired watch with no action", "Do not let an incomplete model influence the named decision" and "Do not close a failed element because the existing assessment skill already described it". A review that assigns actions the team never chose, or names owners it never named, says more than the data does.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `clinical-algorithm-validator` (old DH-01.04.3.2.3, DH-01.04.2.2.3); `ai-ml-governance-director` (old DH-01.06.1.2.2 and .3). Work as a monitoring analyst who records the person's decisions against their rules |
| Skill | DH-01.04.3.2, DH-01.04.2.2 and DH-01.06.1.2 Part B, Performance review and miss owners |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/monitoring-rules.md` section 8; rows DA-90, DA-92, US-12, US-13, EU-05; `references/governance.md` |
| Tools | None beyond A1 and A2. `scripts/drift_check.py words`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/performance-review-and-miss-owners-output.md` |
| Input | The request and its context: A1 and A2 outputs or the person's files and read date, the pass rules (records and personalization), the owners, actions, replacement versions, stop durations and recheck dates the person sets |
| Governance | `references/governance.md`; the person judges and decides |
| Catalogue job | none |

## The rule that shapes this task: people judge and act

The person writes the rules, names the owners, chooses the action and sets the recheck dates. The model reads the facts against the rules and writes down what the person decided. It never decides retrain, roll back or stop, never decides whether an incomplete model may influence a decision, never decides reportability, never names an owner the person has not named and never closes a failed element.

## Workflow

### Step 1. Confirm the pass rules (old "personalisation pass rule")

Write each rule back verbatim with its date: the record rule from A1; for each personalization rule the elements that count (rule, population, outcome watched) and the element that blocks release if it fails (old task DH-01.06.1.2.2). A unit with no rule: "pass rule not given `[GAP]`"; report its facts, mark nothing failed. Do not score a unit before its rule exists.

### Step 2. The misses, with their facts

List each failed element, crossed threshold and fired watch from A1 and A2: model or rule, element, the fact (script output), the threshold and its date (the person's), and what the record already says (watch action specified, owner on the register). Where a reading allows two interpretations on the person's words (for example, whether a crossed input threshold is a fired watch when the watch is defined on O/E), show both and write "your call".

### Step 3. Response for each miss (old "Drift response", "Validation miss")

For each: the owner the person names (or "owner not named"; ask); the action the person chooses, from retrain, recalibrate, roll back or stop the decision, or keep running (or "action not given"; ask); the replacement version or the time the decision stays stopped (or "not given"); for an incomplete validation, the missing item and whether the model may influence the named decision meanwhile, as the person states (old task DH-01.04.3.2.3). Facts that inform the choice: responses range from a warning to retraining or an architecture change (Sahiner et al. 2023, DOI 10.1259/bjr.20220878, DA-90); recalibration fits calibration drift with event-rate shift and stable discrimination (Davis et al. 2017, DOI 10.1093/jamia/ocx030, DA-92). Propose nothing unless asked; label any proposal "proposed".

### Step 4. Personalization misses (old "personalisation miss owner")

For each personalization rule that failed at least one element: the product owner the person names for each failed element and the recheck date, or that the unit is stopped (old task DH-01.06.1.2.3). A failed element stays open until the person closes it with evidence.

### Step 5. Routes the review raises

- A retrain or rule change on an authorized device: a change specified in an authorized PCCP and done per its Modification Protocol needs no new submission but is documented in the quality system (FDA PCCP final guidance, 18 August 2025, US-12); deviating from it would generally make the device adulterated and misbranded (US-13); EU pre-determined changes (Article 43(4), EU-05). Route to `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- An event or a performance change that may be reportable: `dh-regulatory-and-quality` audit-capa-and-complaints.
- A rewritten record or new validation: `clinical-ml-model-development-and-validation` (this pack).

### Step 6. Decisions for the person

List the decisions the review surfaces, each with its facts: action per fired watch, whether to reset a threshold or rule (with the date the new one is written, so later reads use it), whether a model keeps influencing a decision while its record is incomplete, whether to run a micro-randomized test of a rule. Kill, continue, retrain or stop is the person's.

## Build the output

Follow `assets/performance-review-and-miss-owners-output.md`. Answer first: the misses by name, how many have an owner, an action and a recheck date, and the open item that most limits the review. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/drift_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Rules, owners, actions, versions, stop durations and recheck dates are the person's, and the review says so.
- No action chosen, no failed element closed, no reportability decided by the model.
- Units without a rule are not marked failed.
- The review is labeled "performance review draft for the owner".
- Every fact names its source and date in plain words with the row id after it.
- `python3 scripts/drift_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Change control under an authorization: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Reportability and CAPA: `dh-regulatory-and-quality` audit-capa-and-complaints.
- Any wording for a regulator, customer or clinicians: stops for the owner the person names.
