# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may show them with a prefix. Behavior was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

The person's own complaints, MDR files and trace exports never go into a library call.

## regulatory-dh.list_jurisdictions (free)

- No arguments. Observed: US 892 safety events (FDA recalls whose product text mentions software, algorithm, application, firmware or app, plus MAUDE counts), last load 2026-10-19; EU 0 safety events (EUDAMED vigilance not loaded); UK 10 MHRA alerts, last load 2026-10-14; CH 0 (Swissmedic field safety actions not loaded).
- Call it once per A2 run so the output can say which markets the comparable evidence covers.

## regulatory-dh.search_safety_events (counted)

- Arguments: at least one of `manufacturer`, `product`, `product_code`; optional `jurisdiction` (US, EU, UK, CH, all), `since` (YYYY-MM-DD), `limit` 1 to 25. With none of the three it returns nothing and the gap "give manufacturer, product or product_code".
- Returns per event: `source_type` (fda_recall, mhra_alert), `title`, `event_date`, `severity` (recall class, or "device-safety-information"), `manufacturer`, `summary`, `source_url`, `retrieved_at`; plus `maude_counts` per product code and year.
- Search the person's own product first (`manufacturer` = their firm), then comparables (`manufacturer` for named competitors, `product` with a generic device word). Use `since` to bound a monitoring period.
- Observed results: `manufacturer: "Dexcom"` 10 rows (4 distinct events, 2025 to 2026); `product: "insulin", jurisdiction: "US"` 10 rows (8 distinct events); `manufacturer: "Insulet", since: "2025-01-01"` 2 events; `manufacturer: "Insulet", jurisdiction: "US", limit: 15` with no `since`: 4 events, including the 30 November 2023 Omnipod 5 Android Class I recall ("over-delivery of insulin ... if the user does not recognize the error on the bolus calculator screen or the confirmation screen"), checked 19 October 2026 (`examples/live/safety_events_insulet_all.json`); `product_code: "PHV"` Dexcom rows and MAUDE counts (2,081 reports, 2017 to 2026); `jurisdiction: "UK", product: "software"` 8 MHRA alerts (2014 to 2025). Empty: `product_code: "LLZ"`, `product: "somnio"`.

Pitfalls observed:
- **Duplicates.** One recall comes back once per app line or model (the 24 July 2025 Dexcom alert recall as five rows; the 27 February 2025 Tandem recall as two). Fold them before counting: `python3 scripts/risk_feedback.py --from-connector saved.json` does this (22 rows from three calls became 13 events).
- **No recall number, no record link.** FDA rows carry `source_url` = `https://api.fda.gov/device/enforcement.json` (the API endpoint) and no recall or event number. Cite date, firm, product line and retrieval date; confirm on FDA's recall database before external use.
- **MAUDE counts are reports, not events**, by date received (the response says so). The attached product code is not always explained: `product: "insulin"` and `manufacturer: "Insulet"` both returned code QRX with one report and no reason given. Use a MAUDE count only for the person's own product code taken from its authorization record, and never as an incidence rate (no denominator).
- **MHRA manufacturer field.** Mostly null; where filled it can name a firm the alert text does not (Dialog+ alert names B. Braun Avitum AG, stored as "AI Medical AG"; a Medtronic programmer alert stored as "RESTARTIX CENTER SRL"). Read the manufacturer from the alert text.
- **EU and Swiss events are not loaded.** A Germany- or Switzerland-only product gets nothing from this tool; say so.

## analytics.mcda (counted)

- Ranks items the person has scored. Arguments: `alternatives` (each `id` and `scores`, a map of criterion to a number on 0 to 4) and `criteria_weights` (the person's, summing to 1).
- Returns `value_estimate` (0 to 100) and `contributions` per criterion, the method (EVIDEM weighted sum, 0 to 4) and its citation.
- Pitfall: every criterion is treated as "higher is better". The response has a `negative_criteria` field, but the input schema offers no way to declare one. Phrase every criterion so that a higher score means more urgent (for example "ease of repair", not "effort"), and say so to the person.
- It gives no robustness view; work out swap points by hand (register item C17).

## regulatory-dh.retrieve_guidance (counted)

- Three queries on ISO 14971, design controls and traceability, and "QMSR" returned no passage. Do not call it in a run; use `references/`.

## verify.build_record (counted; not called in this build)

- Needs a named human in `cleared_by`; refuses a missing, tool or model name. Call it only when an output leaves the conversation.

## Not used here

- `verify.check_claim` and `verify.verify_text` on recall rows or regulation text: they rate register and regulator pages "no provenance" (register item C1). Cite the row and its source instead.
- Watch tools: never called.
