# Worked example: A1 code and price change tracking, US remote monitoring

Live library calls on 19 October 2026 (saved in `change_tracking_live_2026-10-19.json`). Shown so the model sees the shape of a good answer, not to be reused as current fact. A second section shows the A2 script on an invented sample, clearly labeled.

**Request:** "Our RPM program bills 99453, 99454 and 99457 through partner practices; our nurses are contracted from a monitoring vendor. Our plan was written in 2025 on a 16-day minimum. What has changed, and what is coming? Quick."

**Calls made**

1. `market-access-dh.list_schemes` (free): US_CMS_RPM 4 listings, loaded 15 October 2026.
2. `market-access-dh.find_scheme_precedents {scheme: "US_CMS_RPM", limit: 25}`: 99453, 99454, 99457, 99458 with CY 2026 amounts in the passages.
3. `market-access-dh.get_status_history {reference: "99454", scheme: "US_CMS_RPM"}`: one day-zero snapshot (15 October 2026); no history.
4. `market-access-dh.search_listings {query: "99445", country: "US"}`: nothing stored.
5. `commercial-dh.get_deltas {reference: "deprexis", since: "2026-01-01"}` (a test of the delta feed): the Market Access delta tool "is not on that server". The library cannot report code changes; the publication calendar does.

## Answer (short mode)

**What moved.** Since 1 January 2026 your 16-day assumption is out of date: CMS added 99445 (device supply, 2 to 15 days of data) and 99470 (first 10 minutes of management), and 99454 now covers 16 to 30 days; the short and long codes are alternatives, never billed together (US2, US4; CY 2026 final rule, published 5 November 2025). What is coming matters more for your model: the CY 2027 proposed rule (published 16 July 2026; comments closed 14 September 2026; final rule not published as of 19 October 2026) would pay RPM time only when furnished by clinical staff employed by the billing practice, with no contracting out to third-party companies, from 1 January 2027 (US25).

**Tracked codes today** (library rows, national, before geographic adjustment, CMS PFS indicators for 2026 per the library, retrieved 15 October 2026):

| Code | Today | Baseline | Change |
|---|---|---|---|
| 99453 | 21.71 USD | Not given | Change date `[GAP]`: library holds one snapshot |
| 99454 | 52.11 USD; now 16 to 30 days | 16-day minimum | Definition changed 1 January 2026 (US2) |
| 99457 | 51.77 non-facility, 26.39 facility | Not given | `[GAP]` |
| 99445, 99470 | New in 2026; not stored in the library | Not in plan | New codes (US2) |

**Proposed, not law.** US25 staffing (above). US24 initiation in a face-to-face visit. US26 device codes judged overvalued, revaluation by crosswalk. US27 comment solicitation on replacing 17 codes with four monthly G-codes.

**What it means for you.** If US25 is finalized as proposed, time your contracted nurses furnish stops counting toward billable RPM from 1 January 2027. Your contract with the vendor and with partner practices would need review: that is the coding and contracting skill's work (DH-03.01.2.1), and the decision is the accountable owner's.

**Check.** The CY 2027 final rule when published; your partner practices' remittances for any 2026 short-duration claims.

**Record.** Uncleared draft.

## A2 on an invented sample (not live data)

`contract_sample.csv` and `contract_rules_sample.json` are invented for testing the script. `contract_performance_sample_output.txt` shows the result: for the German row, denial rate 0.05 (rule 0.05: pass), realization 0.9614 against a 0.98 rule (miss, stall point price realization), outcome attainment 0.75 against 0.8 (miss); the statutory volume floors are shown labeled "statutory minimum from 1 January 2027 (not your contract)".

## Why this is a good answer

It separates the change in force from the proposal and dates both. It refuses to invent a change date the library cannot show. It ties the proposal to the person's own staffing model, which is the consequence they need, and routes the response to the sibling skill instead of redesigning the contract.
