# C Turn objectives into measures

Framework task: 2.1 Outcome Discovery, Part C.

## What this task delivers

For the outcomes the organization will hold itself to, a measurable objective: the measure, its unit, today's level (baseline) with its source, the target and date, whether it leads or lags, and a named owner. Outcomes without a measure are listed as such.

Why it matters: Direction holds goals; objectives live with outcomes and their measures (method.md O7). Value is counted only when an outcome is measured as achieved, and an outcome is met when its evaluation passes, not when an output exists (method.md O8). Without a baseline and an owner nobody can later show the outcome moved, and the value declared in Direction can never be proven. The Navigator itself refuses a measure with no baseline or no owner when it stores a value range.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 2.1 Outcome Discovery, Part C |
| Workflow | The steps below |
| Knowledge | `references/method.md` (O7, O8) |
| Tools | `catalogue_search` (measures); `scripts/outcome_statement_check.py measures` |
| Prompt | This guide |
| Template | "Objectives and measures" section of the report |
| Input | The accepted outcome statements from Part B |
| Governance | `references/governance.md` |

## Workflow

### Step 1. Ask which outcomes they will hold themselves to

Not every outcome needs an objective now. Ask in one question: "Which outcomes will you hold yourselves to, and for each: what measure, today's level, the target and date, and who owns it?" Send the worksheet ([assets/outcome-statement-worksheet.md](../assets/outcome-statement-worksheet.md)) if there are more than three.

### Step 2. Offer measures from the library (connector)

`catalogue_search` on the measure pillar at the outcome's level (headline metrics for strategic outcomes, category measures for category outcomes, measures for mission outcomes). Offer up to three per outcome by display name with unit. The person chooses or names their own. The library holds almost no baselines and no owners; never present a library row as today's level.

**Without the connector,** you may propose up to two measure names per outcome, labeled "proposed (H), not from the library", with a unit and no figures, no owner and no target. The person chooses or replaces them.

### Step 3. Record each objective

| Field | Rule |
|---|---|
| Measure and unit | Chosen by the person; library source named if used |
| Baseline | A figure with its source and date (M), or "not measured" (gap) |
| Target and date | Given by the person (O); never proposed by you |
| Leads or lags | Leading if it moves before the outcome; lagging if it confirms it |
| Owner | A named role or person; "no owner" is a gap |

### Step 4. Check

Run `scripts/outcome_statement_check.py measures`. It flags a missing unit, baseline, target, date or owner, a baseline with no source, and a target in the wrong direction (a "reduce" outcome with a target above baseline). Read each flag to the person; change nothing yourself.

## Boundaries

- No targets from benchmarks you know. An external target needs its primary source.
- An objective is about the outcome, never about a named person's performance.
- Missing baselines are normal at this stage. List them; they often become the first piece of work.

## When you are unsure

If the person has no measure for an outcome, record "no measure yet" and ask one question: "What would you look at to know this had moved?" If nothing comes, carry it as a gap.
