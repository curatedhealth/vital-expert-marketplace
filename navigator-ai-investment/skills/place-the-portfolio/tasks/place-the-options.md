# B Place the options

Framework task: 3.3 Portfolio Placement, Part B.

## What this task delivers

Each option (not the baselines) in one of five buckets, with its value, the oversight it needs, the fit against capacity, and the underlying bucket where the consequence override applies.

Why it matters: a ranked list says which option scores best; the grid says what to do with each one now, given what the organization can oversee (method.md I8).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 3.3 Portfolio Placement, Part B |
| Workflow | The steps below |
| Knowledge | `references/method.md` (I8) |
| Tools | `scripts/placement_check.py`; `portfolio_place` to store |
| Prompt | This guide |
| Template | "Placement" section of `assets/portfolio-report.md` |
| Input | Outcome fit and governance burden per option; capacity; consequence answers |
| Governance | `references/governance.md` |

## Workflow

1. **Value split.** Default: the median outcome fit of the options. With fewer than four options, ask the owner what outcome fit counts as high (session question 4); a median would put half of them low by definition.
2. **Compute** with `scripts/placement_check.py`: outcome fit, governance burden, consequence flag per option; capacity scores; value split if stated. Baselines go in marked `is_baseline` and are listed as not placed.
3. **Show the placement**:

| Option | Value (outcome fit) | Oversight needed | Fit (capacity minus needed) | Bucket |
|---|---|---|---|---|

with the grid as text:

| | Oversight fits capacity | Oversight above capacity |
|---|---|---|
| **High value** | Invest now: … | Build the basis first: … |
| **Low value** | Later, in batches: … | Not now: … |

and "Support, do not automate: …" beneath, each with its underlying bucket.

4. **Say what each bucket means** in one line for the options in it: Invest now (high value with oversight the organization can carry: ready for the owner's decision); Build the basis first (method, gates or capacity first, then scale); Later, in batches (group and revisit); Not now (set aside for now; the owner decides); Support, do not automate (AI assists a person who decides). Never write "start", "can start", "go", "fund" or "first investment" about a bucket.
5. **Store** (connector): `portfolio_place` with the computed bucket as the quadrant, if a brief is open.

## Boundaries

- Never move an option between buckets by judgment. If the owner disagrees with a placement, record it as their view; the computed bucket stays.
- Close to a boundary (within 0.5 on either axis) is said as "close to the line" [H, skill practice].

## When you are unsure

If every option lands above capacity, say so plainly: the finding is about capacity, and building it may be the first investment.
