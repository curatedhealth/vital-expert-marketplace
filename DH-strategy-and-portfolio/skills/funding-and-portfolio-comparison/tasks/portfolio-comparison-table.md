# A2 Investment portfolio comparison table

Framework task: DH-DIL.3.1, Part A, task A2. Replaces the old tool skill "DH Diligence Compare a portfolio" (tool `diligence-dh.compare_portfolio`, catalogue job `portfolio-comparison`; old boundary: "Compare 2 to 12 companies the buyer names. A company the store does not hold is a gap.").

## What this task delivers

A side-by-side table of the 2 to 12 companies the person names, from their records only: how each name resolved, authorizations by jurisdiction, registered studies by link tier, safety events, funding signal counts, the library's evidence maturity score with its points and components, and reimbursement as the library reports it. Under the table: the notes the person must see (company level, lookups missed, combined filing names, fields absent, sources not loaded). No order of merit.

Why it matters: a missing row reads as a weak company unless the reason is named. The library's own guide says `none_found` and `not_assessable` are not zero, and its evidence maturity score is "a stated convention ... not a predictive model or a valuation". Published scores that count filings and registered trials miss publications (DL-118, DOI 10.2196/37677) and none of the published frameworks was built for investors (DL-108, DOI 10.1038/s41746-023-00836-5).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (old file: "Worker: not bound") |
| Skill | DH-DIL.3.1 Part A, Investment portfolio comparison table |
| Workflow | The steps below |
| Knowledge | `references/comparison-rules.md`; `references/company-status.md`; rows DL-107 to DL-123 (DOIs in that file), DL-126 to DL-133, DL-135 to DL-168 |
| Tools | `diligence-dh.compare_portfolio`; optionally `diligence-dh.get_funding_signals` for a company whose row has no funding field; `scripts/portfolio_table.py compare` and `crosscheck` |
| Prompt | This guide |
| Template | `assets/portfolio-comparison-output.md` |
| Input | The request and its context: 2 to 12 company names or register numbers, the columns the person cares about, any confidential facts they bring |
| Governance | `references/governance.md`; no ranking unless the person scored (B1) |
| Catalogue job | `portfolio-comparison` (named in the old file; its `start_job` steps were not saved: needs a live check) |

## Read the request

- **Names.** 2 to 12. Fewer than 2: ask for more or run A1. More than 12: ask which 12, or split into two calls and say the calls were separate.
- **Names that may not resolve.** Brands and short names can miss (HelloBetter came back unresolved on 19 October 2026). Use the legal name or a register number where the person has one.
- **Columns.** Default: the library's fields. If the person names other columns (revenue, ARR, valuation), say those are not in the public record and keep any figures they supply in a separate column labeled "from the person".
- **Own product.** If one of the companies is the person's own, ask before sending its name to the library.

## Workflow

### Step 1. Call the library

`diligence-dh.compare_portfolio {companies: ["<name 1>", "<name 2>", ...]}`. Save the response and run `python3 scripts/portfolio_table.py compare FILE.json`.

### Step 2. Resolve every row

For each company, state the resolution basis as returned. If the query and the resolved company differ, say the row covers the whole company (for example "Somryst" resolved to Pear Therapeutics, Inc., whose row carries the reSET and reSET-O recall flags of 7 June 2021). An unresolved name is "lookup missed"; ask for a better reference. Repeat any combined-filing-names flag: "a proposal until a person validates it".

### Step 3. Fill gaps by name, not by silence

For a row with no `funding_signal_counts` field, either say "field absent; not a zero" or, if the person needs it, call `get_funding_signals` for that company and run `scripts/portfolio_table.py crosscheck` to see whether the counts agree. Read `none_found` as "searched, no row" and `not_assessable` as "source not loaded" (gap rules).

Write each studies sub-field only as returned. If `unlinked` (or any sub-field) is absent, write "field absent", never 0; the script lists absent sub-fields per company. Authorizations by jurisdiction say where products are authorized, not where the company is incorporated: never write "US company" from them.

The library's company record holds the CIKs listed in its response only. A parent, listed or successor registrant may file under another CIK, and the store holds selected form types only (a delisting or deregistration form may be absent). Say: "SEC filings in the store are those under CIK(s) [as returned]; other registrants and form types are not shown; open EDGAR for the full list."

### Step 3b. Status of each company

Run the status step in `references/company-status.md` for every company in the table: the script prints one status line per company. Where the filings or register can be opened, quote form, item, date and URL with what the form does not mean (a Form 15 or 25 is not dissolution, DL-144, DL-149). Otherwise write status "`[GAP]`: not read" and list the filings to open (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; Companies House status; German insolvency notices). For an IC or board pre-read, status sits in the answer's first two sentences. Never take status from press or memory.

### Step 4. Show the evidence maturity score with its limits

Give score, points earned of assessable maximum, and components. Say what the rubric counts and leaves out (`references/comparison-rules.md` section 2). Do not sort by it unless asked; if asked, label the order "the library's convention, not a ranking of the companies". If the person asks which published framework the score resembles, point to the counting approach (DL-116, DOI 10.2196/37677) and its critique (DL-119, DOI 10.2196/41715). Assigning an evidence level goes to `company-and-evidence-assessment` (this pack).

### Step 5. Status words

Use the register's word: "510(k) cleared", "De Novo granted", "CE marked (EU, class as stored)". Never "approved" for a 510(k) or a registration (DL-126 to DL-128). Show raw codes in words ("DENG" is FDA's De Novo granted code).

### Step 6. What the person must decide

List what the table cannot settle (which companies stay on the list, which columns matter, how to score them) and offer B1 if the person wants to score.

## Build the output

Follow `assets/portfolio-comparison-output.md`. Answer first: what the records show across the set in two sentences, and the main gap. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_table.py words ANSWER.md`. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Even in short mode, keep the reimbursement column ("not assessable" where the library holds nothing) and its route to `dh-access-and-value` coverage-pathway-and-access-strategy.

## Before you hand it over

- Every row says how the name resolved and which company it covers.
- No order of merit; the score appears with points and components.
- Every company has a status line: a filing or register read with its date, or "`[GAP]`: not read" with the filings to open.
- No 0, none or "US company" was written for a field the record lacks.
- The words were counted with the script and are at or under 450 in short mode.
- No revenue, valuation, outcome or intent was inferred; the person's figures are in their own column.
- Every [PAPER] row cited has its DOI once in prose and beside its row id in every table.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Finding the companies to compare: `market-and-target-screening` (this pack).
- Positioning the person's own product against these companies: `dh-go-to-market` market-segmentation-and-gtm-strategy.
- Whether a company's product is a device, or its pathway: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- Reimbursement status: `dh-access-and-value` coverage-pathway-and-access-strategy.
