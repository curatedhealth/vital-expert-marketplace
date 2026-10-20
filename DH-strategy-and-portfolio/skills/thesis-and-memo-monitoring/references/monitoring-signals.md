# Monitoring signals: what a thesis can be re-checked against, and dated rule changes

Source: `diligence-research.md` (DL rows, read 20 October 2026), `channels-partners-launch-sources.md` (CP rows, read 19 October 2026) and the saved library outputs in `examples/live/` (19 October 2026). Interpretive reference for A1, A2 and B1.

## 1. Which assumptions a public signal can carry

| Assumption type (examples) | Public signal | Where it comes from | What the signal cannot show | Rows or file |
|---|---|---|---|---|
| "Holds FDA clearance for X" | Authorizations with reference and decision date; a new authorization; a recall or safety event | `build_company_profile`; `get_deltas` (authorization, safety event) | Whether the product is still marketed, sold or used: no marketing status is stored | `partner_profile_akili.json` (no marketing status field); DL-126, DL-127 (registration is not approval); DL-133 (name matching (inference)) |
| "Has randomized evidence" | Registered studies by link tier; evidence maturity components | `get_evidence_maturity`; `get_deltas` (study) | Published papers outside the registry; the quality of the evidence | DL-116, DL-118, DOI 10.2196/37677; `evidence_maturity_K191716_somnio.json` |
| "Raised enough to reach a milestone" | New Form D or Form D/A by date; new 8-K | `get_funding_signals`; `get_deltas` (filing) | Valuation, investors, runway, revenue; private rounds | DL-002, DL-005, DL-006, DL-016, DL-018 |
| "Partnership with Y" | 8-K Item 1.01 for a listed party | `get_funding_signals` rows, then the filing at its URL | Item number is not stored; private agreements | DL-020, DL-021 |
| "Acquisition closed" | 8-K Item 2.01 | as above | Deals under the 10 percent significance test may never appear (inference) | DL-022, DL-023, DL-138 |
| "The company is operating" (not bankrupt, delisted, deregistered or acquired) | 8-K Items 1.03, 3.01, 5.01; Form 25; Form 15; Companies House status; German insolvency notices | the filing or register opened at the source (section 6); the library stores no status | Status is `[GAP]` until read; Form 25 or 15 is not dissolution | DL-136 to DL-168 |
| "No material cyber incident" | 8-K Item 1.05; 10-K Item 1C | as above | Private companies file neither | DL-024, DL-027 |
| "No large health-data breach" | HHS OCR portal entry (500 or more individuals) | the person's portal search, main list and archive | Breaches under 500; a vendor breach listed under a client's name (inference) | DL-092, DL-095 to DL-097 |
| "UK entity in good standing" | Confirmation statement and accounts at Companies House | the register, read by the person (not loaded in the library) | P&L for small companies until 1 April 2028 | DL-034 to DL-043 |
| "Revenue of USD X", "churn under Y", "pipeline of Z" | None in the public record | the person's own (non-public) data | Everything: the library holds no revenue, customer or pipeline data | DL-014, DL-040 |

An assumption with no public signal is "not measurable from the record (T3)": it is watched with the person's own data, labeled non-public, or not at all.

## 2. Library change signals and their limits

| Signal | How to read it | Limit | File |
|---|---|---|---|
| `get_deltas` per company since a date | Changes by event date: authorization decision date, study start date, safety event date, filing signal date | "the change log began on the first_entry_at date" (12 October 2026 in the saved run); "no change recorded is a statement about in-window event-dated log rows up to last_sweep_at" (19 October 2026) | `diligence_deltas_Akili_Pear.json`, `diligence_get_deltas_BigHealth_Akili.json` |
| `get_funding_signals` rerun | New filings by type and date compared with the earlier run | No 8-K item number; counterparty null; private rounds `[GAP]` | `funding_signals_pear.json` |
| `get_evidence_maturity` rerun | Score and components compared with the earlier run | Comparable only on the same rubric version (v1, 7 October 2026 in the saved run); company level | `evidence_maturity_K191716_somnio.json` |
| `build_company_profile` rerun | Products, authorizations, Form D rows | Exact name matching; `funding` `[GAP]` beside Form D rows (register C2) | `partner_profile_akili.json` |

A memo dated before 12 October 2026 cannot be checked for changes between its date and the log start through `get_deltas`: rerun `get_funding_signals` and `build_company_profile` and compare dates instead, and say so (flag T5).

## 3. Filing clocks that set when a change can appear

| Clock | Row |
|---|---|
| Form D within 15 days after first sale | DL-002, DL-004 |
| Form D amended at least annually while the offering continues; no amendment needed for a change in amount sold | DL-005, DL-006 |
| Form 8-K generally within four business days | DL-019 |
| 8-K Item 1.05 within four business days after the materiality determination | DL-024 |
| HIPAA individual notice within 60 calendar days of discovery; HHS at the same time for 500 or more | DL-089, DL-092 |
| Business associate to covered entity within 60 calendar days | CP-US-49 |
| FTC Health Breach Notification Rule: 60 calendar days | CP-US-56 |
| UK confirmation statement within 14 days after the review period; accounts 9 months (private) or 6 months (public) | DL-037, DL-039 |
| FDA registration and listing data: updated generally weekly, with a lag | DL-129 |

These are facts about when a record can exist, not deadlines for the person.

## 4. Dated rule changes (compare with the memo date)

| Date | Change | Instrument | Status on the pages read | Row |
|---|---|---|---|---|
| 6 April 2025 | UK company size thresholds changed for periods from this date | Companies House guidance | in force | DL-041 |
| 10 February 2025 | Updated HSR form took effect | FR Doc 2024-25024 | vacated 12 February 2026 | DL-050 |
| 18 November 2025 | Companies House guidance updated for mandatory director identity verification | Companies House guidance | in force | DL-036 |
| 19 December 2025 | Swiss Investment Screening Act adopted | BBl 2026 31 | not in force | DL-081 |
| 16 January 2026 | 2026 HSR thresholds published; DATES line 17 February 2026 | 91 FR 2133 | in force | DL-044 to DL-048 |
| 12 February 2026 | Updated HSR form vacated by a federal district court | Chamber of Commerce v. FTC, No. 6:25-cv-9 | FTC accepts the prior form | DL-051, DL-053 |
| 19 March 2026 | Court of Appeals denied a stay; appeal No. 26-40094 pending | Fifth Circuit | pending on the pages read | DL-051, DL-053 |
| 25 March 2026 | FTC and DOJ request for comment, due 26 May 2026; FTC considering a new rulemaking | FTC press release | status after 26 May 2026 not found | DL-054 |
| 17 April 2026 | Swiss IPG referendum period ended; Federal Council sets entry into force | BBl 2026 31 | SECO: planned 2027 | DL-081, DL-082 |
| 12 June 2026 | Swiss IPG ordinance consultation opened, to 5 October 2026 | Federal Council | draft text not read | DL-085 |
| 17 June 2026 | Regulation (EU) 2026/1386 on screening foreign investments adopted (OJ 26 June 2026) | Regulation (EU) 2026/1386 | some provisions from 16 July 2026; applies from 17 January 2028 | DL-074, DL-075 |

Scheduled, not yet reached on 20 October 2026: Swiss IPG entry into force planned for 2027 (DL-082); EU 2026/1386 applies and 2019/452 is repealed on 17 January 2028 (DL-075); UK small companies deliver the P&L and file by software from 1 April 2028 (DL-042, DL-043); HSR thresholds are revised every year (DL-049). Evidence DEFINED's authors plan updates every 6 to 12 months (DL-113, DOI 10.1038/s41746-023-00836-5).

AI Act dates as amended by Regulation (EU) 2026/1744 are in research_reg2 (not copied); route to `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.

## 5. What a change may touch (hypotheses only)

A change is set beside the assumption it could touch and labeled "hypothesis for review". Examples of the form: "New Form D dated DATE: could touch assumption 3 (funding); the filing shows no valuation or investors (DL-018)." "HSR form vacated 12 February 2026: could touch the condition 'HSR filing on the updated form' in the decision record; the conclusion is for the owner the person names for legal or compliance." Never infer a company's results, intent or financial position from a change.

## 6. Company status: operating, bankrupt, delisted, deregistered, acquired or dissolved

The library stores no company status field, and its 8-K rows carry no item number (saved `funding_signals_pear.json`). Status therefore comes only from the company's own filings or register, opened at the source. Never from press, memory, the date filings stopped or the number of filings. Delisted, deregistered and dissolved are three different states (research file, changes and conflicts item 9).

**Named companies already read (check first).** `references/named-company-status.md` holds what the filings and FDA records stated on 20 October 2026 for Pear Therapeutics, Akili, Big Health and Aidoc, and the current FDA listing holders of Somryst, EndeavorRx, reSET, reSET-O, SleepioRx and DaylightRx (SP-148 to SP-169). For a company covered there, the status line quotes those rows with the source name and date in plain words ("Pear 8-K, 7 April 2023 (SP-156 [WF])") and what each form does not mean; for a product, the current listing holder is stated apart from the company that was authorized. "Status: [GAP]: not read" stays only for companies and registers no row covers. Filings dated after 20 October 2026 are not covered: say "as read on 20 October 2026".

**Steps.** (1) List the latest 8-K, Form 25 and Form 15 rows by date, with accession and URL as stored. (2) Where the assistant can open the filing or register, quote the item and its date. (3) Otherwise write "Company status [GAP]: not read" and list the exact filings to open. (4) State what the form found does not mean.

| Record | What it states | What it does not mean | Rows |
|---|---|---|---|
| 8-K, generally | Filed within four business days of the event, so its date trails the event | The 8-K date is not the event date | DL-135 |
| 8-K Item 1.03 | A receiver or similar officer appointed, or a court assuming jurisdiction over substantially all assets, including management left in possession under court supervision (as in Chapter 11); names the proceeding, court and date | Not the outcome: a later 1.03(b) report follows when a court confirms a plan of reorganization, arrangement or liquidation; with no later report the outcome is still open on EDGAR (inference) | DL-136, DL-137 |
| 8-K Item 2.01 | Completion of an acquisition or disposition of a significant amount of assets: date, counterparty, consideration | Marks closing, not signing | DL-138 |
| 8-K Item 3.01 | An exchange notice of failing a continued-listing standard, an exchange application to delist, or the board's decision to withdraw a listing, including a transfer | A deficiency notice is not yet a delisting (inference); a 3.01 can mean a transfer, not distress | DL-139, DL-140 |
| 8-K Item 5.01 | Who acquired control, when, the basis and percentage of voting securities, from whom | | DL-141 |
| Form 25 | The exchange strikes a class from listing (for example after redemption or substitution in a merger); effective 10 days after filing, 12(b) withdrawal after 90 days; a voluntary delisting needs notice and a press release | Not dissolution; it does not affect 12(g) registration or 15(d) reporting, so a delisted company may still file; after a merger it signals converted shares, not a failed business (inference) | DL-142 to DL-145 |
| Form 15 | Ends 12(g) registration (fewer than 300 holders, or 500 with assets of USD 10 million or less) or suspends 15(d) reporting; reports stop at once; after a merger the successor files it | Not dissolution: the company stopped SEC reporting, not that it ceased to exist; the suspension can lapse (inference); a Form 15 filed by an acquirer for the target is a sign of acquisition (inference) | DL-146 to DL-149 |
| US bankruptcy dockets | PACER (account, 10 cents a page, capped at USD 3.00 per document) and the Case Locator, updated daily | | DL-154 to DL-156 |
| Companies House `company_status` | One of twelve values (active, dissolved, liquidation, receivership, administration, voluntary-arrangement, converted-closed, insolvency-proceedings and others); `company_status_detail`; `date_of_cessation` | "Active" can hide a pending strike-off (inference); "liquidation" is a path to "dissolved", not yet dissolved (inference); the insolvency flags are deprecated, use `links.insolvency` | DL-157 to DL-164 |
| German insolvency notices | Court announcements at insolvenzbekanntmachungen.de; deemed given two days after publication | No hit today does not prove no past insolvency: notices are deleted at the latest six months after proceedings end (inference); Registerportal structured data is not binding, confirm on the official extract (inference) | DL-165 to DL-168 |

**Fair access.** The EDGAR APIs need no key (DL-152); SEC asks automated clients to declare a User-Agent with a contact and caps requests at 10 per second (DL-153). Requests to outside sites never carry the person's email address or name. Ask which contact the person's organization uses for SEC access; if none is given, list the filings to open instead. Never invent a contact.

**Wording.** "Company status [GAP]: not read. The latest 8-Ks (DATE, accession, URL) carry no item number in the library; open them for Items 1.03, 2.01, 3.01 and 5.01 (DL-136 to DL-141), and check for a Form 25 or Form 15 (DL-142 to DL-149)." Once read: "8-K of DATE, Item 1.03: QUOTE (read DATE)."
