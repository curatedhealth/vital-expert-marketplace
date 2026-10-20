# Worked example: A2 change read and B1 thesis review for Pear Therapeutics, Inc.

**Request (illustrative):** "Our memo on Pear Therapeutics is dated 1 September 2026. What changed since then, and does the thesis hold by our triggers?" Register: `examples/live/assumption_register_illustrative.csv` (ILLUSTRATIVE: memo date, owners and triggers written for the build; values at memo set equal to the saved outputs).

**Data:** live library outputs saved on 19 October 2026 by earlier builds, copied to `examples/live/` (read 20 October 2026): `diligence_deltas_Akili_Pear.json` (`get_deltas`, since 1 January 2026), `funding_signals_pear.json`, `evidence_maturity_K191716_somnio.json`. The connector was disconnected during this build; no new call was made. A live run would call `get_deltas` with `since: "2026-09-01"`. Script output: `examples/live/thesis_check_pear_output.md`.

## Answer (short mode)

**Answer.** As of 20 October 2026, by your triggers: 0 assumptions with the rule met, 3 not met, 2 not measurable or not comparable. The read is limited by the change log: it began on 12 October 2026, after your memo date, so "no change recorded" says nothing about 1 September to 12 October 2026 (T5).

| Id | Assumption | At memo | Now | Rule met | Owner | Reread | Flags |
|---|---|---|---|---|---|---|---|
| 1 | No new recall or safety event | 0 | 0 (get_deltas; log began 12 October 2026, last sweep 19 October 2026) | not met | Maria Chen | 15 January 2027 | T5 |
| 2 | Evidence maturity at or above 60 | 67 | 67 (rubric v1, 7 October 2026) | not comparable | Tom Avery | not given | T2, T4 |
| 3 | No new Form D | 5 | 5 (D 4, D/A 1) | not met | owner not named | 15 January 2027 | T1 |
| 4 | No new SEC filing | 10 April 2023 | 10 April 2023 | not met | Priya Nair | 1 October 2026 | T6 |
| 5 | Revenue grows 30 percent a year | not given | not measurable | not measurable from the record | Maria Chen | 15 January 2027 | T3 |

**Limits on the read.** T5: the log cannot show 1 September to 12 October 2026; compare filings and authorizations by date for that period instead. Assumption 1's signal counts authorization, study, safety and filing changes together, so it is broader than the assumption. T4: rubric v1 is dated 7 October 2026, after your memo; the rubric at the memo was not recorded, so 67 against 67 is not a comparison. T3: no public record carries revenue; that needs your own data, labeled non-public.

**Rule changes since 1 September 2026** (only those touching regimes the memo flagged): Swiss IPG ordinance consultation ran to 5 October 2026 (DL-085); none of the HSR items falls after the memo date.

**For you to decide.** Whether a T5 gap needs a filing-by-date check; who owns assumption 3 (owner not named); a reread date for assumption 2; assumption 4's reread date (1 October 2026) is earlier than the read date.

**Company status (as read on 20 October 2026, `named-company-status.md`; SEC rows [WF]).** Chapter 11 filed 7 April 2023 (Pear 8-K, 7 April 2023, SP-156); Nasdaq delisting notice (Pear 8-K, 10 April 2023, SP-160); last EDGAR filing a Form 25-NSE of 2 May 2023, filed by Nasdaq and not in the store, which is not dissolution (SP-155, DL-144). All predate your memo, so assumption 4 stays "not met". Somryst's current FDA listing holder is Nox Medical (SP-167), not Pear.

Full version on request.

Calls made (saved, 19 October 2026): `diligence-dh.get_deltas {companies: ["Akili Interactive Labs, Inc.", "Pear Therapeutics, Inc."], since: "2026-01-01"}`; `diligence-dh.get_funding_signals {company: "Pear Therapeutics, Inc."}`; `diligence-dh.get_evidence_maturity {company: "K191716"}`; `scripts/thesis_check.py`. Research rows read 20 October 2026, no call.

Thesis review draft for the owner. Not investment advice. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Word count: `python3 scripts/thesis_check.py --words ANSWER.md` on the answer above (it drops the calls list and the Source columns, and counts the record line); cut in the house order if it prints "over".

## What the run showed

- The script's T5 flag compares the log's first entry with the memo date; it applies to any memo dated before the log's first entry (12 October 2026 in the saved run).
- The evidence maturity rubric is dated after many memos; a memo that did not record the rubric cannot be compared (T4).
- `list_sources` has no saved output: needs a live check (BUILD_NOTES).
