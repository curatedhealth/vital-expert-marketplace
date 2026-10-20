# A2 Target record check

Framework task: DH-DIL.1.1, Part A, task A2. Replaces the old tool skill "Search companies" (`diligence-dh.search_companies`, catalogue job `market-screen`) and adds the register reading rules a screen needs.

## What this task delivers

For one named candidate: whether the library's store holds it and under which name, and, register by register, what the public record can show about it and what it cannot (FDA databases, the DiGA directory, SEC Form D, 8-K, 10-K and S-1, Companies House, the HHS breach portal), with every statement the person or the company made checked against what that register can carry. It answers "what is actually on record for this company, and how far can each claim about it be read?"

Why it matters: candidate decks say "FDA registered", "approved" or "raised USD N" in words the registers do not support. Reading each claim against what the record can show stops a wrong fact from entering the short list.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | not bound (diligence suite, not a CF-12 row) |
| Skill | DH-DIL.1.1 Part A, Target record check |
| Workflow | The steps below |
| Knowledge | `references/screening-rules.md` sections 2 and 5 (rows DL-001 to DL-043, DL-092 to DL-097, DL-126 to DL-133, DL-135 to DL-168, DE30 to DE34) |
| Tools | `diligence-dh.list_sources` (free; needs a live check); `diligence-dh.search_companies` (needs a live check for name searches) |
| Prompt | This guide |
| Template | `assets/target-record-check-output.md` |
| Input | The request and its context; the company's exact name or identifiers; the statements to check (from the person, a deck, or the person's data-room material) |
| Governance | `references/governance.md`; companies described by their record only; data-room facts labeled |
| Catalogue job | `market-screen` (start card not saved; needs a live check). The direct calls in the steps remain the method. |

## Read the request

- **Company and identifiers.** Exact legal name, brands, FDA submission numbers, SEC CIK, UK company number, LEI or EUDAMED SRN, as the person gives them. If only a brand is given, use it and say the store may hold the company under its legal name.
- **Statements to check.** For example "FDA approved", "FDA registered", "raised USD 20 million (Form D)", "listed DiGA", "no breaches". Quote them as given and say where they came from.
- **Confidential material.** If the statements come from a data room, label them "from your material" and keep them out of the public-record column.

## Workflow

### Step 1. Perimeter (free)

Call `diligence-dh.list_sources` (needs a live check). Note which registers the store loads and which it does not (Companies House and private funding were not loaded on 19 October 2026). The person can still check an unloaded register at the authority; the answer says which and how.

### Step 2. Store lookup

Call `diligence-dh.search_companies` with `{query: "<exact name or identifier>"}` (needs a live check). Report what the row holds (products, authorizations, studies, evidence maturity) with the retrieval date. If nothing returns, try one other exact form (legal name, brand or a submission number) and then write "lookup missed" with the identifiers tried. FDA databases search by applicant or requester, so a product cleared under a predecessor or acquired entity does not show under the current brand (DL-133 (inference)). For the full profile and filings, route to `company-and-evidence-assessment` (this pack); this task stays a check.

### Step 3. Read each statement against its register

Use the table in `screening-rules.md` section 2. For each statement, one row: the statement as given · the register that would carry it · what that register can show (row) · what it cannot show (row) · what the store or the person's material holds · status (on record, not on record in the store, cannot be shown by this register, not checked). Examples of the readings:

- "FDA registered" or "FDA listed": registration and listing do not denote approval (DL-126, DL-127); ask for the premarket submission number the listing should carry (DL-130).
- "FDA approved" for a 510(k) product: a 510(k) does not denote approval and saying so is misbranding (DL-128). Quote the clearance with its number and date if on record.
- "Raised USD N" from a Form D: the amount is "amount sold as of the filing date", which need not be amended when it changes (DL-015, DL-006); the date tracks the first investor's irrevocable commitment, not a closing (DL-002); no valuation, price per share or investor names (DL-018). Never turn a Form D into a round size or a valuation.
- "Listed DiGA": the directory publishes listings, evidence summaries and delisting reasons (DE30); refusals are not published (DE32). A listing is not evidence of clinical effect.
- "No breaches": the HHS portal lists only breaches of 500 or more, and closed or older cases sit in the archive (DL-095, DL-096); a breach may appear under a client's name (DL-097 (inference)). Ask the company for its breach risk assessments (DL-087, DL-094).
- UK company accounts: small companies may file without a profit and loss account today (DL-040); revenue may be absent from the public record.

### Step 4. Company status

The store does not show whether a company was acquired, deregistered, delisted or is in bankruptcy or insolvency. Run the status step in `screening-rules.md` section 5: read the company's own primary filings or register entry where the assistant can open them (8-K Items 1.03, 2.01, 3.01 and 5.01; Form 25; Form 15; Companies House `company_status`; German insolvency notices), quoting form or item, filing date, source and read date, each with its "does not mean" line (Form 15 or Form 25 is not dissolution, DL-144, DL-149). Otherwise write "Status: [GAP]: not read" and list the exact filings to open, with the identifier. Never infer status from press, memory or the absence of filings. SEC requests need a declared contact the person gives (DL-153 [WF]); never send the person's own email address or name, and never invent one.

### Step 5. Gaps and next checks

Word every gap with `gap-rules.md`. For each register the store does not load, give the authority and the identifier to search, from the rows (for example EDGAR full-text search covers filings since 2001, DL-032). Status is the gap line from step 4, never a conclusion from the absence of filings.

## Build the output

Follow `assets/target-record-check-output.md`. Short mode answers first: on record or not, under which name, the status line, and which statements the registers cannot carry; then the statement table and the next checks. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Each statement has its register, its row and its status; facts from the person's material are labeled.
- No revenue, runway, valuation, investors, outcomes or intent inferred.
- One status line from a primary record, or "Status: [GAP]: not read" with the filings to open.
- Missing fields stay missing ("not in the record"); no 0, "none" or country printed for a field the record lacks.
- Word count run (`scripts/screen_helpers.py wordcount <answer.md>`, or by hand): short mode at or under 450 words without the calls list and source columns.
- No statement about whether the product is a device or which pathway applies (route to `dh-regulatory-and-quality` regulatory-pathway-and-classification).
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- A check, not a dossier: the full company profile, filings list and evidence assessment are `company-and-evidence-assessment` (this pack); funding filings in depth are `funding-and-portfolio-comparison` (this pack).
- Reimbursement status and what a scheme pays: `dh-access-and-value` coverage-pathway-and-access-strategy.
