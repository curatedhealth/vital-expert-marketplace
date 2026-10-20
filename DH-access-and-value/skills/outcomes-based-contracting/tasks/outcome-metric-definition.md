# A1 Outcome metric definition

Framework task: DH-03.01.1.1, Part A, task A1. Replaces the earlier "Outcomes Metric Definition" section.

## What this task delivers

A list of candidate outcome measures for an outcomes-based contract, each laid out with its definition, data source and owner, collection burden, attribution risk and baseline need, drawn from the person's own measures and the official measure sets. It answers "what could we put in the contract, and what would each measure cost and risk?"

Why it matters: the OECD names hard-to-get, uninformative outcome data and unvalidated surrogates among the main reasons performance-based agreements fail (`references/outcome-measures.md`). A measure chosen because it is available, not because it is attributable and collectable, decides the contract before anyone negotiates it.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.1.1 Part A, Outcome metric definition |
| Workflow | The steps below |
| Knowledge | `references/outcome-measures.md` (AbEM fields, ACCESS targets, the five properties); `references/outcomes-contracting-sources.md`; `references/access-monitoring-sources.md` rows DE-16 to DE-19 |
| Tools | `market-access-dh.find_scheme_precedents` (optional, comparables); `literature.search_literature`, `literature.get_record`, `verify.qualify_source`, `verify.check_claim` (only when the person asks for validated instruments) |
| Prompt | This guide |
| Template | `assets/outcome-metric-definition-output.md` |
| Input | The request and its context; product, indication, market, payer; the measures the person already collects; their data systems |
| Governance | `references/governance.md`; the person chooses and rates; clinical claims stop for regulatory affairs |

## Read the request

- **Market and payer.** Germany (GKV-Spitzenverband price with the outcome-linked component, or a § 140a fund contract), United States (an ACCESS participant or a commercial payer), or other. The market sets which official measure set applies. If unclear, ask.
- **Listing status.** For a DiGA, trial or permanent? Trial DiGA do not report AbEM (DE-17), which changes which data exists.
- **The person's own measures.** What they already collect, in which system, at which time points. Ask for this before proposing anything; it is the first source.
- **Instruments.** Whether they want validated instruments found in the literature. Do not search unless asked.
- **Mode.** Short for a direct question; full for a document.

## Workflow

### Step 1. List the person's own measures

Write each one down as they name it: what is measured, instrument, when, where it is stored, who holds it. Blank fields stay `[GAP]` with "ask OWNER". These come first in the output because they are the cheapest to collect.

### Step 2. Add the official measure set for the market

From `references/outcome-measures.md`:

- **Germany (DiGA).** AbEM fields: usage duration and frequency (Stage I, from 1 July 2026), satisfaction and a single-item PROM (Stage II, 2027), indication-specific PROMs (Stage III, 2028), with redeemed and repeat prescriptions as denominators (DE-18). State the limits each time: permanent DiGA only, PROM participation voluntary with one reminder, PROM instrument names not sourced `[GAP]`.
- **United States (ACCESS).** The track's measures and targets, for example PHQ-9 5-point reduction if baseline is 10 or more (else final under 10), GAD-7 4-point reduction if baseline is 10 or more (else final under 10), PGIC submission at end of period on BH, systolic BP below 130 mm Hg or a 15 mm Hg reduction, 5 percent weight loss. State the rules: all required measures per patient, baseline within 60 days, self-report only for weight and PROMs, 15-day validity.
- **Other markets.** Say that no official outcome measure set for digital products was sourced (England pays on cost and volume; France has no current confirmed scheme) and work from the person's measures.

### Step 3. Lay out the five properties per measure

For each candidate, fill one row: definition (instrument, unit, window), data source and owner, collection burden, attribution risk, baseline need. Use facts, not ratings: "PROM, voluntary, one reminder allowed (DiGAV § 23a)" for burden; "usage minutes could rise from reminders without health change" for attribution. Where the person has asked you to rate, mark each rating "proposed" with the fact behind it.

### Step 4. Flag the measures that need a decision

Name, in one line each: measures whose data will not exist in time (AbEM PROMs before 2027), measures with no named owner, measures where use stands in for health (usage minutes), and measures that need a baseline the current workflow does not take.

### Step 5. Comparables (optional)

If the person wants to see what similar products are listed with, call `market-access-dh.find_scheme_precedents {scheme: "DE_DIGA", indication: "<ICD code, for example F32>", limit: 10}`. Report status and recorded price with the retrieval date. Say plainly that the library holds no comparator's outcome component or contract terms (`references/tools.md`).

### Step 6. Validated instruments (only when asked)

1. `literature.search_literature {query: "<instrument> validation minimal clinically important difference", limit: 5}`. Read titles; drop off-topic records.
2. `literature.get_record {pmid or doi}` for the abstract text.
3. `verify.qualify_source {doi}`; keep the returned object.
4. `verify.check_claim {claim: {text}, passage: {text: "<quoted abstract sentence>", locator: "abstract"}, source: {source_id, tier, source_type, doi, official_url}}`.
5. Report only claims that come back "supported", with the passage. If a value (for example an MCID) is not in the passage, say "not verified from the abstract".

## Build the output

Follow `assets/outcome-metric-definition-output.md`. Answer first: which two or three measures look strongest on the facts, and the one decision the person must make. Then the measure table.

## Before you hand it over

- Every official measure and rule cites its row in `references/`.
- Every rating of burden or attribution is the person's, or marked "proposed" with its fact.
- No measure is presented as clinical evidence of the product.
- Choosing measures for a contract stops for the accountable owner; wording for a payer stops too.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model lists and lays out; it does not choose the contract's measures.
- No instrument is named as the AbEM PROM for an indication; that is not sourced.
- Drugs, biologics and wellness apps are out of scope.
