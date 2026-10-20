# Worked example: A1 change read and A2 rule movement, two DTx pipeline names

Built on 20 October 2026 from live library outputs saved on 19 October 2026 by earlier builds (the connector was not available on 20 October 2026; origins in `examples/live/README.md`). The request and the person are illustrative; the records are as the library returned them. A rerun on a live connector should repeat step 1, which needs a live check.

**Request.** "Akili and Pear are on our pipeline. Anything new on either since 1 January 2026? And did any deal rules change this year that we should know about for US and EU deals?"

**Calls (as saved).**
1. `commercial-dh.list_commercial_dh_sources {}` (stand-in for `diligence-dh.list_sources`, not saved; same census), 19 October 2026.
2. `diligence-dh.get_deltas {companies: ["Akili Interactive Labs, Inc.", "Pear Therapeutics, Inc."], since: "2026-01-01"}`, 19 October 2026.
3. Scripts: `python3 -I scripts/monitor_helpers.py deltas examples/live/diligence_deltas_Akili_Pear.json`; `python3 -I scripts/monitor_helpers.py rules --since 2026-01-01`.

---

## Answer (short mode)

The library's change log records no change for Akili Interactive Labs, Inc. or Pear Therapeutics, Inc. since 1 January 2026. That is a statement about the log, not about the companies: the log began on 12 October 2026, so changes dated before then may be missing, and it filters on event dates, not load dates (last sweep 19 October 2026).

**No change recorded (log caveat).** Akili Interactive Labs, Inc.; Pear Therapeutics, Inc. Log first entry 12 October 2026, last sweep 19 October 2026; "no change recorded is a statement about in-window event-dated log rows up to last_sweep_at".

**Before the log (1 January to 11 October 2026).** Not covered by the log, so not "no change". The store's dated rows cover it: filing dates and types through `diligence-dh.get_funding_signals` and authorization decision dates through `diligence-dh.build_company_profile`. Pear's latest filing in the store is an 8-K of 10 April 2023 (46 SEC rows from 9 February 2016, `funding_signals_pear.json`); Akili's are not saved here. Run them on request.

**Status (as read on 20 October 2026, `named-company-status.md`; SEC rows [WF]).** Akili (registrant Akili, Inc., SP-148): merger completed and change in control to Virtual Therapeutics Corporation (Akili 8-K, 2 July 2024, SP-151); Form 15, 12 July 2024, which is not dissolution (SP-154; DL-149 (inference)). Pear: chapter 11 (Pear 8-K, 7 April 2023, SP-156); Nasdaq delisting notice (Pear 8-K, 10 April 2023, SP-160); last filing Form 25-NSE, 2 May 2023, not dissolution (SP-155, DL-144); no later 1.03(b) report, so the outcome is open on EDGAR (DL-137 (inference)). Both predate your window; nothing filed after 20 October 2026 is covered.

**Not loaded.** Companies House, the DiGA directory feed, NICE, private funding.

**Rule changes after 1 January 2026 (for the owner you name for legal questions; not applied to any deal here).**

| Date | Change | Rows | Status |
|---|---|---|---|
| 12 February 2026 | New HSR form vacated; FTC accepts the pre-February 2025 form | DL-051 to DL-053 | Litigation pending |
| 17 February 2026 | HSR 2026 thresholds apply (size of transaction USD 133.9 million) | DL-044 to DL-049 | In force; revised every year |
| 25 March 2026 | FTC request for comment; new rulemaking considered | DL-054 | Status after 26 May 2026 not found `[GAP]` |
| 17 June 2026 | EU Regulation 2026/1386 adopted; applies from 17 January 2028; 2019/452 governs until then | DL-074, DL-075 | Adopted, not yet applicable |
| 27 July 2026 | AI Act Omnibus in force; high-risk obligations from 2 December 2027 and 2 August 2028 | EU-17 to EU-19 | In force; obligations dated |

**Hypotheses for review.** None: no change was recorded, and no trigger was given. If you set triggers, B1 checks the pipeline against them.

Full version on request.

Calls made: listed above (one counted `get_deltas` call, one free perimeter call). No watch set.

Change read draft. No watch set. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

## Notes for the builder

- No SEC contact was given for this run, so no EDGAR page was opened in it (DL-153 [WF]). Status comes from the research rows read on 20 October 2026 (`references/named-company-status.md`, SP-148 to SP-160); status is never taken from press or memory.
- The rule list is the script's output filtered to the rows that touch US and EU deals; the Swiss, UK and DiGA rows were left out because the request named US and EU.
- `commercial-dh.get_deltas` for Pear returned no events and no log block (`examples/live/commercial_get_deltas_Pear.json`); the script prints "Log block missing" for it, which is why A1 uses the diligence tool.
