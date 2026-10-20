# Memo fact base: Pear Therapeutics, Inc.

Public record only, from saved library output. Retrieved: 19 October 2026 (`examples/live/generate_report_somryst_commercial.json`). AI-assisted draft; not investment advice.

## Identity

- Identifiers not in this file `[GAP]`

## Products and authorizations

| Product | Reference | Pathway (words) | Product code | Regulation | Decision date | Source |
|---|---|---|---|---|---|---|
| reSet | DEN160018 | De Novo, granted | PWE | 882.5801 | 14 September 2017 | URL not stored `[GAP]` |
| reSET-O | K173681 | 510(k), cleared | PWE | 882.5801 | 10 December 2018 | URL not stored `[GAP]` |
| Somryst | K191716 | 510(k), cleared | QVO | 882.5801 | 23 March 2020 | https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K191716 |

Wording: a 510(k) is cleared, a De Novo is granted; neither is "approved" (DL-128). Registration or listing is not an authorization (DL-126, DL-127).

## Studies

- studies_total: 3
- Counts are registered studies in the loaded registry, by link tier; not a judgment of evidence.

## Safety events

- two Class II recalls on 2021-06-07 (reSET, reSET-O)

## Filings and funding signals

Source: `get_funding_signals {company: "Pear Therapeutics, Inc."}` (`examples/live/funding_signals_pear.json`). SEC CIK: 0001615898, 0001835567.

| Source | Count | Dates |
|---|---|---|
| SEC EDGAR | 46 | 9 February 2016 to 10 April 2023 |
| NIH RePORTER | 6 | 20 June 2017 to 21 September 2020 |
| EU TED | 0 | none_found |

SEC filings by type: 8-K 25, 10-Q 6, D 4, S-4/A 3, 10-K 2, S-1 2, 8-K/A 1, S-4 1, D/A 1, S-1/A 1.

Not quoted: `sum_of_stated_amounts` adds different filing types (tool caveat: "adds the amounts the filings state; a Form D amount sold and an award amount are different things, so read by type").
Private rounds: [GAP] (no funding source loaded).
The latest filing date is not a status; nothing is inferred from when filings stop.

## Company status

Company status `[GAP]`: not read. The library stores no status field and no 8-K item number; status comes only from the filings or the register, opened at the source, never from press, memory or the date filings stopped.

| Filing to open | Date | Accession | URL | What it can and cannot show |
|---|---|---|---|---|
| 8-K | 10 April 2023 | 0001835567-23-000022 | https://www.sec.gov/Archives/edgar/data/1835567/000183556723000022/0001835567-23-000022-index.htm | open it for Items 1.03 (bankruptcy or receivership, DL-136, DL-137), 2.01 (deal completed, DL-138), 3.01 (listing notice or withdrawal, DL-139, DL-140) and 5.01 (change in control, DL-141); no item number is stored |
| 8-K | 7 April 2023 | 0001835567-23-000020 | URL not stored | open it for Items 1.03 (bankruptcy or receivership, DL-136, DL-137), 2.01 (deal completed, DL-138), 3.01 (listing notice or withdrawal, DL-139, DL-140) and 5.01 (change in control, DL-141); no item number is stored |

- Form 25 or Form 15 among the stored filing types: not in the stored types. Whether the library loads those forms needs a live check.
- Also open, where the company has one: Companies House `company_status` and `company_status_detail` (DL-157 to DL-163); German insolvency notices, which are deleted after six months, so no hit is not proof (DL-165 to DL-167); PACER for US bankruptcy dockets (DL-154 to DL-156).
- Automated EDGAR reads need a declared User-Agent contact (DL-153): ask the person which contact their organization uses; never use their name or email unasked and never invent one.

- SEC EDGAR filings in the identity block: 46; latest 8-K 10 April 2023.

Form D shows no valuation, price per share or investor names (DL-016, DL-018); its date tracks first commitment, not closing (DL-002).

## Evidence maturity (library convention)

- Score 67 (60 of 90 assessable points, shown as a percentage), rubric v1 (7 October 2026); retrieved 19 October 2026 (`examples/live/evidence_maturity_K191716_somnio.json`).
- Components: regulatory_status 30/30, clinical_evidence 20/40, active_development 0/10, product_breadth 10/10.
- Not assessable: reimbursement (no reimbursement source is loaded); jurisdiction_breadth (US sources are loaded as a census; EU is exact lookups of known names only, and UK and Swiss sources are not loaded).
- Limit as stated: "a stated convention for comparing documented evidence, not a predictive model or a valuation"
- Limit as stated: "US sources only; absence of EU, UK or Swiss data lowers nothing and proves nothing"
- A stated convention, not an evidence verdict and not a valuation. Framework-based assessment: company-and-evidence-assessment (this pack).

## Gaps

- reimbursement: [GAP] no reimbursement source loaded
- UK and Swiss company registers not loaded (Companies House, Zefix) `[GAP]`.
- HHS breach portal not in the library; a portal search is yours, with its date (DL-095, DL-096).
