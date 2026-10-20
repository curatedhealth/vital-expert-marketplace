# Realized price: definitions the person sets, and the few sourced facts that bear on them

Interpretive reference for tasks A1 and B1. Rows cited from `payer-price-facts.md`, `channels-partners-research.md` and `promotion-and-claims-research.md`. Read on 19 October 2026; not owner-reviewed.

## What is the person's (not sourced, and not the model's)

No research row defines realized price, a deal set, a discount policy or a pricing KPI for digital health. These are the person's rules. The old method is kept as a starting checklist the person may adopt, change or replace:

1. Name the period and the deal types that count (for example new, renewal, pilot).
2. Realized price is the contracted unit price, not the list price. Never average list and realized prices together.
3. Exclude deals whose unit is not the value unit; list them separately rather than converting them silently.
4. List every deal in the period with unit price, currency and contract id. Do not drop a deal because it was discounted.
5. Mark each deal inside, below or above the corridor the person set.
6. For a deal outside the corridor, ask whether the corridor or the deal is wrong; do not treat every discount as a failure of the corridor.

Write the person's version back for confirmation before scoring anything.

## Arithmetic the skill does on the person's data

- Realized unit price per deal = contract value for the period divided by units in the period, only where both are given; otherwise the unit price the person states.
- Position against the corridor: below (under the floor), inside (floor to ceiling inclusive), above (over the ceiling). Both ends are the person's numbers.
- Discount from list per deal = 1 minus realized over list, only where a list price is stated for that deal's unit.
- Summaries: count and share of deals in each position; median and range of realized price per unit and currency. No weighting unless the person names one.

## Sourced facts that bear on realized prices

| Fact | Row | How it is used |
|---|---|---|
| Properly disclosed discounts are one of the statutory exceptions to the US Anti-Kickback Statute (others: bona fide employee pay and disclosed GPO fees); other safe harbors protect only when every condition is met | CP-US-05, CP-US-07 | A discount tied to referrals or volume of federally payable items stops for the compliance or legal owner; the model never says it is protected |
| One purpose to induce referrals is enough under the AKS | CP-US-08 | Same stop |
| In Germany the manufacturer's actual price applies from listing, in any case for at least one year, then the GKV-Spitzenverband amount, binding on all funds | DE1, DE7, DE9 | A German statutory "realized price" after year one is a payer-set amount; route to dh-access-and-value |
| German cash-pay and other-European prices are handed over for the DiGA negotiation | CP-DE-10 | Discounts given to self-payers or abroad can become a negotiation input; flag for the pricing owner |
| Where a German patient chooses extra functions or a price above the amount, the patient pays the difference | CP-DE-03 | Do not count the patient top-up as the fund's price |
| Negotiated DiGA prices for 40 DiGA averaged 227 EUR per quarter, 59 percent below the 552 EUR manufacturer prices they replaced; average cut 57 percent for permanent-from-start and 51 percent for trial-then-permanent | DE-9, DE-10 | Context for a German price review; never a target |
| FDA does not regulate the terms of contracts between firms and payors | PC-US-42 | Contract terms are not a promotion question; the information shared with the payor is (HCEI rows) |

## Payer prices are not this skill's subject

A realized price set by a payer (a German negotiated amount, a CMS fee, a French tariff) is answered by dh-access-and-value (coding-pricing-and-contract-monitoring). This skill reports it as context only when the person supplies it, labeled payer-set.
