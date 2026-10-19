# A Build the longlist

Framework task: 2.1 Outcome Discovery, Part A.

## What this task delivers

A short list of candidate outcomes for the decision, each in the person's words or taken from the library, each with the party it serves and the value driver it contributes to. It is the raw material for Part B and, after that, for scoring.

Why it matters: every walk must reach an outcome before its work counts, and capabilities, processes and agents are in the model only because an outcome needs them (method.md O1, O5). If the list starts from the AI use cases on the table, the decision can only pick among them. Starting from what must become true lets the room find that a different change would serve better.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 2.1 Outcome Discovery, Part A |
| Workflow | The steps below |
| Knowledge | `references/method.md` (O1 to O5, O9) |
| Tools | `catalogue_search` (outcomes), `catalogue_list_children`, `catalogue_pack`, `bridge_for_driver` |
| Prompt | This guide |
| Template | "Outcomes" section of `assets/outcome-list-report.md` |
| Input | Decision frame; chosen value drivers and their linked outcomes, if any |
| Governance | `references/governance.md` |

## Workflow

### Step 1. Carry forward what is known

If *Value-at-Stake Sizing* listed outcomes linked to drivers, start from those and say so ("I've started from the four outcomes you linked to your value drivers"). Do not ask for them again.

### Step 2. Ask what must become true, and for whom

Ask: "For this decision to have been worth it, what must become true, and for whom?" Record each answer in the person's words, with its party, class O.

Listen for three things and handle each in the next turn, never as a lecture:

- **A solution** ("deploy a medical writing copilot"): restate as an outcome ("reduce the writer time spent on routine label updates, for medical writers") and keep the solution on a separate list of options for the Intelligence Core stage.
- **An activity** ("review the content backlog"): ask what it is for; the answer is usually the outcome.
- **No party** ("faster responses"): ask "faster for whom?"

### Step 3. Offer what the library holds (connector)

At the audience's level ([references/audience-calibration.md](../references/audience-calibration.md)):

1. `catalogue_search` on the outcome pillar at that level with words from the decision and goal. Offer up to five by display name: "the library holds these; which belong?"
2. For Medical Affairs decisions, `catalogue_pack` returns the function's mission outcomes as one set; offer the ones that match. Other functions have no pack yet; say so only if it matters.
3. If drivers were chosen at level 3, `bridge_for_driver` lists outcomes the library already links to each. Label them "linked in the library".
4. To go one level finer, search the next level with the parent's words. Drilling by parent alone misses rows (references/tools.md).

The person keeps, drops or rewords. A library outcome they keep is class V with its source "outcome library"; their own is O.

**Without the connector.** Do not promise a library list you cannot show. Ask the Step 2 question in the person's own words and work from their answers; note "library not checked" in the record line only. Never substitute outcomes from general knowledge for library rows.

### Step 4. Check coverage, then stop

Read the list against two checks and raise at most one gap per turn:

- Every chosen value driver has at least one outcome. If not: "Nothing yet contributes to *[driver]*. What would have to improve for it to move?"
- More than one party is represented when the decision touches more than one (patients, prescribers and internal teams, for example).

Keep the list scoreable in one sitting: about 8 to 15 outcomes. If it runs longer, ask the owner which to merge or set aside; never cut on your own [CHECK: list size is the skill's practice, H, pending owner ruling].

## Boundaries

- No scoring, ranking or "top three" here. Order by value driver.
- No targets yet; that is Part C.
- A library outcome is an offer, never a recommendation.
- An outcome the library lacks is not a weaker outcome. Keep it in the person's words.

## When you are unsure

If the person can only name solutions, take each one and ask "if that worked perfectly, what would be different, and for whom?" Two answers usually give the outcome.
