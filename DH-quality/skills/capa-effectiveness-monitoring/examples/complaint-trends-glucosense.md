# Worked example: A2 on a complaint log, with a live check on repeated recalls

Run on 19 October 2026. The complaint log, CAPA log and limits are invented for this example (`illustrative_complaint_log.csv`, `illustrative_capas.csv`, `illustrative_rules.json`); the clocks, the helper output and the library records are real.

**Request:** "Here is our GlucoSense complaint log and CAPA log. Our limit for open complaints is 30 days. Are complaints coming back after our CAPAs, and are we on time with reporting? Also, is it normal for an app to be recalled twice?"

**Calls and runs**

1. `python3 scripts/complaint_trends.py illustrative_complaint_log.csv --capas illustrative_capas.csv --rules illustrative_rules.json --as-of 2026-10-19`: output saved as `complaint_trends_output_2026-10-19.md`.
2. Library (shared with the sibling skill, trimmed in `live/connector_calls_2026-10-19.json`): `regulatory-dh.search_safety_events {manufacturer: "Dexcom", jurisdiction: "all", limit: 10}`.

## Answer (short mode)

**What needs attention.**
- **Candidate recurrences.** CAPA-031 (stale glucose data, closed 31 August 2026, your 90-day window): two later STALE-DATA complaints, C-2026-130 (21 days after) and C-2026-136 (39 days after), both on version 3.2. CAPA-027 (sync failure, closed 15 July 2026, 120-day window): C-2026-118 (27 days, version 3.1) and C-2026-125 (55 days, version 3.2). Whether they share the original cause is yours to decide; if 3.2 carries the fix, that is the stronger signal.
- **A clock passed without a decision.** C-2026-130 (GB, serious incident criteria): awareness 21 September 2026, latest date 6 October 2026 (15 days, reg. 44ZH); still undecided. Route to the reportability assessment in DH-03.02.4.1 A2. GB day counting is not in the sourced rules `[GAP]`; the MDCG calendar-day convention was applied.
- **Late submission.** C-2026-109 (EU): MIR submitted 24 July 2026, 3 days after the 21 July limit (15 days from awareness on 6 July). The US 30-day report for the same complaint was on time.
- **Ageing.** C-2026-121 (UI-UNITS) has been open 53 days against your 30-day limit. Its CAPA-035 has no closure date, no window and no owner: "owner not named".

**Timeliness.** Seven assessments: one report submitted on time, one submitted late, two decided not reportable before their dates (C-2026-101, C-2026-138), one undecided past its date, two undecided within their dates. Federal holidays were not excluded.

**Context.** In FDA's FY 2025 data, CAPA procedures (279) and complaint procedures (211) were the two most cited device areas on 483s. Pre-QMSR, not a complete list, not a benchmark.

**Two recalls of one app.** The library shows the Dexcom G7 iOS app (SW12300) recalled on 24 July 2025 (Class I, missing "Sensor Failed" alert, versions 2.8.0 and earlier) and on 14 April 2026 (Class II, thread-blocking defect, versions 2.9.0 to 2.11.2). The records state two different defects, so they are not a recurrence of one problem. Nothing about that firm's CAPAs can be read from them.

**Record:** Draft from your log. Limits and verdicts are yours. Uncleared.

## What this example shows

- Recurrence is reported as "candidate" with ids, days and versions; the effectiveness verdict stays with the person.
- A late decision and a late submission are shown with their rule and dates, without urgency language.
- A CAPA with no owner gets "owner not named", not a suggested job title.
- Public records are read for what they state: same product, different defects.
