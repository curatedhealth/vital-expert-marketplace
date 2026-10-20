# A3 Market intelligence map

Framework task: DH-DIL.1.1, Part A, task A3. Folds in DH-01.05.2.1 Healthcare Ecosystem Analysis & Market Intelligence Generation (old pack dh-digital-health-strategy): its task sections "Ecosystem Census & Mapping" (DH-01.05.2.1.1, register CF-12.01.05.2.1.1), "Competitive Intelligence Analysis" (DH-01.05.2.1.2, CF-12.01.05.2.1.2) and "Market Sizing & Segmentation" (DH-01.05.2.1.3, CF-12.01.05.2.1.3; segmentation of the record only, sizing declined). The old file bound the worker `chief-compliance-officer-digital-health` to all three sections; this skill keeps `worker: "not bound"` and the build notes record the old binding.

## What this task delivers

A dated ecosystem map for one market: the **buyers**, **payers**, **peers** and **rules** on record, each cell a sourced record with its date or a classed gap, plus one coverage line per lane saying what its source cannot see. It answers "who and what surrounds this market, by the record?" It is the evidence base for a strategy or a screen; it is not a market model and it chooses nothing.

Why it matters: a market read built from memory, vendor decks or one store looks complete and is not. A map that keeps every lane sourced and every blank visible lets the person decide where to look next, and lets `pipeline-and-market-monitoring` A3 (this pack) check its quality later.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | not bound (the old DH-01.05.2.1 file bound `chief-compliance-officer-digital-health`; kept as a build note, not bound here) |
| Skill | DH-DIL.1.1 Part A, Market intelligence map (folds DH-01.05.2.1) |
| Workflow | The steps below |
| Knowledge | `references/market-intelligence-rules.md`; `references/screening-rules.md` sections 1 and 5; `references/named-company-status.md`; rows SP-054 to SP-057, SP-059 to SP-073, SP-148 to SP-169, DL-044 to DL-106, DL-126 to DL-133, DL-135 to DL-168, DE30 to DE34, US7 |
| Tools | `diligence-dh.list_sources` (free; needs a live check); `diligence-dh.screen_market`; `commercial-dh.screen_commercial_peers`; `market-access-dh.list_schemes`; `market-access-dh.search_listings` (needs a live check); `commercial-dh.map_money_flow` (only on roles the person gives) |
| Prompt | This guide |
| Template | `assets/market-intelligence-map-output.md` |
| Input | The request and its context: product type or segment, indication if given, jurisdictions, actors the person already named (buyers, payers, partners, peers), any figures the person brings |
| Governance | `references/governance.md`; companies described by their record only; no market size, share or growth figure from the model |
| Catalogue job | none saved for this task; `market-screen` covers the peers lane (start card not saved; needs a live check). The direct calls in the steps remain the method. |

## Read the request

- **Market.** Product type or segment (the library slugs are `dtx`, `samd-diagnostic`, `cdss`, `rpm`, `digital-health`; on 19 October 2026 only `dtx` held companies), indication if the person gives one, and jurisdictions. If jurisdictions are not given, ask once; never pick them.
- **Lanes.** All four by default; the person may ask for fewer. Which lanes matter for the decision is the person's call.
- **Actors already named.** Buyers, payers, partners or peers the person lists go in "from your material", in their words.
- **Market size, share or growth.** If asked, say in one line that no source in this skill gives one (DL "Not sourced"; SP "Not sourced") and continue with the map. A figure the person brings is shown as theirs, with its source as they give it.
- **"Who should we target" or "which segment wins".** Not this task: the map lays out the record; the choice is the person's (B1 on their criteria, or `dh-go-to-market` market-segmentation-and-gtm-strategy for positioning their own product).

## Workflow

### Step 1. Read the perimeters (free first)

Call `diligence-dh.list_sources` with no arguments (needs a live check; fallback `commercial-dh.list_commercial_dh_sources`, `tools.md`) and `market-access-dh.list_schemes` with no arguments. Note for each lane what is loaded and what is not, with reasons and load dates: on 19 October 2026 the company store held `dtx` only, and the scheme store held DE_DIGA 82 listings ("partial"), FR_LPPR and UK_NICE_NHAP 0 ("gap"), US_CMS_DMHT 3 and US_CMS_RPM 4 ("partial") (`examples/market-intelligence/list_schemes_2026-10-19.json`).

### Step 2. Peers lane

Run A1 steps 2 to 4 for the segment and each jurisdiction (`diligence-dh.screen_market {segment, jurisdiction, limit}`). For a named product, call `commercial-dh.screen_commercial_peers {segment, name, limit}`: it adds the device row and the payer listing check for that product. Record per company only what the record states: products as stored, authorizations, studies, safety records, evidence maturity "N (rubric v1)". Read authorization wording with DL-126 to DL-133 (registration is not approval; 510(k) clearance is not "approval"; De Novo orders sit outside Devices@FDA). Never add a peer from memory; a peer the person names and the store misses is "lookup missed" (`gap-rules.md`). Then add, from `named-company-status.md`, each peer product's current FDA listing holder beside the holder as stored (Somryst: Pear Therapeutics, Inc. as applicant, K191716, SP-165; listed by Nox Medical from 18 December 2024, SP-167), and FDA-listed products in the same product code that the rows hold (SleepioRx, K233577, product code QVO, listed by Big Health Inc, SP-163). A product found only in the FDA listing rows is labeled "FDA listing, not in the store".

### Step 3. Payers lane

For each jurisdiction, list the schemes the store holds with their posture and load date (step 1). For a named product, call `market-access-dh.search_listings {query: "<product name>"}` (needs a live check; a scheme code as the query returns nothing) or read the `search_listings` block of the step 2 peer call. For Germany, add the directory facts DE30 to DE34 (what the directory publishes; refusals undisclosed) and always the DE34 counts row, "BfArM DiGA page, as of 9 September 2026", noting that the counts cover the whole directory, not the indication; never cut it for length. For the US, say the CMS DMHT and RPM rows are code-level, not product-level, and put US7 beside each peer's stored regulation number: G0552 to G0554 are payable only for devices classified under 21 CFR 882.5801 (Federal Register, 9 December 2024, US7); Somryst's 510(k) states 882.5801 (SP-165). Whether a product qualifies is not stated. What a scheme pays or whether a product qualifies: route to `dh-access-and-value` coverage-pathway-and-access-strategy.

### Step 4. Buyers lane

Buyers come from the person. If the person names the user, buyer and payer roles for a product, call `commercial-dh.map_money_flow {reference, user, buyer, payer}` with their words: it echoes the roles, flags conflation and attaches the payer listing. Never read money direction or amounts from its exhibit ("no amounts and no direction of payment", `money_flow_somnio.json`). If the person names no buyers, write the lane as "[GAP]: not given" and ask who adopts and contracts in their market; never propose a buyer type.

### Step 5. Rules lane

List the dated instruments that bear on the market from the rows: EHDS application dates for the EU (SP-068 to SP-073), the WHO strategy's status as policy context (SP-066), and the data and deal rules with their dates (DL-044 to DL-106, `deal-and-data-flags.md`). Each line: instrument, date, what it covers in the row's words, row id. Include every flag the rows support for the data the market runs on (for example GDPR Article 9 for health data, DL-099 to DL-106; HIPAA breach rules and the HHS breach portal, DL-086 to DL-098). If the person's question concerns a device product, add one line routing device status and pathway to `dh-regulatory-and-quality` regulatory-pathway-and-classification, and say in the lane's coverage line that the rules lane holds no device or DiGA rules. Device status and pathways go to `dh-regulatory-and-quality` regulatory-pathway-and-classification; AI Act dates and rule changes since a date go to `pipeline-and-market-monitoring` A2 (this pack). Whether a rule applies to the person's product or deal is for the owner the person names for legal questions.

### Step 6. Group, if asked

If the person wants products grouped by what they do, use the WHO classification second edition (SP-054 to SP-057) and label each assignment "proposed", with the record it rests on. If the person gives their own segment labels, use theirs. Never rank lanes, actors or segments.

### Step 7. Gaps and status

Class every blank with `gap-rules.md`. Each peer company covered by `named-company-status.md` gets its status from those rows, with the source name and date and what each form does not mean (Pear Therapeutics: chapter 11, Pear 8-K, 7 April 2023, SP-156 [WF]; Nasdaq delisting notice, Pear 8-K, 10 April 2023, SP-160 [WF]; Form 25-NSE, 2 May 2023, the last EDGAR filing, SP-155 [WF], which is not dissolution, DL-144. Big Health: no SEC registrant found, SP-162 [WF]). One line "Status: [GAP]: not read" per `screening-rules.md` section 5 covers the peers no row covers, with the filings to open per company on request (A2). Never infer status or a holder from press, memory or a missing filing.

## Build the output

Follow `assets/market-intelligence-map-output.md`. Short mode answers first: the market as scoped, the four lanes in one table (at most four rows per lane), one coverage line per lane, the gaps that change the picture. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words (`scripts/screen_helpers.py wordcount <answer.md>`, or by hand). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every cell has a source named in plain words with its date, then the row id (or the library tool with its save date), never a row id alone; every lane has its coverage line. Payers, DE carries the DE34 counts row; peers covered by `named-company-status.md` carry status and the current FDA listing holder.
- No market size, share, growth, revenue, valuation or intent from the model; figures the person brought are labeled "from your material".
- Buyers are the person's; no buyer type proposed. Money direction is never read from the money-flow exhibit.
- Any WHO grouping is labeled "proposed" with its record.
- One status line for the peers lane; missing fields print as "not in the record", never 0 or "none".
- Word count run: short mode at or under 450 words without the calls list and source columns.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Facts only; no segment choice, target choice or build, partner or buy decision (the old guardrail "Do not invent ... build-partner-buy decision"). Options and choices are `strategic-vision-and-options` (this pack).
- Quality of the map over time (coverage, pass rule, owner of a failed element): `pipeline-and-market-monitoring` A3 (this pack).
- Signals and trends about technologies: `horizon-scanning-and-technology-evaluation` (this pack).
- Positioning one's own product, segments and GTM motion: `dh-go-to-market` market-segmentation-and-gtm-strategy.
- What a payer pays and how to get coverage: `dh-access-and-value` coverage-pathway-and-access-strategy.
