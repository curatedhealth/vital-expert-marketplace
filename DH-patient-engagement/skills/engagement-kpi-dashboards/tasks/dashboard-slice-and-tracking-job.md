# B1 Dashboard slice and tracking job

Framework task: DH-02.03.3.1, Part B, task B1. Replaces register tasks CF-12.02.03.3.1.2 (Dashboard slice) and the ownership half of CF-12.02.03.3.1.3 (Tracking job), and the earlier one-line pass rule and owner sections.

## What this task delivers

One dashboard per audience: the audience and the decisions it takes, only the KPIs that audience decides on (from A1 cards), each with the person's threshold or "no threshold set", the refresh cadence, the job that refreshes it, the owner paged when it fails, how a failed refresh shows, and the timestamp shown. Where the person wants options ranked, it ranks what they scored. It answers "who sees which KPIs, how fresh, and who answers when it breaks?"

Why it matters: the register's own rules are "Do not build one dashboard for every audience" and "Do not hide a stale dashboard behind the last good numbers without a timestamp" (CF-12.02.03.3.1.2 and 3.1.3). NICE asks digital health companies in England to report usage against a profile agreed at commissioning (CS61), so a commissioner audience may need its own slice.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Data & Analytics Lead (`data-analytics-lead`) |
| Skill | DH-02.03.3.1 Part B, Dashboard slice and tracking job |
| Workflow | The steps below |
| Knowledge | `references/kpi-definitions.md`; `references/attrition-curves.md` (tracking facts); A1 cards; A2 figures |
| Tools | `analytics.rice` or `analytics.mcda` (counted, optional, only on the person's scores) |
| Prompt | This guide |
| Template | `assets/dashboard-slice-output.md` |
| Input | The request and its context: the audiences, the decisions each takes, the KPI cards, thresholds and who set them, the data pipeline the person has (source, refresh tool), who owns the job |
| Governance | `references/governance.md`; people choose audiences, KPIs, thresholds and owners; the model lays out and ranks only what they scored |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: people decide

The person names the audiences, the decisions, which KPIs each audience sees, every threshold and every owner. The model shows which cards serve which decision, flags cards that are not ready (missing denominator, no period), and ranks options only on the person's numbers. A slice it drafts is labeled "proposed" until the person confirms it.

## Read the request

- **Audiences.** Who will look (for example site leads, the program steering group, a commissioner). One dashboard each.
- **Decisions.** What each audience decides with the numbers. Take the person's words.
- **Thresholds.** Which KPI has a threshold, its value and who set it. Without one: "no threshold set".
- **Pipeline.** Where the data comes from and what refreshes it, if the person knows. Missing: `[GAP]`, ask.
- **Mode.** Short for one audience; full for a dashboard plan.

## Workflow

### Step 1. Audiences and decisions

List each audience and the decisions it takes, in the person's words. If the person asks for "one dashboard for everyone", lay out the audiences they named and ask whether each takes the same decisions; if not, one slice each.

For a care-team audience, propose a site-level decision. A patient-level outreach list is a person-level cut: it belongs in the care team's own system, built from a rule the clinical team sets.

### Step 2. Place the KPIs

For each audience, place only the KPIs whose card names a decision that audience takes. For each placed KPI give: the card name, numerator over denominator, period, grain, the person's threshold and its owner, or "no threshold set". A card with a fail (no denominator, no period) is placed as "not ready: FIELD missing", not as a number. List the KPIs considered and not placed, with the reason.

### Step 3. Context, labeled

If an audience asks "how do we compare", say that this skill holds no sourced engagement benchmark `[GAP]`. If the person names a published program, its figure is context, labeled with its source and design, never a target. For a commissioner in England, note that NICE expects usage reported against a profile agreed at commissioning (CS61); the profile is agreed with the commissioner.

### Step 4. The tracking job

For each dashboard, write:

- The job that refreshes it and its cadence (the person's).
- The owner paged when the job fails, in the person's words, or "owner not named".
- How a failed refresh shows to the audience (a stale banner, the last good time in red).
- The timestamp shown: data as-of date and last successful run.

These four lines come from the register's tracking-job method. If the person does not know the job or cadence, write `[GAP]` and ask.

### Step 5. Rank options, only if the person scored them

If the person must choose between dashboard or KPI options (which to build first, which to drop), ask for their numbers. With RICE: reach, impact (0.25, 0.5, 1, 2 or 3), confidence as a percentage, effort; call `analytics.rice {initiatives: [...]}` and check one score by hand (`references/tools.md`: confidence given as a fraction is divided again). Offer `analytics.mcda` in the same line when the person would rather score criteria (0 to 4) with weights. With criteria and weights: 0 to 4 scores and weights summing to 1; call `analytics.mcda`. Report the order and the scores the person gave. Without their numbers: no ranking; lay out the facts per option and ask.

### Step 6. Stops

If an audience is outside the company (investors, partners, a customer's board, a payer), the dashboard is an insight pack that leaves the company: it stops for the owner's countersign. If any KPI on it would read as an outcome, coverage or efficacy claim, say so and point to the owner (`references/governance.md`).

## Build the output

Follow `assets/dashboard-slice-output.md`. Answer first: per audience, the KPIs placed, the cadence and the owner paged. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- One dashboard per audience; every KPI placed serves a decision that audience takes.
- Every threshold and owner is the person's; none suggested.
- Every dashboard has a job, a cadence, an owner paged and a visible timestamp, or a `[GAP]`.
- Rankings use only the person's numbers, and one score was checked by hand.
- External audiences are marked as stopping for the owner's countersign.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Placement and tracking only. Card design is A1; the numbers are A2; whether the dashboard number still matches its card is the reliability skill.
- Chart design (chart type, encodings, labels) can be handed to the Data Visualization Specialist (Health) role; this task fixes what is shown, not how it is drawn.
- Payer-facing dashboards and outcome attainment are Market Access.
