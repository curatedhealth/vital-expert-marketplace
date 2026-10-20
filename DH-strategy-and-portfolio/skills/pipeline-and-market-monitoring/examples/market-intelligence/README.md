# Files for task A3 Market intelligence quality check

| File | Origin | What it is |
|---|---|---|
| `list_schemes_2026-10-19.json` | Copied unchanged from `/mnt/user-data/outputs/payer-engagement-and-hta-submission/examples/live/list_schemes_2026-10-19.json` (saved 19 October 2026, read 20 October 2026) | `market-access-dh.list_schemes {}`: scheme postures and load dates, the payers-lane perimeter |
| `screen_commercial_peers_dtx_somryst.json` | Copied unchanged from `/mnt/user-data/outputs/gtm-positioning-monitoring/examples/live/screen_commercial_peers_dtx_somryst.json` via `market-and-target-screening/examples/live/` (saved 19 October 2026) | Somryst device row and "absence from the store is not evidence of absence from the scheme" |
| `ecosystem_map_insomnia_ILLUSTRATIVE.csv` | Written for this skill on 20 October 2026 from the worked A3 example in `market-and-target-screening` (this pack). ILLUSTRATIVE: the last row (a vendor market size with no source) was added to show a failed element | Input for `scripts/monitor_helpers.py mi-check` |
| `mi_check_insomnia_ILLUSTRATIVE.txt` | Output of `python3 scripts/monitor_helpers.py mi-check examples/market-intelligence/ecosystem_map_insomnia_ILLUSTRATIVE.csv --as-of 2026-10-20 --max-age-days 60 --lanes "Buyers,Payers,Peers,Rules" --jurisdictions "US,DE"`, run 20 October 2026 (rerun 20 October 2026 after the notes block was added). The 60-day age and the lanes are a tester's rule, not a recommendation | The check result |
