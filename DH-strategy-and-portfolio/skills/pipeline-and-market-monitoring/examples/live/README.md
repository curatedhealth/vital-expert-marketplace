# Saved library outputs used by this skill

The VITAL Digital Health Library connector was not available when this skill was built (20 October 2026). Every file here is a live response saved on 19 October 2026 by an earlier build, copied unchanged and read on 20 October 2026. Each line names the file it was copied from.

| File here | Copied from | What it shows |
|---|---|---|
| `diligence_deltas_Akili_Pear.json` | `channel-and-partnership-monitoring/examples/live/diligence_deltas.json` | `diligence-dh.get_deltas {companies: ["Akili Interactive Labs, Inc.", "Pear Therapeutics, Inc."], since: "2026-01-01"}`: no change recorded for both; log first entry 12 October 2026, last sweep 19 October 2026, three limits |
| `diligence_get_deltas_BigHealth_Akili.json` | `market-segmentation-and-gtm-strategy/examples/live/diligence_get_deltas_BigHealth_Akili.json` | Same tool, `since: "2025-01-01"`, Big Health and Akili: no change recorded; same log |
| `commercial_get_deltas_Pear.json` | `market-segmentation-and-gtm-strategy/examples/live/commercial_get_deltas_Pear.json` | `commercial-dh.get_deltas`: no events; log block dropped; Market Access feed "not on that server" |
| `screen_dtx_limit8_trimmed.json` | `channel-and-partner-design/examples/live/peer_screen_dtx.json` | `screen_market` block (through `screen_commercial_peers {segment: "dtx", limit: 8}`), trimmed: 8 of 18, products kept for Akili only |
| `screen_dtx_limit10.json` | `gtm-positioning-monitoring/examples/live/screen_commercial_peers_dtx.json` | `screen_market` block (through `screen_commercial_peers {segment: "dtx", limit: 10}`): 10 of 18 with full rows |
| `list_commercial_dh_sources.json` | `market-segmentation-and-gtm-strategy/examples/live/list_commercial_dh_sources.json` | The diligence census loaded and not loaded, with reasons (stand-in for `diligence-dh.list_sources`, not saved) |
| `funding_signals_pear.json` | `channel-and-partner-design/examples/live/funding_signals_pear.json` | `diligence-dh.get_funding_signals {company: "Pear Therapeutics, Inc."}`: 46 SEC filings, 9 February 2016 to 10 April 2023, no 8-K item numbers |
| `verify_build_record_refusal.json` | `market-segmentation-and-gtm-strategy/examples/live/verify_build_record_refusal.json` | `verify.build_record` refuses a non-human clearer |

The illustrative later screen used to test `scripts/monitor_helpers.py screen-diff` is in `evals/files/screen_dtx_limit10_later_illustrative.json`; it is labeled illustrative in its first key and changes no real company's record.

Steps that rest on a call with no saved output are marked "needs a live check" in `references/tools.md`.
