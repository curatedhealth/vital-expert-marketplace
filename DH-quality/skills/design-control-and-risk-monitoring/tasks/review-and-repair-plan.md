# B1 Review and repair plan

Framework task: DH-03.02.1.2, Part B, task B1. Replaces the earlier "Design control repair" task (CF-12.03.02.1.2.3); the earlier "pass rule" and "miss owner" steps are steps 2 and 5 here.

## What this task delivers

A review draft that turns A1 findings and A2 observations into a repair plan: the findings scored by the person on criteria they choose, ranked from those scores only, each with the owner the person named, whether the person's rule says a release waits, and the review that must accept the repair. It answers "what do we fix first", "which findings block release 4.2", and "who owns what".

Why it matters: a findings list with no order and no owner stays a list. A ranking built from the team's own scores can be defended, re-run when facts change, and shown to an auditor as the basis of the plan.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Product Development Lead (`product-development-lead`) |
| Skill | DH-03.02.1.2 Part B, Review and repair plan |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/check-criteria.md` (grading section); `references/post-market-feedback.md` |
| Tools | `analytics.mcda` (ranks what the person scored); A1 and A2 tools if their outputs are missing |
| Prompt | This guide |
| Template | `assets/review-repair-output.md` |
| Input | The request and its context; A1 findings; A2 table; the person's criteria, weights, scores, release rule and named owners |
| Governance | `references/governance.md`; people score, rank inputs, release decisions and owners are theirs |

## The rule that shapes this task: people score

The person chooses the criteria, sets the weights and gives every score. `analytics.mcda` ranks only what the person scored. The model never invents a score. If asked to propose scores, it may, each with the fact behind it and marked "proposed", and it does not rank them until the person confirms. A grade under a public scheme (MDSAP, `check-criteria.md`) is also the person's: the model can lay out the scheme's elements per finding; the person decides each element.

## Workflow

### Step 1. Gather the findings

Use A1 findings and A2 hazards with an observed signal. If either is missing, run it first in short mode, or say the plan covers one side only. Give each finding a stable id.

### Step 2. Agree the rule and the criteria

Ask for the person's release rule, in their words (for example "no release with a hazard that has no verified control"; the earlier task wording carried "Do not ship a release with a hazard that has no control"). Propose criteria and let the person drop, add or rename them; three to five is enough:

| Criterion (higher = more urgent) | The question it answers | Facts that inform it |
|---|---|---|
| Patient impact | How bad is the harm the finding leaves open? | A2 severity on the person's scale; hazard chain |
| Regulatory exposure | How directly does it touch what an inspector or notified body examines? | K criterion and row; inspection model elements (QS33, QS34); MDSAP direct or indirect impact (QS46) |
| Ease of repair | How quickly can it be closed? | Size of the fix as the person estimates it |
| Spread | How many releases, markets or hazards does it touch? | A1 links |

Phrase every criterion so that a higher score means more urgent: `analytics.mcda` treats every criterion as "higher is better" (`references/tools.md`). Write 0, 2 and 4 anchors for each criterion with the person before scoring.

### Step 3. Lay out the facts, then collect scores and weights

Build the findings-by-criteria table with the supporting fact and its source in each cell and no score. Ask for weights (summing to 1) and a 0 to 4 score per cell. Write them back for confirmation.

### Step 4. Rank

Call `analytics.mcda` with `alternatives` (`[{"id": "F1 ...", "scores": {"patient_impact": 4, ...}}]`) and `criteria_weights`. Report each finding's value estimate and its largest contributing criterion. For adjacent pairs, state how far a weight would have to move before they swap, worked out from the scores and weights given. Name the close call. Check the claim against each pair of criteria separately. When two findings tie, say which shifts break the tie and which leave it intact; never write "any move breaks the tie" unless every two-criterion shift does.

### Step 5. Apply the person's release rule and owners

For each finding, state whether the person's release rule is met, with the fact behind it. Where the rule is not met, write "release waits under your rule: owner decides". The owner of a finding is not the owner of the release decision: name a release owner only if the person named one for release; otherwise write "release owner not named" and ask. Name the owner the person gave for each finding, in their words; if none, write "owner not named" and ask. Never suggest a job title. Name the review that must accept the repair (the earlier task wording asked for it): the design review, the CAPA review or another the person names. Map A2 outcomes to responding work: estimate review, control redesign, CAPA proportional to risk (QS18), risk file update (QS22, EU15); a change implemented before its risk assessment maps to change control (QS34).

## Build the output

Follow `assets/review-repair-output.md`. Short mode: the ranking with its basis, the findings that stop a release under the person's rule, owners, the one close call. Full mode adds the fact table, anchors and the swap analysis.

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

## Before you hand it over

- Short mode: count the words, excluding tables' source column and any 'Calls made' log; if over 450, cut in the stated order before sending.
- Every score, weight, rule and owner is the person's, and the output says so.
- The ranking cites the tool's method as returned.
- No finding is called resolved, no control effective, no release ready.
- Release decisions, CAPA records and audit responses stop for the owner. If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft. AI-assisted draft.

## Boundaries

- The model ranks only what people scored; it does not grade, accept or release.
- No dates invented for the repair plan; sequence by dependency (what blocks what).
- Device class and pathway route to the regulatory owner.
