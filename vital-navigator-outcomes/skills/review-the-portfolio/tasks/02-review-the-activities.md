# Task: 02-review-the-activities

Input: team-entered facts for this step; upstream skill outputs listed at intake; connector availability.
Atom: compose-draft
Tool: offline script if present
Template: templates/worksheet.md
Output: step output
Check: no invented numbers; [GAP] listed; autonomy respected
Human: named decision owner

## Steps
1. Restate what is known and what is [GAP].
2. Run the offline tool if listed; otherwise draft from templates only.
3. Present options or draft to the named human; stop for human-only gates.

## Body

# A Review the activities

Framework task: 5.2 Portfolio Review, Part A.

## What this task delivers

For each activity: stop, keep or fix, decided by its owner, with a reason and the outcome it serves, beside the evidence (outcome status, value placement, trial result).

Why it matters: a review that only lists activities keeps everything. A decision per activity, traced to an outcome, is how work that serves nothing gets retired (method.md L6).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Outcome Decision Lead |
| Skill | 5.2, Part A |
| Knowledge | `references/method.md` (L6, L7) |
| Tools | `scripts/review_check.py`; `review_trace` |
| Template | `assets/review-sheet.md` |
| Input | Activities; outcome statuses; value placement; trial results |

## Workflow

1. **Lay out the evidence** per activity: the outcome it serves, its status (achieved, not achieved, not measured), the value placement, the trial result. Missing evidence is a gap, not a guess.
2. **Send the review sheet** (question 2) to the person accountable for each activity; one turn.
3. **Check** with the script: a decision and reason each; activities with no outcome flagged; kept activities whose outcome is not measured as achieved marked "keep and watch".
4. **Store** with `review_trace` if a brief is open.

## Boundaries

- Never suggest stop, keep or fix. If asked, give the evidence in one line per activity and the sheet.
- "Fix" needs what will change, in the person's words.

## When you are unsure

If an activity serves several outcomes, record the main one and list the others.
