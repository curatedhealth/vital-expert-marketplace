# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`), Regulatory suite and Verify. The connector was not connected when this skill was built (20 October 2026), so no call was made for this build. Every behavior below comes from live outputs saved on 19 October 2026 by the dh-regulatory-and-quality builds, copied into `examples/live/` with their file names. Any step without a saved output is marked "needs a live check".

The library holds no model performance, drift or calibration data: those come only from the person's own logs, read with `scripts/drift_check.py`. The library is used for public safety records about the person's authorized product or named comparable devices, and for the record.

## regulatory-dh.search_safety_events (counted)

- Arguments (all optional): `manufacturer`, `product`, `product_code`, `jurisdiction` (US, EU, UK, CH, all), `since` (YYYY-MM-DD), `limit` 1 to 25.
- Saved: `safety_events_aidoc_2026-10-19.json`, `{manufacturer: "Aidoc", limit: 10}`: no recalls; MAUDE counts QAS 0, QFM 0, QIH 10 (2 in 2024, 5 in 2025, 3 in 2026); the same MAUDE block came back for `{product: "BriefCase", limit: 5}`.
- Saved: `safety_events_QIH_since2025_2026-10-19.json`, `{product_code: "QIH", jurisdiction: "US", since: "2025-01-01", limit: 5}`: five Class II recalls (a Philips ultrasound system, 7 August 2026; FUJIFILM Synapse PACS software v7.4.310, 22 July 2026; three Intuitive da Vinci recalls, 24 April 2026, 2 April 2026, 30 December 2025) plus 10 MAUDE reports for QIH. The saved observation: recalls are not filtered to product code QIH.
- Saved: `safety_events_UK_software_2026-10-19.json`, `{jurisdiction: "UK", product: "software", limit: 5}`: MHRA alerts with gov.uk links; one alert (MDA/2019/024) stores manufacturer "AI Medical AG" while its text names B. Braun Avitum AG.
- Pitfalls: the `product_code` filter applies to MAUDE counts, not to recalls; MAUDE counts carry no manufacturer and are never attributed to one company; recall `source_url` is the openFDA endpoint, so quote title and date; the MHRA `manufacturer` field may be wrong, so read the alert text (register N1); manufacturer names must match the stored spelling (find it with `search_devices` first); an empty result is not evidence of safety. Describe each record only by what it states; do not judge its relevance to the person's product.

## regulatory-dh.search_devices (counted)

- Saved: `search_devices_aidoc_2026-10-19.json`, `{query: "Aidoc", jurisdiction: "all", limit: 10}`: 510(k) records for BriefCase-Triage (for example K261317, Substantially Equivalent, 14 May 2026, QAS; K253578, 26 February 2026), manufacturer stored as "Aidoc Medical , Ltd.".
- Use: to confirm the person's authorization and the stored manufacturer spelling before a safety search. No AI flag, PCCP field or performance data on the record.

## regulatory-dh.get_deltas (counted)

- Saved: `get_deltas_QAS_2026-10-19.json`, `{since: "2026-09-01", product_code: "QAS", jurisdiction: "US"}`: no results; "no watch is registered for this scope; the change log has not started" (register C11). This skill never registers a watch. Changes are read by dated reruns of `search_safety_events` with `since`, compared by hand.

## regulatory-dh.retrieve_guidance (counted)

- Saved: `guidance_and_verify_2026-10-19.json`: no passage for PCCP or AI Act queries; "PCCP" returned Health Canada passages without source URL or date (register C6). Not used; rules come from `references/`.

## verify.qualify_source, verify.check_claim, verify.build_record (counted)

- `verify.qualify_source {url: "https://www.fda.gov/media/166704/download"}` returned "inadmissible", "no provenance" (register C1).
- For a [PAPER] row (Davis 2017, Sahiner 2023): `qualify_source {doi}`, then `check_claim` with the full qualify_source object (register C18); accept "supported" only after reading the passage in the same direction (register N3). Needs a live check.
- `verify_build_record_refusal_2026-10-19.json`: `build_record` refuses a record without a human `cleared_by.name`.

## Catalogue jobs

The saved `list_jobs` of 19 October 2026 (`list_jobs_2026-10-19.json`) shows no job for model monitoring or drift. Catalogue job: none. Needs a live check for any technology-suite job.

## Not called

`watch_*` and `watch_register` (never; monitoring is by dated reruns the person schedules), `analytics.*` (nothing is ranked here).
