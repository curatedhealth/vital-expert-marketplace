# A Score privately

Framework task: 2.2 Outcome Prioritization, Part A.

## What this task delivers

A sealed set of scores: every named scorer's importance and satisfaction, whole numbers 1 to 10, for every outcome on the list, given alone and before discussion; computed into each outcome's opportunity, with the group's result ready to show first and the owner's view held back.

Why it matters: the order in which people speak shapes what they say. Private scores with equal weight keep the most senior voice from setting the answer, and keep disagreement visible instead of talked away (method.md O10, O13).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 2.2 Outcome Prioritization, Part A |
| Workflow | The steps below |
| Knowledge | `references/method.md` (O10, O11, O13) |
| Tools | `methods_nav_compute` (template `nav.outcomes`); `decide_attach_scores`; `scripts/outcome_priority_check.py` |
| Prompt | This guide |
| Template | `assets/outcome-score-sheet.md` |
| Input | The outcome list from *Outcome Discovery* |
| Governance | `references/governance.md` |

## Workflow

### Step 1. Check the list is scoreable

Each outcome is in the standard form, names its party and no solution. If one names a solution, restate it before scoring (or send the person to *Outcome Discovery*). Number the outcomes; the numbers are what scorers see.

### Step 2. Name the scorers

Ask who scores in one question, with the score sheet. Good scorers know the outcome from the party's side or own the work that serves it. Three or more gives a group result; fewer is indicative. The owner scores too, on the same sheet; their result is shown later.

### Step 3. Send the sheet, wait

One turn: the sheet ([assets/outcome-score-sheet.md](../assets/outcome-score-sheet.md)), how to return it (to the facilitator only), and that scores are revealed together. Do not discuss outcomes while scores are out.

### Step 4. Compute

Check the set first: every scorer scored both criteria for every outcome, whole numbers 1 to 10. A missing cell is not filled; ask that scorer once, or record "not scored by [name]" and compute without them (named in the report).

Then compute, with neutral item ids (o1, o2, ...):

- With the connector: `methods_nav_compute` with `template_id` `nav.outcomes`, the scores and `owner_scorer_id`. If a brief is open, `decide_attach_scores` with the same cells, then, once every scorer has submitted, `decide_release_scores` with the name of the person who releases them (see references/tools.md).
- Without it: `scripts/outcome_priority_check.py`, which applies the same formula and bands and adds the top-set sensitivity check and the field-test reading.

### Step 5. Reveal the group's result first

Show the group's ranking (Part B). Hold the owner's own ranking until the group has seen theirs.

## Boundaries

- Never score, suggest a score, or "complete" a sheet.
- Never weight a scorer. A weight change needs a reason recorded by the owner; outcome scoring has no weights to change.
- Library opportunity values on outcome rows are not this room's scores. Never show them as such.

## When you are unsure

If only the owner will score, say the result is indicative and that the field-test rule may then apply with more force, and continue.
