# A1 Company change read

Framework task: DH-DIL.1.2, Part A, task A1. Replaces the old "Read company changes" section and tool skill (`diligence-dh.get_deltas`, catalogue job `market-screen`). The old "Watch companies" section (`diligence-dh.watch_companies`) is described in `references/tools.md` and never called.

## What this task delivers

A dated read of what the library's change log records for up to 12 named companies since the person's date: each change with its event date, source and retrieval date, "no change recorded" with the log's own limits, and what the library cannot see. It answers "what is new on record for these companies since we last looked?"

Why it matters: a pipeline goes stale quietly. A dated read with the log's limits stated keeps "nothing new in the log" apart from "nothing happened".

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | not bound (diligence suite, not a CF-12 row) |
| Skill | DH-DIL.1.2 Part A, Company change read |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md` sections 1, 2, 4 and 5 (rows DL-002 to DL-006, DL-018 to DL-024, DL-034 to DL-040, DL-095, DL-096, DL-129, DL-135 to DL-168, DE30 to DE32) |
| Tools | `diligence-dh.list_sources` (free; needs a live check); `diligence-dh.get_deltas`; `diligence-dh.get_funding_signals` to find a filing URL and, for a window before the log, filing dates and types; `diligence-dh.build_company_profile` for authorization decision dates before the log; `scripts/monitor_helpers.py deltas` and `wordcount` |
| Prompt | This guide |
| Template | `assets/change-read-output.md` |
| Input | The request and its context; the company names as the store holds them; the "since" date |
| Governance | `references/governance.md`; no watches; no intent read into a change |
| Catalogue job | `market-screen` (start card not saved; needs a live check). The direct calls in the steps remain the method. |

## Read the request

- **Companies.** Up to 12, with the store's exact legal names (for example "Akili Interactive Labs, Inc."). If the person gives brands, take the legal name from an A1 screen of `market-and-target-screening` (this pack) or ask.
- **Since when.** The person's date (the last review, the last memo). If not given, write "not given" and ask; never pick one.
- **Confidential names.** The pipeline may be confidential. Library calls send the names to the library; ask before sending names the person has not cleared for that, and never put them into a watch.

## Workflow

### Step 1. Perimeter (free)

Call `diligence-dh.list_sources` (needs a live check; `commercial-dh.list_commercial_dh_sources` returns the same census). Note the sources not loaded: no change can be seen in them.

### Step 2. Read the log

Call `diligence-dh.get_deltas` with `{companies: [<names>], since: "<YYYY-MM-DD>"}`. Do not use `commercial-dh.get_deltas`: it drops the log block (`tools.md`). With code execution, save the response and run `scripts/monitor_helpers.py deltas <file>`; it prints the change table and the log caveat, and warns when the "since" date is earlier than the log's first entry.

### Step 3. Report each change as the record states it

For each change: company, what changed (authorization, study, safety record, filing, award, as the row names it), event date, source URL, retrieved date. For a filing, give the form type; where an 8-K item matters, open the filing at its URL (the library's filing rows carry no item number). Read each record type with `monitoring-signals.md` section 2 (for example a Form D amount is "amount sold as of the filing date", DL-015, and shows no valuation or investors, DL-018).

### Step 4. Report "no change recorded" with the log caveat

Quote the three log limits once, with the dates from the response (on 19 October 2026: first entry 12 October 2026, last sweep 19 October 2026). Where the "since" date is before the first entry, say changes dated before the log began may be missing. Then offer the store's own dated rows for that window, which do not depend on the change log: filings by date and type through diligence-dh.get_funding_signals and authorization decision dates through diligence-dh.build_company_profile (funding-and-portfolio-comparison and company-and-evidence-assessment, this pack; for example Pear Therapeutics, Inc. holds 46 SEC rows from 9 February 2016 to 10 April 2023, examples/live/funding_signals_pear.json, 19 October 2026). Quote dates and types only; never read intent or status from them. Never report "no change" for the part of the window before the log began. Never write "no change" without the caveat.

### Step 5. Company status

The library does not show whether a company was acquired, deregistered, delisted or is in bankruptcy or insolvency, and its filing rows carry no 8-K item number. Run the status step in `monitoring-signals.md` section 5 for each named company: read its own primary filings or register entry where the assistant can open them (8-K Items 1.03, 2.01, 3.01 and 5.01; Form 25; Form 15; Companies House `company_status`; German insolvency notices), quoting form or item, filing date, source and read date, each with its "does not mean" line (Form 15 or Form 25 is not dissolution, DL-144, DL-149). Otherwise write "Status: [GAP]: not read" and list the exact filings to open. Never infer status from press, memory, a quiet log or the latest filing date in the store. SEC requests need a declared contact the person gives (DL-153 [WF]); never send the person's own email address or name, and never invent one.

### Step 6. What the library cannot see

One line per source not loaded that bears on the pipeline (for example Companies House for a UK target, the HHS breach portal, the DiGA directory feed), with where to check it at the authority (`monitoring-signals.md` section 2).

### Step 7. What it may touch (hypotheses)

For each change, at most one line on which of the person's triggers it could touch, labeled "hypothesis for review" (`monitoring-signals.md` section 4). Never infer intent, distress, revenue or a valuation.

## Build the output

Follow `assets/change-read-output.md`. Short mode: the changes, then "no change recorded" with the log caveat and, for a window before the log, the offer of dated filings and authorizations, then one status line per company, then what the library cannot see. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every change has its event date, source and retrieval date.
- The log caveat appears wherever "no change recorded" is reported; a window before 12 October 2026 is named as such, with the dated filings and authorization records offered for it.
- One status line per company from a primary record, or "Status: [GAP]: not read" with the filings to open.
- Missing fields stay missing ("not in the record"); no 0, "none" or country printed for a field the record lacks.
- Word count run (`scripts/monitor_helpers.py wordcount <answer.md>`, or by hand): short mode at or under 450 words without the calls list and source columns.
- No watch was set; no intent, distress, revenue or valuation was read into a change.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- A read, not a review: whether a change matters is B1, on the person's triggers.
- A full profile of a company that changed: `company-and-evidence-assessment` (this pack). Funding filings in depth: `funding-and-portfolio-comparison` (this pack).
- Whether a new authorization or recall changes a product's regulatory status: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
