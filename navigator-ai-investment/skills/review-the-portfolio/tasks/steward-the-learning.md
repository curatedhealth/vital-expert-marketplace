# B Steward the learning

Framework task: 5.2 Portfolio Review, Part B.

## What this task delivers

Re-score candidates for outcomes whose results suggest their priority was wrong, prepared with evidence for a named steward to decide one at a time; a readiness re-run (capability gaps re-scored, named factors scored 1 to 10, no index); and, if raised, a direction change routed with two named approvers.

Why it matters: the model learns only through recorded decisions by named people on recorded evidence; otherwise it drifts with the latest anecdote (method.md L7, L8).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 5.2, Part B |
| Knowledge | `references/method.md` (L7, L8) |
| Tools | `scripts/review_check.py`; `rescore_note`, `readiness_check` |
| Template | `assets/rescore-candidate.md` |
| Input | Outcome results; field tests; the review from Part A |

## Workflow

1. **Re-score candidates** (question 3): ask whether any outcome's scores should be re-opened. For each yes, prepare a candidate: the outcome, the evidence (recorded results, field test, satisfaction now), the proposed change ("re-score importance and satisfaction with the original scorers"), risks, a review-by date. Never propose new scores.
2. **The steward** (question 4): a named person; a role alone is a gap until a person is named. `rescore_note` records them. The steward approves, rejects or edits each candidate with a reason. Approved re-scores are run by people with *Outcome Prioritization*.
3. **Readiness re-run** (question 5): re-score the capability gaps with *Strategic Readiness*; named factors (for example data readiness, change capacity, risk appetite) scored 1 to 10 by the people named; `readiness_check` stores them. No index.
4. **Direction**: if the person proposes changing the strategic goal or value drivers, record the proposal and route it to *Decision Framing* with two named approvers.

## Boundaries

- No bulk re-scoring; no automatic adoption; a candidate not reviewed by its date lapses.
- Never compute a readiness index.

## When you are unsure

If results are mixed and no one asks to re-open scores, record "no re-score proposed" and move on.
