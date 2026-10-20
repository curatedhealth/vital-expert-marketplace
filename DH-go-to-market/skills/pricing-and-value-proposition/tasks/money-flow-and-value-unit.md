# A1 Money flow and value unit

Framework task: DH-02.01.3.1, Part A, task A1. Replaces the old "Value unit" and "Map the money flow" sections. Catalogue job on the library: `money-flow` (see the formula table).

## What this task delivers

A one-page map of who uses the product, who buys or prescribes it, who pays and through which route, what unit the price attaches to and what that unit includes and excludes, with the product's listing status per scheme and every fraud-and-abuse or channel rule that the flow touches.

Why it matters: most digital health pricing mistakes start with a merged role. A price set for a payer who is not the buyer, or a unit that no code or contract can carry, fails however good the number is.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-02.01.3.1 Part A, Money flow and value unit |
| Workflow | The steps below |
| Knowledge | `references/money-flow-and-value-unit.md`; `references/channels-partners-research.md` (CP rows); `references/payer-price-facts.md` |
| Tools | `commercial-dh.map_money_flow`; `market-access-dh.find_scheme_precedents` only if the person asks how comparable products are sold; `verify.build_record` when a named person clears the output |
| Prompt | This guide |
| Template | `map_money_flow` response for the listing data; `assets/money-flow-output.md` for the answer |
| Input | The request and its context: the product, its markets, the person's description of users, buyers and payers, and any unit already in use |
| Governance | `references/governance.md` |
| Catalogue job | `money-flow` (map_money_flow). The direct calls in the steps remain the method; the job is the one-call option for the buyer. `examples/live/list_jobs_commercial.json` |

## Read the request

- **Product and markets.** Name the product and the markets the person cares about. If the product is not yet listed or cleared anywhere, the flow is a plan; say so.
- **Roles given?** Take user, buyer and payer in the person's words. If one is missing, ask once; otherwise mark it `[GAP]` and proceed.
- **Short or full?** A direct question gets the short output; "for the board", "pricing paper" or a document to share gets the full output.
- **Is it really a payer question?** "What will the fund pay", "which code", "what is the reimbursement" belong to dh-access-and-value. Answer the commercial part and point there.

## Workflow

### Step 1. Write the three roles back

Restate user, buyer and payer per market in the person's words. Keep them separate even when one organization holds two roles; name the person or function inside it if the person did.

### Step 2. Call the library for listing status

Call `commercial-dh.map_money_flow` with `reference` (product name or identifier), `user`, `buyer`, `payer` and a `note` stating the market. Keep `conflated` and the `payer_listings` block. If `conflated` is true, say which two roles match and ask whether that is intended. Read each scheme cell: listed with status, date and source URL, or `[GAP]`. A `[GAP]` is never "not reimbursed" (`references/gap-rules.md`). Ignore the sankey exhibit: it chains the roles in argument order and does not show who pays whom (`references/tools.md`).

### Step 3. Lay out the routes the money can take

Per market, from `references/money-flow-and-value-unit.md`: for a German DiGA, prescription or fund approval (CP-DE-01), manufacturer price for at least the first year then the GKV-Spitzenverband amount (DE1, DE9), patient pays the difference above the amount (CP-DE-03); for US DMHT, the billing practitioner must bear the device cost (CP-US-59) and G0552 is contractor priced (US19); for a cash-pay or employer route, say that no rule in the references sets the price. Name only rows that apply to the person's flow.

### Step 4. Define the value unit with the person

Use the checklist: the unit (patient-month, prescription period, site, module, outcome), what the buyer receives for it, what is excluded. If the person has not chosen, lay out the units the routes in step 3 already use (prescription period in the DiGA directory, DE20; per course of treatment and monthly time for DMHT, CP-US-57) and ask. A unit you cannot describe is not priced.

### Step 5. Flag the stops in the flow

Check the flow for any of these: a free item or service to a patient or provider; a payment to a prescriber, partner or reseller tied to referrals or volume; an outcomes-based payment to an agent; a DiGA arrangement with a physician on prescriptions, or with a drug or aid maker. For each, cite the rows (CP-US-01, CP-US-07, CP-US-08, CP-US-27, CP-US-34, CP-US-38, CP-DE-06, CP-DE-07; PC-US-93 is [INDUSTRY]) and write "stops for the compliance or legal owner". Never say an arrangement is protected.

## Build the output

Follow `assets/money-flow-output.md`, short or full. Answer first: who pays whom for what unit, in one or two sentences per market.

## Before you hand it over

- Every role and the unit are the person's words or marked `[GAP]`.
- Every listing status carries its source URL and retrieval date, with the caveat that the facts rest on the library's copy of the register.
- Every stop names the owner the person gave, or "owner not named".
- Count the words in short mode (450 maximum, without the calls list and source column).
- If the output leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No price for the product; that is A2 evidence and the person's decision.
- No payer price, code or reimbursement answer; point to dh-access-and-value (coding-pricing-and-payer-contracting).
- No judgment that a discount, free trial, loaner device or partner fee is lawful.
- Drugs, biologics and wellness apps are out of scope: say so in two or three lines and stop without calling the library.
