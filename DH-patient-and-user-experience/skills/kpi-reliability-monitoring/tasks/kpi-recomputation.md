# A2 KPI recomputation

Framework task: DH-02.03.3.2, Part A, task A2. Replaces register task CF-12.02.03.3.2.1 (KPI recomputation) and adds the measurement-property check for questionnaire-based KPIs.

## What this task delivers

For each KPI asked about: the dashboard number beside a recomputation from the source events with the card's rules (value, numerator and denominator compared separately), the difference, and the evidence that explains it (drift, excluded rows, refresh time) or "unexplained". For a KPI built on a questionnaire score, the COSMIN properties the instrument's named evidence meets. It answers "does the dashboard number hold up when we recompute it, and is the instrument behind it reliable enough to report?"

Why it matters: the register's rule is "Do not trust the dashboard number without a recomputation." Two figures can match in value and count different people. A KPI built on a questionnaire inherits the instrument's measurement error: COSMIN rates reliability sufficient at an ICC of at least 0.70 (PE-95) and measurement error sufficient when the smallest detectable change is below the minimal important change (PE-96).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Data & Analytics Lead (`data-analytics-lead`) |
| Skill | DH-02.03.3.2 Part A, KPI recomputation |
| Workflow | The steps below |
| Knowledge | `references/reliability-checks.md` (sections 4 and 5); `references/kpi-definitions.md`; `references/attrition-curves.md`; rows PE-93 to PE-97, PE-19 to PE-21, KX9, KX10 |
| Tools | `scripts/engagement_kpis.py` (needs code execution); optional `verify.qualify_source` and `verify.check_claim` (counted) to cite a COSMIN criterion; optional `literature.search_literature` (counted) to find an instrument's published evidence |
| Prompt | This guide |
| Template | `assets/recomputation-output.md` |
| Input | The request and its context: the KPI card, the dashboard value with its numerator, denominator and refresh time, the dashboard's definition if available, the event export, the eligible list if needed, the as-of date the dashboard used; for an instrument, its name and the evidence the person relies on |
| Governance | `references/governance.md`; the acceptable difference and whether evidence is enough are the person's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. evidence-table grades a set of studies for a product's claims; this task only identifies or checks a source the person names. |

## Read the request

- **Which KPI and period.** One KPI at a time unless the person asks for several.
- **The dashboard number.** Value, numerator, denominator, refresh time and the as-of date it used. Without the counts, compare value only and say so.
- **The source.** The event export and, for reach, the eligible list.
- **Their tolerance.** The difference they accept. Without one: report the difference, no verdict.
- **Instrument.** Name, version and the evidence they rely on (papers, the vendor's documentation).

## Workflow

### Step 1. Recompute with the card

Write the card in the script's format and run `python3 scripts/engagement_kpis.py kpis EVENTS.csv --defs CARD.json [--eligible ELIGIBLE.csv]` with the dashboard's as-of date and period. For an attrition KPI, run `attrition` with the card's start event, use event and days without use (`references/attrition-curves.md`).

### Step 2. Recompute with the dashboard's definition

If the dashboard's own definition is available, recompute it too (same command, its definition as the card). If it reproduces the dashboard number, the gap is drift, not a pipeline fault: hand the field to A1 and B1.

### Step 3. Compare three ways

Value, numerator and denominator side by side: dashboard, recomputed with the card, recomputed with the dashboard definition. Report the difference in the KPI's unit and in counts. A matching value with different counts is reported as a mismatch.

### Step 4. Explain only with evidence

Name what the evidence shows: a field that drifted, rows excluded (and how many), a refresh older than the as-of date, events after the as-of date. Anything else: "unexplained", with what would explain it (a pipeline log, the BI query) as a labeled hypothesis.

### Step 5. Instrument-based KPIs (if any)

- List COSMIN's criteria for sufficient (section 5 of `reliability-checks.md`) and, for each, whether the person's named evidence reports it and meets it. Without the evidence in hand: "not seen".
- For a change-score KPI, ask how a meaningful change is defined; FDA's draft PFDD Guidance 4 asks for a well-justified anchor (PE-20, draft). PAM level cut points are not in the sources `[GAP]`.
- To cite a COSMIN criterion outside the conversation: `verify.qualify_source {doi: "10.1007/s11136-018-1798-3", question}`, then `verify.check_claim` with the passage from PE-95 or PE-96 and the whole `qualify_source` object as `source` (`references/tools.md`). Accept only a passage that states the criterion in the same direction (register N3).
- To find an instrument's published evidence, `literature.search_literature {query: "INSTRUMENT reliability validity", limit: 5}`; report titles and DOIs found; rating them needs the papers.
- Whether the evidence is enough is the person's decision. Published evidence is not evidence about the person's own population.

### Step 6. What it means for the person

Two or three conditional consequences. Example: "The dashboard's 23.5 percent and the card's 23.4 percent are different measures: the dashboard includes 21 people enrolled less than 56 days before 19 October 2026 who could not yet reach the dose."

## Build the output

Follow `assets/recomputation-output.md`. Answer first: match or mismatch, with the three-way comparison and what explains the difference. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Recomputation used the card's rules and the dashboard's as-of date and period.
- Value, numerator and denominator compared separately.
- Every explanation names its evidence; the rest is "unexplained" with labeled hypotheses.
- No instrument is called valid or reliable; COSMIN criteria are shown as criteria met or not met by named evidence.
- No number was adjusted to match.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Recomputation and measurement properties only. Card and drift checks are A1; repairs are B1.
- Validating a clinical outcome assessment for a submission is the clinical and regulatory owners' work (dh-clinical-development, dh-regulatory-and-quality).
- A payer's outcome calculation is Market Access.
