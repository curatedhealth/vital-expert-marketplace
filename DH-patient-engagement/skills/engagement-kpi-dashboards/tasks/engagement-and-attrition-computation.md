# A2 Engagement and attrition computation

Framework task: DH-02.03.3.1, Part A, task A2. Replaces register task CF-12.02.03.3.1.3 (Tracking job) for the computation and its timestamp; the job's owner and cadence are set in B1.

## What this task delivers

The person's KPIs computed from their own event file (numerator, denominator, value, period, as-of date), nonusage attrition curves (raw proportions on a valid denominator and Kaplan-Meier), the usage half-life with the t10 and t25 points, relative risk of stopping between the person's groups, and dropout per follow-up wave. Every figure carries its run date, its as-of date and the rows excluded. It answers "what does our data say about engagement and how fast people stop?"

Why it matters: in any eHealth trial a substantial share of users drop out or stop using the product (PE-101). Eysenbach asks for attrition curves, relative risk and a usage half-life (PE-103, KX2, KX3), computed with survival methods (KX1). Without a valid denominator and a timestamp, the same number can mean several things.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Data & Analytics Lead (`data-analytics-lead`) |
| Skill | DH-02.03.3.1 Part A, Engagement and attrition computation |
| Workflow | The steps below |
| Knowledge | `references/attrition-curves.md`; `references/kpi-definitions.md`; rows PE-101 to PE-105, KX1 to KX5, CS27 |
| Tools | `scripts/engagement_kpis.py` (needs code execution). No library call. |
| Prompt | This guide |
| Template | `assets/engagement-and-attrition-output.md` |
| Input | The request and its context: the event file (user_id, event_date, event_type, optional group column), the eligible list if reach is asked, the KPI cards from A1 or the person's definitions, the as-of date, the start and use events, the days without use that mean "stopped", follow-up waves and their due days |
| Governance | `references/governance.md`; the data stays in the conversation; no figure becomes a clinical claim |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Data.** Ask for the events export in the columns the script reads, or aggregates if they cannot share rows. Pseudonymous ids only.
- **Rules.** Start event, use event, days without use that mean "stopped", follow-up waves and due days, period. Ask for each one missing. No default is applied.
- **As-of date.** Every figure counts to it. Default to the date of the conversation and say so.
- **Groups.** Sites, cohorts or arms the person wants compared (a column in the file).
- **Mode.** Short for one number or one curve; full for a tracking report.

## Workflow

### Step 1. Check the file

Run `python3 scripts/engagement_kpis.py kpis EVENTS.csv --defs KPIS.json` (or the attrition command below) and read the excluded-rows lines first. Report blank or invalid dates, events after the as-of date, use events before a start, and people with use but no start. Never impute.

### Step 2. Compute the KPIs

`python3 scripts/engagement_kpis.py kpis EVENTS.csv --defs KPIS.json [--eligible ELIGIBLE.csv]`

Report each card: numerator, denominator, value, period. If the script says people meet the numerator but sit outside the denominator, report the count and the likely reason it states (not yet observed for the full window, or mismatched definitions). A card that cannot be computed is reported with the missing field `[GAP]`.

### Step 3. Compute attrition

`python3 scripts/engagement_kpis.py attrition EVENTS.csv --start-event START --use-event USE --inactive-days N --as-of YYYY-MM-DD [--interval-days D] [--horizon-days H] [--group COLUMN] [--followup "wave:day,wave:day"] [--csv-out curve.csv]`

Report per group: people, stopped, still using (censored); the curve at the display points (raw stopped proportion with its denominator, and Kaplan-Meier still using); t10, t25 and t50 (usage half-life), or "not reached within the data"; relative risk at the horizon against the reference group; dropout per follow-up wave on people whose wave was due. Read `references/attrition-curves.md` before explaining a difference between the raw and Kaplan-Meier figures.

Without code execution, compute the KPI values by hand from aggregates the person gives, and say the curves need the event file.

### Step 4. Check against the person's thresholds, if any

For each threshold the person set (and its owner), mark met or missed. Without a threshold: "no threshold set", no verdict.

### Step 5. What it means for the person

Two or three consequences from the rows only, stated conditionally. Examples: "Half of South's participants stopped using within 13 days (t50); if the core content sits after week 2, most South participants would not reach it." "Follow-up at week 12 was completed by 9 of 25 people due; dropout of this size may introduce selection bias in any week-12 outcome (KX5)." No cause is stated; hypotheses are labeled and go to the person.

### Step 6. Stamp the run

State the as-of date, the run date, the rules used, and the rows excluded. If the person keeps a dashboard, write the curve table with `--csv-out` for the chart and say which run it came from.

## Build the output

Follow `assets/engagement-and-attrition-output.md`. Answer first: the figures that answer the question, with denominators and the as-of date. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every figure has its numerator, denominator, period and as-of date.
- The rules used (events, days without use, dose) are the person's and are stated.
- Excluded rows are reported, not imputed.
- Group differences are described, not explained; no significance is claimed.
- No figure is described as clinical evidence or as a cause.
- The person's data went into no library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Computation on the person's own data only. Card design is A1; dashboards and the refresh job are B1; recomputation against a dashboard and drift are the reliability skill.
- Equity cuts (who is reached, by group) can be computed with `--group`; what they mean for equity priorities belongs to Patient Engagement 4.x.
- Outcome attainment under a payment model is Market Access.
