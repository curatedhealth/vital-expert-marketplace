# Comparison rules: putting companies side by side without judging them

Interpretive reference for tasks A2 (investment portfolio comparison table) and B1 (scored comparison and decision record). Rows from `diligence-research.md` (prefix DL, read 20 October 2026); library behavior from saved live outputs of 19 October 2026 (`references/tools.md`).

DOIs for the [PAPER] rows used here: DL-107 to DL-115 Evidence DEFINED (Silberman 2023), DOI 10.1038/s41746-023-00836-5; DL-116 to DL-118 clinical robustness score (Day 2022), DOI 10.2196/37677; DL-119 critique letter (Marshall 2023), DOI 10.2196/41715; DL-120 and DL-121 Digital Health Scorecard (Sedhom 2021), DOI 10.1038/s41746-021-00476-7; DL-122 and DL-123 DiMe evaluation framework (Goldsack 2025), DOI 10.1038/s41598-025-21996-2; DL-124 and DL-125 (Vinay 2025), DOI 10.1371/journal.pone.0323390.

## 1. What a comparison row may hold

A row holds what a record or primary filing states, with the date and the source: authorizations by jurisdiction and register, registered studies and how they link to the company, safety events from the loaded sources, public filings by type, and the library's evidence maturity score shown with its rubric. It never holds revenue, runway, outcomes, market share, intent, a valuation or a return (pack rules 2 and 3).

| Column | Read it as | Never read it as | Basis |
|---|---|---|---|
| Authorizations by jurisdiction | Records the library holds, by register | "Approved" for a 510(k) or a registration | DL-126 to DL-128 |
| Studies by link tier | Registered studies linked by brand, by sponsor and indication only, or unlinked | Published evidence or "no evidence" when the count is 0 | compare_portfolio output; DL-118 |
| Safety events | Rows in the loaded sources; `none_found` means searched and no row | "No safety problems" | compare_portfolio reading guide |
| Funding signal counts | Public filings and grants in the store | Money raised, a round, a valuation | `funding-and-filing-rules.md` |
| Evidence maturity score | The library's stated convention, rubric v1 (7 October 2026), with points and components | A quality grade, a rank, a valuation or a prediction | get_evidence_maturity interpretation limits |
| Reimbursement | `not_assessable` in every saved row | "Not reimbursed" | Route to `dh-access-and-value` coverage-pathway-and-access-strategy |

## 2. The library's evidence maturity score

As returned on 19 October 2026 (`examples/live/compare_portfolio_dtx_2026-10-19.json`; formula text from `get_evidence_maturity`, `examples/live/evidence_maturity_K191716_somnio.json`):

- Formula: "score = round(100 x points earned / assessable maximum); a component whose source is not loaded is excluded from the maximum, not counted as zero."
- Components and maxima: regulatory status 30, clinical evidence 40, active development 10, product breadth 10 (90 assessable points). Reimbursement and jurisdiction breadth are excluded as not assessable.
- Its own limits: "a stated convention for comparing documented evidence, not a predictive model or a valuation"; "US sources only; absence of EU, UK or Swiss data lowers nothing and proves nothing". Yet EU authorizations earned regulatory points in saved rows (GAIA AG, Deutschland: EU 31 authorizations, regulatory status 20 of 30). Name the register behind each authorization.

Show the score only with its points and components, and never sort the table by it unless the person asks; if they do, say the order is the library's convention.

## 3. Published evidence frameworks and what each leaves out

Pack rule 7 applies: a level from a framework is labeled "proposed" for the person, with the framework's own limits stated. Level assignment itself belongs to `company-and-evidence-assessment` (this pack); this skill only shows which framework a column follows.

| Framework | What it counts | Its own limits | Rows (DOI) |
|---|---|---|---|
| Clinical robustness score | FDA filings as requester plus registered trials, equally weighted | Registrations as proxies, no publications, USD 2 million+ venture cohort only; authors' employer supplied the cohort | DL-116 to DL-118 (10.2196/37677) |
| Critique of that score | Adds accreditations, externally validated methods, peer-reviewed studies | A letter; authors employed by a digital health company | DL-119 (10.2196/41715) |
| Evidence DEFINED | Screen, GRADE, supplementary checklist, evidence-to-recommendation levels 0 to 4 | Built for payers, PBMs, health systems, pharma, not investors; interrater reliability not quantified; authors employed by a health insurer | DL-107 to DL-115 (10.1038/s41746-023-00836-5) |
| Digital Health Scorecard | Technical, clinical, usability and cost domains | One clinical setting (oncology), small end-user group | DL-120, DL-121 (10.1038/s41746-021-00476-7) |
| DiMe evaluation framework | Evidence, usability, privacy and security, equity across all | Small samples, senior-skewed experts, subjective analysis; authors are DiMe staff | DL-122, DL-123 (10.1038/s41598-025-21996-2) |

The research file's own note: the frameworks disagree on what counts, none was designed for investors, and none has published interrater reliability ("Changes and conflicts" item 8). The library score resembles the counting approach (filings and registered studies) and inherits its blind spot for publications.

## 4. Name matching and company level

- FDA databases search by applicant or requester; a device cleared under a parent, predecessor or acquired entity will not show under the current brand (DL-133 (inference)). A miss is "lookup missed", not "no authorization".
- Devices@FDA searches 510(k) and PMA; De Novo orders sit in a separate database (DL-132).
- The library compares companies, not products: a brand resolves to its maker and carries the maker's flags ("Somryst" carries Pear's reSET and reSET-O recall flags of 7 June 2021). Say which products the row covers.
- Combined filing names ("GAIA AG" and "GAIA AG, Deutschland") are "a proposal until a person validates it". Repeat the flag.

## 5. Ranking only what the person scored (B1)

- `analytics.mcda` returns an EVIDEM weighted sum on a 0 to 4 scale; value = 25 x sum(weight x score). Every criterion is treated as higher-is-better; phrase criteria so 4 is best. No robustness view and no tie flag: `scripts/portfolio_table.py swap` gives swap points and ties. A missing score makes the call fail with HTTP 400; drop that option and list it as not ranked (`references/tools.md`).
- Criteria, weights, scores and any pass rule are the person's. The model never proposes a score for a company, never turns a library field into a score, and never calls the top option the one to invest in (pack rule 1).
- Library fields the person wants to use as a criterion (for example "regulatory status points") are copied as the library states them; turning them into a 0 to 4 score is the person's step, shown in their words.
