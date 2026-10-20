# Monitoring signals: what counts as a change, the clocks, and dated rule changes

Every rule cites its row in `diligence-research.md` (DL, read 20 October 2026), `hta-and-directory-research.md` (DE, read 19 October 2026) or `ai-ml-regulation-research.md` (EU and US, read 19 October 2026), or the saved library output it was observed in (`examples/live/`, saved 19 October 2026). A signal is a reason to look again, never a verdict on a company.

## 1. The library's change log

- `diligence-dh.get_deltas` reports per company "no change recorded" or the changes, plus its log: on 19 October 2026 the first entry was 12 October 2026, the last entry 16 October 2026, the last sweep 19 October 2026 (`examples/live/diligence_deltas_Akili_Pear.json`).
- Its own limits, quoted: "the since filter uses event dates (filing signal_date, authorization decision_date, study start_date, safety event_date), not observed_at (load time)"; "the change log began on the first_entry_at date; older clearances loaded before the log existed may have no entries"; "no change recorded is a statement about in-window event-dated log rows up to last_sweep_at".
- So: a "since" date before 12 October 2026 can miss changes that were loaded before the log existed; a change with an old event date loaded today may be filtered out by the event-date rule; "no change recorded" never means "nothing happened".
- Every change source depends on the perimeter: Companies House, Zefix, the DiGA directory feed, NICE and private funding were not loaded on 19 October 2026 (`examples/live/list_commercial_dh_sources.json`). No change can be seen in a source that is not loaded.

## 2. What counts as a change, by record

| Record | Change the log can carry | Clock or cadence (row) | Read it as |
|---|---|---|---|
| FDA authorization | New decision (510(k), De Novo, PMA) by decision date | Registration and listing data generally updated weekly; public data lags uploads (DL-129) | Clearance or grant as stated; a 510(k) is never "approval" (DL-128) |
| Registered study | New study by start date | not sourced `[GAP]` | A study registered, not a result |
| Safety record | New stored safety record by event date | not sourced `[GAP]` | The record as stated; never a judgment of the product |
| SEC Form D | New notice or amendment | Within 15 days after first sale (DL-002, DL-004); amended at least annually while continuing (DL-005); amount sold need not be updated (DL-006) | An offering the company stated; no valuation or investors (DL-018) |
| SEC Form 8-K | Event report | Within four business days (DL-019); Item 1.01 material agreements (DL-020); Item 2.01 significant acquisitions (DL-022, DL-023); Item 1.05 cyber incidents within four business days of the materiality determination (DL-024) | The item as filed; the library's filing rows carry no item number, so open the filing at its URL (`tools.md`) |
| SEC 10-K | Annual report | not sourced in this skill `[GAP]` | Business, risk factors, cybersecurity sections (DL-025 to DL-027) |
| UK Companies House | Confirmation statement, accounts | Confirmation statement at least yearly, within 14 days after the review period (DL-034, DL-037, DL-038); accounts within 9 months (private) or 6 months (public) (DL-039) | Not loaded in the library: check at the authority |
| HHS OCR breach portal | New breach of 500 or more | Main list covers breaches reported within the last 24 months under investigation; older or closed in the archive (DL-095, DL-096) | Not loaded in the library: check both views at the authority |
| DiGA directory | Listing, change, delisting | Federal Gazette announcements quarterly as a rule (DE31); directory shows delisting reasons (DE30); refusals not published (DE32) | Status as stated; listing is not evidence of effect |
| FDA AI-enabled device list | New entries | Updated "periodically", no fixed cadence; not comprehensive (US-24 to US-26) | A listing, not a complete census |

A missing filing is not a signal of anything by itself: smaller reporting companies need not give risk factors (DL-026 (inference)), small UK companies may omit the profit and loss account (DL-040), and deals below the 8-K significance test may never be reported (DL-023 (inference)). Whether a company still exists is read only from the records in section 5, never from a quiet log or a missing filing.

## 3. Dated rule and register changes (as read on the row dates)

| Date | Change | Instrument | Rows | Status |
|---|---|---|---|---|
| 6 April 2025 | UK company size thresholds changed for periods from this date | Companies House guidance | DL-041 | In force |
| 18 November 2025 | Confirmation statements refused until all directors verify identity (guidance updated) | Companies House guidance | DL-036 | In force |
| 19 December 2025 | Swiss Investment Screening Act adopted; referendum period ended 17 April 2026; SECO plans entry into force in 2027; no applications yet | BBl 2026 31; SECO page | DL-081, DL-082 | Adopted, not in force |
| 12 February 2026 | New HSR form vacated; stay denied 19 March 2026; FTC accepts the pre-February 2025 form; appeal pending on the pages read | FTC page; Chamber of Commerce v. FTC | DL-051 to DL-053 | Litigation pending |
| 17 February 2026 | HSR 2026 thresholds and fees apply (size of transaction USD 133.9 million) | 91 FR 2133, 16 January 2026 | DL-044 to DL-049 | In force; revised every year |
| 25 March 2026 | FTC and DOJ request comment on the HSR form (due 26 May 2026); FTC considering a new rulemaking; later status not found | FTC press release | DL-054 | Open `[GAP]` after 26 May 2026 |
| 12 June 2026 | Swiss IPG ordinance consultation opened, to 5 October 2026 | admin.ch | DL-085 | Consultation closed; ordinance text not read `[GAP]` |
| 17 June 2026 | EU Regulation 2026/1386 on screening foreign investments adopted; some provisions from 16 July 2026; applies and repeals 2019/452 from 17 January 2028 | OJ L, 26 June 2026 | DL-074, DL-075 | Adopted; 2019/452 governs until 17 January 2028 |
| 27 July 2026 | AI Act Digital Omnibus (Regulation (EU) 2026/1744 of 8 July 2026) in force; high-risk obligations deferred to 2 December 2027 (Annex III) and 2 August 2028 (Annex I, including MDR and IVDR devices); new prohibited points from 2 December 2026 | OJ L, 24 July 2026 | EU-17 to EU-19, EU-21 (original dates EU-14) | In force; obligations dated |
| 9 September 2026 | DiGA statistics: 62 listed, 29 refused, 131 withdrawn, 14 in review, 18 delisted (7 at the manufacturer's request) | BfArM page | DE34 | Snapshot |
| 1 April 2028 | UK small companies must deliver the profit and loss account (may opt out of publishing); abridged accounts end; commercial software only | Companies House guidance | DL-042, DL-043 | Announced; opt-out mechanism "to be confirmed" (DL conflicts item 5) |

Not sourced here: the 2025 HSR figures, national FDI laws, CFIUS fees and timelines, state health privacy laws (DL "Not sourced"). Write `[GAP]` and name the owner who would know.

## 4. What a change can touch (hypotheses only)

For each change, at most one line on which of the person's own triggers it could touch, labeled "hypothesis for review": for example a new authorization against a trigger "regulatory status changes"; a new Form D against "new financing filed"; an 8-K against "material agreement or acquisition". Never infer intent, distress, revenue or a valuation. Funding filings are not a proxy for evidence [PAPER] (DL-117, DOI 10.2196/37677; DL-124, DOI 10.1371/journal.pone.0323390).

## 5. Company status: does the company still exist, and in what form?

The library does not show whether a company still exists, filed for bankruptcy or insolvency, was delisted, deregistered or acquired. Its funding rows carry filing dates and form types only, with no 8-K item number (`tools.md`), and Companies House is not loaded. The latest filing date in the store is "latest filing in the store", never a status. Status comes only from the company's own primary filings or its register entry, read by the assistant or by the person. Never infer status from press, memory, a quiet log or a missing filing.

### The status step

**Named companies already read (check first).** `references/named-company-status.md` holds what the filings and FDA records stated on 20 October 2026 for Pear Therapeutics, Akili, Big Health and Aidoc, and the current FDA listing holders of Somryst, EndeavorRx, reSET, reSET-O, SleepioRx and DaylightRx (SP-148 to SP-169). For a company covered there, the status line quotes those rows with the source name and date in plain words ("Pear 8-K, 7 April 2023 (SP-156 [WF])") and what each form does not mean; for a product, the current listing holder is stated apart from the company that was authorized. "Status: [GAP]: not read" stays only for companies and registers no row covers. Filings dated after 20 October 2026 are not covered: say "as read on 20 October 2026".

1. For each named company the answer profiles, compares, monitors or writes a record about, list the primary records that would carry its status (table below), with the identifier to use (SEC CIK, UK company number, German court and register number).
2. If the assistant can open them, read them and quote the status as the record states it: form or item, filing date, source URL, read date. Read each with its "does not mean" line.
3. If the assistant cannot open them, do not guess. Write, per company: "Status: [GAP]: not read. Filings to open: ..." and list the exact filings and where to find them.
4. One status line per company. In a long list of more than five companies, one gap line may cover the whole list, naming the filings to open per company on request.

### What each record shows and does not mean

| Record | What it shows | What it does not mean | Rows |
|---|---|---|---|
| Form 8-K, any item | An event report, due within four business days of the event unless the item says otherwise | The event date: the 8-K date can trail the event by up to four business days | DL-135 |
| 8-K Item 1.03 | A receiver appointed, or a court took jurisdiction over substantially all assets, including Chapter 11 with management in possession; names the proceeding, court and date | The outcome. A later Item 1.03(b) report follows a confirmed plan; a first 1.03 with no later (b) report means the outcome is still open on EDGAR (inference) | DL-136, DL-137 |
| 8-K Item 2.01 | Completion of an acquisition or disposition of a significant amount of assets: completion date, counterparty, consideration | A signing: it marks closing. Deals below the significance test may never appear (DL-023 (inference)) | DL-138 |
| 8-K Item 3.01 | An exchange notice of a failed continued-listing standard, an exchange application to delist, or a board decision to withdraw or transfer a listing | A delisting: a deficiency notice is not yet a delisting (inference), and a 3.01 can mean a transfer to another exchange, not distress | DL-139, DL-140 |
| 8-K Item 5.01 | A change in control: who acquired control, when, the basis and percentage of voting securities, the consideration, and from whom | That the company ceased to exist | DL-141 |
| Form 25 | Exchange delisting of a class; effective 10 days after filing; Section 12(b) withdrawal effective 90 days after filing or sooner; a voluntary delisting needs a press release with reasons | Dissolution or failure. After a merger it signals that the old shares were converted (inference); it does not end Section 12(g) registration or Section 15(d) reporting, so a delisted company may still file | DL-142 to DL-145 |
| Form 15 | The company stopped SEC reporting: Rule 12g-4 (fewer than 300 holders of record, or fewer than 500 with assets of USD 10 million or less) or Rule 12h-3; filing duty suspended at once; after a merger the successor files it | Dissolution. Form 15 is not dissolution; under 12h-3 reporting resumes if the thresholds are no longer met. A Form 15 filed by an acquirer for the target is a sign of acquisition (inference) | DL-146 to DL-149 |
| EDGAR submissions API | Each entity's filing history with current name, former names, exchanges and tickers; recent filings cover at least one year or 1,000 filings; no key needed | Status by itself: it lists filings to open. Read through a fetch tool [WF] | DL-150 to DL-152 |
| PACER bankruptcy dockets | Federal bankruptcy case and docket information for account holders, a nationwide party search updated daily, and a free telephone line at every bankruptcy court; fees of 10 cents a page, capped at USD 3.00 per document | Anything without an account: the assistant usually cannot open it; list it for the person | DL-154 to DL-156 |
| Companies House `company_status` | One of twelve values (active, dissolved, liquidation, receivership, administration, voluntary-arrangement, converted-closed, insolvency-proceedings, registered, removed, closed, open); `company_status_detail` adds states such as a pending strike-off or a petition to restore; `date_of_cessation`; insolvency through `links.insolvency` (the older flags are deprecated) | "Active" alone: it can hide a pending strike-off (inference). Labels differ on screen ("In Administration", "Receiver Action") | DL-157 to DL-161 |
| UK strike-off, liquidation, administration | Struck off means dissolved; a company in liquidation ceases to exist once struck off (so "liquidation" is a path to "dissolved" (inference)); in administration an insolvency practitioner takes control and the appointment is published in The Gazette, and the company can still be wound up | That administration means the company has ceased to exist | DL-162 to DL-164 |
| German insolvency notices (insolvenzbekanntmachungen.de) | The official site where insolvency courts publish notices; notice is deemed given two days after publication | A clean past: insolvency data is deleted at the latest six months after the proceedings end, so no hit today does not prove no past insolvency (inference). Look-alike private registers exist | DL-165 to DL-167 |
| German Registerportal (handelsregister.de) | The commercial and other registers of all states | Binding status: its structured data is a non-binding service that may differ from the current extract; confirm on the official extract (inference) | DL-168 |

### Requests to outside sites

Requests to outside sites never carry the person's email address or name. SEC asks automated clients to declare a User-Agent with a contact and caps requests at 10 per second (DL-153 [WF]); requests without one were refused on the research pass. Ask the person which contact their organization uses for SEC access; if none is given, do not fetch from SEC: list the filings to open (company, CIK, form and item, date range) and mark status "[GAP]: not read". Never invent a contact.

### Missing fields stay missing

Where a saved record lacks a field, write "not in the record" (or "not in saved output" for a saved library file). Never print 0, "none" or a country for it. A `jurisdictions` list is where authorizations sit, not where the company is incorporated: quote the `country` field as stored ("country: US, as stored") and never write "a US company" unless a primary record states its domicile.
