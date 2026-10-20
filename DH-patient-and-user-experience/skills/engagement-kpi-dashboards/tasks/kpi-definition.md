# A1 KPI definition

Framework task: DH-02.03.3.1, Part A, task A1. Replaces register task CF-12.02.03.3.1.1 (KPI definition).

## What this task delivers

A KPI card for each KPI the person wants to track: the decision it serves, the numerator, a valid denominator, the period, the grain, the source table, the missing-data rule and the published definition it follows, plus one KPI considered and left off. It answers "what exactly does each of our engagement KPIs count, over what, and when?"

Why it matters: reach computed on volunteers who showed interest instead of all eligible people is not reach (CS27), and adoption, reach and penetration mean different things in different frameworks (CS research "Changes and conflicts"). A card fixes the definition before any number is shown, so the number can be recomputed and trusted.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Data & Analytics Lead (`data-analytics-lead`) |
| Skill | DH-02.03.3.1 Part A, KPI definition |
| Workflow | The steps below |
| Knowledge | `references/kpi-definitions.md`; `references/customer-success-research.md` (CS22 to CS40); `references/patient-engagement-research.md` (PE-98 to PE-105); `references/kpi-additions.md` (KX6 to KX8) |
| Tools | None required. Optional: `literature.search_literature`, `verify.qualify_source`, `verify.check_claim` (counted) when the person wants a published definition cited |
| Prompt | This guide |
| Template | `assets/kpi-definition-output.md` |
| Input | The request and its context: the program, the decisions the KPIs serve, the events the person records (names of event types), the populations they can list (eligible, enrolled), any KPIs they already use |
| Governance | `references/governance.md`; the person chooses every KPI and every rule |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. evidence-table grades a set of studies for a product's claims; this task only identifies or checks a source the person names. |

## Read the request

- **Decisions.** Which decisions will the KPIs serve, and who takes them? Without a decision, a KPI is not carded.
- **Events and populations.** Which event types exist in their data (for example enrolled, session, module_complete, followup_w4), and can they list all eligible people (a referral list, a panel)? Reach and penetration need the eligible list.
- **Existing KPIs.** If they already have KPIs, card those first, in their words.
- **Mode.** Short for one or two KPIs; full for a KPI tree.

## Workflow

### Step 1. Name the decision for each KPI

Write each decision and its decision-maker in the person's words. Group KPIs under the decision they serve (the KPI tree). A KPI with no decision goes to "considered, not shown".

### Step 2. Match each KPI to a published definition

From `references/kpi-definitions.md`, offer the definition that fits each KPI the person names, with its row (reach CS22 and CS27; adoption CS24, CS28 or CS34; penetration CS39; fidelity CS25, CS29, CS37; maintenance CS26, CS30, CS40; engagement PE-105 and KX6; effective engagement PE-104; attrition PE-101 to PE-103). Where two frameworks define the same word differently, show both in one line and ask the person to pick one.

When the person's reach divides by volunteers, clicks, downloads or sign-ups, offer both alternatives in one line and let them choose: RE-AIM reach on all eligible (CS27) and penetration (CS39). Keep their ratio as a labeled conversion KPI if they want it. For every [PAPER] row cited, give its DOI once.

### Step 3. Write the numerator and denominator

- Numerator: the event, the minimum count and any window from the start (for example "4 or more module_complete within 56 days of enrolled").
- Denominator: a population, named. For reach and penetration, all eligible people (CS27, CS39), not people who downloaded, signed up or showed interest. For a windowed numerator, only people observed for the full window ("min_days_observed" on the card), so no one is counted as failing before they could succeed.
- The dose for effective engagement and the days without use that mean "stopped" are the person's. Ask; never pick.

### Step 4. Period, grain, source, missing data

Write the period (dates, or a rolling window and its anchor), the grain, the source table or file, and the missing-data rule. If the person has no missing-data rule, write "not stated" and ask how blanks, invalid dates and missed assessments are handled (PE-21: avoid missing data and collect reasons).

### Step 5. Instrument-based KPIs

If a KPI rests on a questionnaire score (PAM, a PRO), name the instrument and say its measurement properties are judged with COSMIN in the reliability skill (PE-93 to PE-96). PAM level cut points are not in the sources `[GAP]`; PAM scoring is licensed (CS research "Not sourced").

### Step 6. Cite a published definition (optional)

Only if the person wants the definition cited outside the conversation: `verify.qualify_source {doi, question}`, then `verify.check_claim` with the passage from the reference row and the whole `qualify_source` object as `source` (`references/tools.md`). Accept only a passage that states the claim in the same direction (register N3). If the person wants comparable programs' measures, `literature.search_literature {query, limit: 5}`; report titles and DOIs as found, labeled context.

### Step 7. One KPI not shown

Name at least one KPI considered and left off, and why (no decision depends on it, no valid denominator, no source).

### Step 8. Write the cards

Fill the card fields for each KPI. If the person has code execution and an events file, write the cards as JSON in the format `scripts/engagement_kpis.py` reads (see `examples/sample-data/kpis.json`), so A2 can compute them.

## Build the output

Follow `assets/kpi-definition-output.md`. Answer first: the cards, each with its decision, numerator over denominator, period and the row its definition follows. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every card has a decision, numerator, denominator, period, grain and source, or names the missing field as `[GAP]`.
- No reach or penetration KPI divides by volunteers, downloads or sign-ups without saying so.
- Every dose, window, threshold and owner came from the person; proposals are labeled "proposed".
- No benchmark is presented as a target.
- No KPI is described as evidence that the product works.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Definition only. Computation is A2; audiences and refresh are B1; checking existing cards for drift is the reliability skill.
- Who is reached and who is left out by group (equity) is Patient Engagement 4.x; this task can add a group column to a card, but equity priorities are not set here.
- Outcome measures a payer pays on are Market Access.
