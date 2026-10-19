# A1 Definition quality and drift

Framework task: DH-02.03.3.2, Part A, task A1. Replaces register task CF-12.02.03.3.2.2 (Formula drift) and adds the card quality and missing-data checks the register's KPI definition method implies.

## What this task delivers

For each KPI: whether its card is complete and computable (decision, numerator, valid denominator, period, grain, source, missing-data rule, definition source), whether the dashboard uses the card's formula (match, drift field by field, renamed, no card), and how much of the event data is missing or inconsistent. It answers "are our KPIs defined well enough to trust, and is the dashboard still computing what we agreed?"

Why it matters: reach on volunteers instead of all eligible people is not reach (CS27); a retention KPI that does not say whether it counts dropout or nonusage mixes two different measures (PE-102); missing data with no stated rule hides a choice FDA asks to be explicit about (PE-21). A dashboard formula that drifted from its card can give a number that looks right and counts different people.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Data & Analytics Lead (`data-analytics-lead`) |
| Skill | DH-02.03.3.2 Part A, Definition quality and drift |
| Workflow | The steps below |
| Knowledge | `references/reliability-checks.md` (sections 1 to 3); `references/kpi-definitions.md`; rows CS27, CS39, PE-21, PE-101 to PE-104, PE-93 to PE-96, KX8 to KX10 |
| Tools | `scripts/kpi_definition_check.py` (needs code execution). No library call. |
| Prompt | This guide |
| Template | `assets/definition-quality-output.md` |
| Input | The request and its context: the KPI cards (JSON in the script's format, a table, or text), the dashboard's definitions (export or description), the event export if missing data is asked, the as-of date |
| Governance | `references/governance.md`; checks say whether a card is computable, never whether its value is good |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Cards.** Ask for the KPI cards in any form. If they are text or a table, write them into the script's JSON format and show the person what you wrote before checking.
- **Dashboard definitions.** Ask for the formulas the dashboard actually uses (BI export, SQL, the tool's metric settings). Without them, drift cannot be checked: say so.
- **Events.** Only if missing data is in scope.
- **Mode.** Short for one KPI; full for a measurement framework review.

## Workflow

### Step 1. Check the cards

`python3 scripts/kpi_definition_check.py cards KPIS.json`

Read each fail and check with the card. Keyword-raised checks (reach, retention, downloaded) may not apply: read the card before reporting. Report fails as "cannot be recomputed as written: FIELD missing", and checks as questions for the person, each with its row.

### Step 2. Check drift

`python3 scripts/kpi_definition_check.py drift CARDS.json DASHBOARD.json`

Report each KPI: match; drift with the fields that differ (card against dashboard); grain differs (numbers not comparable); renamed with the same formula (confirm before treating as one); on the dashboard with no card. Never treat a renamed KPI as the same formula without the card owner's confirmation (register).

### Step 3. Check the data

`python3 scripts/kpi_definition_check.py missing EVENTS.csv --as-of YYYY-MM-DD --start-event START`

Report blanks, invalid dates, duplicates, events after the as-of date, events before a start, people with no start, and events per month. A month with no events is reported as "feed outage or real stop, cannot tell from this file". Ask the person for the reasons behind missing data (PE-21); never impute.

### Step 4. Instrument-based KPIs

For a KPI built on a questionnaire, list which COSMIN properties the person's named evidence covers (section 5 of `reliability-checks.md`). Without named evidence: "measurement evidence not named"; the rating is A2's job.

If the KPI uses a follow-up score at week N (for example a week-12 change score), check that the denominator excludes people enrolled less than N weeks before the period end, and that missing follow-up scores have a rule. Report it as a check with the same rows as "window matches denominator" (CS27, PE-21). For each [PAPER] row cited, give its DOI once.

### Step 5. What it means for the person

Two or three consequences from the checks only, conditional. Example: "K2 on the dashboard divides by all 68 enrolled while the card divides by the 47 observed for the full 56 days: the dashboard counts recent enrollees as not yet engaged, so the two figures describe different people even though they read 23.5 and 23.4 percent."

Without code execution, run the same checks by reading each card against the table in `reliability-checks.md`.

## Build the output

Follow `assets/definition-quality-output.md`. Answer first: the KPIs that cannot be recomputed as written, the KPIs whose dashboard formula drifted, and the data gaps that matter. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every fail names the missing field; every check carries its row.
- No verdict on any KPI's value; no statement that a KPI is "valid" or "reliable".
- Drift is reported field by field; which formula is right is left to the card owner.
- Missing data is counted, never imputed.
- The person's data went into no library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Checks only. Recomputation and instrument ratings are A2; repairs and owners are B1; writing new cards is the sibling skill's A1.
- Equity cuts and who is left out are Patient Engagement 4.x.
- Payer outcome measures are Market Access.
