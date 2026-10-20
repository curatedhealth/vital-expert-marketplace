# Worked example: A2 investment portfolio comparison on saved live library data

**Request (illustrative):** "Line up Somryst, Big Health, Akili, deprexis and HelloBetter side by side from the public record. No one has scored them yet. Our partner Lena reviews it."

**Data:** two `diligence-dh.compare_portfolio` calls made live on 19 October 2026 by an earlier build (`examples/live/compare_portfolio_dtx_2026-10-19.json`), read on 20 October 2026, and `get_funding_signals` for Pear (`examples/live/funding_signals_pear.json`). The connector was disconnected during this build, so no new call was made; a rerun would replace these values. Table from `python3 scripts/portfolio_table.py compare examples/live/compare_portfolio_dtx_2026-10-19.json`; funding cross-check from `crosscheck` (Pear: SEC 46 and NIH 6 match in both tools).

---

**Answer.** All four resolved companies have authorizations and registered studies on record; they differ in how studies link to the brand. HelloBetter did not resolve, and funding counts are missing for Big Health and GAIA AG.

| Company as resolved (query) | Authorizations | Studies: brand / indication only / unlinked | Safety events | Funding signal counts | Evidence maturity (rubric v1) |
|---|---|---|---|---|---|
| Pear Therapeutics, Inc. (Somryst) | US 3 | 2 / 1 / field absent of 3 | 2 | SEC 46; NIH 6 | 67 (60 of 90) |
| Big Health, Inc. (Big Health) | US 2 | none found / 2 / 2 of 4 | none found | field absent | 56 (50 of 90) |
| Akili Interactive Labs, Inc. | US 3 | 3 / 6 / 1 of 10 | none found | SEC 2 | 100 (90 of 90) |
| GAIA AG, Deutschland (deprexis) | EU 31 | 7 / field absent / 1 of 8 | field absent | field absent | 78 (70 of 90) |
| HelloBetter | lookup missed | not assessable | not assessable | not assessable | not assessable |

Source: library, retrieved 19 October 2026 (two calls: the first three companies together, the last two together).

**Notes you need.**
- Rows are company level: "Somryst" resolved to Pear and carries Pear's FDA recall flags (Class II, 7 June 2021, reSET and reSET-O).
- GAIA AG: two filing names were combined, "a proposal until a person validates it"; also flagged "2 registered studies terminated, withdrawn or suspended".
- "none found" means the loaded sources were searched and hold no row; "field absent" and "not assessable" are not zeros.
- Not loaded: Companies House, the BfArM DiGA directory feed, NICE, any funding source. Reimbursement is not assessable for every row; listed status goes to `dh-access-and-value` coverage-pathway-and-access-strategy.

**Status, as read on 20 October 2026 (`named-company-status.md`; SEC rows [WF]).** Pear: chapter 11 (Pear 8-K, 7 April 2023, SP-156); last filing Form 25-NSE, 2 May 2023, not dissolution (SP-155, DL-144); Somryst is now listed with FDA by Nox Medical (SP-167). Akili: the stored CIK 0001741200 holds two Form Ds; the registrant Akili, Inc. (CIK 1850266) became a subsidiary of Virtual Therapeutics (Akili 8-K, 2 July 2024, SP-151) and filed Form 15 on 12 July 2024, not dissolution (SP-154). Big Health: no SEC registrant found (SP-162). GAIA AG: `[GAP]`: not read (German register).

**What the score is.** The library's stated convention for documented evidence (rubric v1, 7 October 2026), not a valuation, a prediction or a rank.

**Next step.** For HelloBetter, give the maker's legal name or a register number. To order the set, score each company 0 to 4 on your criteria with weights (B1).

Lena was named as reviewer; who decides was not named. Who decides?

Full version on request.

**Calls made:** `diligence-dh.compare_portfolio` (two calls, 19 October 2026, saved); `diligence-dh.get_funding_signals {company: "Pear Therapeutics, Inc."}` (19 October 2026, saved). None new; research rows read 20 October 2026.

Portfolio comparison draft for Lena. AI-assisted. Clears it: Lena. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

Word count of the answer body (between the two rules, tables included, without the table's source line and the calls list, record line included): 442, counted with `python3 scripts/portfolio_table.py words examples/portfolio-comparison-dtx.md`.
