# A1 Memo fact base

Framework task: DH-DIL.4.1, Part A, task A1. Carries the old tool skills "Generate a company report" (`diligence-dh.generate_report`) as it serves a memo, and the memo use of "Build a company profile" and "Read funding signals". The catalogue job `investment-memo` is never started.

## What this task delivers

A public-record fact base on one named company, laid out under the memo's headings: identifiers, products and authorizations by register (pathway in words, reference, decision date, URL), registered studies by link tier, safety events as stated, SEC filings by type with what a Form D does and does not show, the library's evidence maturity with its rubric and limits, and every gap named with its reason. Each fact carries its source and retrieval date. It answers "what does the record actually show about this company?"

Why it matters: a memo that reads a valuation into a Form D, calls a 510(k) "approved", or treats funding as evidence states things the record does not. The Form D items carry no valuation or investor names (DL-016, DL-018), clearance is not approval (DL-128), and funding did not track evidence in the published samples (DL-117, DOI 10.2196/37677; DL-124, DOI 10.1371/journal.pone.0323390).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (diligence suite); work as a diligence analyst who assembles and checks |
| Skill | DH-DIL.4.1 Part A, Memo fact base |
| Workflow | The steps below |
| Knowledge | `references/memo-sources.md` sections 1 to 6 and 8 (company status, DL-135 to DL-168); rows DL-001 to DL-018, DL-019 to DL-033, DL-034 to DL-043, DL-095 to DL-097, DL-107 to DL-125 (DOIs in SKILL.md), DL-126 to DL-133 |
| Tools | `diligence-dh.list_sources` (free; needs a live check); `diligence-dh.build_company_profile`; `diligence-dh.get_funding_signals`; `diligence-dh.get_evidence_maturity`; optional `diligence-dh.generate_report {template: "memo"}` (needs a live check); `scripts/memo_facts.py facts` |
| Prompt | This guide |
| Template | `assets/memo-fact-base-output.md` |
| Input | The request and its context: one company reference (legal name, brand, FDA number, SEC number), the memo's headings if given, sibling-skill outputs the person brings (company-and-evidence-assessment, funding-and-portfolio-comparison) |
| Governance | `references/governance.md`; the company is described only by its record |
| Catalogue job | `company-dossier` (the buyer's one-call option; `start_job` returns the steps and runs nothing). `investment-memo`: design partners only, never started |

## Read the request

- **Company reference.** Exact legal name, brand, FDA number or SEC number. Matching is exact; a near spelling comes back only as a proposal. If the person names a product (for example "Somryst"), the library resolves it to the company (Pear Therapeutics, Inc.); say which products the facts cover.
- **Headings.** The person's, verbatim. If none, use `memo-sources.md` section 7, labeled "proposed".
- **Non-public material.** If the person attaches data-room material, keep it out of library calls and out of this fact base; it goes under "From you (non-public)" in B1.
- **Sibling outputs.** If the person brings an evidence assessment or a funding comparison from this pack, use it as given and cite it; do not redo it.

## Workflow

### Step 1. Perimeter (free)

Call `diligence-dh.list_sources {}` (needs a live check; see `tools.md`). Note what is not loaded: Companies House, Zefix, private funding rounds, the DiGA directory feed for Diligence, NICE. Until checked live, take the perimeter from the `source_coverage` block of the next calls.

### Step 2. Company profile

Call `diligence-dh.build_company_profile {company: "<reference>"}`. Take identifiers, products with authorizations, studies by link tier and Form D rows. Write pathways in words ("De Novo granted", "510(k) cleared"); "DENG" is FDA's raw code (register C3). Never "approved" unless the record is a PMA (DL-128). If `funding` says `[GAP]` beside Form D rows, report the Form D amounts as amounts the filings state and private rounds as `[GAP]` (register C2).

### Step 3. Filings and funding signals

Call `diligence-dh.get_funding_signals {company: "<legal name as resolved>"}`. Report SEC filings by type with the date range, NIH and EU TED counts. Never quote `sum_of_stated_amounts` as money raised. For each Form D: date and amount as stored, with three caveats: the date tracks first commitment (DL-002), the amount may be stale (DL-006), and no valuation or investor names (DL-016; DL-018 (inference)). 8-K rows carry no item number: to find an Item 1.01 agreement (DL-020) or an Item 1.05 cybersecurity incident (DL-024), open the filing at its URL. The latest filing date is not a status; never infer why filings stopped. Name the latest 8-K rows by date with their URL and write: "Current company status [GAP]: the item of the latest 8-K (DATE) is not stored; open it on EDGAR before the memo describes the company as operating." Put this line in the gaps section of every A1 answer whose latest filing is more than a year before the retrieval date.

### Step 3a. Company status (every A1 answer)

Follow `references/memo-sources.md` section 8. List the latest 8-K, Form 25 and Form 15 rows (the `facts` script prints them). Where the assistant can open the filing or register, quote the item and date: 8-K Item 1.03 bankruptcy or receivership and 1.03(b) plan confirmed (DL-136, DL-137), Item 2.01 deal completed (DL-138), Item 3.01 listing notice or withdrawal (DL-139, DL-140), Item 5.01 change in control (DL-141); Form 25 (DL-142 to DL-145); Form 15 (DL-146 to DL-149); Companies House `company_status` and `company_status_detail` (DL-157 to DL-164); German insolvency notices (DL-165 to DL-168). State what the form does not mean: Form 25 ends the listing, not the company, and does not end 12(g) or 15(d) reporting (DL-144); Form 15 means the company stopped SEC reporting, not that it ceased to exist (DL-149 (inference)). Otherwise write "Company status [GAP]: not read" and list the exact filings to open. Never take status from press, memory or the last filing date. For automated EDGAR reads, SEC asks for a declared User-Agent contact (DL-153): ask which contact the person's organization uses; never put the person's email address or name into a request and never invent a contact.

### Step 4. Evidence maturity (library convention)

Call `diligence-dh.get_evidence_maturity {company: "<reference>"}`. Report score, assessable points, rubric version, components, excluded components and the limits verbatim. It is the library's convention, never the memo's evidence verdict. A framework-based assessment (NICE ESF tiers, Evidence DEFINED, V3) is `company-and-evidence-assessment` (this pack); if the person brings one, it replaces this line under the evidence heading.

### Step 5. Library dossier (only if the person asks for it)

Call `diligence-dh.generate_report {reference: "<reference>", template: "memo"}` (needs a live check). Restate any raw JSON as tables; take authorizations from the identity block with the FDA URL even if another section marks them `[GAP]` (register C7); record the behavior in the build notes. Do not call `build_company_profile` again for the same company.

### Step 6. Build the table and name the gaps

With code execution, save the outputs and run `python3 scripts/memo_facts.py facts --profile PROFILE.json --funding FUNDING.json --maturity MATURITY.json --company "<name>"`. Add the gaps by reason (`references/gap-rules.md`): source not loaded, lookup missed, field not stored. Add what the person must check outside the library: the HHS breach portal, both the main list and the archive (DL-095, DL-096); Companies House for a UK entity (DL-034 to DL-043); EDGAR full-text search for exhibits (DL-032, DL-033); FDA databases under a parent or predecessor name (DL-133).

## Build the output

Follow `assets/memo-fact-base-output.md`. Answer first: what the record shows in two sentences (authorizations, filings, evidence maturity with its limits) and the largest gap. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/memo_facts.py words ANSWER.md` (counts the body above the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every fact has its source reference and retrieval date; nothing comes from memory.
- No valuation, investor name, revenue, runway, outcome or intent is stated or implied.
- Pathways in words; "approved" only for a PMA.
- Evidence maturity carries its rubric version and limits; [PAPER] rows carry their DOI.
- Non-public material is absent from this output.
- The company status line is present: quoted from a filing or register read, or "[GAP]: not read" with the filings to open.
- `python3 scripts/memo_facts.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Evidence maturity by a named framework: `company-and-evidence-assessment` (this pack).
- Funding across several companies: `funding-and-portfolio-comparison` (this pack).
- What an authorization means for the product's pathway: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- Reimbursement status: `dh-access-and-value` coverage-pathway-and-access-strategy.
