# B1 Release review and repair plan

Framework task: DH-02.04.4.2, Part B, task B1. Replaces the earlier "UX release note" section and the one-line pass rule and owner rule.

## What this task delivers

A release review draft for one build: the person's acceptance rules written down, each checked against A1 and A2 (met, missed, not measurable), the tasks and controls that miss, repair options with their sourced basis, the person's scores ranked by the connector if they want a ranking, the owner of each repair and of any block, the facts the regulatory owner needs, and the decision recorded against the build. It answers "can this screen ship, and if not, what do we fix and who owns it?"

Why it matters: without rules written before the numbers, every review reopens what "usable" means. FDA sets no numeric error-rate acceptance for validation (UX-US-43), so the rules are the team's to write, and the old register rule gives a starting shape: block shipment if a misread has no control or if participants returned to the old step.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Service Design Director (`service-design-director`) |
| Skill | DH-02.04.4.2 Part B, Release review and repair plan |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/release-review-rules.md`; `references/ux-usability-research.md` |
| Tools | `analytics.mcda` (counted) for repairs the person scored; `analytics.rice` (counted) only if asked; A1's script if no A1 run exists; `verify.build_record` for the decision record |
| Prompt | This guide |
| Template | `assets/release-review-output.md` |
| Input | The request and its context: the build, the person's rules, A1 and A2 results, repair scores and weights, named owners |
| Governance | `references/governance.md`; people set rules, decide shipping, score repairs and name owners |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: the person's rules decide; the release owner decides

The person writes the rules; the model checks results against them. The model never says a build may ship. It records the person's decision against the build, with the misses and the owners. A block names its owner in the person's words, or "owner not named". If asked to pass a screen that failed the person's own rule, it states the miss and stops for the release owner.

## Workflow

### Step 1. Gather the evidence

Use A1 (results by task) and A2 (controls and field) from the conversation. If either is missing and needed, run it first in short mode. A review on one of them says what was not reviewed.

### Step 2. Write the rules with the person

Offer the shapes in `references/release-review-rules.md`, filled with the person's words and numbers: critical-task use errors, controls in build, training-only controls, return to old step, sample, test conditions, satisfaction. Offer the old register rule as a starting rule they may adopt: "block if a misread has no control or participants returned to the old step". Write the rules back for confirmation. A task without rules gets a factual summary and no verdict.

### Step 3. Check each rule

Mark each rule met, missed or not measurable `[GAP]`, with the count or evidence behind it from A1 or A2. A task "meets your rules" only if every rule is met. Never average tasks into one score.

### Step 4. Hypotheses, not causes

For each miss, list possible reasons as hypotheses with what would confirm them, drawn from the rows: a unit misread may reflect a control missing from the build (confirm from A2); errors after training may reflect training given immediately before testing or different from real training (UX-US-41, CS80; confirm from the protocol). Never state a cause the data does not show.

### Step 5. Repair options

For each miss, list repair options in FDA's order of preference: design change, protective measure, then information for safety (UX-US-33). Mark a labeling or training repair on a critical task "needs data" (UX-US-42). Label all options "proposed".

If the person wants a ranking, ask for criteria phrased higher is better (suggest one on harm severity addressed, since FDA weighs severity over probability, UX-US-32), weights summing to 1 and 0 to 4 scores, then call:

```
analytics.mcda {alternatives: [{id: "<repair>", scores: {...}}], criteria_weights: {...}}
```

Use `analytics.rice` only if the person asks for RICE: every number is theirs, confidence in percent (0.8 returned scores 100 times too small), and say that RICE has no severity term (`examples/live/rice_repairs.json`).

### Step 6. Owners

For each repair and each block, the owner the person names and the forum that will see it. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. No dates proposed by the model.

### Step 7. Regulatory handoff

If a repair changes the user interface, users, uses, environment, training or labeling, list it as a Decision Point B fact for the regulatory owner (UX-US-49); whether new validation data or a submission is needed is theirs (UX-US-48, UX-US-50, UX-US-51). Note that FDA recommends keeping the human factors records either way (UX-US-53).

### Step 8. Record the decision

Record the person's decision (ship, block, ship with named conditions) against the build version, with the misses, owners and the clearer. Call `verify.build_record` with `clearances` naming the human the person gives; the tool refuses a non-human name. Without a name, the review is an uncleared draft and says so.

## Build the output

Follow `assets/release-review-output.md`. Answer first: which rules the build misses, the block or decision and whose it is, and the first repair with its owner. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule, score, owner and decision is the person's, and the output says so.
- Every verdict cites the count or evidence behind it; no averaging.
- Causes are hypotheses, labeled.
- No statement that the build is usable, safe, validated or compliant; no shipping decision made by the model.
- Regulatory questions are handed over, not answered.
- If it leaves the conversation, the record is cleared by a named person through `verify.build_record`, or labeled uncleared.

## Boundaries

- Checks and structures the person's release decision; does not make it.
- Redesign belongs to the design skill (clinical-workflow-ux-design) and the person's UX designer.
- CAPA and complaint handling belong to the Quality pack.
