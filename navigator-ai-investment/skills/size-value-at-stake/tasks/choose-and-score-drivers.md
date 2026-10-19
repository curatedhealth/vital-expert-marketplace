# A Choose and score the value drivers

Framework task: 1.2 Value-at-Stake Sizing, Part A.

## What this task delivers

The one to three value drivers this decision moves, chosen by the person from VITAL's value driver library at the audience's level, each with its value dimension, and a people-scored comparison of them on size of the prize, confidence, time to value and breadth.

Why it matters: "AI will create value" cannot be sized or checked. A named driver (for example *Accelerate Time-to-Approval*) can. Choosing from the library gives the client a shared, tested vocabulary instead of a slogan, and keeps the value tied to the tree it will later be measured against (method.md V5).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 1.2 Value-at-Stake Sizing, Part A |
| Workflow | The steps below |
| Knowledge | `references/method.md` (V5 to V8); `references/audience-calibration.md` |
| Tools | `catalogue_search`, `catalogue_list_children` (value driver pillar); `scripts/value_check.py` for scores |
| Prompt | This guide |
| Template | `assets/driver-score-sheet.md`; "Value drivers" section of `assets/value-at-stake-report.md` |
| Input | The decision frame if present (decision, owner, audience, goal, chosen value theme); otherwise the request |
| Governance | `references/governance.md` |

## Workflow

### Step 1. Start at the audience's level

From the frame or by asking: C-suite starts at value themes (level 1), head of function at value levers (level 2), head of department at levers and drivers (levels 2 and 3). If the frame already holds a chosen theme, start from that theme's children.

### Step 2. Offer candidates

With the connector: `catalogue_search` with `pillar` VD, the level, and words from the decision and goal as `query` (no `function` argument; it removes every row). To go one level down from a chosen row, pass its `id` to `catalogue_list_children`.

Without the connector: offer from the themes in `references/audience-calibration.md`, and say they are the catalogue as last read; levers and drivers below them need the live library.

Show at most five candidates by display name with their value dimension in words (for a level 3 driver, "inherited from [lever]"). Ask which this decision moves. The person picks one to three. Never pick.

### Step 3. Score the chosen drivers

Ask who scores (the owner plus those whose judgment the value needs). Send `assets/driver-score-sheet.md`. Each scorer gives a whole number 1 to 10 per driver on four criteria, privately, before discussion (method.md V6, V8):

| Criterion | 1 means | 10 means |
|---|---|---|
| Size of the prize | Small effect on the organization | Large effect on the organization |
| Confidence in the estimate | A guess | Well evidenced |
| Time to value | Value arrives quickly | Value arrives slowly |
| Breadth | Touches one group | Touches many groups |

### Step 4. Compute and read

The connector cannot run this template today (references/tools.md), so run `scripts/value_check.py drivers` on the scores, or lay the scores out as a table if no code can run. Report per driver: group view and range per criterion, the owner's view after the group's, and a composite with time to value counted inverted (labeled "computed, equal weights").

Read the result, do not rank for the sake of it: at Direction the point is which drivers matter enough to size. Name where confidence is low (the range will need to be wide), and where scorers disagree (discuss, never average away).

## Boundaries

- No driver is chosen or scored by you.
- Do not offer drivers below level 3; sub-drivers and metrics are measures for the outcome work.
- Do not treat a high composite as proof of value. It says which drivers to size, not what they are worth.

## When you are unsure

If no library row fits, record the driver in the person's words, class O, and mark "no catalogue match" as a gap. If the person wants more than three drivers, ask which three matter most; others are listed but not sized.
