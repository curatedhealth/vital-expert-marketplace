# Saved library outputs used by task A3 Market intelligence map

The VITAL Digital Health Library connector was not available when task A3 was added (20 October 2026). Each file here is a live response saved on 19 October 2026 by an earlier build, copied unchanged and read on 20 October 2026.

| File here | Copied from | What it shows |
|---|---|---|
| `list_schemes_2026-10-19.json` | `/mnt/user-data/outputs/payer-engagement-and-hta-submission/examples/live/list_schemes_2026-10-19.json` | `market-access-dh.list_schemes {}` (trimmed by the earlier build): DE_DIGA 82 listings "partial", FR_PECAN 2 "gold", FR_LPPR 0 "gap", FR_LATM 2 "gold", UK_NICE_EVA 15 "partial", UK_NICE_HTG 2 "partial", UK_NICE_NHAP 0 "gap", US_CMS_DMHT 3 and US_CMS_RPM 4 "partial", with last load dates |
| `money_flow_somnio.json` | `/mnt/user-data/outputs/pricing-and-value-proposition/examples/live/money_flow_somnio.json` | `commercial-dh.map_money_flow {reference: "somnio", ...}` on roles a tester typed: echoes user, buyer and payer; DE_DIGA permanent listing, listed 22 October 2020, scheme identifier 00508; exhibit has no amounts and no direction of payment |
| `map_money_flow_reset.json` | `/mnt/user-data/outputs/account-growth-and-renewal/examples/live/map_money_flow_reset.json` | `commercial-dh.map_money_flow {reference: "DEN160018", ...}`: no listed product matches; CMS DMHT and RPM rows are code-level |

The peers lane uses the files already in `../live/` (`screen_market_dtx_via_peer_screen.json`, `screen_commercial_peers_dtx_somryst.json`, `diligence_screen_market_dtx_EU.json`).

Not saved by any build, so marked "needs a live check" in `references/tools.md`: `market-access-dh.search_listings` called directly with a product name, and `diligence-dh.list_sources`.
