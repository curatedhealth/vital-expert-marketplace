# A3 Market intelligence quality check

Framework task: DH-DIL.1.2, Part A, task A3. Folds in DH-01.05.2.2 Market Intelligence Quality Assessment & Ecosystem Coverage Monitoring (old pack dh-digital-health-strategy): its task sections "Ecosystem Coverage Monitoring" (DH-01.05.2.2.1, register CF-12.01.05.2.2.1), "market intelligence pass rule" (DH-01.05.2.2.2, CF-12.01.05.2.2.2; steps 2 and 3 below) and "market intelligence miss owner" (DH-01.05.2.2.3, CF-12.01.05.2.2.3; step 6 below). The old file bound the worker `chief-compliance-officer-digital-health`; this skill keeps `worker: "not bound"` and the build notes record the old binding.

## What this task delivers

A dated check of an ecosystem map (the A3 output of `market-and-target-screening`, this pack, or a market read the person brings): each entry marked pass, fail or not measurable on the elements the person sets (by default proposed: source, date, segment covered), the lanes and jurisdictions with no record, the rule entries that dated facts have moved since the map's date, and for each failed element the owner and recheck date the person gives. It answers "can we still rely on our market read, and what is missing?"

Why it matters: a market read ages quietly. A source drops out of the store, a rule's date moves, a lane was never filled. Checking each element against a written rule keeps the read honest before it feeds a strategy, a screen or a memo.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | not bound (the old DH-01.05.2.2 file bound `chief-compliance-officer-digital-health`; kept as a build note, not bound here) |
| Skill | DH-DIL.1.2 Part A, Market intelligence quality check (folds DH-01.05.2.2) |
| Workflow | The steps below |
| Knowledge | `references/market-intelligence-quality.md`; `references/monitoring-signals.md` section 3; `references/named-company-status.md`; `references/gap-rules.md`; rows SP-054 to SP-057, SP-066, SP-068 to SP-073, SP-134 to SP-137, SP-148 to SP-169, DE33, DE34 |
| Tools | `market-access-dh.list_schemes` (free); `diligence-dh.list_sources` (free; needs a live check); `scripts/monitor_helpers.py mi-check` and `rules` |
| Prompt | This guide |
| Template | `assets/market-intelligence-check-output.md` |
| Input | The request and its context: the map or market read (table or CSV with lane, jurisdiction, entry, source, date, gap), its date, the lanes and jurisdictions the person says matter, the person's pass rule and any maximum age, owners |
| Governance | `references/governance.md`; the pass rule, the blocking element, owners and recheck dates are the person's |
| Catalogue job | none |

## Read the request

- **The map.** The ecosystem map the person brings, with its date. If there is none, say so and offer `market-and-target-screening` A3 (this pack) first; this task checks a read, it does not build one.
- **The pass rule.** The elements that count, in the person's words. If none: offer the old file's three elements, "source, date, and segment covered", labeled "proposed", and apply nothing until the person confirms (`market-intelligence-quality.md` section 2).
- **Maximum age.** Only if the person sets one. Never pick it; without it, ages are shown but not judged.
- **Lanes and jurisdictions that matter.** The person's. Without them, check the lanes present and say so.
- **Blocking element, owner, recheck date.** The person's. Write "not given" and ask.

## Workflow

### Step 1. Write the rule back

Number the person's elements in their words, the maximum age if given, the lanes and jurisdictions that matter, and the element that blocks release if the person named one. Proposals are labeled "proposed".

### Step 2. Check each entry (old "market intelligence pass rule")

For each entry: source present (tool and arguments, row id, or "from your material" with its origin), date present, age against the person's maximum age. A gap entry is "not measurable", never "fail" and never "pass". With code execution, save the map as CSV and run `scripts/monitor_helpers.py mi-check <map.csv> --as-of <date> [--max-age-days N] --lanes "<lanes>" --jurisdictions "<codes>"` with the person's values only. An entry with a figure and no source (for example a market size from a deck) fails "source"; the check never supplies a source for it.

### Step 3. Check coverage (old "Ecosystem Coverage Monitoring")

For each lane and jurisdiction the person said matters: entries present, gaps, or none. Class every missing lane as not loaded, not asked or lookup missed (`market-intelligence-quality.md` section 3). If the map is older than the current perimeter, call `market-access-dh.list_schemes {}` (free) and `diligence-dh.list_sources {}` (free; needs a live check) and report any scheme or source whose posture or load date differs from the map's. Saved baseline, 19 October 2026: `examples/market-intelligence/list_schemes_2026-10-19.json`.

Then, for each lane that passes on count, add one line on what its entries hold against `market-intelligence-rules.md` (screening skill, this pack) section 3: for example a Rules lane with only EHDS and deal rows has no device or DiGA rows; route device rules to `dh-regulatory-and-quality` regulatory-pathway-and-classification. This is a note, not a fail, unless the person's rule says so. For an entry that rests on a whole-directory figure (DE33, DE34), say it is not specific to the person's indication. For a board or other outside reader, say which sources are only row ids or tool names and give the readable source (name and URL) that `mi-check` prints in its notes; whether "readable source" becomes an element is the person's call (`--readable-source`).

### Step 4. Reread the rules lane

For each rules entry, compare its date and wording with the dated facts in `market-intelligence-quality.md` section 4 and, for pipeline rules, `scripts/monitor_helpers.py rules --since <map date>`. Report an entry the facts have moved (for example a map citing Regulation 316/2014 as the current EU technology transfer exemption: it expired 30 April 2026, SP-134, SP-135). Whether a moved rule changes the person's plan is for the owner the person names for legal questions.

### Step 5. Status of peers

Each peer company carries one status line from the A1 status step (`monitoring-signals.md` section 5). Where `named-company-status.md` covers the company or product, the line states what the filings and FDA records say, with source and date (`mi-check` prints these in its notes): for the Pear row, chapter 11 (Pear 8-K, 7 April 2023, SP-156 [WF]), Nasdaq delisting notice (Pear 8-K, 10 April 2023, SP-160 [WF]) and Somryst's current FDA listing holder, Nox Medical (SP-167), apart from the applicant at clearance. Otherwise "Status: [GAP]: not read" with the filings to open; a holder as stored can hide a later owner (DL-133 (inference)). A peer with no status line fails an element only if the person's rule says so.

### Step 6. Failed elements: owner and recheck (old "market intelligence miss owner")

List each failed element with the owner the person names and the recheck date the person sets, or that the person stops the read. Do not close a failed element because another skill already described it (the old file: "Do not close a failed element because the existing assessment skill already described it"). Never supply an owner or date; write "owner not named" or "not given" and ask.

## Build the output

Follow `assets/market-intelligence-check-output.md`. Short mode answers first: how many entries pass, fail or are not measurable on the person's rule, the lanes with no record, the moved rules, and the failed elements with owner and recheck date. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words (`scripts/monitor_helpers.py wordcount <answer.md>`, or by hand). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The elements, maximum age, lanes, blocking element, owners and dates are the person's; proposals are labeled and not applied.
- Gap entries are "not measurable"; no lane is filled from memory; no buyer, payer or peer is proposed.
- Every moved rule cites its rows and dates; no "this rule applies to you".
- No market size, share or growth figure; an unsourced figure fails "source" and stays unsourced.
- Word count run: short mode at or under 450 words without the calls list and source columns.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- This task checks a map; building or refreshing it is `market-and-target-screening` A3 (this pack).
- Changes in named companies since a date: A1; screen and rule movement: A2; the pipeline review: B1.
- Signal quality for technology and horizon scanning: `foresight-signal-monitoring` (this pack).
- Payer coverage questions: `dh-access-and-value` coverage-pathway-and-access-strategy.
