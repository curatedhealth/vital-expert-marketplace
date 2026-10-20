# Worked example: A2 change read on an illustrative holdings list and saved live library data

**Request (illustrative):** "Here's our holdings list (attached). Anything new in the public record as of 20 October 2026? Tomas reviews it."

**Data:** `examples/sample-data/holdings_illustrative.csv` (ILLUSTRATIVE: real company names in the library, invented holdings, owners and dates); two `diligence-dh.get_deltas` calls made live on 19 October 2026 by earlier builds (`examples/live/diligence_deltas.json`, since 1 January 2026; `examples/live/diligence_get_deltas_BigHealth_Akili.json`, since 1 January 2025), read on 20 October 2026. The connector was disconnected during this build, so GAIA AG was not read. Table from `python3 scripts/portfolio_watch.py deltas examples/sample-data/holdings_illustrative.csv examples/live/diligence_deltas.json examples/live/diligence_get_deltas_BigHealth_Akili.json --as-of 2026-10-20`.

---

**Answer.** As of 20 October 2026 the library's log recorded no change for Akili, Pear or Big Health, but it only covers 12 October to 19 October 2026, while your windows start in 2025 or January 2026. GAIA AG was not read, and Pear has no owner and a reread date already reached.

| Holding | Window asked | Library answer | Covered by the log | Owner | Reread date | Flags |
|---|---|---|---|---|---|---|
| Akili (seed follow-on) | from 1 January 2026 | no change recorded | 12 to 19 October 2026 | Tomas Berg | 15 November 2026 | W1 |
| Pear assets (secondary) | from 1 January 2026 | no change recorded | 12 to 19 October 2026 | owner not named | 1 October 2026 | W1, W3, W5 |
| Big Health (observer seat) | from 1 January 2025 | no change recorded | 12 to 19 October 2026 | Tomas Berg | not given | W1, W4 |
| GAIA AG (prospect) | from 1 July 2026 | not read | none | Ana Ruiz | 1 December 2026 | W2 |

Source: library change log, retrieved 19 October 2026. Flags: W1 window starts before the log began; W2 not read; W3 owner not named; W4 reread date not given; W5 reread date reached.

**Before the log began.** The library change log began on 12 October 2026, so it says nothing about your windows from 1 January 2025 or 1 January 2026 to 11 October 2026; that span is not "no change". As returned, "no change recorded is a statement about in-window event-dated log rows up to last_sweep_at". For that span, the dated primary filings: Pear's saved funding signals (19 October 2026) hold SEC filings up to 10 April 2023, the latest filing in the store and not a statement about the company today.

**Status, as read on 20 October 2026 (`named-company-status.md`; SEC rows [WF]; all before your windows).** Akili: became a subsidiary of Virtual Therapeutics (Akili 8-K, 2 July 2024, SP-151); Form 15, 12 July 2024, not dissolution (SP-154). Pear: chapter 11 (Pear 8-K, 7 April 2023, SP-156); last filing Form 25-NSE, 2 May 2023, not dissolution (SP-155); Somryst now listed with FDA by Nox Medical, reSET and reSET-O by Harvest Bio (SP-167, SP-169). Big Health: no SEC registrant found (SP-162). GAIA AG: `[GAP]`: not read.

**Outside the library.** UK filings (Companies House not loaded), the HHS breach portal (not among the loaded sources; check the 24-month list and the archive, DL-096), and private rounds. These are your direct reads.

**Against an earlier run.** None attached, so no diff was run.

**Gaps and asks.** Who owns Pear? What reread date do you want for Big Health? For GAIA AG, run the read with its legal name once the library is reachable.

Full version on request.

**Calls made:** `diligence-dh.get_deltas` (two calls, 19 October 2026, saved). None new; research rows read 20 October 2026.

Portfolio change read draft for Tomas Berg. AI-assisted. Clears it: Tomas. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

Word count of the answer body (between the two rules, table included, without the table's source and flag-key line and the calls list, record line included): 428, counted with `python3 scripts/portfolio_watch.py words examples/change-read-holdings.md`.

**Diff demonstration (illustrative):** `python3 scripts/portfolio_watch.py diff examples/live/compare_portfolio_dtx_2026-10-19.json examples/sample-data/compare_portfolio_later_illustrative.json` prints two field changes (Akili `safety_events` none_found to 1; Big Health `evidence_maturity.components.active_development` 0/10 to 10/10). The "later" file was edited by hand for the demonstration and is not library output.
