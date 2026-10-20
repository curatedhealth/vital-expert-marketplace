# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`), Regulatory and Verify suites. Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; a call that returns an error says "Nothing was counted".

**How this file was built.** The connector was disconnected during this build (20 October 2026), so no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by the dh-regulatory-and-quality builds, copied unchanged into `examples/live/` (file named on each entry, read 20 October 2026), and from those builds' `tools.md` files. Where a tool has no saved output for the use made here, the step is marked **needs a live check**. Most of this skill runs on the person's own hazard list, test records, plan register, release log, SBOM, capacity and placement records and miss log through `scripts/delivery_check.py`; the library supplies public recall records of comparable software for a period and the person's own clearance record.

## regulatory-dh.list_jurisdictions (free; run first when a safety search is planned)

- Saved: `list_jurisdictions_2026-10-19.json`: US 1,226 authorizations and 892 safety events (sources openfda, openfda_enforcement, openfda_pma; loaded 19 October 2026); EU 3,142 authorizations, 0 safety events, decision date empty on every EU row; UK 0 authorizations and 10 MHRA alerts (loaded 14 October 2026; device registration not loaded).
- Pitfall: an EU safety search can only come back empty. Say so instead of reporting "no events".

## regulatory-dh.search_safety_events (counted; A2 step 6, public recall records of comparable software in the person's period)

- Arguments (all optional): `manufacturer`, `product`, `product_code`, `jurisdiction` (US, EU, UK, CH, all), `since` (YYYY-MM-DD), `limit` 1 to 25.
- Saved: `safety_events_QRX_2026-10-19.json` (`{jurisdiction: "US", product_code: "QRX", limit: 10}`): Class I and Class II recalls of Dexcom CGM apps (for example "Dexcom G7 CGM iOS App, SW12300, Versions 2.9.0 through 2.11.2", 14 April 2026, Class II, a low-priority file check blocking the thread that processes glucose values; "Dexcom G6 and G6 Pro Android US CGM App, SW11678, version 1.15.0", 28 August 2025, Class I, the app can terminate unexpectedly), one Omnipod 5 iOS app recall (11 September 2025, Class II, a digit duplicated with the iPhone magnifier), and a sensor-theft recall that matched only because its title says "Software Version: N/A". MAUDE block: QRX, 1 report (2022), "counts are reports, not confirmed events".
- Saved: `safety_events_other_2026-10-19.json`: `{jurisdiction: "US", product: "software", since: "2025-01-01", limit: 10}` returned 10 recalls, for example "FUJIFILM Synapse PACS software v7.4.310", 22 July 2026, Class II, "Software issue may cause the ruler measurement to be inaccurate"; `{product_code: "LLZ", since: "2025-01-01"}` returned nothing; `{jurisdiction: "UK", limit: 5}` with no other filter returned "give manufacturer, product or product_code".
- Saved: `safety_events_uk_software_2026-10-19.json`: `{product: "software", jurisdiction: "UK", limit: 10}` returned 8 MHRA alerts with gov.uk links (for example BD BodyComm version 3.3 software and the transition to Windows 11, DSI/2025/006, 6 October 2025).
- Pitfalls (register P1 and N1):
  - Rows carry no product code; a `product_code` filter cannot be confirmed from the row. Read every title and keep only rows that name software comparable to the person's.
  - The free-text `product` filter matches title words ("software" matched a sensor-theft recall).
  - `source_url` on US recalls is the openFDA endpoint, not the recall page: quote the title, date and class so the person can find the record.
  - MAUDE counts are per product code, are reports and not confirmed events, and carry no manufacturer.
  - The MHRA `manufacturer` field is often null or names a firm the alert text does not.
  - An empty result is not evidence of safety.
- Use: pass the person's period start as `since` (never a date the person did not give). A recall describes what happened to someone else's software as its record states it. It is a signal the person may weigh for their own hazards; the skill never judges its relevance to the person's product.
- Change log: `get_deltas` would need a watch (register C11), which this skill never sets. Monitoring is by dated reruns of `search_safety_events` with `since`, compared by the person.

## regulatory-dh.search_devices and get_authorization (counted; A1 step 1, only to quote the person's own clearance record when they give its number)

- Saved: `authorization_K252818_K222888_2026-10-19.json`: `search_devices {query: "Dexcom G7", jurisdiction: "US"}` returned nothing; `{query: "Dexcom"}` returned two rows; `get_authorization {reference: "K252818"}` returned Dexcom Smart Basal, 510(k), class 2, "Substantially Equivalent", decided 18 November 2025, product code QRX, regulation 862.1358, predicate K222888, `software_device: true`; `{reference: "K222888"}` returned the BlueStar CGM insulin dose calculator (Welldoc, Inc.), decided 11 August 2023.
- Pitfalls: a full product name can miss; search by manufacturer and read the rows. No field states whether a PCCP was authorized with a clearance. EU rows have no decision date. De Novo rows show FDA's raw code "DENG" (register C3).
- Use: to quote the person's clearance by number and date in the read header. The record does not hold the cleared software version, its specification, or whether a PCCP was authorized; those come from the person.

## verify.build_record (counted; on sign-off only)

- Saved: `verify_build_record_refusal_2026-10-19.json`: `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name".
- Call it only when the output leaves the conversation and the person names who clears it.

## verify.qualify_source (counted; not used for regulator texts)

- Earlier builds saw FDA guidance URLs rated "inadmissible, no provenance" (register C1, in the dh-regulatory-and-quality tools files). The reference rows carry URL, quote and read date instead. **Needs a live check** before any use here.

## retrieve_guidance (not used)

- Earlier builds saw no passage for design controls, QMSR or the FDA software change guidance, and passages without source URLs (register C6). Requirements come from `references/`.

## Catalogue jobs

- No software quality, delivery or release-monitoring job appears in the saved catalogue listings read for this build (the trimmed `list_jobs` output saved by the strategy build, 19 October 2026). Every task's formula row says "Catalogue job: none known (needs a live check)".

## Not called

`watch_*` tools (never), `get_deltas` and `get_register_deltas` (the change log needs a watch; register C11), `generate_report`.
