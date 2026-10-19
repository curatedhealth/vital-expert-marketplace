# B Place the work and its oversight

Framework task: 4.1 Delivery and Oversight Planning, Part B.

## What this task delivers

For each job: the risk factors people scored, the computed tier proposal, the tier the person chose (with a reason if it differs), the intervention level it corresponds to, the oversight owner, the review point and question, and a context-of-use statement wherever AI sits at a critical decision point.

Why it matters: how much AI does around a job is a risk decision; who decides at a critical point is not negotiable. Scored factors and named owners keep the first honest and the second visible (method.md X3 to X6).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 4.1, Part B |
| Workflow | The steps below |
| Knowledge | `references/method.md` (X3 to X6) |
| Tools | `scripts/delivery_check.py`; `delegation_place` to store |
| Template | `assets/job-risk-score-sheet.md`; `assets/context-of-use-statement.md` |
| Input | The sequenced jobs (Part A) |
| Governance | `references/governance.md` |

## Workflow

1. **Score the four risk factors** privately (question 5), 1 to 10 per job: consequence (costly if wrong), reversibility (easy to undo), checkability (easy to check), regulatory (regulated basis). Average them; flag a spread of 3 or more.
2. **Compute the proposal** with `scripts/delivery_check.py` and show it with its reason, worded as a proposal ("your scores propose people only: consequence and regulatory at 8 or more"), never as an outcome. Flag any job that sends content to a clinician, patient, payer or regulator, or makes a regulated decision, as a likely critical decision point needing a context-of-use statement.
3. **The person chooses** (question 6). A different choice gets the person's reason. Regulated work other than people only needs an exception in the person's words.
4. **Name oversight** (question 7): a role per delegated job, the review point (default: the job's gate) and a review question the owner sets.
5. **Context of use** (question 8): for AI at a critical decision point (high consequence, patient risk or regulatory impact), draft the statement from what is known ([assets/context-of-use-statement.md](../assets/context-of-use-statement.md)) and ask the person to complete it. Without it, the job is placed as people only and the gap is named.
6. **Store** with `delegation_place` if a brief is open.

## Boundaries

- Never choose a tier; never treat the proposal as the decision.
- Orchestrate and redesign are set by the process owner at outcome level, not here.
- A critical decision point is decided by a qualified person whatever the tier.

## When you are unsure

If people cannot score a job's risk because the job is unclear, return to Part A and split it.
