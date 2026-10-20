# Company status and the change-log window

Source: rows DL-135 to DL-168 of `references/diligence-research.md` (section 7, read 20 October 2026), plus the saved library outputs of 19 October 2026 in `examples/live/`. Rows marked "(inference)" in the research file are cited as "the research file's inference".

## Why this step exists

The library does not show whether a company still exists, filed for bankruptcy, was delisted, deregistered or acquired. Its company record holds only the SEC CIKs it lists and selected form types: a parent, listed or successor registrant may file under another CIK, and forms such as Form 25 or Form 15 may be absent from the store. The latest filing in the store is not a statement about the company today. Delisted, deregistered and dissolved are three different states (research file, changes and conflicts item 9).

Never infer status from press, from memory, from a filing gap or from the date of the latest filing. Status comes only from the company's own primary filings or its register, read with the date read.

## The status step (every skill that profiles, compares, monitors or records a named company)

**Named companies already read (check first).** `references/named-company-status.md` holds what the filings and FDA records stated on 20 October 2026 for Pear Therapeutics, Akili, Big Health and Aidoc, and the current FDA listing holders of Somryst, EndeavorRx, reSET, reSET-O, SleepioRx and DaylightRx (SP-148 to SP-169). For a company covered there, the status line quotes those rows with the source name and date in plain words ("Pear 8-K, 7 April 2023 (SP-156 [WF])") and what each form does not mean; for a product, the current listing holder is stated apart from the company that was authorized. "Status: [GAP]: not read" stays only for companies and registers no row covers. Filings dated after 20 October 2026 are not covered: say "as read on 20 October 2026".

1. **Registrants.** List the CIKs and register numbers the library returned. Say: "SEC filings in the store are those under CIK(s) [as returned]; other registrants and form types are not shown." Where the person names a parent, listed entity or former name, add it. The EDGAR submissions record gives current name, former names, exchanges and tickers (DL-150), and needs no API key (DL-152).
2. **Read the primary record where it can be opened.** For each registrant, look for these forms and items and quote form, item, filing date and URL:

| Record | What it states | What it does not mean | Rows |
|---|---|---|---|
| 8-K Item 1.03 | A receiver was appointed or a court took jurisdiction over substantially all assets (including Chapter 11 with management in possession); names the court and date | Not liquidation or dissolution. Without a later 1.03(b) report confirming a plan, the outcome is open on EDGAR (inference) | DL-136, DL-137 |
| 8-K Item 2.01 | The registrant completed an acquisition or disposition of a significant amount of assets: date, counterparty, consideration | Not signing. Read which side the registrant was on; it does not by itself mean the registrant was acquired | DL-138 |
| 8-K Item 3.01 | The exchange gave notice of a continued-listing failure or applied to delist, or the board acted to withdraw or transfer the listing | A deficiency notice is not yet a delisting (inference); a 3.01 can mean a transfer to another exchange, not distress | DL-139, DL-140 |
| 8-K Item 5.01 | A change in control: who acquired control, when, the basis and percentage, the consideration, from whom | Not dissolution; the company may continue under new control | DL-141 |
| Form 25 | The exchange or issuer struck a class from listing; effective 10 days after filing, 12(b) withdrawal after 90 days | Not dissolution and not the end of SEC reporting: 12(g) and 15(d) duties are unaffected. After a merger it signals that the old shares were converted, not that the business failed (inference) | DL-142 to DL-145 |
| Form 15 | The issuer certified it is below the holder thresholds and suspended SEC reporting (12g-4 or 12h-3); reporting stops at once | Not dissolution: the company stopped SEC reporting, not existing, and must resume if holder counts rise (inference). Filed by a successor after a merger, it is a sign of acquisition (inference) | DL-146 to DL-149 |
| US bankruptcy docket | Case and docket information through PACER (account, fees) or the court clerk's terminals; the Case Locator searches parties nationwide | No source read says which bankruptcy filings are public or sealed `[GAP]` | DL-154 to DL-156 |
| Companies House `company_status` | One of twelve values (active, dissolved, liquidation, receivership, administration, voluntary-arrangement, converted-closed, insolvency-proceedings and others); `date_of_cessation` dates closure, dissolution or removal | "Active" alone can hide a pending strike-off (inference); "liquidation" is a path to dissolved, not yet dissolved (inference); administration can still end in winding up | DL-157 to DL-164 |
| German insolvency notices | Courts publish at insolvenzbekanntmachungen.de; notice deemed given two days after publication | No hit today is not proof of no past insolvency: notices are deleted at the latest six months after proceedings end (inference). Registerportal structured data is a non-binding service; confirm on the official extract (inference) | DL-165 to DL-168 |

Dates: an 8-K trails its event by up to four business days (DL-135). Exchange continued-listing rules and cure periods, the Form 25 and Form 15 forms themselves, The Gazette notices and German register law were not read: `[GAP]`. Other jurisdictions (for example Swiss Zefix, not loaded in the library and not sourced): `[GAP]`.

3. **If the record cannot be opened**, write status "`[GAP]`: not read" and list the exact records to open: the registrant's EDGAR filing list for each CIK (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15), PACER for a bankruptcy docket, the Companies House company profile, the German insolvency notice site. Never fill the status from press or memory.
4. **Report** one status line per company: "Status as the record states: FORM ITEM, DATE, URL, read on DATE; what it does not mean: ..." or "Status: `[GAP]`: not read; open: ...". A status line is a fact about a filing, never a judgment about the company's prospects.

## Requests to outside sites

Requests to SEC, Companies House or any other site never carry the user's email address, name or any account identifier. SEC fair access asks automated clients to declare a User-Agent with a company name and an admin contact, at no more than 10 requests per second; requests without it were refused on the research pass (DL-153). So: ask the person which contact their organization uses for automated SEC access and use only that; if they give none, do not send a request and list the filings to open instead. Never invent a contact.

## The change-log window

The library change log (`diligence-dh.get_deltas`) began on 12 October 2026 (`first_entry_at` in the saved outputs of 19 October 2026). When the period the person asks about starts before 12 October 2026:

- Say so first: "The library change log began on 12 October 2026; it covers [12 October 2026 to the last sweep date] of your window, not [the start date to 11 October 2026]."
- Never report "no change" for the uncovered span. "No change recorded" covers only the log window.
- Offer instead the company's dated primary filings and authorization records for that span: the funding signals already saved (for example Pear: SEC filings in the store up to 10 April 2023, the latest filing in the store and not a statement about the company today), the EDGAR filing list for each CIK, FDA and DiGA records, and the status step above.
