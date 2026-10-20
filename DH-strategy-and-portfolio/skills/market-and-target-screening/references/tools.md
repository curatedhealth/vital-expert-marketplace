# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `diligence-dh_screen_market`). Counted calls draw on the library key's monthly allowance; free calls do not.

**How this file was written.** The connector was not available when this skill was built on 20 October 2026. Behavior below comes from live outputs saved on 19 October 2026 by earlier builds (copied into `examples/live/`, read on 20 October 2026; each origin is in `examples/live/README.md`) and from those builds' tools.md files. Where no saved output exists, the call is described from the old skill text or a saved listing only and marked **needs a live check**. The library twice returned "could not answer this call (503). Nothing was counted" in earlier builds; a retry a minute later worked.

## diligence-dh.list_sources (free)

- No arguments. The old skill says it returns "every source with credential state, last load, and row counts. A source not loaded states the reason. This call is free."
- **Needs a live check**: no saved output of this call exists. The same census was read on 19 October 2026 through `commercial-dh.list_commercial_dh_sources` (`examples/live/list_commercial_dh_sources.json`): loaded counts include openFDA 1,224, openFDA enforcement 892, ClinicalTrials.gov 128, EUDAMED software 3,141, SEC EDGAR 175, NIH RePORTER 18, EU TED 41, MHRA alerts 10; not loaded: Companies House, Zefix, the DiGA directory feed, NICE, private funding, each with its reason.
- Use it first in A1 and A2: it is the perimeter. A source not loaded makes every related field `[GAP]`.

## diligence-dh.screen_market (counted)

- Arguments: `segment`, `jurisdiction` (US, EU, UK, CH), `min_evidence_maturity`, `limit`. The old skill's boundary: "Segment, jurisdiction (US, EU, UK, CH), and a minimum evidence maturity the buyer supplies. Rank only by those criteria."
- Observed, `{segment: "dtx", jurisdiction: "EU", limit: 10}`: one company, Novasight, Ltd. (IL), product CureSight-CS100, jurisdictions EU and US, 2 authorizations, 5 studies, evidence maturity 56; perimeter 2,205 companies in the store, jurisdictions CA, EU, TW, US, segments `dtx` only, "this screen covers only the companies the store holds, not the market" (`examples/live/diligence_screen_market_dtx_EU.json`).
- Observed through `commercial-dh.screen_commercial_peers {segment: "dtx", limit: 10}`, whose `screen_market` block is this tool's output: 18 total matches, 10 returned, each with `country: "US"` as stored (the record does not say whether that is domicile; write "country: US, as stored"); per company `country`, `jurisdictions`, `products`, `authorizations`, `studies`, `safety_events`, `evidence_maturity_score`; ranking "evidence maturity score, highest first, then company name; no other weighting" (`examples/live/screen_market_dtx_via_peer_screen.json`).
- Pitfalls:
  - Only `dtx` was loaded. Other segment values are offered but empty (see `search_companies`).
  - DiGA makers are not returned for `dtx` and EU, although the DiGA directory mirror is loaded; the response itself flags the contradiction. Say so in the coverage note.
  - `min_evidence_maturity` is a filter on the library's score. Use it only if the person sets it; never set it for them.
  - Product strings can be long kit descriptions (NightWare: "NightWare Kit, Apple iPhone, Apple Watch, ..."). Quote them as stored.
  - `safety_events` is a count of stored safety records (for Pear Therapeutics, Inc. the 2 matches the two Class II recalls of 7 June 2021 that `compare_portfolio` lists for reSET and reSET-O, saved 19 October 2026). Quote the count with its source; it is not a judgment of a product, and which record types it counts needs a live check.
- **Needs a live check**: a direct `screen_market` call with `jurisdiction: "US"` and with `min_evidence_maturity` set has no saved output.

## diligence-dh.search_companies (counted)

- Arguments (from the channel build's tools.md, 19 October 2026): `query` and/or `segment` (`dtx`, `samd-diagnostic`, `cdss`, `rpm`, `digital-health`), `country`, `has_authorization`, `limit`. The old skill: "Search by name, product, identifier, or segment slug ... Matching is exact, not semantic."
- Observed, `{segment: "rpm", limit: 10}`: `result_count` 0, sources used openFDA and ClinicalTrials.gov (`examples/live/search_companies_and_guidance_other_calls.json`). An empty segment is a coverage limit.
- **Needs a live check**: no saved output of a name, product or identifier search. Until checked, look a named company up with its exact legal name, a brand, or an FDA, LEI, EUDAMED or SEC number; if nothing returns, write "lookup missed" and name the identifier to try (`gap-rules.md`). For a full profile, route to `company-and-evidence-assessment` (this pack), which calls `diligence-dh.build_company_profile`.

## analytics.mcda (counted)

- `alternatives` (each `id` and `scores`, a map of criterion to 0 to 4) and `criteria_weights` (sum to 1). Returns an EVIDEM weighted-sum `value_estimate` (0 to 100) and contributions per criterion.
- Observed with ILLUSTRATIVE scores in the partnership-screen job run: Big Health 70, Akili 62.5, Click 60 on weights 0.5, 0.3, 0.2 (`examples/live/mcda_illustrative_partnership_screen.json`). The scores are the tester's, not an assessment of these companies.
- Pitfalls: every criterion is treated as higher-is-better (`negative_criteria` cannot be set), so phrase each criterion so 4 is best; a missing score refused the whole call with HTTP 400 and no message: drop an unscored candidate before the call and list it "not ranked"; no robustness view: run `scripts/screen_helpers.py swap`; `name` is null on every row.
- Ranks only what the person scored. Never call it with proposed scores.

## verify.build_record (counted)

- Needs a human `cleared_by.name`. `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name" (`examples/live/verify_build_record_refusal.json`). Call it only when an output leaves the conversation and the person names who clears it.

## Catalogue job market-screen

- The old skill files name `market-screen` as the catalogue job for "Screen a market", "Search companies", "Watch companies" and "Read company changes".
- **Needs a live check**: its `start_job` card (steps, tools, inputs) was not saved by any earlier build. In other suites `start_job` took only `job_id`, returned the method and ran nothing. The direct calls in A1 and A2 remain the method.

## Outside sites for company status (not library tools)

- The library does not show whether a company still exists, filed for bankruptcy or insolvency, was delisted, deregistered or acquired; its funding rows carry no 8-K item number. Status comes from the company's own primary filings or register entry: EDGAR (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; the submissions API, DL-150 to DL-152 [WF]), PACER (account needed, DL-154 to DL-156), Companies House `company_status` (DL-157 to DL-161), insolvenzbekanntmachungen.de and the German register extract (DL-165 to DL-168). How to read each: `screening-rules.md` section 5.
- Requests to outside sites never carry the person's email address or name. SEC asks automated clients to declare a User-Agent with a contact and caps requests at 10 per second; requests without one were refused on the research pass (DL-153 [WF]). Ask which contact the person's organization uses; if none is given, do not fetch from SEC: list the filings to open and write "Status: [GAP]: not read". Never invent a contact.

## Tools added for A3 Market intelligence map

These four calls serve the ecosystem map (task A3). Saved outputs are in `examples/market-intelligence/` (origins in its README) and `examples/live/`.

### market-access-dh.list_schemes (free)

- No arguments; free per the payer-engagement-and-hta-submission and coverage-pathway-and-access-strategy tools.md files. Observed 19 October 2026 (`examples/market-intelligence/list_schemes_2026-10-19.json`, trimmed by the earlier build): per scheme `code`, `listing_count`, `last_load`, `posture` ("gold", "partial", "gap") and `posture_reason`. DE_DIGA 82 "partial" ("Directory listings are stored ... this is not the history feed"); FR_LPPR and UK_NICE_NHAP 0 "gap"; US_CMS_DMHT 3 and US_CMS_RPM 4 "partial".
- Use it as the payers-lane perimeter. A "partial" or "gap" posture goes in the coverage line.

### market-access-dh.search_listings (counted)

- **Needs a live check** as a direct call: no saved output. Its result was read inside `commercial-dh.screen_commercial_peers {segment: "dtx", name: "Somryst"}` (`examples/live/screen_commercial_peers_dtx_somryst.json`): "no stored listing matches 'Somryst' in DE_DIGA, FR_PECAN, ... SE_TLV; absence from the store is not evidence of absence from the scheme".
- Pitfall carried from the earlier builds: a scheme code as the query returns nothing; search by product name.

### commercial-dh.screen_commercial_peers (counted)

- Arguments `segment`, `name` (optional), `limit`. Observed 19 October 2026: with `name: "Somryst", limit: 3` it returns the named product's device row (Pear Therapeutics, Inc., K191716, QVO, 882.5801, decision 2020-03-23, FDA URL) plus the top two screened companies; "name replaces the lowest-ranked slot" (`examples/live/screen_commercial_peers_dtx_somryst.json`). With `limit: 10` its `screen_market` block is the screen (`examples/live/screen_market_dtx_via_peer_screen.json`).
- Coverage line of the call: `market_access_dh.search_listings: [GAP]` for the unnamed peers. Quote it.

### commercial-dh.map_money_flow (counted)

- Arguments `reference` (product name or FDA number), `user`, `buyer`, `payer`, `note`. Observed 19 October 2026 on roles a tester typed: it echoes the three roles, returns `conflated: false`, and attaches payer listings (somnio: DE_DIGA "permanent", listed 2020-10-22, identifier 00508; `money_flow_somnio.json`. reSET DEN160018: no listed product matches, CMS rows code-level; `map_money_flow_reset.json`).
- Pitfalls: the roles are the caller's input, not a finding; the exhibit links run user to buyer to payer in argument order, "with no amounts and no direction of payment". Call it only on roles the person gives.

## Not used here

- `diligence-dh.watch_companies` and every `watch_*` tool: never called. Monitoring is by dated reruns (`pipeline-and-market-monitoring`, this pack).
- `diligence-dh.build_company_profile`, `get_evidence_maturity`, `retrieve_guidance`, `generate_report`: `company-and-evidence-assessment` (this pack). `diligence-dh.retrieve_guidance {query: "anti-kickback safe harbor"}` returned no passage on 19 October 2026; the deal and data rules here come from the DL rows, not the guidance store.
- `diligence-dh.get_funding_signals`, `compare_portfolio`: `funding-and-portfolio-comparison` (this pack).
- `diligence-dh.get_deltas`: `pipeline-and-market-monitoring` (this pack).
- Catalogue job `investment-memo`: design partners only; never started.
