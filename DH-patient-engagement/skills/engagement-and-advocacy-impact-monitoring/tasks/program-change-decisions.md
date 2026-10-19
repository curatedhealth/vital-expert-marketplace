# B1 Program change decisions

Framework task: DH-02.03.2.2, Part B, task B1. Replaces the earlier "Programme change" section (CF-12.02.03.2.2.3) and holds the pass rule and the owner of each miss as steps.

## What this task delivers

For each activity, the person's rule and whether the A2 result met it; for each missed activity, one decision recorded as the person makes it (stop, change the audience, or change the content), the owner they name, and the next date if they set one; a ranking of the changes by the person's own scores where they want one; the order of decisions by dependency; and the points that stop for an owner. It answers "what do we change, who owns it, and what has to be decided first?"

Why it matters: the old rule holds that no new activity is added before the one that missed is decided. Changes that add support to patients or new partner payments reopen compliance questions (CP-US-26 to CP-US-28, PE-71), and off-list claims reopen review.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Marketing Manager (`digital-marketing-manager`) |
| Skill | DH-02.03.2.2 Part B, Program change decisions |
| Workflow | The steps below |
| Knowledge | A1 definitions, A2 results; `references/indicators.md`; `references/governance.md` |
| Tools | `analytics.rice` or `analytics.mcda` (counted, only on the person's numbers) |
| Prompt | This guide |
| Template | `assets/program-change-decisions-output.md` |
| Input | The request and its context: A2 results, the person's pass rules, their decision per miss, owners, scores for ranking (RICE inputs or 0 to 4 scores and weights), dates if they set them |
| Governance | `references/governance.md`; the person decides, the connector ranks, owners clear |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: one decision per miss, the person's

The model lays out the three options for each missed activity with the facts from A2 that bear on each. The person picks. The model never picks, never adds a new activity before the miss is decided, and labels any suggestion "proposed".

## Read the request

- **Rules.** The person's pass rule per activity. No rule: no miss; ask.
- **Results.** From A2, with the as-of date.
- **Decisions and owners.** Ask for both in one question.
- **Ranking.** Only if the person wants the changes ordered and supplies the numbers. RICE: reach, impact (0.25, 0.5, 1, 2 or 3), confidence as a percent, effort. MCDA: 0 to 4 scores and weights summing to 1.
- **Mode.** Short for a direct question; full for a program review paper.

## Workflow

### Step 1. Rule against result

Table: activity, the person's rule, the A2 result, met or missed. Unscored activities stay "unscored (no record)", not missed; the decision for them is whether to create a record.

### Step 2. Options per miss

For each miss: stop, change the audience, change the content. Beside each, the A2 facts that bear on it (for example "webinar: 37 bookings against your target of 60, 9 percent of 412 reached; peer-mentor calls: 71 completions against your target of 60"). Mark any option that would add support to patients, pay a partner, or use a new claim with the stop it triggers.

### Step 3. Record the person's decision and owner

Write the decision as the person states it, the owner in their words or "owner not named", and the next date only if they give one.

### Step 4. Rank the changes (optional)

If the person supplies RICE numbers, call `analytics.rice` with `initiatives` (id, reach, impact, confidence as a percent, effort). Read `references/tools.md`: a fraction for confidence is read as a percent and shrinks scores a hundredfold. If they supply 0 to 4 scores and weights, call `analytics.mcda`. Report the order as the result of their numbers, never as a recommendation.

### Step 5. Sequence by dependency

Write which decision blocks which, with the reason: for example "create a record for the newsletter before judging it"; "partner agreement signed before any further support to that partner (PE-71, PE-80 [INDUSTRY])"; "compliance owner decides on support above the year's figure before the loan is extended (CP-US-27)". No urgency language.

### Step 6. Stops

List what stops for an owner: support changes (compliance owner), partner payments or agreement remedies (compliance or legal owner), off-list claims (review owner), any statement of clinical benefit (regulatory owner), any report to a partner or regulator (the owner named for that report). When the person asks for wording, draft only what the facts support, labeled "draft for the owner".

## Build the output

Follow `assets/program-change-decisions-output.md`. Answer first: the misses, the decision recorded for each (or "decision not made"), and the first decision in the dependency chain. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule, decision, score, owner and date is the person's.
- No new activity is proposed before each miss is decided.
- The ranking, if any, is described as the result of their numbers.
- No sentence says support is protected or that the program improved health.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Changes to program activities and partnerships. Redesigning the program's purpose is DH-02.03.2.1 A1.
- Payer or outcomes contracts are Market Access.
