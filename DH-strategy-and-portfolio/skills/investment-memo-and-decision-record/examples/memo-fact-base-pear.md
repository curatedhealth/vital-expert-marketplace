# Worked example: A1 memo fact base for Pear Therapeutics, Inc., then A2 on illustrative deal facts

**Request (illustrative):** "We're preparing an IC memo on the company behind Somryst. Build the public-record fact base, and tell us what our deal facts need flagged." Deal facts: `evals/files/deal_facts_illustrative.json` (ILLUSTRATIVE, written for the build).

**Data:** live library outputs saved on 19 October 2026 by earlier builds and copied to `examples/live/` (read 20 October 2026): `generate_report_somryst_commercial.json` (identity block of `build_company_profile`), `funding_signals_pear.json`, `evidence_maturity_K191716_somnio.json`, `compare_portfolio_dtx_2026-10-19.json`. The connector was disconnected during this build; no new call was made. Script runs saved as `examples/live/memo_facts_pear_output.md` and `examples/live/deal_flags_illustrative_output.md`.

## A1 answer (short mode)

**Answer.** As of 19 October 2026 the library holds three FDA authorizations for Pear Therapeutics, Inc. (one De Novo granted, two 510(k) cleared, all regulation 882.5801), two Class II recalls dated 7 June 2021, and 46 SEC filings ending 10 April 2023; its evidence maturity is 67 on rubric v1, "a stated convention for comparing documented evidence, not a predictive model or a valuation". The largest gap: private rounds and any UK or Swiss filing are not in the library.

**Products and authorizations**

| Product | Reference | Pathway | Decision date | Source |
|---|---|---|---|---|
| reSet | DEN160018 | De Novo, granted | 14 September 2017 | identity block |
| reSET-O | K173681 | 510(k), cleared | 10 December 2018 | identity block |
| Somryst | K191716 | 510(k), cleared (QVO) | 23 March 2020 | FDA 510(k) record URL |

A 510(k) is cleared, not approved (DL-128).

**Filings and funding signals.** SEC EDGAR 46 filings, 9 February 2016 to 10 April 2023 (8-K 25, 10-Q 6, D 4, D/A 1, others); NIH RePORTER 6 grants; EU TED none found. Form D shows no valuation or investor names (DL-016, DL-018); private rounds `[GAP]`. The latest filing date in the store is not a status.

**Evidence.** Library evidence maturity 67 (60 of 90 assessable points; reimbursement and jurisdiction breadth not assessable). Company level: it covers reSet, reSET-O and Somryst. A framework-based reading is `company-and-evidence-assessment` (this pack).

**Safety events.** Two Class II recalls on 7 June 2021 (reSET, reSET-O), as the record states.

**Company status (as read on 20 October 2026, `named-company-status.md`; SEC rows [WF]).** Pear filed for chapter 11 on 7 April 2023 in the District of Delaware, case 23-10429 (Pear 8-K, 7 April 2023, SP-156); Nasdaq gave notice of delisting (Pear 8-K, 10 April 2023, SP-160); the last EDGAR filing is a Form 25-NSE of 2 May 2023, which is not dissolution (SP-155, DL-144). No later Item 1.03(b) report appears, so the outcome is open on EDGAR (DL-137 (inference)). The library store ends at 10 April 2023. Current FDA listing holders differ from Pear as applicant: Somryst, Nox Medical from 18 December 2024 (SP-167); reSET and reSET-O, Harvest Bio from 14 November 2024 (SP-169). The buyers are named only in court sale orders, not read (SP-161).

**Gaps and checks outside the library.** Identifiers not in the identity block (call `build_company_profile` for CIK and EUDAMED); Companies House and Zefix not loaded; HHS breach portal, main list and archive (DL-095, DL-096); 8-K item numbers not stored, so open each filing for Item 1.01 or 1.05 (DL-020, DL-024).

Full version on request.

Calls made (saved, 19 October 2026): `commercial-dh.generate_report {reference: "Somryst", template: "commercial", ...}` (identity block only); `diligence-dh.get_funding_signals {company: "Pear Therapeutics, Inc."}`; `diligence-dh.get_evidence_maturity {company: "K191716"}`; `scripts/memo_facts.py facts`. Research rows read 20 October 2026, no call.

Memo fact base draft. Public record only. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Word count: run `python3 scripts/memo_facts.py words ANSWER.md` on the answer above (it drops the calls list and the Source and Rows columns, and counts the record line) and cut in the house order if it prints "over".

## A2 answer on the illustrative deal facts (short mode, abridged)

**Answer.** Your stated value of USD 150,000,000 is above the 2026 size-of-transaction figure of USD 133.9 million (DL-044, DL-045) and below USD 535.5 million, so the size-of-person figures also apply and your party sizes are not given (DL-046, DL-047); 40,000 US individuals' health data is above the DOJ bulk threshold of 10,000 (DL-066) and at or below CFIUS's one-million test (DL-056). Whether any of this makes the deal reportable or covered is for the owner you name for legal or compliance; owner not named.

The table is `examples/live/deal_flags_illustrative_output.md`. Missing facts to ask for: party sizes, the co-investor's country, genetic or 'omic data, any foreign access to the data, the target's HIPAA role. The co-investor's board seat is a listed right for a non-controlling investment in a TID US business (DL-062); its 20% voting and the 30% government interest sit below the 25% and 49% substantial-interest figures (DL-064).

Transaction and data flags draft for the owner. Not legal advice. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## What the run showed

- The commercial report's identity block holds K191716 while its readiness section marks authorization `[GAP]` (register C7); A1 takes the identity block.
- `diligence-dh.generate_report` and `list_sources` have no saved output: needs a live check (BUILD_NOTES).
