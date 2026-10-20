# Screening rules: what the screen covers and how to read each record

Every rule cites its row in `diligence-research.md` (DL rows, read 20 October 2026) or `hta-and-directory-research.md` (DE rows, read 19 October 2026), or the saved library output it was observed in (`examples/live/`, saved 19 October 2026). Rows marked "(inference)" in the research are the research reader's reading across several items; say so when you apply one.

## 1. The screen is the store, not the market

- The library's market screen "covers only the companies the store holds, not the market" (`screen_market` perimeter statement, `examples/live/diligence_screen_market_dtx_EU.json`). On 19 October 2026 the store held 2,205 companies, loaded the segment `dtx` only, and the jurisdictions CA, EU, TW and US.
- `segment: dtx, jurisdiction: EU` returned one company (Novasight, Ltd., Israel). German DiGA makers are not in this screen, although the DiGA directory mirror holds 82 records: the same response lists `diga_verzeichnis` (82 records) as loaded and the DiGA directory feed as not loaded ("access under section 21 DiGAV not yet granted"). An empty or short screen is a coverage limit, never an empty market.
- `segment: dtx` over all jurisdictions gave 18 matches; the ten returned were all US companies (`examples/live/screen_market_dtx_via_peer_screen.json`).
- Ranking inside the screen is "evidence maturity score, highest first, then company name; no other weighting". It is the library's sort order, not a ranking of targets.
- Not loaded on 19 October 2026, with the reasons the library gives: Companies House ("API key not yet provisioned"), Zefix ("credentials not available"), the DiGA directory feed ("access under section 21 DiGAV not yet granted"), NICE ("commercial licence deferred until the Market Access product"), private funding ("no funding source licensed or integrated") (`examples/live/list_commercial_dh_sources.json`). Every field that depends on one of these is `[GAP]`.

## 2. How to read each register and filing

| Record | What it shows | What it does not show | Rows |
|---|---|---|---|
| FDA establishment registration and device listing | That an establishment registered and listed devices; where premarket authorization is required, the listing should carry the submission number | Approval. "Registration ... does not in any way denote approval". A listed device with no number may be exempt or may need checking (inference) | DL-126, DL-127, DL-130 |
| FDA registration and listing database | Weekly updates, "generally completed weekly by Monday evening" | Same-week uploads: public data lags | DL-129 |
| 510(k) clearance | Substantial equivalence; summaries on the web interface for more recent records only | Approval: calling a 510(k) "approval" is misbranding | DL-128, DL-131 |
| Devices@FDA | 510(k) and PMA records | De Novo orders, which sit in a separate database: a Devices@FDA search alone can miss a De Novo (inference) | DL-132 |
| FDA databases by name | Records under the applicant or requester | A device cleared under a parent, predecessor or acquired entity does not show under the current brand (inference) | DL-133 |
| DiGA directory | Listed DiGA, evidence and study summaries with registry links, prices, and the reasons for any delisting | Which manufacturers applied or which products were refused: BfArM gives only aggregate counts | DE30, DE32 |
| DiGA announcements | New listings, changes and delistings in the Federal Gazette, quarterly as a rule | Refusals | DE31 |
| DiGA statistics | As of 9 September 2026: 62 listed, 29 refused, 131 withdrawn, 14 in review, 18 delisted (7 at the manufacturer's request) | Names behind the counts | DE34 |
| SEC Form D | A notice of an exempt offering under Rule 504 or 506; executive officers, directors and promoters; industry group; revenue range or "Decline to Disclose"; total offering amount and amount sold as of filing; number of investors; amount paid to named insiders | Valuation, price per share, lead investor or investor names (DL-018 (inference)). "Digital health" as an industry code: software companies may be coded as Technology (inference) | DL-001, DL-012 to DL-018 |
| Form D dates and amounts | Filed within 15 days after the first sale, the date the first investor is irrevocably committed; amended at least annually while the offering continues | Closing or announcement date. A change in amount sold or number of investors needs no amendment, so "amount sold" can be stale | DL-002, DL-004 to DL-006 |
| Rule 506(b) or 506(c) box | 506(c): every purchaser accredited and verified, "not subject to limitation on manner of offering", which signals a publicly marketed raise | Who bought | DL-010, DL-011 |
| Form 8-K | Events within four business days; Item 1.01 material definitive agreements (date, parties, material terms); Item 2.01 completed significant acquisitions with consideration; Item 1.05 material cybersecurity incidents | Deals below the significance test (10 percent of total assets): smaller tuck-ins may never appear in an 8-K (inference) | DL-019 to DL-024 |
| Form 10-K and S-1 | Business (S-K Item 101: regulation, headcount, and for smaller companies the status of government approval of principal products), risk factors (S-K Item 105), cybersecurity (Item 1C) | Risk factors for smaller reporting companies, which need not provide them: absence is not a signal of low risk (inference) | DL-025 to DL-031 |
| EDGAR full-text search | All electronic filings since 2001 with exhibits; Boolean, exact phrase, NEAR and wildcard syntax | Natural-language queries; filings before 2001 | DL-032, DL-033 |
| UK Companies House | Annual confirmation statement (directors, PSC, registered office; statement of capital and shareholders where updated); accounts within 9 months (private) or 6 months (public) | A profit and loss account for small companies and micro-entities, which may omit it today; from 1 April 2028 small companies must deliver it but may opt out of publishing it | DL-034 to DL-043 |
| HHS OCR breach portal | Breaches of unsecured PHI affecting 500 or more individuals: entity, state, type, individuals affected, submission date, breach type, location, business associate present | Breaches under 500; older or closed cases sit in the archive, not the main 24-month list; a vendor's breach may appear under its client's name (inference) | DL-092, DL-095 to DL-097 |

When a register shows nothing, word it with `gap-rules.md`: the register was searched and holds no row, the lookup used the wrong name, or the register is not loaded. Never "not authorized", "no breach" or "no funding".

## 3. Evidence maturity in a screen

- The library score: "score = round(100 x points earned / assessable maximum); a component whose source is not loaded is excluded from the maximum, not counted as zero"; rubric v1 of 7 October 2026; components regulatory status (30), clinical evidence (40), active development (10), product breadth (10); reimbursement and jurisdiction breadth excluded as not assessable. Its own limit: "a stated convention for comparing documented evidence, not a predictive model or a valuation" (`market-segmentation-and-gtm-strategy/examples/live/evidence_maturity_K191716_somnio.json`, saved 19 October 2026). Write it as "N of M assessable points (rubric v1)", never as a grade.
- Published frameworks disagree on what counts and none was built for investors (DL "Changes and conflicts" item 8):
  - Evidence DEFINED [PAPER] (DL-107 to DL-115, DOI 10.1038/s41746-023-00836-5): built for payers, PBMs, health systems, pharma and societies, not investors (DL-108); several authors employed by a health insurer (DL-115).
  - Clinical robustness score [PAPER] (DL-116 to DL-118, DOI 10.2196/37677): FDA filings plus registered trials; 44 percent of 224 US venture-backed companies scored 0 and the score did not correlate with funding (DL-117); its own limits include selection bias and authors at the firm whose database supplied the cohort (DL-118).
  - Critique [PAPER] (DL-119, DOI 10.2196/41715): summing trials and filings is too narrow for services not regulated by FDA.
- Funding is not a proxy for evidence: in a dementia-prevention sample, 7 of 10 top-funded companies had no qualifying evidence [PAPER] (DL-124, DOI 10.1371/journal.pone.0323390). Commercial funding databases may lack full funding details, so a vendor funding total is a claim (DL-125, the last sentence an inference).
- The full assessment of one company's evidence against a named framework is `company-and-evidence-assessment` (this pack). Here the score is context in a long list only.

## 4. What no source gives

Market size, valuation multiples, return benchmarks and sector funding totals are not sourced by design: the only sources are vendors and data firms (DL "Not sourced"). The model never supplies one. A vendor figure the person brings is labeled "your figure (vendor: NAME, as you supplied it)" and never used to rank.

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
