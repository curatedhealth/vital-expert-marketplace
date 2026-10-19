# Library tools and helpers used by this competency

This competency runs mainly on the person's own records: the CAPA plan with its effectiveness criteria, the CAPA log and the complaint log. The library adds public context only. Behavior below was observed in live calls on 19 October 2026 (trimmed outputs in `examples/live/connector_calls_2026-10-19.json`, shared with the sibling skill).

## regulatory-dh.list_jurisdictions (free)

- No arguments. Observed: US 892 safety events (FDA recalls and MAUDE counts), UK 10 MHRA alerts, EU 0, CH 0. EU vigilance data is not in the library.

## regulatory-dh.search_safety_events (counted)

- At least one of `manufacturer`, `product` (one word), `product_code`; optional `jurisdiction`, `since`, `limit`.
- Use in A2 only, and only when the person asks how their recurrence pattern compares with public records, or wants to see whether a comparable product had repeated recalls. One or two calls.
- Pitfalls (details in the sibling skill's `tools.md`): whole-phrase matching ("insulin dosing app" returned nothing, "insulin" returned five recalls); `product_code` unreliable (LLZ empty, PHV returned rows) and not shown on rows; the software filter is loose (a stolen-sensor recall with "Software Version: N/A" came back); MHRA `manufacturer` can be wrong ("AI Medical AG" on a B. Braun alert); `event_date` basis not stated; MAUDE counts are reports, not confirmed events.
- Describe each event only by what its record states. Two recalls of the same product are not a "recurrence" unless the records state the same defect.

## regulatory-dh.retrieve_guidance (counted)

- Observed: no sourced passage on vigilance timelines, CAPA or complaints (passages carry `source_url` "[GAP]", some cite retired QS sections, some are off-topic). Do not use it for rules in this skill.

## FDA 483 observation data

- Not in the library. The FY 2025 figures are in `effectiveness-and-trends.md` section 4, from FDA's spreadsheet (QS51 to QS54). Pre-QMSR.

## verify.build_record

- Requires a human name in `cleared_by`. Not called in this build. Call it when a review leaves the conversation and the person names the clearer.

## scripts/complaint_trends.py (local)

- `python3 scripts/complaint_trends.py complaints.csv [--capas capas.csv] [--rules rules.json] [--as-of YYYY-MM-DD] [--holidays file] [--json]`
- Work-day clocks (us-mdr-5, us-806-correction) always exclude Federal holidays: by default from `scripts/us_federal_holidays.txt` (OPM, 2026 and 2027, R14), or from `--holidays`. Each work-day row names the holidays excluded and warns when its window runs outside the file's years. For us-mdr-5 rows the awareness_date must be the management awareness date (803.3, VG19).
- Columns are listed in the script header. One row per complaint and jurisdiction assessed; a complaint assessed for two jurisdictions has two rows with the same id (counted once for ageing and counts).
- Sections: recurrence after CAPA closure (same code, after closure, within the person's window); open complaint ageing (against the person's limit, or no verdict); reporting timeliness (due date per clock from the awareness date; on time, late, undecided past due, decided not reportable after the due date); counts by code and month.
- Tested on `examples/illustrative_complaint_log.csv` (invented data) and on edge cases (missing awareness date, unknown event type, decision after the due date, reportable but not submitted).
