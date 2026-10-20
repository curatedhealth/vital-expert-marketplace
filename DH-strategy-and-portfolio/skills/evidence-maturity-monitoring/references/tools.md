# Tools: calls this skill uses, as measured by earlier builds

Connector: VITAL Digital Health Library (`mcp.vital.expert`), diligence suite `diligence-dh`. Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; free calls do not.

**How this file was built.** The connector was disconnected during this build (20 October 2026); no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by the dh-go-to-market builds, read on 20 October 2026, and copied into `examples/live/`. Where no saved output exists, the step is marked **needs a live check**.

This skill does not watch. It compares runs the person saved on two dates (or a saved run and a fresh one) with `scripts/maturity_diff.py`. No `watch_*` tool is called.

## diligence-dh.get_evidence_maturity (counted)

- **Saved calls:** `{company: "K191716"}` and `{company: "somnio"}` (`examples/live/evidence_maturity_K191716_somnio_2026-10-19.json`, from market-segmentation-and-gtm-strategy, read 20 October 2026).
- **Returned:** K191716 resolved to Pear Therapeutics, Inc. by FDA submission number, 67 (60 of 90), rubric v1 (7 October 2026), formula, component rules and inputs (clinical evidence 20 of 40: 3 product-linked studies, 2 completed interventional, 1 randomized, 0 with results posted), reimbursement and jurisdiction breadth not assessable, limits. somnio resolved to mementor DE GmbH, 33 (30 of 90), with two risk flags.
- **Use here:** rerun with exactly the same `company` argument as the earlier run, save the output with its date, and diff. A different reference (for example "Somryst" instead of "K191716") may resolve to the same company and cover different products; the script says so.
- **Pitfalls:** the trimmed saved output for somnio lacks the rubric version, the maximum per component and the excluded list; save full responses for monitoring. The limits say "US sources only" while a German maker's authorizations earn points (register P2 evidence). A rubric version change makes the two scores not comparable as a trend.
- **Needs a live check:** whether `rubric_version` changes are announced anywhere other than the response.

## diligence-dh.build_company_profile and diligence-dh.compare_portfolio (counted)

- **Saved:** `examples/live/build_company_profile_akili_2026-10-19.json` (Akili 100, 90 of 90; excluded reimbursement and jurisdiction breadth) and `examples/live/compare_portfolio_dtx_2026-10-19.json` (Pear 67, Big Health 56, Akili 100, GAIA AG, Deutschland 78; HelloBetter unresolved). Both embed the same score: "the same function produces the score in every tool" (compare_portfolio formula note).
- **Use here:** either may serve as one snapshot when it is what the person saved. `compare_portfolio` returns component points as "30/30" strings and no inputs, so the script compares points but not inputs; say so. The portfolio view itself belongs to `funding-and-portfolio-comparison` (this pack).

## diligence-dh.get_deltas (counted; owned by pipeline-and-market-monitoring)

- **Saved calls:** `{companies: ["Akili Interactive Labs, Inc.", "Pear Therapeutics, Inc."], since: "2026-01-01"}` and `{companies: ["Big Health, Inc.", "Akili Interactive Labs, Inc."], since: "2025-01-01"}` (`examples/live/diligence_get_deltas_*.json`, read 20 October 2026): "no change recorded" for all; log first entry 12 October 2026, last sweep 19 October 2026, limits quoted in `monitoring-signals.md` section 4.
- **Use here:** optional, only to date the record events behind an INPUT change found by the diff. Report its limits with every use. Ongoing change monitoring is `pipeline-and-market-monitoring` (this pack).
- **Pitfall:** events loaded before 12 October 2026 may have no log entry, so a change between two maturity runs can have no matching delta. For a period that starts before 12 October 2026, say the log does not cover it and offer the company's dated primary filings and authorization records instead of "no change".

## diligence-dh.list_sources (free)

- **Needs a live check:** no saved output. Use it at each rerun to record the perimeter beside the score; a COVERAGE change explains a score move with no new evidence.
- **Nearest saved evidence:** `examples/live/list_commercial_dh_sources_2026-10-19.json` (census counts and five sources not loaded, with reasons).

## verify.qualify_source, verify.check_claim, verify.build_record

- For a paper the person cites as new evidence: `qualify_source {doi}` then `check_claim` with the passage `{text, locator}` and the full qualify_source object; accept only a passage read in the same direction (register N3).
- `verify.build_record` refuses a record without a human `cleared_by.name`; call it only with the name of the person who clears the output.

## Company status (no library tool)

- No diligence-dh tool returns whether a company still exists, filed for bankruptcy, was delisted, deregistered or acquired; a score that holds steady says nothing about it. Use the status step in `company-status.md`.
- SEC pages refuse automated requests without a declared User-Agent contact (DL-153 [WF]). Ask which contact the person's organization uses; never send the person's email address or name and never invent a contact. Without one, list the filings to open and write "Status: [GAP]: not read".

## Safety events and recall flags

- Saved only in `compare_portfolio` (`examples/live/compare_portfolio_dtx_2026-10-19.json`, retrieved 19 October 2026): Pear Therapeutics, Inc. `safety_events` 2 and `risk_flags` "fda_recall: Class II on 2021-06-07" for reSET and reSET-O (truncated in the saved file; quote as saved); Big Health and Akili `safety_events: none_found` (none found in the loaded enforcement source; not proof of none). `get_evidence_maturity` and `build_company_profile` carry no safety field: never print 0 or none from their silence.

## Catalogue jobs

- `evidence-maturity` (named by the old skill): **needs a live check**; no saved job card. Monitoring is not a catalogue job: the method is in this skill's tasks.

## Not used here

- `diligence-dh.watch_companies` and every `watch_*` tool: never called.
- `diligence-dh.get_funding_signals`, `generate_report`, `screen_market`, `search_companies`: other skills in this pack.
