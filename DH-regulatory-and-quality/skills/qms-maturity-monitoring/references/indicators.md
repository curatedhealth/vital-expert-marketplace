# Governance effectiveness indicators

Interpretive reference for A2 and B1. It defines indicators the person's own data can produce, the external context beside them, and what each can and cannot show. No indicator carries a target here: thresholds come from the person.

## Indicators from the person's data

| Indicator | Computed from | What it can show | What it cannot show | Rows behind the indicator |
|---|---|---|---|---|
| Management review coverage | Each review's inputs against the person's own list of required inputs | Whether the inputs the person decided on reached the review | Whether decisions were good | QS16, QS19 |
| Management review action closure | Actions raised and closed per review | Whether review outputs are followed through | Effect of the actions | QS16 |
| Audit finding closure | Findings with audit date, source, process, due date, closed date | Share closed, open past the person's own due date, by source and process | Whether the fix worked | QS15 |
| Repeat findings | Findings the person links to an earlier finding (repeat_of), within three years | Corrections that may not have held, by MDSAP's definition | Cause | QS47 |
| CAPA ageing | Opened, closed, due date per CAPA | Age of open CAPA, open past the person's due date, time to close | Whether depth matched the risk | QS18 |
| CAPA effectiveness verification recorded | Closed CAPA with or without a recorded verification | Closures without a recorded verification | That a recorded verification was adequate | EU4 |
| Reporting timeliness | Awareness date and report date per reportable event | Reports beyond 15, 10 or 2 days (EU) or 30 days or 5 work days (US) | Reportability decisions | VG4 to VG6, VG12, VG17, VG18 |

`scripts/qms_indicators.py` computes the first six from CSV files (`capa`, `findings`, `mr` subcommands). Reporting timeliness is computed by hand from the person's event list: count calendar days from the awareness date (day 0) for the EU (VG12).

Ageing bands are display bins the person chooses (`--bins`). They are not thresholds. "Overdue" always means past the person's own due date.

## External context

### FDA Form 483 observations, fiscal year 2025 (pre-QMSR)

- FDA publishes yearly spreadsheets of regulation areas cited on system-generated 483s; they are not a complete list of observations (QS51).
- FY 2025 covers inspections ending 1 October 2024 to 30 September 2025: 791 system-generated 483s in the Devices area (QS52).
- Measured from the Devices tab: 185 cite rows, 2,660 citations. Top five: CAPA procedures 820.100(a) 279; complaint procedures 820.198(a) 211; purchasing controls 820.50 115; nonconforming product 820.90(a) 95; process validation 820.75(a) 93 (QS53). Also management review procedures 820.20(c) 49; quality audit procedures 820.22 57; MDR procedures 803.17 63 (QS54).
- Grouped by section with `qms_indicators.py fda483`: 820.100 342 citations (12.9 percent), 820.30 315 (11.8 percent), 820.198 286 (10.8 percent), 820.50 190 (7.1 percent), 820.20 119 (4.5 percent), 820.22 107 (4.0 percent) (`examples/fda483_fy2025_by_section.md`).

How to use it: label every figure "FY 2025, pre-QMSR". FY 2025 ended before the QMSR took effect on 2 February 2026, so these cite the retired QS regulation sections; comparing them with later years needs a crosswalk the research did not read (research "Changes and conflicts"). Use them to say which process areas FDA cited most often across all device firms. Never as a benchmark, a target, or a prediction for the person's inspection.

### What FDA looks at now

Under CP 7382.850 an inspection evaluates at least one element in each of six QMS areas and four other requirements (model 1), or a named minimum set including management review, complaint handling, internal audits and corrective action (model 2) (QS32, QS33, BX3). Management review and audit reports can be inspected (QS15). This tells the person which records an investigator may ask for; it says nothing about their likelihood.

### MDSAP grades

If the person holds MDSAP findings, read their grades with QS44 to QS46. One grade 5, or more than two grade 4, triggers a notice to regulators within 5 working days (QS48). These are facts about the audit process, not a maturity measure.

### Safety events from the library

`regulatory-dh.search_safety_events` returns recalls and MHRA alerts for a named manufacturer or product. Use them as external signals that a problem reached the field, described only by what the record states. A recall is not a finding about a QMS process, and no event in the library is not evidence of no events (`tools.md`).

## Never

- Never use a national or FDA-wide figure as a target or a pass mark.
- Never read low numbers of findings or CAPA as evidence that a process works.
- Never compute an indicator from data the person has not supplied.
