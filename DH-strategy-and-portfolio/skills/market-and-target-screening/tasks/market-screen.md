# A1 Market screen

Framework task: DH-DIL.1.1, Part A, task A1. Replaces the old "Screen a market" section (tool `diligence-dh.screen_market`, catalogue job `market-screen`) and folds in "List diligence sources" as the perimeter step.

## What this task delivers

A dated long list of the companies the library's store holds for a segment and jurisdiction: products, authorizations, studies, safety records and the evidence maturity score with its rubric, each "as of" its retrieval date, with a coverage note that says plainly what the screen cannot see. It answers "who is on record in this market?"

Why it matters: a long list built from one store looks like the market and is not. A screen that states its perimeter keeps the gaps visible before anyone scores a candidate.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | not bound (diligence suite, not a CF-12 row) |
| Skill | DH-DIL.1.1 Part A, Market screen |
| Workflow | The steps below |
| Knowledge | `references/screening-rules.md` sections 1, 3, 4 and 5; rows DE30 to DE34, DL-116 to DL-125, DL-135 to DL-168 |
| Tools | `diligence-dh.list_sources` (free; needs a live check); `diligence-dh.screen_market`; `diligence-dh.search_companies` (segment or named additions); `scripts/screen_helpers.py table` |
| Prompt | This guide |
| Template | `assets/market-screen-output.md` |
| Input | The request and its context; segment, jurisdictions, any minimum evidence maturity the person sets, named companies to add |
| Governance | `references/governance.md`; companies described by their record only; no market size |
| Catalogue job | `market-screen` (start card not saved; needs a live check). The direct calls in the steps remain the method. |

## Read the request

- **Segment.** The library's segments are `dtx`, `samd-diagnostic`, `cdss`, `rpm`, `digital-health`; on 19 October 2026 only `dtx` held companies. If the person's segment is not one of these, say so and ask which slug comes closest, or search by name (step 4).
- **Jurisdictions.** US, EU, UK or CH for the screen. If not given, ask once; never pick one.
- **Filters.** A minimum evidence maturity or a minimum number of authorizations only if the person sets it, in their words.
- **Named companies.** Companies the person wants on the list whether or not the screen returns them.
- **Market size.** If asked, say no source gives one (DL "Not sourced") and continue with the screen.

## Workflow

### Step 1. Read the perimeter (free)

Call `diligence-dh.list_sources` with no arguments (needs a live check; if it fails, `commercial-dh.list_commercial_dh_sources` returns the same census, `tools.md`). Note for the coverage line: the companies in the store, the segments and jurisdictions loaded, and each source not loaded with its reason (on 19 October 2026: Companies House, Zefix, the DiGA directory feed, NICE, private funding).

### Step 2. Run the screen

Call `diligence-dh.screen_market` with `{segment, jurisdiction, limit}` and `min_evidence_maturity` only if the person set it. One call per jurisdiction. Keep `total_matches` beside `result_count`: "10 of 18 shown" is a different statement from "10 companies". With code execution, save each response and run `scripts/screen_helpers.py table <file>`; add `--min-authorizations N` or `--min-score N` only for a rule the person gave.

### Step 3. Read the result against the perimeter

- Every company row: company, country (as stored; never "a US company" unless a primary record states it), jurisdictions, products as stored, authorizations, studies, safety records, evidence maturity "N (rubric v1)", retrieved date.
- If a jurisdiction returns few or none (EU `dtx` returned one company, Novasight, Ltd., on 19 October 2026), write the coverage reason, not "few companies": the DiGA makers sit in a directory mirror the screen does not use, and the response flags it (`screening-rules.md` section 1).
- The order is the library's sort ("evidence maturity score, highest first, then company name"). Say so once; never call it a ranking of targets.

### Step 4. Add named companies and other segments

For each company the person named that the screen did not return, call `diligence-dh.search_companies` with `{query: "<exact legal name, brand or identifier>"}` (needs a live check; matching is exact, not semantic). For a segment other than `dtx`, a `search_companies {segment}` call returned 0 for `rpm` on 19 October 2026: write "segment not loaded" and offer a name search. A miss is "lookup missed", not absence (`gap-rules.md`).

### Step 5. Evidence maturity as context

Show the score with "N of M assessable points (rubric v1)" where the response gives points, and the excluded components (reimbursement, jurisdiction breadth). Add one line from `screening-rules.md` section 3: the score is a stated convention for comparing documented evidence; published frameworks disagree on what counts and none was built for investors (DL conflicts item 8); funding is not a proxy for evidence [PAPER] (DL-117, DOI 10.2196/37677; DL-124, DOI 10.1371/journal.pone.0323390). Route a full evidence reading to `company-and-evidence-assessment` (this pack).

### Step 6. Classify gaps

Word every missing fact with `references/gap-rules.md`. Never "no competitor", "empty market" or a count presented as the market. The store does not show whether a company was acquired, deregistered, delisted or is in bankruptcy or insolvency: write it as [GAP] and give the next check, the company's latest EDGAR filings by date and type (8-K Items 1.03, 2.01, 3.01 and 5.01, Form 25, Form 15; DL-135 to DL-149) or its Companies House or German insolvency record (DL-157 to DL-168), per the status step in `screening-rules.md` section 5. Never infer status from press, memory or the absence of filings. One gap line covers the whole list; offer A2 for the status of a named company.

## Build the output

Follow `assets/market-screen-output.md`. Short mode answers first: how many companies the store holds for the screen and how many are shown, the long-list table, the coverage note, the gaps that change the picture. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every company fact has its source and retrieval date; the screen's own perimeter statement is quoted.
- No market size, valuation, revenue, round size, investor or intent.
- One status gap line for the list (step 6); no status taken from press or memory. Missing fields print as "not in saved output", never 0 or "none".
- Word count run (`scripts/screen_helpers.py wordcount <answer.md>`, or by hand): short mode at or under 450 words without the calls list and source columns.
- The library's sort order is not presented as a ranking; filters are the person's.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Facts only; no choice of target (that is B1, on the person's criteria and scores).
- A company's full profile, filings and evidence: `company-and-evidence-assessment` and `funding-and-portfolio-comparison` (this pack).
- Changes since an earlier screen: `pipeline-and-market-monitoring` (this pack).
- Positioning one's own product against these companies: `dh-go-to-market` market-segmentation-and-gtm-strategy.
