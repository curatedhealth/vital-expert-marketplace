# A1 Adoption and drift

Framework task: DH-02.04.2.2, Part A, task A1. Replaces the register task "Behind-version count" (CF-12.02.04.2.2.2).

## What this task delivers

Counts computed from the person's component inventory: which products use each component and on which version, which uses are behind the current version and by how far, behind-version counts by owner with clinical and medical device surfaces shown separately, the accessibility status of each component version as the person recorded it, local overrides and forks, and uses of components carrying a flagged lifecycle status. It answers "who is behind on our components, and where has the product drifted from the system?"

Why it matters: a published component is not the component in the product. A product on an old or forked version keeps the old behavior, including any accessibility defect fixed since (a fork receives no system updates, DSX-33), and the register rule is never to hide a clinical task on an old component.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | UX/UI Designer, Digital Health (`ux-ui-designer-digital-health`) |
| Skill | DH-02.04.2.2 Part A, Adoption and drift |
| Workflow | The steps below |
| Knowledge | `references/indicators.md`; `references/governance-models.md` sections 3 to 5 |
| Tools | `scripts/ds_adoption.py`; no library call |
| Prompt | This guide |
| Template | `assets/adoption-and-drift-output.md` |
| Input | The request and its context: the inventory (columns in the script header), the person's current versions, their full product list, the as-of date, any rules they set |
| Governance | `references/governance.md`; the inventory stays in the conversation; no verdict without the person's rule |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Inventory.** One row per component version in use with the products using it and the accessibility status in the person's words. Optional columns add owner, clinical, device UI, modification and lifecycle. A pasted table is enough.
- **Current versions.** Ask which version is current for each component. Without it the script uses the highest version in the inventory and the output says so.
- **Product list.** The full list, so products using no listed component show up.
- **As-of date.** Default to the conversation date and say so.
- **Rules.** Ask whether they have any (for example "no clinical surface more than one minor version behind"). Without rules, report numbers and no verdict.
- **Mode.** Short for a direct question; full for a design-system health report.

## Workflow

### Step 1. Take the data

Check the columns. Flag inconsistencies to the person: a product listed twice for the same component at different versions, a use "ahead of current", a clinical flag that cannot be right for every product on the row (split the row). Blank means not recorded: say which indicator cannot be counted.

### Step 2. Compute

With code execution: `python3 scripts/ds_adoption.py INVENTORY.csv --products "A;B;C"` (add `--current CURRENT.csv` if current versions sit in a separate file, `--flag "..."` with the lifecycle values the person wants listed). Without code execution, compute the same by hand using the definitions in `references/indicators.md`.

### Step 3. Read the output for the person

Lead with clinical and device uses behind current, by owner. Then: components with the most versions in use; forks and overrides (a fork gets no system update, DSX-33; an override may break on update or reduce accessibility, DSX-31); uses of components the person's lifecycle marks for caution or deprecation (a USWDS "use with caution" component fails accessibility, usability or development requirements, DSX-28, if the person uses that scheme); component versions in use whose accessibility status the person recorded as not tested or with open issues. Quote the person's status words; never translate them into "conformant" or "accessible".

### Step 4. Check against their rules, if any

For each rule the person set, mark the count met or missed. Without a rule: "no rule set". Never borrow a rule from another system as a target; GOV.UK's 3-month rule applies to its community resources only (DSX-16).

### Step 5. What it means for the person

Two or three consequences stated from the rows, conditionally. Examples: "The dosing calculator's fork of Dose input will not receive any fix made to the system component (DSX-33)." "Finding the system's code in a product does not show the implementation is usable or accessible (DSX-41); A2 checks a surface."

## Build the output

Follow `assets/adoption-and-drift-output.md`. Answer first: clinical and device uses behind current with owners, then the largest drift. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every number comes from the person's inventory via the script or by hand, and the as-of date is stated.
- The source of "current" is stated (declared by the person, or highest in the inventory).
- Clinical and device uses are shown, not folded into totals.
- No cause is stated for drift; no team is judged.
- No verdict without the person's rule; no conformance statement.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Measurement on the inventory. A live surface check is A2; what to fix and who owns it is B1.
- Product accessibility conformance belongs to the Accessibility & Inclusion skills (DH-02.04.1.x).
- Writing contracts and governance is the development skill (DH-02.04.2.1).
