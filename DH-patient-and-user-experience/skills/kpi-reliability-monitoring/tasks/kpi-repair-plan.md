# B1 KPI repair plan

Framework task: DH-02.03.3.2, Part B, task B1. Replaces register task CF-12.02.03.3.2.3 (KPI repair) and the earlier one-line pass rule and owner sections.

## What this task delivers

For each KPI that misses the person's rules (from A1 and A2): what was found, whether the card or the dashboard changes (the card owner decides), the owner in the person's words, the refresh after which the numbers must match, and how the old version is retired so that only one is live. Where the person wants repairs ordered, the order comes from their scores. It answers "which KPIs do we fix, who fixes them, and when must the numbers agree?"

Why it matters: the register's rules are "Name the owner of the card or the job", "State whether the card or the dashboard changes", "Name the refresh after which the numbers must match" and "Do not leave both versions live." A KPI repaired in one place and not the other produces two numbers for one name.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Data & Analytics Lead (`data-analytics-lead`) |
| Skill | DH-02.03.3.2 Part B, KPI repair plan |
| Workflow | The steps below |
| Knowledge | `references/reliability-checks.md`; A1 and A2 results; `references/kpi-definitions.md` for the definition options |
| Tools | `analytics.rice` or `analytics.mcda` (counted, optional, only on the person's scores) |
| Prompt | This guide |
| Template | `assets/repair-plan-output.md` |
| Input | The request and its context: A1 and A2 results, the person's rules (which fails matter, the acceptable difference), owners of cards and of the refresh job, the refresh schedule, any scores for ordering |
| Governance | `references/governance.md`; people decide which formula is right, owners and refreshes; never change a number to meet a target |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: people decide

The card owner decides which formula is right. The person names owners and the refresh by which the numbers must match. The model lays out each finding with its evidence, the options for repair (change the card, change the dashboard, retire the KPI), labels any it drafts "proposed", and ranks repairs only on the person's numbers.

## Read the request

- **Findings.** From A1 and A2 in this conversation, or the person's own list. Without findings, run A1 first.
- **Their rules.** Which fails and differences they treat as needing repair. Without rules: list findings, no verdict, ask.
- **Owners.** Card owner and refresh-job owner per KPI, in the person's words.
- **Refresh schedule.** The refreshes they run. Without it: `[GAP]`, ask; never pick a date.
- **Mode.** Short for one KPI; full for a repair plan across the framework.

## Workflow

### Step 1. Check each finding against the person's rules

For each finding: rule (theirs), evidence (A1 or A2, with the number), met or missed. Without a rule: "no rule set", no verdict.

### Step 2. Lay out the repair options per KPI

For each missed rule, the options with their consequence, from the evidence:

- Change the dashboard to the card (the card stands; the dashboard number will move, say by how much from A2).
- Change the card to the dashboard (the card owner accepts the dashboard's formula; say what it counts differently).
- Write a card for a dashboard KPI that has none, or retire the KPI.
- Add the missing field (period, missing-data rule, denominator) so the card can be recomputed.

Label any option the model drafts "proposed". Never propose a change whose purpose is to meet a target.

### Step 3. Owners and the matching refresh

For each KPI: the owner of the card and of the refresh job, in the person's words, or "owner not named" and ask. The refresh after which card and dashboard must match, the person's, or `[GAP]`. How the old version is retired (removed, or relabeled with its end date) so only one version is live.

### Step 4. Hypotheses for unexplained differences

For A2 differences marked "unexplained", list hypotheses labeled as such, each with what would confirm it (the BI query, the pipeline log, a refresh history). No cause is stated as fact.

### Step 5. Order the repairs, only if the person scored them

Ask for their numbers. With RICE: reach, impact (0.25, 0.5, 1, 2 or 3), confidence as a percentage, effort; call `analytics.rice {initiatives: [...]}` and check one score by hand (`references/tools.md`). With criteria and weights: 0 to 4 scores and weights summing to 1; call `analytics.mcda`. Without their numbers: no order; sequence only by dependency (a card must exist before the dashboard can be aligned to it; a missing period blocks recomputation).

### Step 6. Stops

If a repair would change a figure already reported outside the company, or one used in a contract, a claim or a submission, it stops for the accountable owner (`references/governance.md`); draft the note for the owner stating old and new figures with their definitions.

## Build the output

Follow `assets/repair-plan-output.md`. Answer first: per KPI, what changes (card or dashboard), the owner, and the refresh by which the numbers must match. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every repair traces to a finding with evidence.
- Which formula is right is left to the card owner; proposals are labeled.
- Every owner and refresh is the person's, or `[GAP]` and asked; no job title suggested, no date picked.
- Each KPI ends with one live version.
- Any order comes from the person's scores, with one score checked by hand.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Repair planning only. Doing the repair (editing the BI tool, the pipeline) is the owner's.
- New KPIs and dashboards are the sibling skill (engagement-kpi-dashboards).
- Payer outcome measures and contract terms are Market Access.
