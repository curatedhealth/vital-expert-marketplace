# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `regulatory-dh_search_safety_events`). This competency is mostly method: the person's records are the input, and the library adds public comparables. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/connector_calls_2026-10-19.json`.

## regulatory-dh.list_jurisdictions (free)

- No arguments. Returns stored authorization and safety-event counts per jurisdiction with last load date.
- Observed: US 892 safety events (FDA enforcement recalls and MAUDE counts, last load 19 October 2026); EU 0 safety events; UK 10 (MHRA alerts, last load 14 October 2026); CH 0, Swissmedic FSCA not loaded.
- Use it first in A2 so the output says which jurisdictions the library can show comparables for. The EU has none: EU vigilance comparables are `[GAP]` in the library.

## regulatory-dh.search_safety_events (counted)

- Arguments: at least one of `manufacturer`, `product`, `product_code`; optional `jurisdiction` (US, EU, UK, CH, all), `since` (YYYY-MM-DD), `limit` 1 to 25. With no filter it returns nothing and the gap "give manufacturer, product or product_code".
- Returns per event: `source_type` (fda_recall or mhra_alert), title, `event_date`, `severity` (Class I, II, III for FDA; "device-safety-information" for MHRA), manufacturer, summary, `source_url`, `retrieved_at`; plus `maude_counts` per product code by year (reports, not confirmed events).
- US scope is recalls whose product text mentions software, algorithm, application, firmware or app. Individual MAUDE reports are not returned, only yearly counts.

Pitfalls seen:

1. **Use one word or a manufacturer name.** `product: "insulin dosing app"` returned nothing; `product: "insulin"` returned five Class I and II software recalls (Tandem, Insulet). Matching is on the whole phrase.
2. **Product code is not a reliable filter.** `product_code: "LLZ"` returned nothing; `product_code: "PHV"` returned Dexcom rows. The rows carry no product code field, so you cannot see why a row matched. Prefer manufacturer or a single product word.
3. **The text filter is loose.** A Dexcom G7 sensor recall with "Software Version: N/A" (stolen scrap lots, sterility) came back as a software event. Read the summary before counting a row as a software comparable.
4. **MHRA manufacturer field can be wrong.** An alert for a B. Braun device carried manufacturer "AI Medical AG"; a Medtronic alert carried "RESTARTIX CENTER SRL". Use the manufacturer named in the alert title or summary, and say the field disagrees.
5. **`event_date` basis is not stated.** For FDA recalls it may be the recall initiation, classification or posting date `[GAP]`. Quote it as "event date as stored".
6. **MAUDE counts attach loosely.** A product search for "insulin" returned MAUDE counts for code QRX only. Report counts only with their product code and the line "reports, not confirmed events".
7. **No recall number, no root cause, no product code on rows.** For those, open the `source_url` at FDA.

How to use it in A2: two or three calls at most (manufacturer of a comparable product; one product word; a UK call with a product word). Describe each event only by what its record states (title, date, class, summary). Never infer the event's cause, the firm's CAPA, or whether it was reported under 803. A missing record is not evidence that nothing happened.

## regulatory-dh.retrieve_guidance (counted)

- Arguments: `query`, optional `namespace` (guidance), `limit`.
- Observed: no passage for "serious incident reporting timelines manufacturer awareness date vigilance"; "MDCG 2023-3" returned only a footnote from MDCG 2019-7 pointing to it; "corrective and preventive action" and "complaint" returned passages with `source_url` "[GAP]" and no retrieval date, some citing retired QS regulation sections (820.100, 820.198) with no date, and some off-topic (an eHealth Network service-desk guideline; a PROMIS pain study).
- Rule: do not use guidance passages as a source for any rule in this skill. The rules live in `references/`. Call it at most once, only if the person asks about a guidance document not covered there, and quote any hit as "library passage, source not stored".

## agent-pack.list_experts and download_agent

- `list_experts {query: "quality"}` returned the QA Manager, Software (V&V) (`quality-assurance-manager-software`, the worker bound to this competency in the register) and the Quality & Software Lifecycle Director (`quality-systems-director-software`). The bound worker's remit says it "does not own the quality system". Download it only if the person wants the expert as a standing agent.

## verify.build_record

- Requires a human name in `cleared_by`; refuses a tool or model name. Not called in this build (it writes a record). Call it only when an output leaves the conversation and the person names who clears it.

## scripts/reporting_clock.py (local)

- `python3 scripts/reporting_clock.py --date YYYY-MM-DD --event all-for-incident [--reportability-date ...] [--holidays file] [--as-of ...] [--json]`
- Computes EU, GB and US limits from one anchor date. `us-806-correction` counts from the initiation date; run it separately if that differs from the awareness date. `us-mdr-5` counts from management awareness that remedial action is needed (803.3, VG19); run it separately with that date. Federal holidays are always excluded from work-day counts: by default from `scripts/us_federal_holidays.txt` (OPM list, 2026 and 2027, R14), or from the file passed with `--holidays`; the output names each holiday excluded and warns when a window runs outside the file's years.
