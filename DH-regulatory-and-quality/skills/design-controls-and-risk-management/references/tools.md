# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may show them with a prefix. Behavior was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

This competency is mostly method. The library adds one thing a design team cannot easily get alone: **software-related recalls and safety alerts for comparable products**, which seed hazard identification (task A2) with failures that have actually happened.

## regulatory-dh.list_jurisdictions (free)

- No arguments. Returns per jurisdiction: authorizations, safety_events, last load, scope line.
- Observed: US 892 safety events (FDA recalls whose product text mentions software, algorithm, application, firmware or app, plus MAUDE counts), last load 2026-10-19; EU 0 safety events (EUDAMED vigilance not loaded); UK 10 MHRA alerts, last load 2026-10-14; CH 0 (Swissmedic field safety actions not loaded).
- Use it to say which jurisdictions can contribute comparables at all. An EU or Swiss absence is a store gap, never "no events".

## regulatory-dh.search_safety_events (counted)

- Arguments: at least one of `manufacturer`, `product`, `product_code`; optional `jurisdiction` (US, EU, UK, CH, all), `since` (YYYY-MM-DD), `limit` 1 to 25.
- With none of the three, returns nothing and the gap "give manufacturer, product or product_code".
- Returns per event: `source_type` (fda_recall or mhra_alert), `title`, `event_date`, `severity` (recall class, or "device-safety-information" for MHRA), `manufacturer`, `summary`, `source_url`, `retrieved_at`; plus `maude_counts` by product code and year.
- What worked: `manufacturer: "Dexcom"` (10 software-related recalls), `product: "insulin"` (10 recalls, Tandem and Insulet), `manufacturer: "Insulet", since: "2025-01-01"` (2), `product_code: "PHV"` (Dexcom rows and MAUDE counts), `jurisdiction: "UK", product: "software"` (8 MHRA alerts).
- What returned nothing: `product_code: "LLZ"`; `product: "somnio"`. A product outside the store's software-recall perimeter returns empty with the line "absence from the store is not evidence of absence".

Pitfalls observed:
- **Duplicates.** One recall appears once per app line or model (the 24 July 2025 Dexcom "Sensor Failed" alert recall came back as five rows). Count events, not rows. `scripts/trace_check.py` does not do this; the monitoring skill's `risk_feedback.py --from-connector` folds them.
- **No recall number, no link to the recall record.** `source_url` for FDA rows is the API endpoint `https://api.fda.gov/device/enforcement.json`, not the recall page, and no recall or event number is returned. Cite the row as "FDA enforcement report, event date, firm, product line, via the library, retrieved DATE" and tell the person to confirm on FDA's recall database before external use.
- **Truncated titles.** FDA titles are cut at about 200 characters.
- **MAUDE counts are reports, not events.** The response says so ("counts are reports, not confirmed events"). The product code attached is not always explained: `product: "insulin"` and `manufacturer: "Insulet"` both returned MAUDE counts for code QRX with one report, without saying why that code was matched. Do not quote a MAUDE count for a product unless the code is the product's own, from its authorization record.
- **MHRA manufacturer field.** Mostly null; where filled it can name a firm other than the one the alert text names (Dialog+ alert names B. Braun Avitum AG, stored as "AI Medical AG"). Use the alert text.

## regulatory-dh.retrieve_guidance (counted)

- Three queries on ISO 14971, design controls and traceability, and "QMSR" returned no passage ("no passage retrieved in this namespace"). The guidance store holds nothing for this competency today. Do not call it again in a run; use `references/`.

## regulatory-dh.search_devices (counted)

- `query: "Dexcom G7", jurisdiction: "US"` returned nothing: the store's US perimeter is a set of digital health product codes, and CGM systems were not found under that name. Use it only when the person wants a product code or authorization for a comparable; never conclude a device is unauthorized from an empty result.

## find_job

- `query: "design controls risk management safety"` returned no job. There is no catalogue job for this competency; the skill is the method.

## verify.build_record (counted; not called in this build)

- Writes the record of an output that leaves the conversation. It refuses a record whose `cleared_by` name is missing or is a tool or model name (tool description, and observed in the Market Access builds). Call it only with the name of the person who clears the output.

## Not used here

- `verify.check_claim` and `verify.verify_text` on recall rows or regulation text: Verify rates register and regulator pages "no provenance" (register item C1), so they return unverifiable. Cite the row and its source instead.
- Watch tools: never called.
