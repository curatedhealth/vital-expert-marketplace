# A1 Realized price tracking

Framework task: DH-02.01.3.2, Part A, task A1. Replaces the old "Price outcome definition" and "Realized price score" sections.

## What this task delivers

A deal table for a period the person names: which deals count, the realized unit price of each, its position against the corridor (below, inside, above), the discount from list where a list price exists, and a short summary. Every rule comes from the person; the arithmetic is shown.

Why it matters: list prices say what the company hopes; realized prices say what the market accepts. Without a fixed deal set and one realized-price rule, every review compares different things.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-02.01.3.2 Part A, Realized price tracking |
| Workflow | The steps below |
| Knowledge | `references/realized-price-rules.md`; `references/payer-price-facts.md` (context); the corridor and value unit from the sibling skill if they exist |
| Tools | None from the library; arithmetic in the conversation or with code execution; `verify.build_record` when a named person clears the output |
| Prompt | This guide |
| Template | `assets/realized-price-output.md` |
| Input | The request and its context; the person's deal list (period, deal type, units, contract value or unit price, currency, list price if any, contract id); the corridor; the value unit |
| Governance | `references/governance.md`; rules and corridor are the person's |
| Catalogue job | none. Arithmetic on the person's deal list. |

## Read the request

- **Corridor known?** If not, the deals can be listed and summarized but not positioned. Say so and ask for both ends with currency and unit.
- **Unit known?** Deals in another unit are listed apart, not converted.
- **Payer-set prices?** A German negotiated amount, a CMS fee or a French tariff is payer-set; report it as context and point to dh-market-access (coding-pricing-and-contract-monitoring).
- **Short or full?** "How did Q3 go on price" is short; "pricing review pack" is full.

## Workflow

### Step 1. Write the deal rules back

From `references/realized-price-rules.md`, offer the checklist (period and deal types; realized price is the contracted unit price, not list; exclude other units; keep discounted deals; contract ids). Write the person's version back in their words and get a yes before scoring. If the person says "use the defaults", label them "proposed, adopted by the person".

### Step 2. Build the deal table

One row per deal: contract id, deal type, date, units, contract value, realized unit price (value divided by units, or the stated unit price), currency, list price if stated. A missing field is `[GAP]` for that deal; never estimated. Do not put deal data into any library call.

Check each deal's term against the unit. If a deal covers a period other than one unit period (for example a 6-month pilot priced per member-year), list it with its term, mark the realized price "[GAP]: term differs from unit", and ask the person whether to count it, prorate it or exclude it. Do not prorate on your own.

### Step 3. Position each deal

Mark below, inside or above against the person's corridor for that unit and currency. Compute discount from list where a list price exists for the same unit. Deals in other units or currencies go to a separate list.

### Step 4. Summarize

Count and share in each position; median and range of realized unit price per currency; number of deals excluded and why. No weighting unless the person names one. National figures (DE-9, DE-10 for German DiGA) are context with their period, never a target.

### Step 5. Flag what stops

Any deal whose discount or rebate is tied to referrals or volume of federally payable items, any free units, or any price given to German self-payers or other countries (a negotiation input under CP-DE-10): list it with the rows (CP-US-05, CP-US-07, CP-US-08, CP-DE-10) and the owner the person named. The model does not judge whether a discount is lawful.

## Build the output

Follow `assets/realized-price-output.md`. Answer first: how many deals landed inside, below and above, and the realized price range.

## Before you hand it over

- The rules and corridor are the person's and the output says so.
- Every computed number shows its inputs; no estimate fills a gap.
- Count the words in short mode.
- If the output leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No judgment of whether the corridor or the deal is wrong; that is B1, and the person decides.
- No verdict on salespeople or teams.
- No payer price monitoring; dh-market-access.
