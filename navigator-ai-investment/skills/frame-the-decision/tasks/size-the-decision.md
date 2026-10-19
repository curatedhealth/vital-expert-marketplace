# C Size the decision

Framework task: 1.1 Decision Framing, Part B, task C.

## What this task delivers

A people-scored size for the decision on four criteria (stakes, reversibility, commitment horizon, functions involved), the spread between scorers, and what the size implies: how deep the work ahead should go, and whether the outcome scores will need a field test before the decision.

Why it matters: "the format matches the decision, not the budget" (method.md M6). A reversible, single-function decision does not need a three-day program; a hard-to-reverse, multi-year, cross-function decision should not be settled in a meeting. Sizing also triggers a rule later: when a decision is hard to reverse and commits money or people widely, its top outcomes must be checked in the field before the decision (method.md M7).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 1.1 Decision Framing, Part B, Size the decision |
| Workflow | The steps below |
| Knowledge | `references/method.md` (M6 to M8) |
| Tools | `methods_nav_compute` with template `nav.sizing`; or `scripts/sizing_check.py` |
| Prompt | This guide |
| Template | `assets/sizing-score-sheet.md` to collect scores; `assets/decision-contract-output.md` "Size" block for the answer |
| Input | The accepted decision statement (task A); the names of the people who will score |
| Governance | `references/governance.md` |

## Workflow

### Step 1. Name the scorers

Ask who scores: the decision owner plus the colleagues whose judgment the decision needs. Each scorer is a named person. Each scorer's weight is equal (method.md M8). If only one person scores, the size is that person's view; label it so.

### Step 2. Collect scores privately

Send or show `assets/sizing-score-sheet.md`. Each scorer gives a whole number 1 to 10 on each criterion, before any discussion. The anchors are fixed:

| Criterion | 1 means | 10 means |
|---|---|---|
| Stakes | A wrong call is cheap | A wrong call is costly for the organization |
| Reversibility | Very hard to reverse | Easy to reverse |
| Commitment horizon | A few weeks | Several years |
| Functions involved | One function | Many functions |

Do not show anyone's scores, including the owner's, until all are in. The owner's view is shown beside the group's only after the group's scores are revealed (method.md M8).

Never fill a missing score. A scorer who does not score is listed as missing.

### Step 3. Compute

**With the connector:** call `methods_nav_compute` with `template_id` `nav.sizing`, `items` `[{"item_id": "decision"}]`, `scores` as one cell per scorer per criterion (`scorer_id`, `item_id` "decision", `criterion_key`, `value`), and `owner_scorer_id` set to the owner. The engine counts reversibility inverted (a 10, easy to reverse, lowers the size) and returns the group result, the owner's view, sensitivity and a trace (references/tools.md).

**Without the connector:** run `scripts/sizing_check.py` on the same scores. It applies the same rule and also reports the spread per criterion and the field-test flags.

If the computation is not possible at all, show the scores as a table and say the composite was not computed.

### Step 4. Read the size

Report per criterion the group view, the range (lowest to highest score) and the owner's view; then the composite. Where scorers are far apart on a criterion, say so plainly and name it as disagreement to discuss, never average it away (method.md M8).

Then read the pattern, not only the size of the gaps. When one scorer differs from the others on most criteria in the same direction, they are often picturing a different decision (for example a contained pilot versus an enterprise commitment). Say so as a hypothesis, propose writing the scope into the decision statement (what is in, what is out), and, where two decisions are hiding in one, offer to split them. Then ask the scorers to score again against the agreed statement. The first round's scores and the disagreement stay in the record.

### Step 5. Say what the size implies

Use the stage signals in method.md M6. They are qualitative; give the signal that best matches the pattern of scores and say why, then let the owner decide:

| Pattern | Points to |
|---|---|
| One function, reversible, team mostly knows the ground | A short working session on one question |
| One decision that matters, several functions, costly to reverse | A one-day session with the full record |
| Several connected decisions, many functions, hard to reverse, years of commitment | A multi-day program of connected decisions |
| The organization itself has to change | A transformation program |

Then ask the owner the two field-test questions (method.md M7), showing the scores that bear on each, and record the owner's answer (class O):

- (a) "Is this decision hard to reverse?" Show the reversibility scores.
- (b) "Does it commit money or people beyond one planning cycle, or across more than one function?" Show the commitment horizon and functions involved scores.

The scores inform the answer; they do not decide it, because the method sets no score threshold for either condition. If the owner answers yes to both, say plainly that the top outcomes will need a short field check before the decision, unless the owner records a reason to proceed without it. The third condition (outcomes scored only in the room) is checked later, in outcome prioritization.

## Build the output

Feeds the "Size" section of the full report: the score table with ranges, the owner's view, sensitivity if returned, the pattern reading, the format signal and the field-test answers. If the person asked only what the scores tell them, use the direct answer format.

## Boundaries

- Never score, suggest a score, or "estimate what they would say".
- Never present the composite as the decision's value or priority. It sizes the process, not the opportunity.
- Never choose the session format. Recommend the signal; the owner decides, and a smaller format than asked for is a legitimate recommendation.

## When you are unsure

With one or two scorers, label the size indicative. If scorers disagree widely on reversibility, that disagreement is the first thing to discuss; do not proceed to a format until it is.
