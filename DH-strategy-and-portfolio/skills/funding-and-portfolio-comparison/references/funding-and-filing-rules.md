# Funding and filing rules: what a public filing shows and what it does not

Interpretive reference for task A1 (funding signals read) and the funding columns of A2. Every rule cites its row in `diligence-research.md` (row prefix DL, read 20 October 2026). Rows marked "(inference)" in the research file are the researcher's reading across several items: when an answer rests on one, label it "(inference)". Rows DL-124 and DL-125 are [PAPER] rows, DOI 10.1371/journal.pone.0323390.

## 1. Form D (US exempt offerings)

| What the person may read from it | Rule | Rows |
|---|---|---|
| That an exempt offering was made | Form D is a notice filed by a company that sold securities without registration under Rule 504 or 506 of Regulation D or Section 4(a)(5) | DL-001 |
| When investors committed | Due within 15 days (15 calendar days, Rule 503) after the first sale, which is the date the first investor is irrevocably committed. The filing date tracks commitment, not closing or announcement | DL-002, DL-004 |
| Whether the offering continues | A continuing offering is amended at least annually, on or before the anniversary of the last filing | DL-005 |
| The amounts | Item 13 gives the total offering amount and the amount sold as of the filing date; "Indefinite" is allowed; non-cash consideration is the issuer's own good-faith valuation | DL-015 |
| How stale the amount may be | No amendment is required for a change in the amount sold or the number of investors, or for changes after the offering ends. A Form D amount sold can be stale | DL-006 |
| Who leads the company | Item 3 names executive officers, directors and promoters | DL-012 |
| How many investors | Item 14 gives counts (non-accredited and total), never names | DL-016 |
| Revenue | The issuer may answer "Decline to Disclose" for its revenue range | DL-014 |
| Use of proceeds | Only the amount paid to named officers, directors or promoters | DL-017 |
| How the raise was marketed | The 506(c) box signals an offering not subject to the limitation on manner of offering, with accredited purchasers only and verified | DL-010, DL-011 |
| Offering size cap under Rule 504 | Rule 504 caps an offering at USD 10,000,000 in 12 months and is not available to SEC reporting companies | DL-007 |
| Industry | The industry menu has Health Care subgroups and no "digital health" code, so a screen by industry code misses software companies coded as Technology (inference) | DL-013 |

**Never from a Form D:** valuation, price per share, lead investor or investor names (DL-018 (inference)). Never compute a valuation, a post-money figure or an investor list from it.

## 2. Form 8-K, 10-K and S-1 (US reporting companies)

| Event or section | Rule | Rows |
|---|---|---|
| Timing | A Form 8-K is generally due within four business days after the event | DL-019 |
| Partnerships, licenses | Item 1.01 reports a material definitive agreement outside the ordinary course: date, parties, material relationship, material terms | DL-020, DL-021 |
| Completed acquisitions | Item 2.01 reports date, assets, counterparty and the nature and amount of consideration for a significant acquisition; significant means above 10 percent of consolidated total assets or significant under S-X 11-01(b). Smaller deals may never appear in an 8-K (inference) | DL-022, DL-023 |
| Cybersecurity incidents | Item 1.05, within four business days after the registrant determines the incident is material | DL-024 |
| Business and regulation | 10-K Item 1 follows S-K Item 101: material effects of government regulation, human capital including headcount; a smaller reporting company discusses where an unreceived approval stands. Check that status claim against the FDA records | DL-025, DL-029, DL-030 |
| Risk factors | 10-K Item 1A follows S-K Item 105; smaller reporting companies need not provide them. Absence is not a signal of low risk (inference) | DL-026, DL-028 |
| Cybersecurity section | 10-K Item 1C under S-K Item 106 | DL-027 |
| IPO | Form S-1 pulls in S-K Items 105 and 101 | DL-031 |
| Searching filings | EDGAR full-text search covers electronic filings since 2001, including exhibits; Boolean, phrase and NEAR syntax; no natural-language queries | DL-032, DL-033 |

The library's funding rows carry no 8-K item number and a null counterparty (`references/tools.md`). To say what an 8-K reports, open the filing at its URL; until then write "8-K, item not stated in the library row".

## 3. UK company records

| Record | Rule | Rows |
|---|---|---|
| Confirmation statement | Every UK company files one at least once a year, confirming directors, PSC, registered office and email; within 14 days after the review period ends | DL-034, DL-035, DL-037, DL-038 |
| Identity verification | Companies House will not accept a confirmation statement until all directors have verified their identity | DL-036 |
| Accounts deadlines | Private companies 9 months after the accounting reference date, public companies 6 months | DL-039 |
| What accounts show | Filed accounts are public, but small companies and micro-entities may file without the profit and loss account, so a UK filing may show no revenue | DL-040, DL-041 |
| From 1 April 2028 | Small companies must deliver the profit and loss account, with an option to opt out of publishing it; abridged accounts end; filing by commercial software | DL-042, DL-043 |

The library does not load Companies House ("API key not yet provisioned", `examples/live/compare_portfolio_dtx_2026-10-19.json`, 19 October 2026). UK company facts are `[GAP]` in the library; the person reads the register directly.

## 4. Grants and public contracts

The library returns NIH RePORTER grants and EU TED awards with counts and date ranges (`examples/live/funding_signals_pear.json`). A grant or award is public funding for a stated project, not an equity round. Report it by source and date range; never add it to an offering amount.

## 5. Funding is not evidence, and vendor totals are claims

- In 224 US venture-backed companies, a clinical robustness score (FDA filings plus registered trials) did not correlate with total funding (DL-117, DOI 10.2196/37677). Of the 10 top-funded dementia-prevention lifestyle companies, 7 had no qualifying evidence (DL-124, DOI 10.1371/journal.pone.0323390). These are published findings about those cohorts, not a rule about the person's companies.
- Commercial funding databases may lack full funding details (DL-125, DOI 10.1371/journal.pone.0323390). A funding total the person brings from a vendor is labeled as theirs ("the person's figure, source: <vendor as named>").
- No source in this skill gives a market size, a valuation multiple, a return benchmark or a funding total by sector ("Not sourced" section of the research file). Never supply one.
