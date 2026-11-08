# Task: 01-plan-the-scaling

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

# C Plan the scaling

Framework task: 5.2 Portfolio Review, Part C.

## What this task delivers

For each activity kept and whose outcome was measured as achieved: what is scaled, the owning role, and the order of steps, written by the person.

Why it matters: scaling what has not been shown to work multiplies the risk; scaling without an owner and order stalls (method.md L9).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Outcome Decision Lead |
| Skill | 5.2, Part C |
| Knowledge | `references/method.md` (L9) |
| Tools | `scripts/review_check.py`; `scaling_plan` |
| Template | "Scaling" section of the report |
| Input | Kept activities with achieved outcomes |

## Workflow

1. **Name the candidates**: kept activities whose outcome was measured as achieved. Kept activities without that are "keep and watch".
2. **For each** (question 6, then owner, then order): what will be scaled (more users, markets, content types), who owns it, and the order of steps.
3. **Check and store**: the script, then `scaling_plan` if a brief is open.
4. **Hand on**: each scaling step can go to *Delivery and Oversight Planning* as jobs, with tiers and oversight re-scored for the larger scope.

## Boundaries

- Never write the steps for them; never scale a stop or fix.
- A larger scope may change risk: the delivery tiers are re-scored, not carried over.

## When you are unsure

If nothing qualifies for scaling, say so; it is a finding.
