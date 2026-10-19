# Money flow and value unit: what is sourced, what is the person's

Interpretive reference for task A1. Rows cited from `channels-partners-research.md` (CP-), `promotion-and-claims-research.md` (PC-) and `payer-price-facts.md` (DE, US, FR). Read on 19 October 2026; not owner-reviewed.

## Three roles, never merged

| Role | Question | Whose fact |
|---|---|---|
| User | Who uses the product day to day? | The person's description |
| Buyer | Who decides to acquire it, prescribes it or signs the order? | The person's description |
| Payer | Whose budget the money comes from, and through which route? | The person's description, checked against listing records |

`commercial-dh.map_money_flow` echoes the three roles the person gives and attaches the product's market matrix. It adds no fact beyond the listing block. When two roles are the same string it sets `conflated: true`; say so and ask whether that is intended (a cash-pay consumer app can be user, buyer and payer at once).

## Sourced facts that shape the money flow

| Market | Fact | Row |
|---|---|---|
| Germany | Two routes to a listed DiGA: prescription by the treating physician or psychotherapist, or approval by the sickness fund | CP-DE-01 |
| Germany | GKV-Spitzenverband agrees the amount with the manufacturer, binding on all funds; it applies after the first year from listing | DE1 |
| Germany | Until then the manufacturer's actual price applies, in any case for at least one year after listing | DE7, DE9 |
| Germany | Where the patient chooses extra functions or a price above the amount, the patient pays the difference | CP-DE-03 |
| Germany | Delivery electronically or on data carriers; public app stores only where that is not possible | CP-DE-05 |
| Germany | No prescription steering; no deals with physicians on allocating or transmitting prescriptions | CP-DE-06 |
| Germany | A DiGA must be free of advertising and may not process its data for advertising | PC-DE-15, PC-DE-16 |
| Germany | No opaque offers such as auto-renewing subscriptions or time-limited special offers (DiGAV Annex 2 checklist) | PC-DE-17 |
| Germany | Cash-pay and other-European prices are handed over for the negotiation | CP-DE-10 |
| United States | G0552 (DMHT) requires the billing practitioner to incur the device cost; a manufacturer-pays or direct-to-patient model cannot use it | CP-US-59 |
| United States | G0552 is contractor priced; each MAC sets the price | US19 |
| United States | FDA does not regulate the terms of risk-sharing or value-based contracts with payors; only the information communicated is in scope | PC-US-42 |
| United States | Paying anything of value to induce referrals or purchases of federally payable items is a felony; one purpose is enough | CP-US-01, CP-US-08 |
| United States | Safe harbor protection applies only when every condition is met | CP-US-07 |
| United States | Properly disclosed discounts are a statutory exception | CP-US-05 |
| United States | Anything of value to a Medicare beneficiary likely to influence the choice of provider or supplier is subject to civil money penalties; narrow exceptions exist | CP-US-34, CP-US-36, CP-US-38 |
| United States | Patient engagement tools from device makers: in-kind, capped at a retail value OIG states as $623 for calendar year 2026 | CP-US-27 |
| United States | Free services that remove an HCP overhead cost are named as an unlawful inducement example [INDUSTRY] | PC-US-93 |
| United States | When a covered entity is paid to make a marketing communication, the HIPAA treatment and operations exceptions are lost | PC-US-86 |
| France | The LPP price may exceed the reimbursed tariff; the rate is set after CEPS negotiation with no predefined range | FR5 |

## Value unit

The unit is the person's decision. The old method still holds as a checklist: state the unit (patient-month, prescription period, site, module, outcome); state what the buyer receives for it; state what is excluded. Do not price a unit you cannot describe.

What the sources fix about units:

- Germany: the directory publishes prescription periods and the amount per period (DE20). The library's DE_DIGA `price` field carries no unit and no prescription period; state both as `[GAP]` and point to the directory page.
- United States: DMHT G0552 is device supply and onboarding per course of treatment; G0553 and G0554 are monthly management time (CP-US-57, via the channels research file). A unit that does not match a code's unit cannot ride on that code.
- Thresholds and group maximums in Germany are set per calendar day (DE14). Converting a prescription-period price to a daily figure needs the period length, which the library does not hold.

## Stops in the money flow

Any free item to patients or providers, any payment tied to referrals or volume, and any outcomes-based payment to an agent or partner stops for the person's compliance or legal owner. Lay out the elements from the CP rows; never say an arrangement is protected.
