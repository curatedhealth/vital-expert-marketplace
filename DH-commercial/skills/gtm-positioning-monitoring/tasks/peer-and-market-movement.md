# A2 Peer and market movement

Framework task: DH-02.01.2.2, Part A, task A2. New in this version; it carries the separate tool skills "Read commercial changes" (as it applies to positioning) and the peer screen rerun.

## What this task delivers

A dated read of what changed since the positioning was set: in named peers' public records, in the peer screen for the segment, in the payer routes the positioning relies on, and in the rules on wording. Each change carries its source and date, and the read says plainly what the library cannot see. It answers "has anything moved that our positioning depends on?"

Why it matters: a line that was distinct from peers, or that named a route, can stop being true without anyone touching it. A dated comparison with an earlier saved run makes the question answerable.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Marketing Manager (`digital-marketing-manager`) |
| Skill | DH-02.01.2.2 Part A, Peer and market movement |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md` (signals 3 to 6); the earlier saved run or the positioning date |
| Tools | `commercial-dh.list_commercial_dh_sources` (free); `diligence-dh.get_deltas`; `commercial-dh.screen_commercial_peers`; `diligence-dh.compare_portfolio` and `diligence-dh.get_evidence_maturity` (peer evidence position); `market-access-dh.find_scheme_precedents` and `market-access-dh.get_status_history` (listed status only); `scripts/positioning_check.py peers-diff` |
| Prompt | This guide |
| Template | `assets/movement-output.md` |
| Input | The request and its context; named peers; the segment and its markets; the date the positioning was set or the earlier saved run |
| Governance | `references/governance.md`; peers described by their record only |
| Catalogue job | `competitor-landscape` (peer position via `diligence-dh.compare_portfolio`); `screen-commercial-peers` for the rerun. The direct calls in the steps remain the method; the job is the buyer's one-call option (`start_job` returns the steps and inputs and runs nothing; `examples/live/start_job_runs.json`). |

## Read the request

- **Since when.** The date the positioning was set, or the earlier run's date. If not given, ask; never pick one.
- **Peers.** Named by the person, or from the segmentation skill's A1. Company names as the store holds them (for example "Big Health, Inc.").
- **Routes and rules.** The routes and markets the positioning names.

## Workflow

### Step 1. Perimeter (free)

Call `commercial-dh.list_commercial_dh_sources`. Note the last load dates and what is not loaded. Compare scheme listing counts and clock rules with the earlier saved run, if the person has one.

### Step 2. Peer record changes

Call `diligence-dh.get_deltas` with `{companies: [<up to 12 names>], since: "<YYYY-MM-DD>"}`. Report changes with their event dates and URLs. Always quote the log: first entry 12 October 2026 in the live test, last sweep, and that "no change recorded" is about the log, not the company. Do not use `commercial-dh.get_deltas` for this: it drops the log block and its Market Access feed is missing (`tools.md`).

### Step 3. Peer screen rerun (if the person has an earlier run)

Call `commercial-dh.screen_commercial_peers` with the same arguments as the earlier run. With code execution, save both and run `scripts/positioning_check.py peers-diff <earlier.json> <later.json>`. Report companies added and changes in authorization counts or products. A company "not returned" is not an exit. If the arguments differ, say no change can be inferred.

### Step 3b. Peer evidence position

Where the positioning rests on a contrast with named peers (for example "the only one with randomized evidence"), call `diligence-dh.compare_portfolio` with `{companies: [<the same 2 to 12 names>]}` and compare authorizations by register, studies by link tier and evidence maturity points with the earlier saved run. Use `diligence-dh.get_evidence_maturity {company}` to show which input moved for one peer. A change in points is reported with the input that changed (for example a new product-linked study); if the rubric version differs between runs, no change can be inferred. This is context about a peer's published evidence; it never rates the person's product and never says the line is now true or false. Pitfalls (company level, exact names, reimbursement cell always `not_assessable`, EU authorizations counted under a "US sources only" note) are in `tools.md`; trimmed run in `examples/live/compare_portfolio_dtx_2026-10-19.json`.

### Step 4. Listed peers in the person's indication

Where the positioning sits on a listing route, call `market-access-dh.find_scheme_precedents` with `{scheme, indication, limit: 10}` (for example DE_DIGA with "F51") and compare listings and listing dates with the earlier run. Status only; prices stay with Market Access.

For each listed peer, call `market-access-dh.get_status_history {reference: <product>, scheme: "DE_DIGA"}`. Report any BfArM notice entry with its change date (for example HelloBetter Schlafen: permanent from 17 December 2024, BfArM notice 18 of 2 January 2025; `examples/live/get_status_history_DE_DIGA_F51.json`). The first entry's `changed_on` is the listing date, not a status change. Where only that first entry is stored, say "status changes not stored `[GAP]`", not that none happened.

### Step 5. Route and rule changes

From `monitoring-signals.md`, list the dated changes (signals 4 and 5) that fall after the positioning date and touch the person's segment or wording. State each with its instrument and date (for example "FDA General Wellness guidance issued 6 January 2026, supersedes the 2019 version, PC-US-57"). Drafts and proposals are labeled as such.

### Step 6. What it may mean (hypotheses)

For each change, one line on which part of the positioning it could touch (the "what it is not" boundary, a route named in the line, a wording rule), labeled "hypothesis for review". Never infer a peer's intent or results.

## Build the output

Follow `assets/movement-output.md`. Short mode: the changes that touch the positioning, then "no change recorded" with the log caveat, then what the library cannot see. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every change has its date, source and retrieval date; every rule change its instrument.
- The log caveat appears wherever "no change" is reported.
- No peer intent, results or revenue. Evidence maturity appears as points with rubric version and limits, never as a verdict on the person's product.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No watches are set; monitoring is by dated reruns the person keeps.
- What a route pays, and whether the product qualifies, is Market Access's question.
- Drugs, biologics and wellness apps are out of scope.
