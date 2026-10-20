# Eval files

- `screen_dtx_limit10_earlier.json`: a live `screen_market` block saved on 19 October 2026 (copy of `examples/live/screen_dtx_limit10.json`).
- `screen_dtx_limit10_later_illustrative.json`: ILLUSTRATIVE, written for the build on 20 October 2026. Same arguments; one fictional company ("Example Therapeutics (illustrative)") added and `total_matches` set to 19, so the tenth real company drops past `limit: 10`. No real company's record was changed. It tests that a company "not returned" is read against `total_matches` and `limit`, not as an exit.
- `ecosystem_map_insomnia_ILLUSTRATIVE.csv`: ILLUSTRATIVE, written on 20 October 2026 from the worked A3 example in `market-and-target-screening` (this pack); the vendor market size row has no source or date by design. Copy of `examples/market-intelligence/ecosystem_map_insomnia_ILLUSTRATIVE.csv`. Used by eval 5 (A3).
