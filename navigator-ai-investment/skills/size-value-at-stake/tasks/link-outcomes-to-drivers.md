# C Link outcomes to drivers

Framework task: 1.2 Value-at-Stake Sizing, Part C.

## What this task delivers

The outcomes that must improve for the value to appear, each linked to the driver it contributes to, as a starting list for outcome discovery and prioritization (the next cluster). It closes Direction by pointing it at what must become true.

Why it matters: value is declared at the top and proven at the bottom. A driver that no outcome contributes to cannot be proven, and the work it funds cannot be counted (method.md V4). Every outcome must reach at least one driver.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 1.2 Value-at-Stake Sizing, Part C |
| Workflow | The steps below |
| Knowledge | `references/method.md` (V4) |
| Tools | `bridge_for_driver`, `bridge_explain` (driver level 3 only) |
| Prompt | This guide |
| Template | "Outcomes the value depends on" section of the report |
| Input | The chosen drivers (task A); any outcomes the person names |
| Governance | `references/governance.md` |

## Workflow

### Step 1. Ask what must improve

Ask: "Which outcomes must improve for this value to appear?" Record them in the person's words. An outcome says what must become true for someone, not what will be built ("medical information answers reach clinicians faster", not "deploy a chatbot"); restate solutions as outcomes and keep the solution as an option.

### Step 2. Show the outcomes the library already links (connector)

For each chosen driver at level 3, call `bridge_for_driver` with its `id` (or `bridge_explain` for a plain-language path). Show up to five linked outcomes by display name, labeled "outcomes the library links to this driver". The person keeps, drops or adds. For drivers chosen at level 1 or 2, the bridge does not read those links today; say so, offer to drill to level 3 drivers, or carry the person's outcomes forward with the link marked `[GAP]` "library link not readable at this level".

### Step 3. Record the links

Write each as "*[outcome]* contributes to *[driver]*". Each outcome reaches at least one driver; a driver with no outcome is flagged "no outcome yet: cannot be proven" (method.md V4).

## Boundaries

- Do not score or rank outcomes here. That is outcome prioritization, the next cluster, where people score importance and satisfaction.
- Do not write numeric targets on outcomes here; measures and baselines belong to the outcome work.
- Use "contributes to". Never show the library's internal edge names.

## When you are unsure

If the person cannot name any outcome, carry the drivers forward with "outcomes to be discovered" and point to outcome discovery as the next step.
