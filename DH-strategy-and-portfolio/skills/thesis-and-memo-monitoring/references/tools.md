# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; free calls do not.

**How this file was built.** The connector was disconnected during this build (20 October 2026), so no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, copied into `examples/live/` (file named on each entry, read 20 October 2026), and from those builds' `tools.md` files. Where a tool has no saved output, it is described from the old skill text only and the step is marked **needs a live check**.

## diligence-dh.get_deltas (counted)

- Arguments: `companies` (1 to 12 references), `since` (YYYY-MM-DD).
- Saved: `diligence_deltas_Akili_Pear.json` (`{companies: ["Akili Interactive Labs, Inc.", "Pear Therapeutics, Inc."], since: "2026-01-01"}`) and `diligence_get_deltas_BigHealth_Akili.json` (`{companies: ["Big Health, Inc.", "Akili Interactive Labs, Inc."], since: "2025-01-01"}`). Every company: "no change recorded", `change_count` 0. Log: first entry 12 October 2026 23:34 UTC, last entry 16 October 2026 11:14 UTC, last sweep 19 October 2026 09:42 UTC. Limits verbatim: "the since filter uses event dates (filing signal_date, authorization decision_date, study start_date, safety event_date), not observed_at (load time)"; "the change log began on the first_entry_at date; older clearances loaded before the log existed may have no entries"; "no change recorded is a statement about in-window event-dated log rows up to last_sweep_at".
- Use in A2: always quote the log start and last sweep beside "no change recorded". A `since` date earlier than the log start gives no assurance for the earlier period (flag T5). No watch is needed.
- Pitfalls: `commercial-dh.get_deltas` drops this log block and reports "market_access_dh.get_deltas is not on that server" (register C12, saved in the commercial builds); use the diligence tool. The old skill text says: "State when the watch has no later sweep. Do not invent an event."

## diligence-dh.watch_companies (described only, never called)

- Old skill text: "Register a watch on 1 to 12 companies and return the snapshot hash. since is ignored on the write. One watch per tenant."
- Never called by this skill. Monitoring is by dated reruns the person keeps. Watches elsewhere in the library are not separated by customer key (register N2), and one watch per tenant would overwrite the person's colleagues' watch.

## diligence-dh.get_funding_signals (counted)

- Argument: `company`. Saved: `funding_signals_pear.json` (`{company: "Pear Therapeutics, Inc."}`, 19 October 2026): SEC 46 filings (8-K 25, 10-Q 6, D 4, S-4/A 3, 10-K 2, S-1 2, 8-K/A 1, S-4 1, D/A 1, S-1/A 1), 9 February 2016 to 10 April 2023; NIH 6; EU TED none found; private rounds `[GAP]`.
- Use in A2: compare counts by type and the latest date with the run saved at the memo date. A new row is reported by type and date with its URL.
- Pitfalls: no 8-K item number, `counterparty` null (register P5); `sum_of_stated_amounts` mixes types and is never quoted as money raised; the latest filing date is not a status, and nothing is inferred from a filing gap. Company status comes from the step in `monitoring-signals.md` section 6 (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; registers), or is `[GAP]`: not read. Whether the library loads Form 25 or Form 15 needs a live check. Automated sec.gov reads need a declared User-Agent contact (DL-153): ask which contact the person's organization uses; never the person's email address or name, never an invented one.

## diligence-dh.get_evidence_maturity (counted)

- Argument: `company`. Saved: `evidence_maturity_K191716_somnio.json`: `K191716` resolved to Pear Therapeutics, Inc., 67 (60 of 90), rubric v1 (7 October 2026), components regulatory status 30 of 30, clinical evidence 20 of 40, active development 0 of 10, product breadth 10 of 10; limits "a stated convention for comparing documented evidence, not a predictive model or a valuation" and "US sources only; absence of EU, UK or Swiss data lowers nothing and proves nothing".
- Use: compare score and components with the earlier run only on the same rubric version; report the component that moved and its input. Over time, with a named framework: `evidence-maturity-monitoring` (this pack).
- Pitfalls: company level; registered studies only; EU authorizations earn points under a "US sources only" note.

## diligence-dh.build_company_profile (counted)

- Argument: `company` (exact). Saved: `partner_profile_akili.json` (19 October 2026): EndeavorRx DEN200026 15 June 2020, K231337 13 December 2023, EndeavorOTC K233496 14 June 2024 (QFT, 882.5803); 10 studies; Form D 9 June 2021 USD 110,000,007 and 23 May 2018 USD 55,000,010; evidence maturity 100.
- Use in A2 when the memo predates the change log: compare authorizations and Form D rows by date with the memo's fact base.
- Pitfalls: `status` "DENG" (register C3); `funding` `[GAP]` beside Form D rows (register C2); no marketing status.

## diligence-dh.compare_portfolio (counted, only for a thesis that names peers)

- Saved: `compare_portfolio_dtx_2026-10-19.json` (Pear 67 with two Class II recall flags dated 7 June 2021; Big Health, Inc. 56; Akili 100). Several holdings at once: `investment-portfolio-monitoring` (this pack).

## diligence-dh.list_sources (free) (needs a live check)

- No saved output. Old skill text: "Every source with credential state, last load, and row counts. A source not loaded states the reason." Until checked, use the `source_coverage` block of `compare_portfolio` (not loaded: Companies House, Zefix, private funding, the DiGA directory feed for Diligence, NICE).

## verify.build_record (counted)

- Saved: `verify_build_record_refusal.json`: `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name". Call only when the output leaves the conversation and the person names the clearer.

## Catalogue jobs

- Saved `list_jobs_commercial.json` lists the Diligence job `company-dossier` (build_company_profile, generate_report, get_funding_signals). The old menu put Watch companies and Read company changes under `market-screen`; no saved output shows its steps (**needs a live check**). `start_job` returns steps and runs nothing (register C12). No job is started here.

## Not used here

- `watch_companies` and every `watch_*` tool.
- `diligence-dh.generate_report`, `screen_market`, `search_companies`: sibling skills.
