# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `regulatory-dh_search_devices`). Counted calls draw on the library key's monthly allowance; free calls do not.

**How this file was written.** The connector was disconnected when this skill was built on 20 October 2026. Behavior below comes from live outputs saved on 19 October 2026 by earlier builds (copied unchanged into `examples/live/`, read on 20 October 2026; origins in `examples/live/README.md`) and from those builds' tools.md files. Where no saved output exists, the call is marked **needs a live check**. Earlier builds twice saw "could not answer this call (503). Nothing was counted"; a retry a minute later worked.

Monitoring here is by dated rereads, never by watches. No `watch_*` tool is called: watches are not separated by customer key in another suite (register N2), and the person's confidential technology names, calls and partners must not go into one.

## regulatory-dh.list_jurisdictions (free)

- No arguments. Saved run: US 1,226 authorizations, loaded 19 October 2026; EU 3,142, decision date empty on all; UK 0 authorizations (device registration not loaded); CH nothing loaded (`examples/live/list_jurisdictions_2026-10-19.json`).
- Compare with the scan's saved perimeter: a newly loaded source can look like "new signals" that are only new coverage.

## regulatory-dh.search_devices (counted)

- `query` (3+ characters), optional `jurisdiction`, `limit` 1 to 25. Saved runs: Aidoc (ten US 510(k) rows, newest K261317, 14 May 2026); EU "Briefcase" (Briefcase-Triage, "On the EU market", Basic UDI-DI 7290018052BC.TRGSU); EU "stroke" (ORTEC "Stroke Triage App", "No longer placed on the EU market", retrieved 14 October 2026); EU "Viz" (no row) (`examples/live/search_devices_aidoc_2026-10-19.json`, `search_devices_eu_2026-10-19.json`).
- Use in A1 to reread a logged signal (Q7) and in A2 to resolve calls and selections that rest on a register fact. Match on identifiers, not names. EU rows have no decision date: an EU status change has no date in the library; write "status as read on the retrieval date".

## regulatory-dh.get_pathway_precedents (counted)

- `product_code` or `emdn_code`; optional `jurisdiction`. Saved run QAS (US): 88 decisions, by year 2018 to 2026 (2025: 15; 2026: 10 to 16 September 2026), median 104 stored-date calendar days (`examples/live/pathway_precedents_QAS_2026-10-19.json`).
- Use to resolve count-based calls. The current year is partial; a count before the horizon date does not resolve a call.

## regulatory-dh.get_deltas and get_register_deltas (counted)

- Saved runs (QAS, Brainomix, EMDN Z11030592): no rows and "no watch is registered for this scope; the change log has not started", while `search_devices` held a QAS decision of 14 May 2026 (`examples/live/get_deltas_QAS_2026-10-19.json`, `register_deltas_2026-10-19.json`).
- Rule: never resolve a call or pass a signal on an empty log. Reread dated records instead.

## regulatory-dh.search_safety_events (counted)

- Saved run `{product_code: "QAS"}`: ten Siemens recalls, none naming a QAS device; the filter applied to MAUDE counts, not recalls (`examples/live/safety_events_QAS_2026-10-19.json`). Use only for a selection rule that names recalls; describe each record by what it states.

## literature.search_literature (counted)

- Saved run (digital CBT for insomnia, limit 8): 29 records after merge; off-topic records ranked in; design labels and trial ids unreliable (register N8) (`examples/live/literature_search_2026-10-19.json`). Use to reread a publication signal by DOI; a record is never a finding.

## diligence-dh.get_deltas (counted)

- `companies` (legal names), `since`. Saved runs: Big Health and Akili since 1 January 2025; Akili and Pear since 1 January 2026: "no change recorded"; log first entry 12 October 2026, last sweep 19 October 2026, with three limits lines (`examples/live/diligence_get_deltas_BigHealth_Akili.json`, `diligence_deltas_Akili_Pear.json`).
- Rule: a call or selection made before 12 October 2026 cannot be resolved from this log (flag R5 in `scripts/foresight_check.py`). Quote the log start and limits beside every "no change recorded". For a window before 12 October 2026, give the company's dated filings and authorization records instead; for Akili, Pear, Big Health and Aidoc they are already read (`company-status.md` section 6, SP-148 to SP-169).
- The log names "Akili Interactive Labs, Inc.", which the SEC record shows is the wholly owned subsidiary of the registrant Akili, Inc. (CIK 1850266), not a former name (Akili EDGAR record, read 20 October 2026; SP-148 [WF]). Read status at the registrant.

## diligence-dh.get_funding_signals (counted; only to find a filing a selection points to)

- `company`. Saved run for Pear Therapeutics, Inc.: 46 SEC filings dated 9 February 2016 to 10 April 2023, 25 of them 8-K; filing rows carry no 8-K item number (`examples/live/funding_signals_pear.json`).
- The latest filing date is "latest filing in the store", never a status. Company status comes from the filings themselves (`company-status.md`). The two newest stored Pear filings are the 8-Ks of 7 April 2023 and 10 April 2023; both are now read: chapter 11 filed 7 April 2023, case no. 23-10429 (Pear 8-K, filed 7 April 2023, Item 1.03; SP-156 [WF]) and the Nasdaq delisting notice of 10 April 2023 (Pear 8-K, filed 10 April 2023, Item 3.01; SP-160 [WF]). The library's store stops at 10 April 2023; EDGAR shows one later filing, the Form 25-NSE of 2 May 2023, and no Form 15 (Pear EDGAR record; SP-155 [WF]). For any other company, name the newest stored filings by type and date as the first to open, and ask the person to open them or give the contact their organization uses for EDGAR requests (never invent one, DL-153).

## analytics.mcda (counted)

- Only to re-rank options the person rescored after a review. Saved run shape and pitfalls (no robustness view, register C17; all criteria higher-is-better): `examples/live/mcda_partner_options.json` (illustrative scores). Re-ranking itself belongs to `horizon-scanning-and-technology-evaluation` B1 (this pack).

## verify.build_record (counted)

- Needs a human `cleared_by.name`; `{name: "Claude"}` was refused (`examples/live/verify_build_record_refusal.json`).

## Catalogue job

- `list_jobs` on 19 October 2026 lists no foresight or signal monitoring job (`examples/live/list_jobs_2026-10-19.json`). Every task's formula table says "Catalogue job: none".

## Steps that need a live check

1. Rereading a signal whose record changed between two runs (no saved pair of runs of the same call exists).
2. `diligence-dh.get_deltas` with a non-empty change row.
3. `search_devices` rereads for products other than those saved.
4. `literature.get_record` by DOI for a publication signal (no saved output in this skill).

## Not used here

Every `watch_*` tool; `commercial-dh.get_deltas` (drops the log block); `market-access-dh.*` (coverage changes route to `dh-access-and-value` coverage-strategy-and-access-rate-monitoring); `diligence-dh.screen_market` (investment pipeline routes to `pipeline-and-market-monitoring`, this pack).
