# Worked example: A2 decision tracking, an insomnia DTx in Germany and France

Live library calls on 19 October 2026. Raw outputs in `examples/live/`; the script output is `decision_table_2026-10-19.md`. The person's own submission dates are an illustration supplied in `live/own_submissions_example.json`; the library cannot see submissions in review.

**Request:** "BfArM confirmed our DiGA application complete on 15 July 2026 and HAS acknowledged our PECAN file as complete on 1 September 2026. Where do we stand, and how have comparable products fared? Quick view please."

**Calls made**

1. `market-access-dh.list_schemes` (free): DE_DIGA 82 (partial), FR_PECAN 2, FR_LATM 2, FR_LPPR 0, UK_NICE_HTG 2.
2. `market-access-dh.find_scheme_precedents` `{scheme: "DE_DIGA", indication: "F51", limit: 10}`: 3 rows, all permanent.
3. `market-access-dh.find_scheme_precedents` `{scheme: "FR_PECAN", limit: 10}`: 2 rows (ODYSIGHT, Continuum+ Connect).
4. `market-access-dh.get_reimbursement_status` `{reference: "Continuum+ Connect", scheme: "FR_PECAN"}`: provisional, `ends_on` 22 September 2025, `days_to_stated_end` -392.
5. `market-access-dh.find_scheme_precedents` `{scheme: "FR_LATM", limit: 5}` and `{scheme: "UK_NICE_HTG", limit: 5}`: 2 rows each.
6. `scripts/decision_tracker.py live/*.json --as-of 2026-10-19 --own live/own_submissions_example.json --official`.

## Answer (short mode)

**Both clocks are at or past their statutory point; neither is a decision.**

- **BfArM:** three months from your completeness confirmation of 15 July 2026 ran to 15 October 2026 (`DE21`). The ordinance allows up to three more months in justified cases. Ask BfArM whether the extension applies. Silence is not a refusal.
- **HAS, PECAN:** the CNEDiMTS opinion is due within 60 days of a complete file, so by 31 October 2026 (`FR14`). If HAS lists missing items, you have 30 days or the request is deemed abandoned. If PECAN is granted, a 6-month LPPR filing clock starts on the decision (`FR14`).

**Comparables (library copy, retrieved 15 and 16 October 2026).**

| Product | Route | Status | Since | Note |
|---|---|---|---|---|
| somnio, HelloBetter Schlafen, somnovia | DiGA, F51 | Permanent | 22 October 2020, 18 December 2022, 28 October 2024 | Evidence behind each is on its directory page |
| ODYSIGHT | PECAN | Provisional | 28 November 2025 | No end date stored |
| Continuum+ Connect | PECAN | Provisional in the library | 23 September 2024 | Stated end 22 September 2025 has passed; the library has not updated it. Check the Journal officiel; do not read it as still covered |
| Sleepio | NICE HTG624 | Recommended | 20 May 2022 | Guidance row, not a product listing |

The library holds no CNEDiMTS opinions and no LPPR rows, so unfavorable PECAN opinions on comparable products cannot be shown here.

**Official context, not your odds.** BfArM, as of 9 September 2026: 254 applications, 62 listed, 29 refused, 131 withdrawn, 14 in review (`DE33`, `DE34`); withdrawals far exceed refusals. CNEDiMTS 2025: 5 PECAN requests, 1 favorable and 4 unfavorable (`FR23`); 69 percent of LPP requests suspended at least once for incompleteness (`FR24`).

**Not published.** BfArM does not name refused products or applicants (`DE32`) and does not publish actual review days.

**Record:** Uncleared draft, AI-assisted. Any letter to BfArM or HAS is a draft for the accountable owner (owner not named).

## What this example shows

- Own submissions come from the person's documents; the library sees only published listings.
- A stated end date in the past with a provisional status is a stale record, flagged and not interpreted.
- National figures sit in their own block, with period and the "not your odds" line.
