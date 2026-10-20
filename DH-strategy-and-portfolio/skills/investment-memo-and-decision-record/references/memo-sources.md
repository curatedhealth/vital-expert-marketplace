# Memo sources: what each public record shows and does not show

Source: `diligence-research.md` (DL rows, read 20 October 2026) and `channels-partners-launch-sources.md` (CP rows, read 19 October 2026). Interpretive reference for A1 and B1. Every line carries its row; rows marked "(inference)" in the research file are the researcher's reading and are labeled here too.

## 1. SEC Form D (Regulation D offerings)

| What it shows | Row |
|---|---|
| A notice of an exempt offering under Rule 504 or 506 or Section 4(a)(5) | DL-001 |
| Filed within 15 days after first sale; first sale is when the first investor is irrevocably committed, so the date tracks commitment, not closing or announcement | DL-002, DL-004 |
| No SEC fee; filed through EDGAR | DL-003 |
| Amended at least annually while the offering continues | DL-005 |
| Names executive officers, directors and promoters (Item 3): usable to confirm leadership names | DL-012 |
| Health Care industry subgroups; there is no "digital health" code (inference) | DL-013 |
| Revenue range may be "Decline to Disclose" | DL-014 |
| Total offering amount and amount sold as of filing; "Indefinite" allowed | DL-015 |
| Number of investors, not their names | DL-016 |
| Only use-of-proceeds field: amounts paid to named officers, directors, promoters | DL-017 |

| What it does not show | Row |
|---|---|
| Valuation, price per share, lead investor, investor names: a valuation must not be inferred from a Form D (DL-018 (inference)) | DL-018 |
| A current amount sold: no amendment is required for a change in amount sold or investor count, or after the offering ends, so the figure can be stale | DL-006 |
| Whether the raise was publicly marketed, except through the 506(b) or 506(c) box (506(c) is not subject to the limit on manner of offering) | DL-011 |

Memo wording: "Form D filed DATE states amount sold USD X as of filing (DL-015); Form D does not show valuation or investor names (DL-016, DL-018); the amount may be stale (DL-006)."

## 2. SEC current and periodic reports

| Report | What it shows | Row |
|---|---|---|
| 8-K | Generally due within four business days of the event | DL-019 |
| 8-K Item 1.01 | Material definitive agreements outside the ordinary course: date, parties, material relationship, material terms | DL-020, DL-021 |
| 8-K Item 2.01 | Completed significant acquisitions: date, assets, counterparty, nature and amount of consideration; smaller deals may never appear (inference) | DL-022, DL-023 |
| 8-K Item 1.05 | Material cybersecurity incidents, within four business days after the materiality determination | DL-024 |
| 10-K Item 1 | Business, under S-K Item 101: material effects of regulation, human capital including headcount | DL-025, DL-029 |
| 10-K Item 1A | Risk factors under S-K Item 105; smaller reporting companies need not provide them, so absence is not a signal of low risk (inference) | DL-026, DL-028 |
| 10-K Item 1C | Cybersecurity under S-K Item 106 (Item 106 text not read) | DL-027 |
| S-K 101 for smaller companies | Status of any government approval not yet received: where an FDA status claim sits; check it against FDA databases | DL-030 |
| S-1 | Pulls in S-K Items 105 and 101 | DL-031 |
| EDGAR full-text search | All electronic filings since 2001 incl. exhibits; Boolean, phrases, NEAR; no natural-language search | DL-032, DL-033 |

Library pitfall: `get_funding_signals` rows carry no 8-K item number and a null counterparty, so an Item 1.01 agreement cannot be told from other 8-K events without opening the filing at its URL (`tools.md`).

## 3. UK Companies House

| What it shows or requires | Row |
|---|---|
| Confirmation statement at least yearly, even for dormant companies | DL-034, DL-038 |
| It confirms directors, secretary, people with significant control, registered office and email; may update SIC code, capital and shareholders | DL-035 |
| Not accepted until all directors have verified identity | DL-036 |
| File within 14 days after the review period; fine up to GBP 5,000 and possible strike-off | DL-037 |
| Accounts: private 9 months, public 6 months after the reference date | DL-039 |
| Small and micro companies may file without a profit and loss account, so a UK filing may show no revenue | DL-040, DL-041 |
| From 1 April 2028 small companies must deliver the P&L (may opt out of publishing it); abridged accounts end; software filing only | DL-042, DL-043 |

The library does not load Companies House ("API key not yet provisioned", saved `compare_portfolio` output, 19 October 2026): every UK filing fact is `[GAP]` in the library and comes from the register itself, read by the person. PSC register rules and the public search help pages are not sourced.

## 4. FDA status as a diligence fact

| Fact | Row |
|---|---|
| Establishment registration or a registration number does not denote approval; an "FDA registered" or "FDA listed" claim is not a marketing authorization | DL-126, DL-127 |
| A 510(k) clearance does not denote approval; representing it as approval is misbranding | DL-128 |
| Registration and listing data lag uploads; updated generally weekly | DL-129 |
| A listing should carry the premarket number where one is required; a listing with no number may be exempt or may need checking (inference) | DL-130 |
| 510(k) summaries are online for more recent records only | DL-131 |
| Devices@FDA covers 510(k) and PMA; De Novo orders sit in a separate database, so a Devices@FDA search alone can miss a De Novo (inference) | DL-132 |
| FDA databases search by applicant or requester, so a device cleared under a parent, predecessor or acquired entity will not show under the current brand (inference) | DL-133 |

Memo wording: "cleared" for a 510(k), "granted" for a De Novo; never "approved" unless the record is a PMA. The pathway and what it means for the product are `dh-regulatory-and-quality` regulatory-pathway-and-classification.

## 5. Health data and breach records

| Fact | Row |
|---|---|
| HHS OCR portal lists breaches of unsecured PHI affecting 500 or more individuals | DL-095 |
| Main list: last 24 months and under investigation; older or closed ones in an archive: search both | DL-096 |
| Fields: entity, state, type, individuals affected, submission date, breach type, location, business associate present; a vendor's breach may appear under the client's name (inference) | DL-097 |
| Breaches under 500 are reported to HHS yearly and do not show in the portal (inference from DL-095) | DL-092 |
| Ask for the four-factor risk assessments, not only breach counts (inference) | DL-086, DL-087 |
| The covered entity or business associate carries the burden of proof: ask for its documentation | DL-094 |
| A business associate notifies the covered entity within 60 calendar days of discovery | CP-US-49 |
| A consumer health app outside HIPAA falls under the FTC Health Breach Notification Rule; unauthorized disclosure is a breach | CP-US-54, CP-US-55 |

The library holds no breach-portal source; a portal search is the person's, with its date. The HHS archive page and portal FAQ were not read (`[GAP]`).

## 6. Evidence frameworks (context for the memo's evidence section)

The evidence assessment itself is `company-and-evidence-assessment` (this pack). The memo carries its result with the framework's name and limits:

| Framework | What it does | Its own limits | Rows |
|---|---|---|---|
| Evidence DEFINED [PAPER] | Four steps: screen, GRADE, checklist, evidence-to-recommendation; levels 0 to 4 | Built for payers, PBMs, health systems, pharma, not investors; interrater reliability not quantified; authors employed by a health insurer; checklist items not quoted (supplement not read) | DL-107 to DL-115, DOI 10.1038/s41746-023-00836-5 |
| Clinical robustness score [PAPER] | Count of FDA filings plus registered trials | Proxies only; excludes publications; selection bias; authors at the funding-database firm | DL-116 to DL-118, DOI 10.2196/37677 |
| Critique [PAPER] | Argues the score is too narrow | Authors employed by a digital health company | DL-119, DOI 10.2196/41715 |
| Library evidence maturity | Rubric v1 (7 October 2026), points over assessable maximum | "a stated convention for comparing documented evidence, not a predictive model or a valuation"; "US sources only" | saved `evidence_maturity_K191716_somnio.json` |

Funding is not a proxy for evidence: in 224 venture-backed companies the robustness score did not correlate with funding (DL-117, DOI 10.2196/37677); in 10 top-funded dementia-prevention companies, 7 had no qualifying evidence (DL-124, DOI 10.1371/journal.pone.0323390). None of the frameworks was designed for investors (research file, changes and conflicts item 8). Never write "clinically validated" beyond a framework's own words.

## 7. Proposed memo headings (labeled "proposed"; the person's headings replace them)

Used only when the person gives no headings. Each heading lists what fills it.

1. Company and identity: identifiers, filing names, leadership names from Form D Item 3 (DL-012). Source: A1.
2. Products and authorizations: by register, with reference, pathway in words and decision date (DL-126 to DL-133). Source: A1.
3. Evidence: the framework applied by `company-and-evidence-assessment`, with its limits (section 6). Source: that skill, or A1's library evidence maturity labeled as the library's convention.
4. Filings and funding signals: by filing type, with what Form D does not show (section 1). Source: A1.
5. Safety and breach records: recalls and events as stated; breach portal search by the person (section 5). Source: A1 and the person.
6. Transaction and data flags: rule, figure, date and row; conclusion for the owner the person names for legal or compliance, or owner not named. Source: A2.
7. From you (non-public): data-room facts, kept apart.
8. Thesis, criteria, scores: the person's. Source: B1.
9. Decision, decider, date, dissent, conditions, open items: the person's. Source: B1.
10. Gaps and what the library cannot see.

## 8. Company status: operating, bankrupt, delisted, deregistered, acquired or dissolved

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
