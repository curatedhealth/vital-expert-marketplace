# Saved library outputs used by this skill

The VITAL Digital Health Library connector was not available when this skill was built (20 October 2026). Every file here is a live response saved on 19 October 2026 by an earlier build, copied unchanged and read on 20 October 2026. Each line names the file it was copied from.

| File here | Copied from | What it shows |
|---|---|---|
| `diligence_screen_market_dtx_EU.json` | `market-segmentation-and-gtm-strategy/examples/live/diligence_screen_market_dtx_EU.json` | `diligence-dh.screen_market {segment: "dtx", jurisdiction: "EU", limit: 10}`: one company, the perimeter block and a DiGA source contradiction |
| `screen_market_dtx_via_peer_screen.json` | `gtm-positioning-monitoring/examples/live/screen_commercial_peers_dtx.json` | The `screen_market` block inside `commercial-dh.screen_commercial_peers {segment: "dtx", limit: 10}`: 10 of 18 matches, all US, with products, authorizations, studies, safety events and evidence maturity scores |
| `list_commercial_dh_sources.json` | `market-segmentation-and-gtm-strategy/examples/live/list_commercial_dh_sources.json` | The diligence census sources loaded and not loaded, with reasons (the same census `diligence-dh.list_sources` reports; that call itself was not saved) |
| `search_companies_and_guidance_other_calls.json` | `channel-and-partner-design/examples/live/other_calls.json` | `diligence-dh.search_companies {segment: "rpm", limit: 10}` returned 0; `diligence-dh.retrieve_guidance {query: "anti-kickback safe harbor"}` returned no passage |
| `mcda_illustrative_partnership_screen.json` | `channel-and-partner-design/examples/live/job_partnership_screen.json` | `analytics.mcda` on ILLUSTRATIVE scores (Big Health 70, Akili 62.5, Click 60) and the HTTP 400 on a missing score. The scores are not anyone's assessment of these companies |
| `verify_build_record_refusal.json` | `market-segmentation-and-gtm-strategy/examples/live/verify_build_record_refusal.json` | `verify.build_record` refuses a record without a human `cleared_by.name` |

Steps that rest on a call with no saved output are marked "needs a live check" in `references/tools.md`.

Added for the A2 eval and record checks (same origin and dates):

| File here | Copied from | What it shows |
|---|---|---|
| `partner_profile_akili.json` | `channel-and-partner-design/examples/live/partner_profile_akili.json` | `diligence-dh.build_company_profile {company: "Akili Interactive Labs, Inc."}`: EndeavorRx DEN200026 (15 June 2020) and K231337, EndeavorOTC K233496; two Form D rows (9 June 2021, USD 110,000,007; 23 May 2018, USD 55,000,010) while `funding` reads `[GAP]` |
| `screen_commercial_peers_dtx_somryst.json` | `gtm-positioning-monitoring/examples/live/screen_commercial_peers_dtx_somryst.json` | Somryst device row: Pear Therapeutics, Inc., 510(k) K191716, QVO, 882.5801, decision 23 March 2020, FDA URL |
