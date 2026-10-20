# Company status: does the company still exist, and in what state?

Interpretive reference for every task that profiles, compares, monitors or writes a record about a named company. Rows come from `diligence-research.md` section 7 (DL-135 to DL-168, read 20 October 2026). Rows the research file marks "(inference)" are the researcher's reading: label it "(inference)" every time it is cited. Rows marked [WF] were read through a fetch tool: say "[WF]" whenever one is applied.

The library does not show whether a company still exists, filed for bankruptcy, was delisted, deregistered or acquired. No library field states it, and a library profile with recent rows is not proof the company is active. Status comes only from the company's own primary filings or its register entry, read in this request. Never infer status from press, a deck, a vendor database or memory.

## 1. The status step

**Named companies already read (check first).** `references/named-company-status.md` holds what the filings and FDA records stated on 20 October 2026 for Pear Therapeutics, Akili, Big Health and Aidoc, and the current FDA listing holders of Somryst, EndeavorRx, reSET, reSET-O, SleepioRx and DaylightRx (SP-148 to SP-169). For a company covered there, the status line quotes those rows with the source name and date in plain words ("Pear 8-K, 7 April 2023 (SP-156 [WF])") and what each form does not mean; for a product, the current listing holder is stated apart from the company that was authorized. "Status: [GAP]: not read" stays only for companies and registers no row covers. Filings dated after 20 October 2026 are not covered: say "as read on 20 October 2026".

1. **Say what the library does not show.** One line: "Company status is not in the library; it comes from the filings and registers below."
2. **List the records that apply** to the company's identifiers and markets (table in section 2): a SEC CIK means EDGAR; a UK company number means Companies House; a German maker means the insolvency notice site and the register portal.
3. **Read them only where you can open them in this request** (a web fetch tool the person allows). Quote the filing or register line with its URL and read date.
4. **Where you cannot open them,** list the exact filings to open and write `Status: [GAP]: not read`. Never fill the gap with what a press story or your memory says.
5. **Say what each finding does not mean** (section 3). A Form 15 or a Form 25 is not dissolution.
6. **The person decides what the status means** for their question. Status is a fact with its record and date, never a judgment about the company.

## 2. Records to read, by jurisdiction

| Record | What it states | Where | Rows |
|---|---|---|---|
| 8-K Item 1.03 | Bankruptcy or receivership: the proceeding, the court and the date; includes Chapter 11 with management in possession | EDGAR filing index for the company's CIK | DL-136 |
| 8-K Item 1.03(b) | A court confirmed a plan of reorganization, arrangement or liquidation. A first 1.03 with no later (b) report means the outcome is still open on EDGAR (DL-137 (inference)) | EDGAR | DL-137 |
| 8-K Item 2.01 | A completed acquisition or disposition of significant assets: completion date, counterparty, consideration. Closing, not signing | EDGAR | DL-138 |
| 8-K Item 3.01 | An exchange deficiency notice, an exchange application to delist, or a board decision to withdraw or transfer a listing. A deficiency notice is not yet a delisting (DL-139 (inference)); a transfer is not distress (DL-140) | EDGAR | DL-139, DL-140 |
| 8-K Item 5.01 | A change in control: who acquired control, when, the percentage, the consideration, from whom | EDGAR | DL-141 |
| Form 25 | The exchange strikes a class from listing: redeemed, retired, substituted (for example in a merger) or extinguished. Delisting effective 10 days after filing; 12(b) withdrawal 90 days | EDGAR | DL-142, DL-143, DL-145 |
| Form 15 | The company stops SEC reporting under Rule 12g-4 (fewer than 300 holders of record, or 500 with small assets) or Rule 12h-3. After a merger the successor files it | EDGAR | DL-146 to DL-148 |
| EDGAR submissions record | Current name, former names, exchanges and tickers; recent filings at least one year or 1,000 filings | EDGAR submissions API (no key) | DL-150 to DL-152 [WF] |
| Bankruptcy docket | Case and docket information for a federal bankruptcy case; the Case Locator searches parties nationwide, updated daily at midnight | PACER (account and per-page fee) | DL-154 to DL-156 |
| Companies House `company_status` | One of twelve values, among them active, dissolved, liquidation, receivership, administration, voluntary-arrangement, converted-closed, insolvency-proceedings; `company_status_detail` adds states such as a pending strike-off; `date_of_cessation` gives the date closed, dissolved or removed | Companies House company profile | DL-157 to DL-161 |
| German insolvency notices | Insolvency courts' official announcements under the InsO | insolvenzbekanntmachungen.de | DL-165, DL-167 |
| German register portal | Commercial and other registers of all states | handelsregister.de; confirm on the official extract | DL-168 |

The library loads no Companies House feed ("API key not yet provisioned", 19 October 2026) and no German or Swiss register. Every UK, German or Swiss status is a direct read or `[GAP]: not read`.

## 3. What each finding does not mean

- **Form 25 is not dissolution.** It ends the exchange listing and Section 12(b) registration only; it does not end Section 12(g) or 15(d) reporting (DL-144). After a merger it signals that the old shares were converted, not that the business failed (DL-142 (inference)).
- **Form 15 is not dissolution.** It means the company stopped SEC reporting, not that it ceased to exist; under Rule 12h-3 reporting resumes if holder counts rise (DL-149 (inference)). A Form 15 filed by an acquirer for the target is a sign of acquisition (DL-147 (inference)).
- **Delisted, deregistered and dissolved are three different states** (`diligence-research.md`, "Changes and conflicts" item 9). An EDGAR filing gap is not a company's end.
- **An 8-K Item 1.03 is not liquidation.** Chapter 11 can leave management in possession under court supervision (DL-136). Read for a later 1.03(b) (DL-137).
- **An 8-K date trails the event** by up to four business days (DL-135).
- **Companies House "active" can hide a pending strike-off** (DL-159 (inference)). "Liquidation" is a path to "dissolved" (DL-163 (inference)); "struck off" means dissolved (DL-162); a company in administration can still be wound up (DL-164).
- **No German insolvency notice today does not prove no past insolvency:** notices are deleted at the latest six months after proceedings end (DL-166 (inference)).
- **The German register portal's structured data is not binding;** confirm status on the official extract (DL-168 (inference)).
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
