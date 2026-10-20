# A1 Watch rules and signals

Framework task: DH-DIL.3.2, Part A, task A1. New for the diligence suite: the old files had no investment portfolio monitoring competency; the old "Watch companies" and "Read company changes" tool skills fold into `pipeline-and-market-monitoring` (this pack), and this task reuses their read call only.

## What this task delivers

The person's watch rules, written in their words, for their holdings: which signals they watch per holding, where each signal comes from, its clock, what it can and cannot tell, and which moves do not count (a quiet log, a stale Form D amount, a registration called an approval). Any rule the person asks the model to propose is labeled "proposed" and carries the row behind it. No benchmark, no target, no score.

Why it matters: a watch that reads "no change recorded" as "nothing happened" misses everything before the library's log began (12 October 2026 in the saved runs) and every source the library does not load. An 8-K count says nothing until its item is read (DL-020 to DL-024). A Form D amount sold need not be updated (DL-006).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound |
| Skill | DH-DIL.3.2 Part A, Watch rules and signals |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md`; `references/company-status.md` (DL-135 to DL-168); rows DL-002, DL-005, DL-006, DL-019 to DL-030, DL-034 to DL-042, DL-092, DL-095 to DL-098, DL-126 to DL-133 |
| Tools | None |
| Prompt | This guide |
| Template | `assets/watch-rules-output.md` |
| Input | The request and its context: the holdings (names, public or private, US or UK or EU), what the person wants to catch, who owns the watch, how often the person reads (their cadence, if given) |
| Governance | `references/governance.md`; the person sets every rule and threshold |
| Catalogue job | none (no saved job covers investment portfolio monitoring; `find_job {query: "portfolio monitoring"}` needs a live check) |

## Read the request

- **Holdings.** For each: is it an SEC reporting company (8-K, 10-K), a private US company (Form D only; a company the person says files Form Ds gets the Form D rows in its table even if it also files 8-Ks: new Form D (DL-002, DL-004, DL-018) and amendment (DL-005, DL-006)), a UK company (Companies House), an EU or Swiss company (EUDAMED, DiGA directory, no company register in the library)? The answer decides which signals exist.
- **What to catch.** Partnerships and licenses, acquisitions, cybersecurity incidents, new offerings, new authorizations, safety events, breaches. Take the person's words.
- **Cadence.** Use the person's. If none: "cadence not given"; ask. Never set one.
- **Thresholds.** The person's. Never propose a number of events or days as normal; no source sets one.

## Workflow

### Step 1. Map signals to holdings

For each holding type, list the signals that exist from `references/monitoring-signals.md` section 1, with source, clock and row. Mark signals the library cannot read (Companies House, the HHS portal, private rounds) as "the person reads the source directly". Add the status signals for every holding from `references/company-status.md`: 8-K Items 1.03, 2.01, 3.01, 5.01, Form 25 and Form 15 for SEC registrants, Companies House `company_status` for UK companies, German insolvency notices for German companies, each with what it does not mean.

### Step 2. Write each rule in the person's words

Rule = signal + what counts + who owns it + when it is read again. Example shape (proposed, only if asked): "Every new 8-K for HOLDING: open the filing and name the item (DL-019 to DL-024); owner as the person names; read at the person's next review." Never fill the owner or the date.

### Step 3. Write what does not count

At least: "no change recorded" before the log began; a Form D amount as current (DL-006); a registration or listing as an approval (DL-126, DL-127); a missing 8-K as no event (DL-023 (inference)); a breach under 500 as absent from the portal (DL-092 (inference)); a vendor's breach as absent because it is not under the vendor's name (DL-097 (inference)); a Form 15 or Form 25 as dissolution (DL-144, DL-149); a missing risk factor section as low risk (DL-026 (inference)).

### Step 4. Countable facts

List the facts the A2 script can count (W1 to W6, field changes, new filings by type) and say which rule each one serves. A count is not a score.

### Step 5. What the person must decide

Rules, thresholds, cadence, owners, and which signals they will read directly outside the library.

## Build the output

Follow `assets/watch-rules-output.md`. Answer first: the signals that exist for these holdings and the two most important things that do not count. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_watch.py words ANSWER.md`. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule is the person's or labeled "proposed" with its row.
- No benchmark, target or score; no cadence, owner or date the person did not give.
- Signals the library cannot read are named as the person's direct reads.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Watching companies in a market or pipeline rather than holdings: `pipeline-and-market-monitoring` (this pack).
- Watching evidence levels: `evidence-maturity-monitoring` (this pack). Watching the thesis: `thesis-and-memo-monitoring` (this pack).
- Register watches for regulatory changes of the person's own product: `dh-regulatory-and-quality` regulatory-pathway-monitoring.
