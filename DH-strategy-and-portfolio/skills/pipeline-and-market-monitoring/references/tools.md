# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `diligence-dh_get_deltas`). Counted calls draw on the library key's monthly allowance; free calls do not.

**How this file was written.** The connector was not available when this skill was built on 20 October 2026. Behavior below comes from live outputs saved on 19 October 2026 by earlier builds (copied into `examples/live/`, read on 20 October 2026; each origin is in `examples/live/README.md`) and from those builds' tools.md files. Where no saved output exists, the call is described from the old skill text only and marked **needs a live check**. The library twice returned "could not answer this call (503). Nothing was counted" in earlier builds; a retry a minute later worked.

## diligence-dh.get_deltas (counted)

- Required `companies` (1 to 12 names) and `since` (YYYY-MM-DD). Returns per company "no change recorded" or the changes, plus a `log` block: `first_entry_at`, `last_entry_at`, `last_sweep_at` and `limits`.
- Observed: `{companies: ["Akili Interactive Labs, Inc.", "Pear Therapeutics, Inc."], since: "2026-01-01"}` and `{companies: ["Big Health, Inc.", "Akili Interactive Labs, Inc."], since: "2025-01-01"}`: "no change recorded" for all, `change_count` 0; log first entry 12 October 2026, last entry 16 October 2026, last sweep 19 October 2026 (`examples/live/diligence_deltas_Akili_Pear.json`, `examples/live/diligence_get_deltas_BigHealth_Akili.json`).
- The old skill says it reads "what the store recorded for the watch since a date" and to "state when the watch has no later sweep". The saved calls returned the log without any watch registered; no watch is needed and none is set.
- Pitfalls:
  - The `since` filter uses event dates, not load dates, and the log began on 12 October 2026: quote the three `limits` lines whenever "no change recorded" is reported (`monitoring-signals.md` section 1).
  - Names must match the store's legal names ("Akili Interactive Labs, Inc.", "Big Health, Inc.", "Pear Therapeutics, Inc."). **Needs a live check**: how an unresolved name is reported (no saved output of a miss).
  - **Needs a live check**: the shape of a non-empty change row (no saved output contains a change). Report whatever event fields come back with their dates and URLs; `scripts/monitor_helpers.py deltas` prints any keys it finds.
- Use `diligence-dh.get_deltas`, not `commercial-dh.get_deltas`: the commercial wrapper dropped the log block and its Market Access feed returned "market_access_dh.get_deltas is not on that server" (`examples/live/commercial_get_deltas_Pear.json`, `{reference: "Pear Therapeutics, Inc.", since: "2026-01-01"}`).

## diligence-dh.screen_market (counted)

- Arguments: `segment`, `jurisdiction` (US, EU, UK, CH), `min_evidence_maturity`, `limit`. Returns `results` with company, country, jurisdictions, products, authorizations, studies, safety records and evidence maturity score, plus `total_matches` and the perimeter ("this screen covers only the companies the store holds, not the market").
- For monitoring, rerun with exactly the arguments of the earlier saved run and compare with `scripts/monitor_helpers.py screen-diff`. Runs with different arguments are not comparable; the script says so.
- Saved runs: `segment: dtx, limit: 8` (trimmed; products kept for one company only) and `segment: dtx, limit: 10`, both 19 October 2026, both through `commercial-dh.screen_commercial_peers`, whose `screen_market` block is this tool's output (`examples/live/screen_dtx_limit8_trimmed.json`, `examples/live/screen_dtx_limit10.json`). Their arguments differ, so no change can be inferred between them; the example shows the warning.
- Pitfalls: only `dtx` was loaded; DiGA makers are not returned; the order is the library's sort (evidence maturity, then name), so a company moving down the list is not a change in its record. A company "not returned" with a fixed `limit` may simply have been pushed past the limit: compare `total_matches` first.

## diligence-dh.list_sources (free)

- No arguments. Old skill: "Every source with credential state, last load, and row counts. A source not loaded states the reason."
- **Needs a live check**: no saved output of this call. The same census was read on 19 October 2026 through `commercial-dh.list_commercial_dh_sources` (`examples/live/list_commercial_dh_sources.json`). For monitoring, compare the loaded counts and the not-loaded list with the earlier saved run: a source newly loaded can show "changes" that are only new coverage.

## diligence-dh.watch_companies (described only, never called)

- Old skill: "Register a watch on 1 to 12 companies and return the snapshot hash. since is ignored on the write. One watch per tenant."
- Not called in this skill. The register records that watches in another suite were not separated by customer key (register item N2); say it in these words ("watches in another suite were not separated by customer key") and do not add a consequence the register does not state; the person's confidential pipeline names must not go into a watch. `get_deltas` answers without a watch (above).

## diligence-dh.get_funding_signals (counted; only to open a filing a change points to)

- `company`. Observed for `Pear Therapeutics, Inc.`: 46 SEC filings dated 9 February 2016 to 10 April 2023, 25 of them Form 8-K, 6 NIH grants; filing rows carry no 8-K item number and `counterparty` is null; `sum_of_stated_amounts` adds different filing types (`examples/live/funding_signals_pear.json`).
- Use here only to find the URL of a filing that a change read points to; the funding view itself is `funding-and-portfolio-comparison` (this pack). The latest filing date is "latest filing in the store", never a statement about the company's status. For a "since" date before the change log began (12 October 2026), its filing dates and types cover that window (`company-change-read.md` step 4).

## verify.build_record (counted)

- Needs a human `cleared_by.name`; `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name" (`examples/live/verify_build_record_refusal.json`). Call it only when an output leaves the conversation and the person names who clears it.

## Outside sites for company status (not library tools)

- The library does not show whether a company still exists, filed for bankruptcy or insolvency, was delisted, deregistered or acquired; its funding rows carry no 8-K item number. Status comes from the company's own primary filings or register entry: EDGAR (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; the submissions API, DL-150 to DL-152 [WF]), PACER (account needed, DL-154 to DL-156), Companies House `company_status` (DL-157 to DL-161), insolvenzbekanntmachungen.de and the German register extract (DL-165 to DL-168). How to read each: `monitoring-signals.md` section 5.
- Requests to outside sites never carry the person's email address or name. SEC asks automated clients to declare a User-Agent with a contact and caps requests at 10 per second; requests without one were refused on the research pass (DL-153 [WF]). Ask which contact the person's organization uses; if none is given, do not fetch from SEC: list the filings to open and write "Status: [GAP]: not read". Never invent a contact.

## Catalogue job market-screen

- The old skill files name `market-screen` for "Watch companies" and "Read company changes". **Needs a live check**: its `start_job` card was not saved by any earlier build. The direct calls in A1 and A2 remain the method.

## market-access-dh.list_schemes (free; used in A3)

- No arguments; free per the payer-engagement-and-hta-submission and coverage-pathway-and-access-strategy tools.md files. Saved baseline of 19 October 2026 (`examples/market-intelligence/list_schemes_2026-10-19.json`, trimmed by the earlier build): DE_DIGA 82 listings "partial"; FR_PECAN 2 and FR_LATM 2 "gold"; FR_LPPR 0 and UK_NICE_NHAP 0 "gap"; UK_NICE_EVA 15 and UK_NICE_HTG 2 "partial"; US_CMS_DMHT 3 and US_CMS_RPM 4 "partial", each with `last_load`.
- Use in A3 step 3 to compare the payers-lane perimeter now with the map's date. A posture or load date that differs is a perimeter change, not a market change.
- **Needs a live check**: a fresh call; only the 19 October 2026 output is saved, so no perimeter movement can be shown yet.

## scripts/monitor_helpers.py mi-check (local, no library call)

- Input: a CSV with columns `lane, jurisdiction, entry, source, date, gap` (one row per map entry; `date` as YYYY-MM-DD). Arguments are the person's only: `--as-of`, `--max-age-days` (optional, no default), `--lanes`, `--jurisdictions`.
- Tested 20 October 2026 on `examples/market-intelligence/ecosystem_map_insomnia_ILLUSTRATIVE.csv` with a tester's rule (60 days; lanes Buyers, Payers, Peers, Rules; US and DE): 3 failed elements (an unsourced, undated market size row; an empty buyers lane), output in `examples/market-intelligence/mi_check_insomnia_ILLUSTRATIVE.txt`.

## Not used here

- `commercial-dh.get_deltas` (see above), every `watch_*` tool.
- `diligence-dh.build_company_profile`, `get_evidence_maturity`, `retrieve_guidance`, `generate_report`: `company-and-evidence-assessment` (this pack).
- `diligence-dh.compare_portfolio`: `funding-and-portfolio-comparison` (this pack).
- Catalogue job `investment-memo`: design partners only; never started.
