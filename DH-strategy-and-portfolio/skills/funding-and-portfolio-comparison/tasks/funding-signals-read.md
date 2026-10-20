# A1 Funding signals read

Framework task: DH-DIL.3.1, Part A, task A1. Replaces the old tool skill "DH Diligence Read funding signals" (tool `diligence-dh.get_funding_signals`; old boundary: "Public filings that name the company. An amount the filing does not state stays blank.").

## What this task delivers

For one named company: the public filings, grants and awards the library holds, by type and date range, each read for what that form shows and does not show; amounts quoted only per filing and by type; what is a gap and why. No valuation, no investor names, no round size beyond what a filing states, no reading of status or intent.

Why it matters: a Form D date tracks the first investor's commitment, not a closing (DL-002), its amount sold need not be updated (DL-006), and it never shows a valuation or investors (DL-018). An 8-K count says nothing until the item is read (DL-020 to DL-024). Funding totals from vendors may be incomplete (DL-125, DOI 10.1371/journal.pone.0323390).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (old file: "Worker: not bound") |
| Skill | DH-DIL.3.1 Part A, Funding signals read |
| Workflow | The steps below |
| Knowledge | `references/funding-and-filing-rules.md`; `references/company-status.md`; rows DL-001 to DL-043, DL-135 to DL-168, DL-117 (DOI 10.2196/37677), DL-124 and DL-125 (DOI 10.1371/journal.pone.0323390) |
| Tools | `diligence-dh.get_funding_signals`; `scripts/portfolio_table.py funding` |
| Prompt | This guide |
| Template | `assets/funding-signals-output.md` |
| Input | The request and its context: the company (legal name, brand or SEC CIK), the question (all filings, a round, a partnership, an acquisition), any figure the person brings and its source |
| Governance | `references/governance.md`; no valuation, no investor names, no status inference |
| Catalogue job | none for this task alone; `company-dossier` (Diligence) lists `get_funding_signals` among its tools and belongs to `company-and-evidence-assessment` (this pack) (`examples/live/list_jobs_commercial.json`, 19 October 2026) |

## Read the request

- **Company.** Exact legal name works best ("Pear Therapeutics, Inc."). A brand may resolve to its maker; say so. If two companies share a name, ask.
- **Question.** "What have they raised" becomes "what offerings and filings are on record"; say that private rounds are `[GAP]` in the library.
- **Person's figures.** A round size or valuation from a vendor or a press release is labeled "the person's figure, source as named" and kept apart from the record (DL-125).
- **Confidential material.** Data-room terms stay in their own section, labeled, and never go into the library call (pack rule 5).

## Workflow

### Step 1. Call the library

`diligence-dh.get_funding_signals {company: "<exact name>"}`. Save the response. Run `python3 scripts/portfolio_table.py funding FILE.json`.

If the company has no SEC CIK (for example a German or Swiss company), the response shape is not yet measured: **needs a live check**; report what comes back and mark the rest `[GAP]`.

### Step 2. Read each filing type by its rule

| Type | Say | Do not say | Rows |
|---|---|---|---|
| D, D/A | "An exempt offering notice; first investor committed within 15 days before the filing date; amount as stored, may be stale" | A valuation, investors, a lead, a closing date | DL-001, DL-002, DL-006, DL-015, DL-018 |
| 8-K, 8-K/A | "A current report; item not stated in the library row" until the filing is opened; then name the item (1.01, 2.01, 1.05) | That it is a partnership or acquisition before reading it | DL-019 to DL-024 |
| 10-K | "Periodic report"; Item 1 business, Item 1A risk factors (not required for smaller reporting companies), Item 1C cybersecurity | That missing risk factors mean low risk | 10-K rows DL-025 to DL-029 |
| 10-Q | "Quarterly report" | Anything about its content: no row for 10-Q in the research file `[GAP]` | none `[GAP]` |
| S-1, S-4 and amendments | "Registration statement"; S-1 carries business and risk factors | That an offering completed | DL-031 |
| NIH RePORTER, EU TED | "Public grant or award for a stated project" | Equity, a round | `references/funding-and-filing-rules.md` section 4 |

Where the person needs what an 8-K or 10-K says, open the filing at its `source_url` and quote it with the date read. EDGAR full-text search covers filings since 2001 (DL-032).

### Step 3. Amounts

Quote an amount only from a filing row, with type, date and reference. Never quote or rebuild `sum_of_stated_amounts`; the tool's own caveat says the types differ. If the person asks for "total raised", answer: "No total is on record; private rounds are `[GAP]`; the filings state these amounts by type."

### Step 4. Dates and status

Give the date range of filings in the store. The latest filing in the store is not a statement about the company today: never infer that it stopped operating, was acquired, or is raising.

Run the status step in `references/company-status.md` for the company, whether or not the person asked: the script's `funding` output prints which status forms the store holds. Say "SEC filings in the store are those under CIK(s) [as returned]; other registrants and form types are not shown." Where the filings can be opened (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; Companies House status; German insolvency notices), quote form, item, date and URL with the read date and what the form does not mean (a Form 15 or 25 is not dissolution, DL-144, DL-149). Otherwise write status "`[GAP]`: not read" and list those filings to open, for each CIK and for any listed parent or successor the person names. Never take status from press or memory. Requests to SEC carry only a User-Agent contact the person's organization gives (DL-153, [WF]), never the user's email address or name; with no contact given, list the filings instead.

If the person asks what happened since a date before the library change log began (12 October 2026), say the log does not cover that span and give the dated filings in the store for it instead of "no change".

### Step 5. Gaps and the person's figures

List what the library does not load (funding source, Companies House) and what each filing type cannot show. Place any figure the person brought in its own line, labeled as theirs.

## Build the output

Follow `assets/funding-signals-output.md`. Answer first: what the record holds (types, counts, date range) and the one thing it cannot show that the person asked about. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_table.py words ANSWER.md`. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every amount is a single filing's, with type, date and reference; no sum across types.
- No valuation, investor name, round size or status was inferred; the status line quotes a filing or register read, or says "`[GAP]`: not read" and lists the filings to open.
- No 0, none or country was written for a field the record lacks.
- The words were counted with the script and are at or under 450 in short mode.
- Every [PAPER] row cited has its DOI once in prose and beside its row id in every table.
- The person's figures and any confidential material sit in their own labeled section.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- A full company dossier: `company-and-evidence-assessment` (this pack).
- New filings since a date: `investment-portfolio-monitoring` or `pipeline-and-market-monitoring` (this pack).
- Whether a funding round or deal needs HSR, CFIUS or EU or Swiss screening: the owner the person names for legal or compliance questions (or owner not named) (`references/governance.md`).
