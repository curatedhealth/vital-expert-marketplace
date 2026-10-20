# A1 Segment landscape

Framework task: DH-02.01.2.1, Part A, task A1. Replaces the old "Segment definition" task and the separate tool skills "Screen commercial peers", "Commercial landscape report" and "List commercial sources".

## What this task delivers

A fact table, one row per candidate segment the person names (or proposes, labeled), that says who buys, uses and pays, which payer route and channel rules exist in that market, and which peers the public record shows, each with its source and date. It answers "what segments could we serve, and what does the record say about each?"

Why it matters: segment choices made without the payer route and the channel rules in view tend to fail at the first buyer meeting. A dated fact table makes the later choice (B1) arguable and repeatable.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Marketing Manager (`digital-marketing-manager`) |
| Skill | DH-02.01.2.1 Part A, Segment landscape |
| Workflow | The steps below |
| Knowledge | `references/segment-and-payer-routes.md`; `references/channel-rules.md`; `references/drug-digital-combination.md` (software sold with or for a drug); `references/channels-partners-launch-sources.md` (CP rows) |
| Tools | `commercial-dh.list_commercial_dh_sources` (free); `commercial-dh.screen_commercial_peers`; `market-access-dh.find_scheme_precedents` and `market-access-dh.get_status_history` (listed status only); `regulatory-dh.search_devices` (US DMHT makers); `diligence-dh.compare_portfolio` and `diligence-dh.get_evidence_maturity` (peer evidence position); optional `diligence-dh.build_company_profile` or `commercial-dh.generate_report` for one named company or product |
| Prompt | This guide |
| Template | `assets/segment-landscape-output.md` |
| Input | The request and its context; the product, its intended use and device status as the person states them; candidate segments and markets |
| Governance | `references/governance.md`; peers described only by their record |
| Catalogue job | `competitor-landscape` (peer position: `commercial-dh.generate_report` plus `diligence-dh.compare_portfolio`); `screen-commercial-peers` for a peer list only. The direct calls in the steps remain the method; the job is the buyer's one-call option (`start_job` returns the steps and inputs and runs nothing; `examples/live/start_job_runs.json`). |

## Read the request

- **Product and intended use.** Needed to know which routes can apply (for example DMHT needs 21 CFR 882.5801 or 882.5803, CP-US-58, CP-US-62). If not stated: `[GAP]`; still build the table, and say which cells depend on it.
- **Sold with or for a drug.** If the software is sold with a drug, for a drug, or with a drug maker, read `references/drug-digital-combination.md` and flag those segments. The combination's regulatory status is `[GAP]` here; route it to `dh-regulatory-and-quality`.
- **Candidate segments.** Use the person's. If they name none, propose up to four from the routes in `segment-and-payer-routes.md` for their markets, each labeled "proposed".
- **Markets.** If not stated, ask once; default to the markets the person's product is authorized in, as they state them.
- **Depth.** "Who are our peers" alone is a peer screen (steps 1, 3, 6). "Competitor landscape" or "how do our rivals compare" adds step 4. "Commercial landscape for X" adds step 5.

## Workflow

### Step 1. Read the perimeter (free)

Call `commercial-dh.list_commercial_dh_sources` with no arguments. Note for the answer: which jurisdictions hold device authorizations (on 19 October 2026: US 1,226, EU 3,142, UK 0, CH 0), which schemes hold listings, and what is not loaded and why. These lines become the coverage note; they tell the person what the screen cannot see.

### Step 2. Write each segment's roles and route

For each candidate segment, fill buyer, user, payer, setting and job, market (`segment-and-payer-routes.md`, "How a segment is written"). Then fill the payer route from the per-market tables with its row ids: for example "US Medicare DMHT: practitioner bills G0552 to G0554 and must bear the device cost (CP-US-59)"; "Germany DiGA: prescription or fund approval with proof of indication (CP-DE-01, CP-DE-02)"; "England: NHS procurement with DTAC review (CP-UK-01)"; "US employer: rules not sourced `[GAP]`". For a segment flagged "with or for a drug", take the route and channel cells from `drug-digital-combination.md` (for example "Germany: DiGA route excluded for an app meant for use with a specific drug, CP-DE-04"); keep its `[GAP]` lines. Add the two or three channel rules that will bind a motion in that segment from `channel-rules.md` (for example AKS where Medicare pays, BAA for a health system, HBNR for direct to consumer).

### Step 3. Screen peers

Call `commercial-dh.screen_commercial_peers` with `{segment: "<taxonomy segment>", limit: 10}`. Taxonomy segments are `dtx`, `samd-diagnostic`, `cdss`, `rpm`, `digital-health`; on 19 October 2026 only `dtx` was loaded. To include a named product, add `name` (it takes one of the `limit` slots). The response is large; with code execution, save it and run `scripts/gtm_helpers.py peers <file>`. Read products from the screen's own results: the per-peer device lookup uses company names and missed 9 of 10 companies in the live test (`tools.md`).

For a US DMHT segment, also call `regulatory-dh.search_devices` with `{query: <short maker name>, jurisdiction: "US"}` for each known maker (for example "Big Health" returns Sleepio K233577, QVO, 882.5801, and Daylight K233872, SCP, retrieved 13 October 2026; `examples/live/search_devices_BigHealth_US.json`). Report the regulation number and product code. Where the miss remains, say 'lookup missed' and name the product code to search.

For a market the screen does not reach (Germany), call `market-access-dh.find_scheme_precedents` with `{scheme: "DE_DIGA", indication: "<ICD code>", limit: 10}` for listed peers in the indication (for example "F51" returned somnio, HelloBetter Schlafen and somnovia, all permanent, retrieved 15 October 2026). Use status, listing date and URL only; prices there are Market Access's subject.

`listed_on` is the first listing date, not the date the current status began. For each DiGA peer, call `market-access-dh.get_status_history {reference, scheme: "DE_DIGA"}` and report the status date where a BfArM notice records it (for example HelloBetter Schlafen: listed 18 December 2022, permanent from 17 December 2024, BfArM notice 18; `examples/live/get_status_history_DE_DIGA_F51.json`). Where only the first-load snapshot is stored (somnio, somnovia on 19 October 2026), write the listing date and "date status began not stored `[GAP]`".

### Step 4. Peer evidence position (competitor landscape)

Call `diligence-dh.compare_portfolio` with `{companies: [<2 to 12 references>]}`, using the names the screen or the listing returned. It returns, per company, authorizations by jurisdiction, studies by link tier (named by brand, same sponsor and indication only, unlinked), safety events, public funding signal counts and the evidence maturity score with its components. For one peer whose score needs explaining, call `diligence-dh.get_evidence_maturity` with `{company: "<exact name, brand or FDA number>"}`: it shows the rubric (v1, 7 October 2026), every input and the components excluded because their source is not loaded.

Read it as context about a peer's published evidence, never as a judgment of the person's product, never as a ranking of segments, and never as a prediction. Write the score as "N of M assessable points (rubric v1)" beside its components; `none_found` and `not_assessable` are not zero. Pitfalls from the live run (`tools.md`; `examples/live/compare_portfolio_dtx_2026-10-19.json`):
- It works at company level. "Somryst" resolved to Pear Therapeutics, Inc., so the score and the two recall flags cover reSET and reSET-O as well. Say which products the company row covers.
- An unresolved name ("HelloBetter") returns every cell `not_assessable`. Retry with the exact maker or brand from the listing; otherwise write "lookup missed".
- Reimbursement listings show `not_assessable` ("no reimbursement source is loaded") even for DiGA makers. Take listed status from step 3, not from this table.
- The rubric note says "US sources only", yet EU authorizations count (deprexis: EU 31, from EUDAMED). Say which register each authorization comes from.
- Two filing names combined into one company are "a proposal until a person validates it"; repeat that flag.

This is the method of the catalogue job `competitor-landscape`, which pairs it with `commercial-dh.generate_report` (step 5).

### Step 5. Company or product view (only when asked)

If the person wants a view of one named company or product, call `diligence-dh.build_company_profile` with `{company: "<exact name or FDA number>"}`, or, for a shareable memo, `commercial-dh.generate_report` with `{reference, template: "commercial", segment, limit, buyer, user, payer}`. Restate the identity block as a table; take the authorization from the identity block, not the readiness checklist (they disagreed in the live test); never paste the raw JSON. Do not call both for the same company.

### Step 6. Classify gaps

Word every missing fact with `references/gap-rules.md`: lookup missed, covered but absent, not covered, code-based route. Never "no competitor" or "empty market".

## Build the output

Follow `assets/segment-landscape-output.md`. Short mode answers first: the segment table (roles, payer route, top channel rule, peers on record), then the coverage note, then the gaps that change a decision. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every route and rule carries its row id; every peer fact its source URL and retrieval date.
- Proposed segments are labeled "proposed".
- No peer outcome, revenue, intent or price. Evidence maturity is shown as points with its rubric and limits, as context on a peer's published evidence, never as a verdict on the person's product.
- Coverage note present: what the library does not load.
- If it leaves the conversation, ask who clears it and call `verify.build_record` with that person in `cleared_by`; otherwise label it an uncleared draft.

## Boundaries

- Facts only; no choice of segment (that is B1, on the person's scores).
- Whether a product qualifies for a payer route, and what it pays, is the Market Access pack's question.
- Drugs and biologics themselves are out of scope; software sold with or for a drug is in scope for its route and channel facts only, and its regulatory status goes to `dh-regulatory-and-quality`. Wellness apps are out of scope; a wellness product cannot use device-only routes (CP-US-70).
