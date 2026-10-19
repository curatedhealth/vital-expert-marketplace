# A2 Price evidence

Framework task: DH-03.01.2.1, Part A, task A2 (old name: Pricing Strategy).

## What this task delivers

The sourced price facts a pricing decision rests on, in three labeled layers: the price rules that bind (DiGA threshold and group maximums, the year-one and month-13 rules, US relative values and conversion factor, French fee caps); the registered prices of comparators and codes; and, only on the person's own inputs, model outputs labeled hypotheses. It answers "what do the rules and the market say about price here?" It never answers "what should our price be".

Why it matters: in Germany negotiated DiGA prices averaged 227 EUR per quarter, 59 percent below the manufacturer prices they replaced (DE-9). A pricing plan that reads year-one prices as the market, or a model ceiling as a price, is built on the wrong number.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.2.1 Part A, Price evidence |
| Workflow | The steps below |
| Knowledge | `references/price-rules.md`; `references/coding-pricing-sources.md`; `references/access-monitoring-sources.md` (DE-9, DE-10, DE-4); `references/france-pecan-lppr-latm.md` |
| Tool | `find_scheme_precedents`, `search_listings`, `commercial-dh.get_pricing_corridor` (own row only), `commercial-dh.map_money_flow`, `analytics.vba-price-anchor`, `analytics.budget-impact-model`; `scripts/price_facts.py` |
| Prompt | This guide |
| Template | `assets/price-evidence-output.md` |
| Input | The request and its context; A1 map if present; the person's own inputs for any model |
| Governance | `references/governance.md`; pricing position stops for its owner |

## Read the request

- **Markets and routes.** Take them from A1 if it ran. Otherwise ask which route (DiGA, PECAN, LATM, RPM, DMHT, ACCESS, NHS procurement).
- **Indication.** For comparators.
- **Model inputs.** Only if the person wants a model: comparator cost, QALY gain and the threshold(s) they choose for `vba-price-anchor`; eligible population, current mix, cost and uptake for budget impact. The model never supplies these.
- **A request for "our price".** Say the price is the owner's decision; offer the facts and the person's own model runs.

## Workflow

### Step 1. Price rules that bind

From `references/price-rules.md`, write the rules for each route with their validity window. Germany: who sets the price and when (DE1, DE7, DE9), arbitration (DE5), threshold 0.84 EUR per day and the published group maximums for 1 October 2026 to 31 March 2027 (DE14), the mechanics (DE15), the 20 percent outcome share (DE2) and the 2027 volume discount (DE3). US: conversion factors (US8), no national floor (US9), DMHT contractor pricing (US19), ACCESS amounts and withhold (US31 to US33). France: PECAN caps and LATM fee structure (France file). England: the MTFM tests (EN1).

### Step 2. Registered prices of codes

US: use the stored rows from A1, or call `find_scheme_precedents` for US_CMS_RPM and US_CMS_DMHT. Report the national amounts as stated, with setting (facility or non-facility) and the conversion factor; say they are before geographic adjustment. Run `scripts/price_facts.py` to recompute RVU x conversion factor and flag empty price fields.

### Step 3. Registered prices of comparators

Germany: `find_scheme_precedents` with `{scheme: "DE_DIGA", indication: <ICD code or German term>, limit: 25}`. For each comparator report status, listing date, months listed and the stored price. Say which rule applies by time since listing (year one: manufacturer price; after: negotiated or arbitrated amount) and that the library does not say which kind the stored figure is or its prescription period `[GAP]`. Put DE-9 and DE-10 beside it as national context. France: `find_scheme_precedents` on FR_PECAN and FR_LATM; amounts are in the passages. Never call `get_pricing_corridor` for comparators: it mixes unrelated products (`tools.md`).

### Step 4. The product's own registered price, if listed

`search_listings` with the product name. If found, `get_pricing_corridor` may be used for the product's own row; discard the other rows.

### Step 5. Who pays whom, on the person's description

If the money flow is unclear, call `commercial-dh.map_money_flow` with the user, buyer and payer as the person states them. Report the three roles and the `conflated` flag. It is the person's description, not a finding.

### Step 6. Models, only on the person's inputs

If asked: `analytics.vba-price-anchor` with the person's comparator cost, QALY gain and thresholds (plain numbers list). `analytics.budget-impact-model` with the person's population, mix, cost and uptake; if it returns 422, do the arithmetic in the conversation and show it. Label every output "hypothesis on your inputs; not a price". Show the inputs beside the result.

### Step 7. What the facts constrain

Close with conditional consequences from the rules only, for example: "if listed on trial, the year-one price runs at least 12 months, then the GKV-Spitzenverband amount applies (DE1, DE9)"; "above 10,000 redeemed codes the group maximum falls to 75 percent (DE15)"; "if listed on trial, the listing itself can end: seven DiGA were removed in 2025, almost all after more than 12 months on trial (DE-4, access-monitoring-sources.md)". No recommendation of a number.

## Build the output

Follow `assets/price-evidence-output.md`. Answer first: the rule that bounds price on this route and the comparator range as stored. Keep the three layers in separate tables.

## Before you hand it over

- No number in the output is a price for the person's product.
- Every rule has its row and validity window; every registered price its source and retrieval date; every model output its inputs and the label "hypothesis".
- National averages are labeled context.
- Confidential prices from the person are not sent to any library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record`.

## Boundaries

- The pricing position, list price, discount and corridor are the owner's.
- No QALY-based launch price as a recommendation; the health economics pack owns cost-effectiveness modeling.
- Drugs, biologics and wellness apps are out of scope.
