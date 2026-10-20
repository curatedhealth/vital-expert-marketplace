# A2 Screen and rule movement

Framework task: DH-DIL.1.2, Part A, task A2. New in this version; it carries the "rerun the screen" practice that replaces watches (`diligence-dh.watch_companies` is never called) and adds the dated rule and register changes a pipeline depends on.

## What this task delivers

Three dated comparisons: the person's earlier saved market screen against a rerun with the same arguments (companies added or not returned, counts that moved); the library's perimeter then and now (sources newly loaded or dropped); and the rule and register changes dated after the person's date that touch the pipeline (HSR, EU and Swiss investment screening, AI Act, UK accounts, DiGA directory), each with its instrument and status. It answers "what moved in the market view and in the rules since we last looked?"

Why it matters: a screen can change because the market changed, because the store loaded a new source, or because the arguments differ. A rule can be adopted, vacated or deferred. Keeping those apart stops a coverage change or a pending rule from being read as news.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | not bound (diligence suite, not a CF-12 row) |
| Skill | DH-DIL.1.2 Part A, Screen and rule movement |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md` sections 1 and 3 (rows DL-036, DL-041 to DL-054, DL-074, DL-075, DL-081, DL-082, DL-085, EU-14, EU-17 to EU-19, EU-21, US-24 to US-26, DE31, DE34) |
| Tools | `diligence-dh.list_sources` (free; needs a live check); `diligence-dh.screen_market`; `scripts/monitor_helpers.py screen-diff` and `rules` |
| Prompt | This guide |
| Template | `assets/movement-output.md` |
| Input | The request and its context; the earlier saved screen and its arguments; the earlier perimeter if saved; the person's date; the jurisdictions and deal types in the pipeline |
| Governance | `references/governance.md`; coverage changes are not market changes; rule changes are facts for the owner the person names for legal questions |
| Catalogue job | `market-screen` (start card not saved; needs a live check). The direct calls in the steps remain the method. |

## Read the request

- **Earlier run.** The saved screen file (or table) and its exact arguments. Without one, there is no comparison: run the screen once and offer to keep it as the baseline.
- **Since when.** The person's date for the rule list. If not given, write "not given" and ask.
- **Jurisdictions and deal types.** Which rules to list: US deals (HSR, CFIUS, DOJ bulk data), EU or Swiss targets, UK companies, DiGA makers, AI-enabled products.

## Workflow

### Step 1. Perimeter then and now (free)

Call `diligence-dh.list_sources` (needs a live check). Compare loaded counts and the not-loaded list with the earlier saved perimeter, if the person has one. A source newly loaded explains new rows; say "new coverage, not a market change".

### Step 2. Rerun the screen with the same arguments

Call `diligence-dh.screen_market` with exactly the earlier arguments. With code execution, save it and run `scripts/monitor_helpers.py screen-diff <earlier.json> <later.json>`. Report companies added, companies not returned, and changes in authorizations, studies, safety records, products or evidence maturity score, each from the two runs' own rows. Before reading "not returned", compare `total_matches` with the `limit`: a company can drop past the limit while its record is unchanged. "Not returned" is never a statement about the company's status: status comes only from the status step (`monitoring-signals.md` section 5); offer A1 for a named company. If the arguments differ, say no change can be inferred (the saved `limit: 8` and `limit: 10` runs of 19 October 2026 are an example).

### Step 3. Evidence maturity movement

Where a score moved, say which input moved if the response shows it; if the rubric version differs between runs, no change can be inferred. The score is a stated convention, never a rating. A full reading of one company's evidence over time is `evidence-maturity-monitoring` (this pack).

### Step 4. Dated rule and register changes

From `monitoring-signals.md` section 3, list the changes dated after the person's date that touch the pipeline's jurisdictions and deal types. With code execution, `scripts/monitor_helpers.py rules --since YYYY-MM-DD` prints the table rows after that date. For each: date, change, instrument, row ids, status (in force, adopted not yet applicable, litigation pending, consultation, announced). Where the status after the read date is not found (the HSR rulemaking after 26 May 2026, DL-054), write `[GAP]`. Say plainly that applying any change to a deal is for the owner the person names for legal questions.

### Step 5. What it may touch (hypotheses)

For each change, at most one line on which of the person's triggers it could touch, labeled "hypothesis for review".

## Build the output

Follow `assets/movement-output.md`. Short mode: screen changes (or "runs not comparable"), perimeter changes, rule changes after the date, and what the library cannot see. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Same arguments in both runs: yes or no, stated.
- No company status read from a screen; "not returned" is not an exit.
- Word count run (`scripts/monitor_helpers.py wordcount <answer.md>`, or by hand): short mode at or under 450 words without the calls list and source columns.
- Coverage changes are labeled as coverage, not as market changes.
- Every rule change has its instrument, date, row id and status; adopted rules not yet applicable say so.
- No market size, no intent, no valuation; no deal called clear.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- No watches are set; monitoring is by dated reruns the person keeps.
- Whether a rule change makes a deal reportable or non-compliant: the owner the person names for legal or compliance questions.
- AI Act classification of a specific product: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
