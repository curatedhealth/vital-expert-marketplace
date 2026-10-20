# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; free calls do not.

**How this file was built.** The connector was disconnected during this build (20 October 2026), so no call was made for this skill. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, read on 20 October 2026 and copied unchanged into `examples/live/` (origins in `examples/live/SOURCES.md`). A step marked **needs a live check** rests on a description, not on a saved output. Counted calls in this build: 0.

This competency runs mostly on the person's own holdings list and their saved earlier runs. The library adds what changed in the public record for named companies, a rerun of the comparison to set beside an earlier run, filings by type, a ranking calculator for follow-up work the person scored, and the record. It holds no portfolio, no valuation, no company financials and no investor data.

## diligence-dh.get_deltas (counted): task A2

- **Arguments:** `companies` (1 to 12 references), `since` (YYYY-MM-DD).
- **Saved calls:** `{companies: ["Akili Interactive Labs, Inc.", "Pear Therapeutics, Inc."], since: "2026-01-01"}` (`examples/live/diligence_deltas.json`) and `{companies: ["Big Health, Inc.", "Akili Interactive Labs, Inc."], since: "2025-01-01"}` (`examples/live/diligence_get_deltas_BigHealth_Akili.json`), both 19 October 2026. Every company: "no change recorded", `change_count` 0.
- **The log block, as returned:** first entry 12 October 2026, last entry 16 October 2026, last sweep 19 October 2026; limits: "the since filter uses event dates (filing signal_date, authorization decision_date, study start_date, safety event_date), not observed_at (load time)"; "the change log began on the first_entry_at date; older clearances loaded before the log existed may have no entries"; "no change recorded is a statement about in-window event-dated log rows up to last_sweep_at".
- **Pitfalls:**
  - A window that starts before 12 October 2026 is not fully covered by the log: both saved windows (1 January 2025, 1 January 2026) start before it. `scripts/portfolio_watch.py deltas` flags this (W1). Say "no change recorded in the library's log from 12 October 2026 to the last sweep on 19 October 2026", never "nothing happened".
  - No watch is needed for `get_deltas`; the old skill's "Watch companies" is described only and never called here.
  - The shape of a response with changes was not seen in any saved output: **needs a live check**. Report each change as returned, with its event date and source.
  - `commercial-dh.get_deltas` drops this log block and reports "market_access_dh.get_deltas is not on that server" (register C12); use the diligence tool.
- **Use:** `python3 scripts/portfolio_watch.py deltas HOLDINGS.csv DELTAS.json [more] --as-of YYYY-MM-DD`.

## diligence-dh.compare_portfolio (counted): task A2, reruns

- **Saved calls:** `examples/live/compare_portfolio_dtx_2026-10-19.json` (19 October 2026): Pear Therapeutics, Inc. (queried as Somryst) 67, Big Health, Inc. 56, Akili 100, GAIA AG, Deutschland (queried as deprexis) 78, HelloBetter unresolved.
- **Use for monitoring:** rerun with the same company list as the person's earlier saved run and compare with `python3 scripts/portfolio_watch.py diff EARLIER.json LATER.json`. Runs with different company lists are compared only for the companies in both; the rest are "not comparable".
- **Pitfalls:** company level (a brand carries its maker's flags); exact matching (HelloBetter unresolved); `funding_signal_counts` absent on some rows; reimbursement `not_assessable` for every row; the evidence maturity score is rubric v1 (7 October 2026): a score change after a rubric change is a rubric change, not a company change. Score drift is read by `evidence-maturity-monitoring` (this pack).

## diligence-dh.get_funding_signals (counted): task A2, new filings by type

- **Saved call:** `{company: "Pear Therapeutics, Inc."}` (`examples/live/funding_signals_pear.json`, 19 October 2026): 46 SEC filings dated 9 February 2016 to 10 April 2023 (8-K 25), NIH 6, EU TED none found, private rounds "[GAP]".
- **Use for monitoring:** compare filing counts by type and the latest date with the person's earlier saved run. A new 8-K says an event was reported; the item is not in the row (`counterparty` null, no item number): open the filing URL before saying what it reports.
- **Pitfalls:** `sum_of_stated_amounts` adds different filing types; never quote it. The latest filing date is not a statement about the company today. For a W1 window, report the SEC date range as "filings in the store up to DATE (latest filing in the store, not a statement about the company today)"; for Pear, none after 10 April 2023.

## analytics.rice (counted): task B1, only on follow-up work the person scored

- **Saved call** (`examples/live/rice_confidence_percent.json`, 19 October 2026, illustrative inputs typed for the measurement): four initiatives; scores 540, 200, 150 and 133.33. Method "RICE Prioritization (Reach x Impact x Confidence / Effort)".
- **Pitfalls:** confidence is read as a percent: send 80, not 0.8; a fraction gives scores 100 times too small with no warning (register N5). Impact 1.5 was accepted although the tool description allows only 0.25, 0.5, 1, 2 or 3 (description as recorded in `channel-and-partner-design/references/tools.md`, 19 October 2026; the saved file's note says 1.5 "was sent on purpose to test validation; it was accepted"); check impact values before the call.
- Never call it with proposed values. It ranks follow-up work, never holdings.

## Catalogue jobs

- No saved job covers investment portfolio monitoring. The old files name `market-screen` for "Watch companies" and "Read company changes" (folded into `pipeline-and-market-monitoring`, this pack) and `portfolio-comparison` for "Compare a portfolio" (folded into `funding-and-portfolio-comparison`, this pack). Whether a monitoring job exists: **needs a live check** (`find_job {query: "portfolio monitoring"}`).

## verify.build_record (counted)

- Needs a named human in `cleared_by.name`; `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name" (`examples/live/verify_build_record_refusal.json`). Call it only when an output leaves the conversation and the person names who clears it.

## Direct SEC and register reads (status step)

- The library holds the CIKs and form types it lists only. A parent, successor or listed registrant (other CIK) and forms such as 15-12G, 25-NSE or SC 13D may be missing. When the log or the store does not cover the window or the status question, say so and name EDGAR company search as the person's direct read (`references/company-status.md`).
- The EDGAR submissions record gives current and former names, exchanges and tickers, needs no API key, and holds at least one year or 1,000 recent filings (DL-150 to DL-152, [WF]).
- If EDGAR is read directly, the User-Agent contact is one the person's organization gives and approves, never the user's email address, name or any account identifier; SEC caps automated access at 10 requests per second (DL-153, [WF]). With no contact given, send nothing and list the filings to open. Never invent a contact.
- Companies House and Zefix are not loaded in the library (19 October 2026); Companies House `company_status` is the person's direct read (DL-157 to DL-161). German insolvency notices: insolvenzbekanntmachungen.de (DL-165 to DL-167).

## Not in the library (the person checks the source)

- The HHS OCR breach portal (DL-095 to DL-098): not listed among the loaded sources in any saved output. A breach check is the person's direct read of the portal, both the 24-month list and the archive (DL-096).
- Companies House (UK filings) and Zefix: not loaded ("API key not yet provisioned", "credentials not available", 19 October 2026).
- Any funding source for private rounds: not loaded.

## Not used here

- `diligence-dh.watch_companies` and every `watch_*` tool: never called.
- `diligence-dh.get_evidence_maturity` over time: `evidence-maturity-monitoring` (this pack).
- `diligence-dh.generate_report`: `investment-memo-and-decision-record` (this pack).
