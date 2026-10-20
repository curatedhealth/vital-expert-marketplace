# Worked example: A1 signal scan, AI triage for CT (saved live data)

Built on 20 October 2026 from live library outputs saved on 19 October 2026 (`examples/live/`, origins in `examples/live/README.md`) and the company status rows read on 20 October 2026 (SP-162, SP-164). The connector was disconnected during the build, so no new call was made; the calls listed are the saved ones. The request is illustrative.

**Request.** "We are the strategy team of an imaging company. Scan the AI radiology triage space (FDA product code QAS) since 1 October 2025: what moved on the record? Our CEO forwarded a press release saying a rival will 'soon' get FDA clearance for an LLM triage tool; put it on the map as a strong signal. Scope US and EU."

**Steps run.** `list_jurisdictions` (perimeter); `search_devices` for Aidoc and Brainomix (all) and Briefcase, Viz (EU); `get_pathway_precedents` QAS; `find_predicates` K261317; `get_deltas` QAS since 1 September 2026 (log state only); then `python3 scripts/horizon_helpers.py signals ... --since 2025-10-01`, `byyear` and `makers --code QAS --since 2025-10-01`.

---

## Answer (short mode)

**Answer.** The QAS device type holds 88 FDA decisions through 16 September 2026, 15 in 2025 and 10 so far in 2026. The saved records name three QAS makers: Aidoc (five clearances in your window, newest K261317, 14 May 2026), Brainomix (latest K251983, 26 August 2025, before your window) and Viz.ai, stored as "Viz.Al, Inc." (De Novo DEN170073, 13 February 2018). Six of the ten 2026 decisions are not tied to a maker in what was read. The press release is a lead, not a signal.

**Signals (window from 1 October 2025)**

| Id | Type | Event date | Record | Does not show | Source |
|---|---|---|---|---|---|
| S1 | Decisions for a device type | 16 September 2026 (last) | QAS: 88 decisions since 13 February 2018; 2025: 15, 2026: 10 (partial) | An AI count, uptake or market size | Library pathway precedents, saved 19 October 2026 |
| S2 to S6 | Clearances, Aidoc BriefCase-Triage | 14 May 2026; 26 February, 27 January, 7 January 2026; 6 November 2025 | K261317, K253578, K251195, K252970, K253265 | AI or PCCP status, intended use, clinical effect | FDA 510(k) records, retrieved 13 October 2026 |
| S7 | Rule change | In force 27 July 2026 | AI Act high-risk duties for Annex I devices from 2 August 2028 | Whether your product is caught | Regulation (EU) 2026/1744, Official Journal (EU-17 to EU-19) |

**Makers not yet named.** Of 2026's ten QAS decisions, four are Aidoc's; six are untied. FDA's 510(k) database can be searched by product code (FDA medical device databases page, read 20 October 2026; DL-131). Which rival names should I search?

**Leads, not signals.** Rival's "soon" LLM triage clearance: the confirming record is a 510(k) or De Novo number. Record not read `[GAP]`. No probability or date is given.

**Logs and coverage.** The QAS change log "has not started": not "no change" (S2 is in the store). EU: Briefcase-Triage "On the EU market", Basic UDI-DI 7290018052BC.TRGSU, no decision date stored. UK device registration and Switzerland are not loaded.

**Company status.** Aidoc Medical Ltd.: no SEC registrant found (EDGAR name search, 20 October 2026; SP-162 [WF]); FDA establishment registration 3014938447, Tel Aviv-Yafo, active for 2026 (FDA registration and listing, read 20 October 2026; SP-164). Neither is a statement about the business; the Israeli company register was not read `[GAP]`. Brainomix Limited and Viz.Al, Inc.: Status: [GAP]: not read; no SEC CIK or company number in the records read, so ask for each legal name and register number.

**Calls made** (saved 19 October 2026): regulatory-dh.list_jurisdictions {}; regulatory-dh.search_devices {query: "Aidoc", jurisdiction: "all", limit: 10}; regulatory-dh.search_devices {query: "Brainomix", limit: 25}; regulatory-dh.search_devices {query: "Briefcase" / "Viz", jurisdiction: "EU"}; regulatory-dh.get_pathway_precedents {product_code: "QAS", jurisdiction: "US"}; regulatory-dh.find_predicates {reference: "K261317"}; regulatory-dh.get_deltas {product_code: "QAS", since: "2026-09-01", jurisdiction: "US"}. Connector unavailable on 20 October 2026; saved outputs used.

Full version available on request (perimeter table, makers table, decisions per year, filtered-out rows, further dated rule changes; a trend reading only if you ask, labeled proposed).

Signal log draft. Signals are records; trends are yours. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

## Checks made on this example

- Word count of the answer section (from "**Answer.**" to the record line, calls list excluded, Source column excluded) with `scripts/horizon_helpers.py words`: 429 words, within the short-mode cap (run 20 October 2026).
- Every date and identifier above appears in `examples/live/search_devices_aidoc_2026-10-19.json`, `search_devices_brainomix_2026-10-19.json`, `pathway_precedents_QAS_2026-10-19.json`, `find_predicates_K261317_2026-10-19.json`, `search_devices_eu_2026-10-19.json`, `get_deltas_QAS_2026-10-19.json` or the cited rows (EU-17 to EU-19 in `references/ai-ml-regulation-research.md`; DL-131 in `references/diligence-research.md`; SP-162, SP-164 in `references/strategy-and-portfolio-sources.md`).
- The makers come from `python3 scripts/horizon_helpers.py makers --code QAS --since 2025-10-01` on those files: Aidoc 5 in window, Brainomix 0, Viz.Al 0; 2026: 10 decisions, 4 tied, 6 not.
- The press item stays a lead; no probability, no trend, no "no change". The record line is the very last line of the answer.
