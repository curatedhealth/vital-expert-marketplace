# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`), Regulatory suite. Names are the library's; your assistant may prefix them. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`. `list_jurisdictions` is free; the others are counted.

## regulatory-dh.list_jurisdictions (free)

- Returned: US 1,226 authorizations and 892 safety events (loaded 19 October 2026); EU 3,142 authorizations and 0 safety events; UK 0 authorizations and 10 MHRA alerts (loaded 14 October 2026); CH nothing loaded.
- Use it first: an EU or Swiss safety search can only come back empty, and that says nothing about the market.

## regulatory-dh.search_safety_events (counted)

- Arguments (all optional): `manufacturer`, `product`, `product_code`, `jurisdiction` (US, EU, UK, CH, all), `since` (YYYY-MM-DD), `limit` 1 to 25.
- Returns `results` (FDA recalls with title, event_date, severity, manufacturer, summary, source_url; MHRA alerts with gov.uk URLs) and `maude_counts` (reports by product code and year, "counts are reports, not confirmed events").
- Observed:
  - `{product_code: "QAS"}` returned ten Class II recalls, all Siemens fluoroscopy and CT systems, none a QAS device, plus a MAUDE block of 0 reports for QAS.
  - `{product_code: "QIH", jurisdiction: "US", since: "2025-01-01"}` returned recalls for an ultrasound system, a PACS, and da Vinci surgical systems, plus 10 MAUDE reports for QIH (2 in 2024, 5 in 2025, 3 in 2026).
  - `{manufacturer: "Aidoc"}` and `{product: "BriefCase"}` returned no recalls and the same MAUDE block for QAS (0), QFM (0) and QIH (10).
  - `{jurisdiction: "UK", product: "software"}` returned MHRA alerts with gov.uk links; one alert names "AI Medical AG" as manufacturer while its text says the device is made by B. Braun Avitum AG.
- Pitfalls:
  - The `product_code` filter applies to MAUDE counts, not to recalls. Read every recall's title before using it; keep only those that name the product or a comparable device.
  - MAUDE counts are per product code and carry no manufacturer. Never attribute them to one company.
  - Recall `source_url` is the openFDA endpoint, not the recall page. Quote the title and date so the person can find it in FDA's recall database.
  - The `manufacturer` field on MHRA alerts may be wrong; read the alert text.
  - Manufacturer names must match the stored spelling. `{manufacturer: "Viz.ai"}` returned nothing because the store holds "Viz.Al, Inc." (letter l). Find the stored spelling with `search_devices` first. `{manufacturer: "Brainomix"}` returned no recalls and MAUDE counts for POK (1, in 2021), QAS (0) and QIH (10).
  - An empty result is not evidence of safety.
  - A manufacturer search matches the stored legal name only (see the Viz.ai observation above); a recall filed under a distributor, subsidiary or other entity name will not match. Say so when reporting zero results.

## regulatory-dh.search_devices and get_pathway_precedents (counted)

- Used to identify comparable devices for the safety search and to read the person's own authorization. Arguments and pitfalls as in the pathway skill: name search; no AI or PCCP field; EU rows have no decision date and a generic source URL; spellings differ across jurisdictions.
- Observed: `get_pathway_precedents {product_code: "QAS"}` gave 88 decisions (87 510(k), 1 De Novo), last decision 16 September 2026, which is later than the latest decision on FDA's AI-enabled device list (29 June 2026) [AI US-35].

## regulatory-dh.get_deltas and get_register_deltas (counted)

- Required: `since`. Scope: `product_code`, `manufacturer` or `emdn_code`.
- Observed: `{since: "2026-09-01", product_code: "QAS", jurisdiction: "US"}` returned nothing: "no watch is registered for this scope; the change log has not started".
- Pitfall: the change log only starts when a watch is registered with `watch_register`, which this skill does not call. Without a watch, use `search_devices` and `search_safety_events` with `since` and compare runs yourself.

## regulatory-dh.retrieve_guidance (counted)

- Observed: no passages for "predetermined change control plan artificial intelligence" or "AI Act high-risk medical device"; five passages for "PCCP" that read as Health Canada guidance, with no source URL or date. Do not use them. Requirements come from `references/`.

## verify.qualify_source and verify.build_record (counted)

- `verify.qualify_source` with FDA's PCCP guidance URL returned "inadmissible, no provenance". Regulator texts cannot be checked through Verify today; the reference rows carry URL, quote and read date.
- `verify.build_record` needs a named human in `cleared_by`.

## Not called

`watch_register` (would start a change log; out of scope), `compare_authorizations`, `generate_report` (its market-status block contradicts the device it describes; see the pathway skill's tools file).
