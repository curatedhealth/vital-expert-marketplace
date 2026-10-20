# Public record rules: what each record shows, and what it does not

Interpretive reference for A1 (company profile) and B1 (assessment record). Every rule cites its row in the copied research files: `diligence-research.md` (DL rows, read 20 October 2026), `reg-pathways-submissions-research.md` (US- and EU- rows), `hta-submissions-research.md` (DE and UK rows), `clinical-study-and-rwe-research.md` (CV rows), all read 19 October 2026 unless stated. Rows the research file marks "(inference)" are the researcher's reading across items, not a quoted rule: label it "(inference)" every time it is cited.

The rule behind the whole file: describe a company only by what its record or primary filing states (pack rule 3). A record that is silent is a gap, never a negative fact.

## 1. US securities filings (SEC EDGAR)

| Record | What it states | What it does not state | Rows |
|---|---|---|---|
| Form D | Notice of an exempt offering under Rule 504 or 506 or Section 4(a)(5) (DL-001). Names executive officers, directors and promoters (DL-012). Total offering amount and amount sold as of the filing date; "Indefinite" allowed (DL-015). Number of investors, not names (DL-016). Revenue range, or "Decline to Disclose" (DL-014). | No valuation, price per share, lead investor or investor names (DL-018 (inference)). Amount sold need not be updated (DL-006), so it can be stale. Filing date tracks the first sale, the date the first investor is irrevocably committed, not a close or an announcement (DL-002). No "digital health" industry code, so a software company may be coded Technology (DL-013 (inference)). | DL-001 to DL-018 |
| Form D, 506(b) or 506(c) box | 506(c) is "not subject to limitation on manner of offering", all purchasers accredited and verified (DL-010, DL-011). | Whether the raise closed, or for how much. | DL-008 to DL-011 |
| Form 8-K | Generally filed within four business days of the event (DL-019). Item 1.01: material definitive agreement, with date, parties and material terms (DL-020, DL-021). Item 2.01: completed significant acquisition, with consideration (DL-022). Item 1.05: material cybersecurity incident, within four business days of the materiality determination (DL-024). | A deal below the 10 percent significance test may never appear (DL-023 (inference)). The library's filing rows carry no item number (see `tools.md`), so the item must be read at the filing URL. | DL-019 to DL-024 |
| Form 10-K and S-1 | Business section under S-K Item 101, including material effects of government regulation and headcount (DL-025, DL-029, DL-031). Smaller reporting companies discuss the status of any government approval not yet received (DL-030). Cybersecurity section (DL-027). | Smaller reporting companies need not give risk factors in the 10-K; their absence is not a low-risk signal (DL-026 (inference)). An approval status written in a filing is the company's own statement: check it against the FDA databases (DL-030). | DL-025 to DL-031 |
| EDGAR full-text search | Covers electronic filings since 2001, with exhibits (DL-032). Boolean and NEAR syntax, no natural-language queries (DL-033). | Filings before 2001. | DL-032, DL-033 |

## 2. UK company records (Companies House)

| Record | What it states | What it does not state | Rows |
|---|---|---|---|
| Confirmation statement | Filed at least once a year by every company, confirming directors, people with significant control, registered office, and optionally capital and shareholders (DL-034, DL-035). Not accepted until all directors have verified their identity (DL-036). Due within 14 days after the review period (DL-037, DL-038). | Trading performance. | DL-034 to DL-038 |
| Annual accounts | Public (DL-040). Private companies file within 9 months, public within 6 (DL-039). | Small companies and micro-entities may omit the profit and loss account today, so a filing may show a balance sheet and no revenue (DL-040). From 1 April 2028 small companies must deliver the profit and loss account but may opt out of publishing it (DL-042). Size thresholds changed for periods from 6 April 2025 (DL-041). | DL-039 to DL-043 |

The library does not load Companies House ("API key not yet provisioned", `list_commercial_dh_sources`, 19 October 2026). A UK fact therefore comes from the person or a direct read of the register, and says so.

## 3. Device and listing records

| Record | What it states | What it does not state | Rows |
|---|---|---|---|
| FDA registration and listing | That an establishment registered and listed a device; where premarket authorization is required, the listing should carry the submission number (DL-130). | Approval. "Registration ... does not in any way denote approval" (DL-126, DL-127). Public data lag uploads, updated generally weekly (DL-129). | DL-126, DL-127, DL-129, DL-130 |
| 510(k) record | A substantial-equivalence determination, searchable by number, applicant, device name or product code (US-65, DL-131). | Approval: representing a clearance as approval is misbranding (DL-128). Summaries exist only for more recent records (DL-131). | US-65, DL-128, DL-131 |
| De Novo record | De Novo classification orders sit in their own database (US-66). | A Devices@FDA search alone can miss a De Novo (DL-132 (inference)). | US-66, DL-132 |
| Applicant name | Records are searched by applicant or requester. | A device cleared under a parent, predecessor or acquired entity will not show under the current brand (DL-133 (inference)). | DL-133 |
| openFDA | 510(k) endpoint counts and its last update (US-69). | openFDA says its results are unvalidated (US-69). | US-69 |
| EUDAMED | Actor registration, UDI and device registration, notified bodies and certificates, and market surveillance became mandatory on 28 May 2026 (EU-36, EU-37). | Vigilance and clinical investigation modules are still in development (EU-38). | EU-36 to EU-39 |
| DiGA directory (Germany) | Listed DiGA, evidence and study summaries with registry links, prices, and the reasons for any delisting (DE30). Listings, changes and delistings are announced in the Federal Gazette, quarterly as a rule (DE31). | Refusals: BfArM does not disclose which manufacturers applied or were refused; only aggregate counts are published (DE32). A company's refused or withdrawn application will not appear. | DE30 to DE34 |

## 4. Trial registries

| Record | What it states | What it does not state | Rows |
|---|---|---|---|
| ClinicalTrials.gov or a WHO primary registry | Registration of a trial; the ICMJE requires registration at or before first enrollment (CV132); US applicable trials register within 21 days of first enrollment (CV141). | Results: posting follows its own clocks (US: 1 year after primary completion, CV145, with certified delays, CV146; WHO norm 12 months, CV140); a registered trial without results is not a negative result. DiGA studies must be registered and published within 12 months of completion (DE14). | CV132, CV140, CV141, CV145, CV146, DE14 |

## 5. Health data incidents

| Record | What it states | What it does not state | Rows |
|---|---|---|---|
| HHS OCR breach portal | Breaches of unsecured PHI affecting 500 or more individuals (DL-095), with entity, state, type, individuals affected, submission date, breach type, location and business associate presence (DL-097). The main list holds the last 24 months under investigation; older or closed breaches sit in an archive (DL-096). | Breaches under 500 (they are logged and reported yearly, DL-092 (inference)). A vendor's breach may appear under its client's name (DL-097 (inference)). The library holds no breach portal feed: this is a direct read, and says so. | DL-092, DL-095 to DL-098 |
| The company's own breach file | Presumption of breach unless a four-factor risk assessment shows low probability of compromise (DL-086, DL-087); the covered entity or business associate carries the burden of proof (DL-094). | Anything, until the person obtains it. Ask for the assessments, not only counts (DL-087 (inference)). | DL-086 to DL-094 |

## 6. Company status

Whether the company still exists, filed for bankruptcy, was delisted, deregistered or acquired is not in the library. It is read from 8-K Items 1.03, 2.01, 3.01 and 5.01, Form 25, Form 15, Companies House `company_status` and German insolvency notices, by the step in `company-status.md` (DL-135 to DL-168). A Form 15 or Form 25 is not dissolution (DL-144; DL-149 (inference)). Not read means "Status: [GAP]: not read", never a guess.

## 7. What no record states (never supply it)

Market size, valuation multiples, return benchmarks and funding totals by sector are not sourced by design (`diligence-research.md`, "Not sourced"). Revenue, runway, burn, customers, outcomes and intent are not stated by any record above. Vendor funding databases can be incomplete (DL-125 (inference)): a funding total the person brings is labeled as theirs.
