# Company status: does the company still exist, and in what state?

Interpretive reference for every task that profiles, compares, monitors or writes a record about a named company. Rows come from `diligence-research.md` section 7 (DL-135 to DL-168, read 20 October 2026). Rows the research file marks "(inference)" are the researcher's reading: write "(inference)" after the row id every time one is cited. Rows marked [WF] were read through a fetch tool: write "[WF]" every time one is applied. Status for the companies named in the saved outputs (Akili, Pear Therapeutics, Big Health, Aidoc) and the current FDA listing holder of their products comes from the strategy research rows SP-148 to SP-169 (`strategy-and-portfolio-sources.md` section 8, read 20 October 2026; section 6 below).

The library does not show whether a company still exists, filed for bankruptcy, was delisted, deregistered or acquired. No library field states it, and a library profile with recent rows is not proof the company is active. Status comes only from the company's own primary filings or its register entry, read in this request. Never infer status from press, a deck, a vendor database or memory.

## 1. The status step

1. **Say what the library does not show.** One line: "Company status is not in the library; it comes from the filings and registers below."
2. **List the records that apply** to the company's identifiers and markets (table in section 2): a SEC CIK means EDGAR; a UK company number means Companies House; a German maker means the insolvency notice site and the register portal.
3. **Use the status already read** for the companies in section 6 (SP-148 to SP-169, read 20 October 2026), citing each filing by name and date in plain words with the row id after it ("Pear 8-K, filed 7 April 2023 (SP-156) [WF]"), never a row id alone. **Otherwise read the records only where you can open them in this request** (a web fetch tool the person allows). Quote the filing or register line with its URL and read date.
4. **Where you cannot open them,** list the exact filings to open and write `Status: [GAP]: not read`. Never fill the gap with what a press story or your memory says.
5. **Say what each finding does not mean** (section 3). A Form 15 or a Form 25 is not dissolution.
6. **State the product's current FDA listing holder separately from the company that was authorized.** The 510(k) or De Novo page shows the applicant at clearance; the registration and listing record shows who lists the device now (SP-165 to SP-169). Neither is the sale record.
7. **The person decides what the status means** for their question. Status is a fact with its record and date, never a judgment about the company.

## 2. Records to read, by jurisdiction

| Record | What it states | Where | Rows |
|---|---|---|---|
| 8-K Item 1.03 | Bankruptcy or receivership: the proceeding, the court and the date; includes Chapter 11 with management in possession | EDGAR filing index for the company's CIK | DL-136 |
| 8-K Item 1.03(b) | A court confirmed a plan of reorganization, arrangement or liquidation. A first 1.03 with no later (b) report means the outcome is still open on EDGAR (DL-137) (inference) | EDGAR | DL-137 (inference) |
| 8-K Item 2.01 | A completed acquisition or disposition of significant assets: completion date, counterparty, consideration. Closing, not signing | EDGAR | DL-138 |
| 8-K Item 3.01 | An exchange deficiency notice, an exchange application to delist, or a board decision to withdraw or transfer a listing. A deficiency notice is not yet a delisting (DL-139) (inference); a transfer is not distress (DL-140) | EDGAR | DL-139, DL-140 |
| 8-K Item 5.01 | A change in control: who acquired control, when, the percentage, the consideration, from whom | EDGAR | DL-141 |
| Form 25 | The exchange strikes a class from listing: redeemed, retired, substituted (for example in a merger) or extinguished. Delisting effective 10 days after filing; 12(b) withdrawal 90 days | EDGAR | DL-142 (inference), DL-143, DL-145 |
| Form 15 | The company stops SEC reporting under Rule 12g-4 (fewer than 300 holders of record, or 500 with small assets) or Rule 12h-3. After a merger the successor files it | EDGAR | DL-146 to DL-148 |
| EDGAR submissions record | Current name, former names, exchanges and tickers; recent filings at least one year or 1,000 filings | EDGAR submissions API (no key) | DL-150 to DL-152 [WF] |
| Bankruptcy docket | Case and docket information for a federal bankruptcy case; the Case Locator searches parties nationwide, updated daily at midnight | PACER (account and per-page fee) | DL-154 to DL-156 |
| Companies House `company_status` | One of twelve values, among them active, dissolved, liquidation, receivership, administration, voluntary-arrangement, converted-closed, insolvency-proceedings; `company_status_detail` adds states such as a pending strike-off; `date_of_cessation` gives the date closed, dissolved or removed | Companies House company profile | DL-157 to DL-161 |
| German insolvency notices | Insolvency courts' official announcements under the InsO | insolvenzbekanntmachungen.de | DL-165, DL-167 |
| German register portal | Commercial and other registers of all states | handelsregister.de; confirm on the official extract | DL-168 (inference) |

The library loads no Companies House feed ("API key not yet provisioned", 19 October 2026) and no German or Swiss register. Every UK, German or Swiss status is a direct read or `[GAP]: not read`.

## 3. What each finding does not mean

- **Form 25 is not dissolution.** It ends the exchange listing and Section 12(b) registration only; it does not end Section 12(g) or 15(d) reporting (DL-144). After a merger it signals that the old shares were converted, not that the business failed (DL-142) (inference).
- **Form 15 is not dissolution.** It means the company stopped SEC reporting, not that it ceased to exist; under Rule 12h-3 reporting resumes if holder counts rise (DL-149) (inference). A Form 15 filed by an acquirer for the target is a sign of acquisition (DL-147) (inference).
- **Delisted, deregistered and dissolved are three different states** (`diligence-research.md`, "Changes and conflicts" item 9). An EDGAR filing gap is not a company's end.
- **An 8-K Item 1.03 is not liquidation.** Chapter 11 can leave management in possession under court supervision (DL-136). Read for a later 1.03(b) (DL-137 (inference)).
- **An 8-K date trails the event** by up to four business days (DL-135).
- **Companies House "active" can hide a pending strike-off** (DL-159) (inference). "Liquidation" is a path to "dissolved" (DL-163) (inference); "struck off" means dissolved (DL-162); a company in administration can still be wound up (DL-164).
- **No German insolvency notice today does not prove no past insolvency:** notices are deleted at the latest six months after proceedings end (DL-166) (inference).
- **The German register portal's structured data is not binding;** confirm status on the official extract (DL-168) (inference).
- **An authorization country is not a company's country.** "US" in `authorizations_by_jurisdiction` says where a product is authorized; it does not say where the company is incorporated or whether it exists.

## 4. Reaching outside sites

- A request to an outside site never carries the person's email address or name.
- SEC fair access asks automated clients to declare a User-Agent with a company name and an admin contact, and caps requests at 10 per second (DL-153 [WF]); requests without it were refused on the research pass. Ask the person which contact their organization uses for SEC access. If they give none, do not invent one: list the filings to open and write `[GAP]: not read`.
- PACER needs the person's own account (DL-154). Name the docket search; do not run it.

## 5. Wording

| Situation | How to word it |
|---|---|
| Read, with a finding | "8-K filed DATE, Item 1.03: [the filing's words] (EDGAR, URL, read DATE). An Item 1.03 is not liquidation (DL-136)." |
| Read, nothing found | "No 8-K Item 1.03, 2.01, 3.01 or 5.01, Form 25 or Form 15 in the EDGAR filing list for CIK N as read on DATE (URL). Not proof of none outside the filings read." |
| Not read | "Status: [GAP]: not read. Open: EDGAR filings for CIK N (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15); Companies House status for company number N; insolvenzbekanntmachungen.de for the German maker." |
| No identifier stored | "Status: [GAP]: not read; no SEC CIK or UK company number in the record. Ask the person for the legal name and register number." |

## 6. Status already read for companies in the saved outputs (SP-148 to SP-169, read 20 October 2026)

All SEC rows are [WF] (read through a fetch tool, so quotes are close but not guaranteed verbatim). Cite each line by the filing or record name and date in plain words, then the row id.

| Company | Status line to use (source in plain words, row) | What it does not mean |
|---|---|---|
| Akili, Inc. (CIK 1850266; Akili Interactive Labs, Inc. is its wholly owned subsidiary, not a former name; SP-148 [WF]) | Merger agreement with Virtual Therapeutics Corporation signed 29 May 2024, cash tender offer at $0.4340 per share (Akili 8-K, 29 May 2024, Item 1.01; SP-150 [WF]). Offer completed and change in control on 2 July 2024; Akili became a wholly owned subsidiary of Virtual Therapeutics Corporation (Akili 8-K, 2 July 2024, Items 2.01 and 5.01; SP-151 [WF]). Nasdaq asked to file Form 25 (same 8-K, Item 3.01; SP-152 [WF]); Form 25-NSE filed by Nasdaq 2 July 2024 (SP-153 [WF]); Form 15-12G filed 12 July 2024 (SP-154 [WF]). | Not dissolution: Form 25 ends the listing (DL-144); Form 15 ends SEC reporting, not existence (DL-149) (inference); a Form 15 filed after a merger is a sign of acquisition (DL-147) (inference). The Form 25-NSE body was not readable (SP-153). |
| Pear Therapeutics, Inc. (CIK 1835567; SP-155 [WF]) | Chapter 11 filed 7 April 2023, US Bankruptcy Court for the District of Delaware, case no. 23-10429 (Pear 8-K, filed 7 April 2023, Item 1.03; SP-156 [WF]); the same 8-K records about 170 employees (92% of full-time staff) terminated (SP-158 [WF]) and a planned section 363 sale process with no buyer named (SP-159 [WF]). Nasdaq delisting notice 10 April 2023, trading suspended 19 April 2023, no appeal (Pear 8-K, filed 10 April 2023, Item 3.01; SP-160 [WF]). Last filing: Form 25-NSE, 2 May 2023; no Form 15 and no 8-K after 10 April 2023 in the EDGAR submissions record (SP-155 [WF]). | An Item 1.03 is not liquidation (DL-136); no later Item 1.03(b) report is on EDGAR, so the case outcome is open on EDGAR (DL-137) (inference). No SEC filing names a buyer of Somryst, reSET or reSET-O (SP-161 [WF]); the court sale orders were not read: `[GAP]: not read`. Stopping filing is not dissolution. |
| Big Health Inc. | Not an SEC filer: EDGAR name lookup for "Big Health Inc" and a Form D full-text search returned 0 hits (EDGAR search, 20 October 2026; SP-162 [WF]). FDA establishment registration 3024442350 (Newport Beach), active, registration year 2026, listing SleepioRx (K233577) and DaylightRx (K233872) (FDA registration and listing, read 20 October 2026; SP-163). | No SEC record is not a status: Companies House or other registers were not read, `[GAP]: not read`. An active FDA registration says the establishment registered for 2026, not that the business is sound. |
| Aidoc Medical Ltd. | Not an SEC filer: EDGAR name lookup for "Aidoc Medical" returned 0 hits (EDGAR search, 20 October 2026; SP-162 [WF]). FDA establishment registration 3014938447 (Tel Aviv-Yafo, Israel), active, registration year 2026, 25 device listings including BriefCase products under QAS (FDA registration and listing, read 20 October 2026; SP-164). | The Israeli company register was not read: `[GAP]: not read`. Same limit on what an active registration means. |

Current FDA listing holder, stated apart from the company that was authorized:

| Product | Authorized to (as the decision record states) | Listed today by (FDA registration and listing, read 20 October 2026) |
|---|---|---|
| Somryst (K191716, QVO) | Pear Therapeutics, Inc., cleared 23 March 2020 (FDA 510(k) K191716; SP-165) | NOX MEDICAL, Reykjavik, Iceland, listing created 18 December 2024 (SP-167) |
| EndeavorRx (DEN200026) | akili interactive labs, inc. (FDA De Novo DEN200026; SP-166) | "AKILIINTERACTIVE Labs, Inc. C/O Virtual Therapeutics", Kirkland, WA (SP-168) |
| reSET (DEN160018) and reSET-O (K173681) | A Pear product per Pear's own 8-K record (SP-161 [WF]); the decision records were not copied into this skill (research_tm TM131): requester `[GAP]` | HARVEST BIO LLC, Middletown, CT, both listings created 14 November 2024 (SP-169) |

A listing holder is who lists the device with FDA now. It is not the buyer named in a sale order (not read), not proof of marketing, and not a statement about the original company. Any other company in an answer (for example Brainomix, ORTEC, Viz.ai, GE, Evidencio, Siemens in the saved outputs) has no status row: `Status: [GAP]: not read`, with the records to open from section 2.
