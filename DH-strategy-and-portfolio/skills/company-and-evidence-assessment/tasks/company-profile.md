# A1 Company profile

Framework task: DH-DIL.2.1, Part A, task A1. Replaces the old dh-diligence skills "Build a company profile", "List diligence sources" and "Read diligence guidance" (catalogue job `company-dossier`).

## What this task delivers

A profile of one named company built only from public records: identifiers, products with their authorizations as stored (pathway in words, dates, source URLs), registered studies as linked, filings stored with what each form does and does not show, the perimeter of what the library holds and does not hold, and every gap with its reason. Facts the person supplies from their own material sit in a separate column marked "your material".

Why it matters: a diligence view built from a pitch deck repeats the company's own words. The records say less but say it reliably: a clearance is not an approval (DL-128), registration is not approval (DL-126, DL-127), and a Form D shows an amount sold, not a valuation (DL-015, DL-018 (inference)).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (old skill "Worker: not bound"); see `references/governance.md` |
| Skill | DH-DIL.2.1 Part A, Company profile |
| Workflow | The steps below |
| Knowledge | `references/public-record-rules.md`; `references/company-status.md`; rows DL-001 to DL-043, DL-095 to DL-098, DL-126 to DL-133, DL-135 to DL-168, US-65 to US-69, EU-36 to EU-39, DE30 to DE32, CV132, CV141 |
| Tools | `diligence-dh.list_sources` (free; needs a live check), `diligence-dh.build_company_profile`, optionally `diligence-dh.retrieve_guidance` (needs a live check); the saved `compare_portfolio` result for safety events and recall flags; `scripts/profile_table.py` |
| Prompt | This guide |
| Template | `assets/company-profile-output.md` |
| Input | The request and its context: one company reference (legal name, brand, FDA submission number, LEI, EUDAMED SRN or SEC filer number), the markets the person cares about, any material the person supplies |
| Governance | `references/governance.md`; records only; no investment advice |
| Catalogue job | `company-dossier` (profile step only; `start_job` needs a live check) |

## Read the request

- **One company, one reference.** Matching is exact. If the person gives a near spelling, a brand used by several makers, or a product name, say which reference you will send and ask if unsure.
- **Public or private target.** If the person says the target is confidential or unpublished, ask before sending its name to the library.
- **The person's material.** Data-room documents, management figures, vendor databases: keep them in the "your material" column and never restate them as public record (pack rule 5).
- **Markets.** US, EU, UK, Germany, Switzerland: each has its own record (`public-record-rules.md`). The library loads no UK company register and no Swiss register.
- **Missing fields stay missing.** Where the saved record lacks a field, write it as not in the record; never print 0, "none" or "US company". `authorizations_by_jurisdiction` says where a product is authorized, not where the company is incorporated.
- **A period before the change log.** The library's change log began on 12 October 2026. If the person asks what changed over a period that starts earlier, say so and offer the company's dated primary filings (the EDGAR filing list with dates) and authorization records (FDA decision dates) for that period instead of reporting "no change".

## Workflow

### Step 1. State the perimeter

Call `diligence-dh.list_sources {}` (free; needs a live check). Until a live check confirms its output, use the census lines of `commercial-dh.list_commercial_dh_sources` as saved on 19 October 2026 (`references/tools.md`). Note every source not loaded that touches the person's markets, with its reason.

### Step 2. Build the profile

Call `diligence-dh.build_company_profile {company: "<exact reference>"}`. Save the output and run:

`python3 scripts/profile_table.py FILE.json`

Report the products table, studies line, filings table and the contradictions the script prints. Do not restate counts in your own arithmetic.

### Step 3. Read each record by its rules

For each record type present, add one line from `references/public-record-rules.md` on what it does not show: Form D (DL-002, DL-006, DL-015, DL-018 (inference)), 510(k) is a clearance (DL-128), De Novo database separate (US-66), name matching (DL-133 (inference)), registry rows are not publications. Where the person's markets include Germany, add that refusals are not published (DE32). Where they include the UK, add that small company accounts may omit the profit and loss account (DL-040).

### Step 4. Safety events and recall flags

The profile carries no safety or recall field. If a saved `compare_portfolio` result covers the company (`references/tools.md`), quote its `safety_events` and `risk_flags` as stored with the retrieval date: a recall flag verbatim (for example Pear Therapeutics, Inc.: "fda_recall: Class II on 2021-06-07" for reSET and reSET-O Mobile App); `none_found` as "none found in the loaded enforcement source, retrieved 19 October 2026; not proof of none". If nothing saved covers the company, write "safety events and recalls not read in this request `[GAP]`" and name the direct FDA recall read. Describe a recall only by what the record states; never judge its relevance.

### Step 5. Company status

Run the status step in `references/company-status.md`: say the library does not show whether the company still exists, filed for bankruptcy, was delisted, deregistered or acquired; read the company's own filings or register entry where you can open them (8-K Items 1.03, 2.01, 3.01 and 5.01, Form 25 and Form 15 on EDGAR for its CIK; Companies House status; German insolvency notices); otherwise list the exact filings to open and write "Status: [GAP]: not read". State what each form does not mean (a Form 15 or Form 25 is not dissolution, DL-144, DL-149 (inference)). Never infer status from press or memory. For SEC access, ask which contact the person's organization uses for the User-Agent (DL-153 [WF]); never send the person's email address or name and never invent a contact.

### Step 6. Direct reads the library does not hold

List, as next steps for the person, the records to read directly and what each can show: the HHS OCR breach portal and its archive (DL-095, DL-096), Companies House filings (DL-034 to DL-040), EDGAR full-text search for 8-K Items 1.01, 2.01 and 1.05 (DL-020, DL-022, DL-024, DL-032). Do not state their content unless the person supplies it or you read it in this request with a URL and date.

### Step 7. Guidance passages (optional)

If the person asks what a rule says and the references do not cover it, call `diligence-dh.retrieve_guidance {query: "<short keyword>", limit: 3}` (needs a live check). Quote a passage only with its `source_url` and retrieval date. A passage without a source is not a source. If nothing returns, say so and rest on the rows.

### Step 8. Separate the person's material

If the person supplied material, add a column or section "Your material" with each fact and the document name they give. Never merge it into the public-record table.

## Build the output

Follow `assets/company-profile-output.md`. Answer first: who the company resolves to, what the records hold (authorizations, studies, filings), its status as read (or "[GAP]: not read"), and the largest gap with its reason. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every fact has a record reference and retrieval date, or is marked "your material".
- No revenue, runway, valuation, customer, outcome or intent is inferred.
- Pathways are in words; "DENG" is translated; clearance is not called approval.
- Every source not loaded that touches the person's markets is named with its reason.
- Safety events and recall flags are quoted from the saved `compare_portfolio` result, or marked not read; status is read from a filing or register, or "[GAP]: not read" with the filings to open.
- No missing field is printed as 0, "none" or "US company".
- Word count: run `python3 scripts/profile_table.py --count ANSWER.md` on the short answer; at or under 450 words, counted without the calls list and source columns.
- Inference rows are labeled; each [PAPER] paper cited has its DOI once in prose and beside its row id in every table.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Funding signals and filing detail across forms: `funding-and-portfolio-comparison` (this pack).
- Whether the company's product is a device and its class: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- Reimbursement status: `dh-access-and-value` coverage-pathway-and-access-strategy.
- Changes since the last profile: `pipeline-and-market-monitoring` (this pack).
