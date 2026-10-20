# A1 Signal scan and triage

Framework task: Part A, task A1. Replaces the old tasks DH-01.08.4.1.1 Signal Collection, DH-01.08.4.1.2 Signal Triage & Filtering and DH-01.05.3.1.1 Technology Trend Analysis.

## What this task delivers

A signal log for the person's scope: each signal one sourced, dated record (an authorization decision, decisions per device type by year, a publication record, a company record change, a dated rule or program change), with its source, event date, retrieval date and what it does not show. The log is filtered by the person's scope and filters, deduplicated on identifiers, and split into signals, leads (press or vendor claims whose record is not yet read) and noise (per the person's definition). Where the person asks for trends, it adds proposed readings, each tied to signal ids. It answers "what has moved in our area, on the record, and what is only talk?"

Why it matters: a horizon map built on press releases and remembered dates fails the first time someone asks "where does that come from?". A dated, sourced log can be rerun and checked (`foresight-signal-monitoring`, this pack).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`), as bound to DH-01.08.4.1 in the old skill |
| Skill | DH-01.08.4.1 Part A, Signal scan and triage (with DH-01.05.3.1.1 Technology Trend Analysis) |
| Workflow | The steps below |
| Knowledge | `references/horizon-methods.md` (SP-001 to SP-026; EU-17 to EU-21, US-21 to US-27, US-34, US-35, UK-04, UK-06 to UK-08; SP-066, SP-068 to SP-073, SP-121 to SP-124, SP-134 to SP-141); `references/company-status.md` when a signal names a company |
| Tools | `regulatory-dh.list_jurisdictions` (free); `regulatory-dh.search_devices`; `regulatory-dh.get_pathway_precedents`; `regulatory-dh.find_predicates`; `regulatory-dh.get_deltas` (only to show the log state; never a watch); `literature.list_sources` (free); `literature.search_literature`; `literature.find_trial` (needs a live check); `diligence-dh.get_deltas` for named companies; `scripts/horizon_helpers.py signals`, `byyear` and `makers` |
| Prompt | This guide |
| Template | `assets/signal-scan-output.md` |
| Input | The request and its context: the person's scope (technology area, markets, product codes, companies, topics), time window, filters, sources they already hold, and any leads they bring |
| Governance | `references/governance.md`; signals are records, trends are the person's |
| Catalogue job | none (`list_jobs` on 19 October 2026 lists no horizon scanning job; `examples/live/list_jobs_2026-10-19.json`) |

## Read the request

- **Scope.** Technology area, markets, and any product codes, makers, topics or companies. If none, ask once; propose scope lines labeled "proposed" from the person's own product and markets.
- **Window.** "Since" date. If not given, ask; never pick one. The time horizon ahead (for the B1 scenarios) is the person's; Ormstad's "3 years up to a few months before market entry" (SP-014, [PAPER] DOI 10.1017/S0266462323002684) is context, never their horizon.
- **Filters.** In or out (markets, product types, sources). Theirs; any proposal is labeled.
- **Leads.** Press items, vendor claims or rumors the person brings. Each becomes a lead with the record that would confirm it.
- **Trend wanted?** "What are the trends" adds Step 6. "Technology trend analysis" (old task name) is this task with Step 6.

## Workflow

### Step 1. Perimeter (free)

Call `regulatory-dh.list_jurisdictions {}` and `literature.list_sources {}`. Note what the scan cannot see: on 19 October 2026, UK device registration and CH not loaded, EU decision dates empty on all 3,142 rows, CA rows excluded by the software filter, Cochrane and Embase not queried. These lines become the coverage note.

### Step 2. Authorization signals

For each maker, product or topic in scope, call `regulatory-dh.search_devices {query: "<maker or product>", jurisdiction: "all", limit: 25}`. For each product code in scope, call `regulatory-dh.get_pathway_precedents {product_code: "<code>", jurisdiction: "US"}` and run `python3 scripts/horizon_helpers.py byyear FILE` for decisions per year. Example (saved, `examples/live/`): Aidoc returned K261317, BriefCase-Triage, QAS, decided 14 May 2026; QAS shows 88 decisions from 13 February 2018 (DEN170073, ContaCT, Viz.Al, Inc.) to 16 September 2026.

**Name every maker on record under the product code.** When a product code is in scope, the library names only the makers searched by name. Run `python3 scripts/horizon_helpers.py makers --code <code> --since <window start> FILES` on every saved or live output (search_devices for each maker, get_pathway_precedents, find_predicates) and name every maker it lists, not only the one asked about. Saved records for QAS show Aidoc Medical , Ltd. (five clearances in a window from 1 October 2025), Brainomix Limited (four clearances, latest K251983, 26 August 2025) and Viz.Al, Inc. as stored (De Novo DEN170073, 13 February 2018). Say how many decisions fall in the window's years (get_pathway_precedents) and how many are not yet tied to a maker (2026: 10 decisions, 4 tied, 6 not), and name the public record that lists all of them: FDA's 510(k) database, searchable by product code (FDA medical device databases page, read 20 October 2026; DL-131). Ask for the maker names to search. Each maker named carries its status line (Step 3).

Write what each does not show: a clearance says nothing on AI use, PCCP, clinical effect or uptake; a product-code count is a device type, not an AI count; EU rows carry no decision date. The FDA AI-enabled device list is a separate source (US-24 to US-27): 1,614 rows in the CSV read on 19 October 2026, latest decision 29 June 2026, not comprehensive (US-25, US-35).

### Step 3. Change logs: say what they can and cannot show

If the person asks "what changed since", call `regulatory-dh.get_deltas {product_code, since, jurisdiction}` once. On 19 October 2026 it returned "no watch is registered for this scope; the change log has not started" for every scope tried: quote that line and use Step 2's dated records filtered with `python3 scripts/horizon_helpers.py signals FILES --since YYYY-MM-DD` instead. Never report "no change", and never set a watch.

For named companies, call `diligence-dh.get_deltas {companies: [<legal names>], since}`. Quote the log start (12 October 2026), last sweep and limits beside every "no change recorded". For a window before 12 October 2026, list the company's dated filings and authorizations instead. Any signal about a named company carries the company status line (`references/company-status.md`): for Akili, Pear Therapeutics, Big Health and Aidoc, the status already read (section 6), cited by filing or register name and date ("Aidoc: no SEC registrant found, EDGAR search, 20 October 2026 (SP-162) [WF]; FDA establishment registration 3014938447 active for 2026 (SP-164)"); for any other company, "Status: [GAP]: not read" with the filings to open. A product's current FDA listing holder is stated apart from the company that was authorized (SP-165 to SP-169).

### Step 4. Publication and trial signals

Call `literature.search_literature {query: "<topic>", limit: 20, filters: {date_from: "<window start>"}}`. Each record is a signal that something was published, with DOI and year; it is not a finding. Flag records the person's scope excludes (the saved run ranked a brain-injury depression preprint and a non-digital 2015 trial into a digital insomnia search). Design labels and trial ids are drafts (register N8). For an RCT the person cares about, call `literature.find_trial {record}` (needs a live check).

### Step 5. Rule and program changes, then leads

Add the dated changes from `horizon-methods.md` section 4 that fall in the window and touch the scope (for example AI Act high-risk dates moved by Regulation (EU) 2026/1744, EU-17 to EU-19; MHRA AI Airlock phase 3, UK-07; TAP expansion, SP-122; EHDS dates, SP-068 to SP-073), each with instrument, date and status as read.

For each lead the person brought, name the record that would confirm it and look it up where a library call can (a K number, a maker name). If found, it becomes a signal with the record's date; if not, it stays "lead, not a signal: record not read `[GAP]`". A press date is never an event date.

### Step 6. Triage, deduplicate and (if asked) propose readings

Run `python3 scripts/horizon_helpers.py signals FILES [--since DATE]` on the saved outputs; it dedupes on identifiers, sorts by event date, and prints caveats for empty logs. Apply the person's filters; put out-of-scope rows under "filtered out" with the filter that removed them (never silently). Noise is what the person's definition says it is; if they gave none, list candidates labeled "proposed noise" with the reason.

Trend readings only when asked: each is a "proposed reading" naming the signal ids it rests on and any that cut against it (for example "QAS decisions per year rose from 3 in 2018 to 15 in 2025; 2021 and 2023 fell; 2026 is partial"). Whether it is a trend is the person's call. Any scoring of signal strength or likelihood is the person's; rank only what they scored (B1).

## Build the output

Follow `assets/signal-scan-output.md`. Short mode answers first: how many signals in the window, the two or three that bear most on the person's scope, the leads not yet confirmed, and the coverage limit that most changes the picture. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/horizon_helpers.py words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows and Retrieved columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every signal has a source, an event date, a retrieval date and a "does not show" line. Leads are separate from signals.
- No "no change" from an empty or not-started log; log start and limits quoted.
- No probability, date of arrival, market size or signal-strength score from the model; trends are "proposed readings".
- Every maker the records show under a product code in scope is named, with the count of decisions not yet tied to a maker and the 510(k) database by product code (DL-131).
- Every named company carries the company status line; a product's current FDA listing holder is stated apart from the company authorized.
- Every fact names its source in plain words with its date, then the row id; never a row id alone.
- [PAPER] rows carry their DOI; [WF] rows say so.
- Coverage note present.
- The record line is the very last line of the answer; the calls list and the one-line offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Evaluating one named technology in depth: A2. Scenarios and implications: B1.
- Whether a signal changed the person's earlier calls, and signal quality over time: `foresight-signal-monitoring` (this pack).
- Watching investment targets or holdings: `pipeline-and-market-monitoring` or `investment-portfolio-monitoring` (this pack).
- What a register change means for the person's pathway: `dh-regulatory-and-quality` regulatory-pathway-monitoring.
