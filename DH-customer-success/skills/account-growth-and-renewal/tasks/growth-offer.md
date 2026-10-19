# A2 Growth offer

Framework task: DH-02.02.2.1, Part A, task A2. Replaces the earlier "Growth offer" section (CF-12.02.02.2.1.2).

## What this task delivers

For each account the person wants to grow, a draft offer sheet: the additional module, site or population as the person names it, the result the account has already seen that the offer builds on (or `[GAP]`), each element of the offer (price change, free or bundled item, trial, services, anything for patients, fees to third parties, outcome terms) with the sourced rules it is tested against and the facts still missing, and a flag table for every claim the offer's materials make. It answers "what can we offer this account, and what can our proposal say?"

Why it matters: a free module attached to a renewal is not a "discount" under the federal safe harbor unless narrow conditions hold (FA10). A free device can remove a customer's DMHT billing basis (CP-US-59). A success story repeated in a proposal becomes the company's own claim (PC-UK-03). Each of these is found before the offer goes out, not after.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Partnerships Director (`digital-partnerships-director`) |
| Skill | DH-02.02.2.1 Part A, Growth offer |
| Workflow | The steps below |
| Knowledge | `references/offer-rules.md`, `references/discount-rule-additions.md`, `references/account-materials-claims.md`, `references/starter-rules.md` (SR5 to SR8) |
| Tools | `commercial-dh.audit_claims` (counted, authorization record only); `commercial-dh.map_money_flow` (counted, optional); for a value case, `commercial-dh.get_pricing_corridor`, `analytics.budget-impact-model`, `analytics.vba-price-anchor` (counted, only on the person's numbers) |
| Prompt | This guide |
| Template | `assets/growth-offer-output.md` |
| Input | The request and its context: the ready accounts (A1), the offer elements as the person describes them, the draft proposal or deck text, the product's exact regulatory identifier and intended purpose as the regulatory owner gives it, markets, who uses, buys and pays, the compliance, legal and regulatory owners as the person names them |
| Governance | `references/governance.md`; offer elements stop for the compliance or legal owner; claims stop for the regulatory or legal owner |
| Catalogue job | `health-system-value-brief` for the value case behind a growth offer to a health system (numbers the person types or adopts); `claim-labels` for the authorization record. The direct calls in the steps remain the method. `examples/live/job_health_system_value_brief_somnio.json` |

## The rule that shapes this task: lay out, never clear

The skill names the rule each offer element meets, the elements that rule requires, and the facts still missing. It never writes "protected", "compliant", "safe harbor met" or "low risk", because protection needs every condition met (CP-US-07) and an advisory opinion protects only its requestor (CP-US-43). The price is the pricing owner's; the claim is the regulatory owner's.

## Read the request

- **Which accounts.** From A1, or as the person names them. If an account is "not ready" on the person's rule, say so and ask whether to proceed.
- **The offer, element by element.** Ask the person to list everything the offer contains, not only the price: discounts or rebates, anything free or reduced, trials, services, devices or apps for patients, fees or credits to anyone, terms tied to results.
- **What the account has seen.** The result the offer builds on (SR6, if adopted). If not recorded, `[GAP]`.
- **Who uses, buys and pays.** In the person's words. Whether a Federal health care program pays is the compliance owner's call.
- **Materials.** The proposal, deck or email text, if any.
- **Value case.** Does the person want a value case for the growth offer (budget impact or price anchor for the account)? Only on numbers they type or adopt.
- **Owners.** Compliance or legal, regulatory, pricing: as the person names them, or "owner not named".
- **Mode.** Short for "can we include X for free?"; full for an offer pack per account.

## Workflow

### Step 1. Name the offer and the money flow

Write back each account's offer in the person's words: the module, site or population (SR5), and the result seen it builds on (SR6, or `[GAP]`). If the person adopted SR8, check that the account uses the current module before offering the next. Record who uses, buys and pays. Optional: call `commercial-dh.map_money_flow` with `reference` (the product), `user`, `buyer`, `payer` as the person stated them; report only the echo and `conflated`. Its payer listings do not decide whether a Federal program pays (`references/tools.md`).

### Step 2. Split the offer into elements

One row per element. Classify each into the element types in `references/offer-rules.md`: price reduction or rebate; free or reduced item to win a purchase; evaluation or trial; donated technology; anything reaching patients; device given where the customer bills DMHT codes; payment to a champion, clinician, reseller or referral source; price or payment tied to outcomes; Germany; England.

### Step 3. Lay out the rule for each element

For each element: the rows that apply, the elements the rule requires as the row states them, the facts the person gave against each, the facts missing. Start with Step 0 of `offer-rules.md`: write "Federal program payment: as the compliance owner determines `[GAP]`" unless the owner has stated it. When stating CP-US-01 in an answer, keep 'knowingly and willfully'; never shorten to 'is a felony'. Examples of the form:

- "Free analytics module with the renewal: outside the discount definition unless both items are reimbursed by the same Federal program by the same methodology and the reduced charge is fully disclosed (FA10). Missing: whether either is Federal-program reimbursed; disclosure on the invoice (FA5)."
- "Patient app subscriptions given free to patients: beneficiary inducement rule (CP-US-34); patient engagement tool conditions and the $623 cap for 2026 (CP-US-25 to CP-US-28). Missing: recommendation by the patient's licensed professional; whether availability depends on insurance."

Mark every [INDUSTRY] row as a code, not law. End each element with "Stops for: [owner as named, or owner not named]".

### Step 4. Fetch the authorization record

If the materials make function or outcome claims, call `commercial-dh.audit_claims` with `reference` set to the product's exact regulatory identifier (K, DEN or P number, or the exact registered name) and `claims` set to the claims (up to 20). Use the response only for the authorization record: route, class, product code, regulation number, decision date and source URL, as the record states them. Do not report the claim labels: with no intended purpose on file every claim came back `exceeds_record` in testing, and a name query missed an EU record held in the same response (`references/tools.md`). If no authorization returns, write "no authorization in the library for this reference; absence is not evidence of none".

### Step 5. Flag the claims

For each claim in the materials, one row from `references/account-materials-claims.md`: the claim as written; the audience; the rows it touches; what the row requires (indication and population, evidence and limitations, denominator, status words); what is missing; a safer wording labeled "draft for the owner". Treat customer results as the account's own measurement (CS32 [PAPER], DOI 10.1007/s10488-010-0319-7; PC-UK-03). Cite PC-US-23 and PC-US-24 for PMA and De Novo products; cite PC-US-22 only for 510(k) or exempt products. Quote FA12 as 'services under a personal or management services contract', not 'bundled services'. Where an advisory opinion is mentioned or relevant, add CP-US-43. If a literature result is quoted, check it only with `verify.qualify_source` then `verify.check_claim` on a passage read in the same direction (register N3); otherwise mark "source not checked".

### Step 5b. Value case for the growth offer (only if asked)

Run the catalogue job `health-system-value-brief` (or its calls directly) on the person's numbers for this account: `commercial-dh.get_pricing_corridor` with `reference` only if they want the public registered price as context (keep only the row whose `source_url` is the product's own record; the other rows are other products, register N4); `analytics.budget-impact-model` with eligible population, current mix, new cost per patient and uptake; `analytics.vba-price-anchor` with comparator cost, incremental QALYs and thresholds. A corridor or study number enters a calculator only if the person adopts it, and it keeps its tool and source. In the live run (`examples/live/job_health_system_value_brief_somnio.json`) the budget impact call returned HTTP 422: print "[GAP] budget impact: calculator rejected the payload" and, if the person wants it, show the arithmetic line by line labeled a hypothesis. The job's scenario and sensitivity tools (`analytics.scenario-modeler`, `analytics.risk-tornado`) are not exposed: "[GAP] scenario and sensitivity: tool not exposed". The value case is a hypothesis on the person's numbers, never the account's result and never clinical evidence; any figure from it placed in the proposal is a claim and goes through Step 5. A price or discount it suggests is not proposed here: prices are the pricing owner's.

### Step 6. Say what it means for the person

Two or three lines. Examples: "Two of four offer elements raise a fraud-and-abuse question your compliance owner must answer before the proposal goes out: the free module (FA10) and the patient subscriptions (CP-US-34)." "The deck's '30 percent fewer readmissions' is one customer's figure with no stated denominator; as written it reads as a product claim."

## Build the output

Follow `assets/growth-offer-output.md`. Answer first: per account, the offer elements that stop for an owner and the claims that need the regulatory owner. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words and write 'Words: N' as the first line of the Calls made list. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- No element is called protected, compliant or low risk; every element ends with its stop.
- Every [INDUSTRY] row is labeled a code, not law; every [WF] row is labeled.
- No price is proposed; prices and terms are the person's. Value-case figures are labeled hypotheses with the person's inputs shown.
- Claim labels from `audit_claims` are not presented as findings.
- Customer results are never presented as clinical evidence.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Offer structure and its rules only. List and offer price positioning and the value message are the Commercial pack (`pricing-and-value-proposition`); claim audits of marketing at large are `pricing-and-value-message-monitoring`.
- Payer prices, codes, coverage and outcome-based contracts with payers are Market Access (`coding-pricing-and-payer-contracting`, `outcomes-based-contracting`).
- No legal opinion. The compliance or legal owner decides.
