# Risk-share models: the official types, their known problems, and three worked anchors

Interpretive reference for task A2. Rows cited as in `outcome-measures.md`: `OC` = `outcomes-contracting-sources.md` by table and topic; `DE-` = `access-monitoring-sources.md`; `US` = the coding and pricing research pass (cited, not copied). Read on 19 October 2026. Not owner-reviewed.

## The taxonomy

The OECD splits managed entry agreements into two kinds (OC Method guidance "OECD MEA taxonomy"; OECD Health Working Paper No. 115, 16 December 2019):

| Kind | What it means | Designs named |
|---|---|---|
| Financial | Not linked to performance (for example discounts, volume terms) | (examples beyond this are not in the sourced row `[GAP]`) |
| Performance-based | Coverage, payment or rebates conditional on performance | Patient-level payment-by-result (PbR); population-level coverage with evidence development (CED); conditional treatment continuation (CTC), used by some countries |

ISPOR's task force calls these performance-based risk-sharing arrangements: performance tracked in a defined population over a set period, with payment based on the health and cost outcomes achieved (OC Method guidance "ISPOR PBRSA definition"). The full ISPOR taxonomy wording is not sourced (OC "Not sourced").

**Scope caution.** The OECD paper covers medicines. Apply its findings to digital products as lessons, and say so.

## Known problems (OECD findings)

From OC Method guidance "OECD: known problems":

1. Administrative burden and data collection cost for providers, firms and payers.
2. Difficulty recouping payments or delisting once paid or listed.
3. Difficulty getting outcome data that is informative, and finding validated, easily measured surrogate endpoints.
4. Payment-by-result data often not aggregated into evidence.
5. CED has a poor track record at reducing uncertainty.

ISPOR adds that negotiation, monitoring and evaluation costs can be substantial, and that an arrangement is worth doing only if the cost of extra data is justified by better decisions (OC Method guidance "ISPOR: cost of evidence" and "ISPOR: when worth doing").

## Anchor 1: Germany, the mandatory outcome-linked component

| Fact | Row |
|---|---|
| From 1 January 2026, every negotiated DiGA price must set outcome-dependent components at no less than 20 percent of the amount | OC Germany "DiGA outcome-linked price share"; DE-19 |
| Existing agreements had to be replaced by a compliant amount by 1 January 2026 | OC Germany "Existing DiGA agreements" |
| The latest listed framework agreement (valid from 28 February 2024) still says outcome components "can" be included, with successes defined and proven by the parties; it sets no measure list, attainment method or payment formula | OC Germany "Framework agreement: current version" and "how outcome components are defined" |
| How AbEM feeds the outcome component is still to be set by the framework partners | DE-19 (BfArM guide v3.6) |
| Payer and manufacturer associations both call the mandatory component disproportionate and flag that pricing applies from 2026 while AbEM data starts 15 April 2027 | OC Germany "Payer and industry position" |
| No arbitration ruling or framework amendment implementing the 20 percent rule was found | OC "Not sourced" |
| From 1 January 2027 a separate volume discount applies (at least 2 percent above 3,000 units a year, at least 30 percent above 100,000) | OC Germany "Volume discount from 2027"; DE-19 |
| Outcome clauses may be shared with sickness funds because they matter for billing | OC Germany "Framework agreement: disclosure of outcome clauses" |

What this means for design: the 20 percent floor is law; the method is open. Any German design is a proposal to the GKV-Spitzenverband, not an application of a set rule. Selective contracts with individual funds under § 140a SGB V are a separate legal route; the statute does not mention outcome-based pay (OC Germany "Selective contracts").

## Anchor 2: United States, the ACCESS withhold (a worked example of payment design)

| Mechanic | Rule | Row |
|---|---|---|
| Annual allowed amount per beneficiary (initial / follow-on) | eCKM $360 / $180; CKM $420 / $210; MSK $180 / none; BH $180 / $90; $15 rural add-on for eCKM and CKM initial period; effective 5 July 2026 to 31 December 2027 | OC United States "ACCESS: annual payment amounts"; US31 |
| Withhold | Monthly payments capped at 50 percent of the Medicare portion; the other 50 percent is reconciled after the 12-month care period | OC "ACCESS: withhold"; US32 |
| Payment basis | Allowed amounts include the Medicare payment (80 percent) and beneficiary coinsurance (20 percent); both downward adjustments apply to the Medicare paid amount. BH initial: $180 allowed, $144 Medicare portion, $72 withheld. Payment is limited to months for which claims are submitted | OC "ACCESS: Medicare portion and payment basis" |
| Attainment threshold | Full payment if at least 50 percent of aligned beneficiaries meet all required targets | OC "ACCESS: attainment threshold and formula" (RFA v1.1, formula and cap); US33 (payment amounts PDF, 50 percent OAT) |
| Below threshold | Payment = (attainment rate / 50 percent) x full payment; reduction capped at 50 percent | same |
| Substitute spend | If fewer than 90 percent avoid listed substitute services from other providers, payment is cut proportionally, capped at 25 percent; only the larger of the two adjustments applies per semi-annual reconciliation | OC "ACCESS: substitute spend adjustment"; US33 |
| Substitute services that hit a BH participant | DMHT (G0552, G0553) and RTM setup (98975) billed by another provider | US34 |
| Billing | Monthly G-codes (for example G0674 BH initial $15.00); claims zero-paid by MACs, CMS pays, less 2 percent sequestration; no other FFS billing for aligned beneficiaries | US35, US36 |
| Payee | Part B enrolled care organizations; a device maker reaches ACCESS only as a participant or a vendor to one | OC "ACCESS: who is paid" |

Worked arithmetic from these rules (BH initial): the factor applies to the Medicare portion, $144 (80 percent of the $180 allowed amount), of which $72 is withheld. If 40 percent of aligned beneficiaries meet all targets, the outcome adjustment pays 40 / 50 = 0.8 of $144, $115.20, a $28.80 reduction taken from the $72 withhold. At 20 percent attainment the formula gives 0.4, but the reduction is capped at 50 percent, so 0.5 of $144, $72, is paid: the whole withhold is lost. `scripts/payment_scenarios.py` reproduces this. Coinsurance and sequestration are not modeled here, and patients with fewer billed months accrue less.

Design lessons the ACCESS rules make visible: the withhold sets how much is at risk; the threshold sets where full payment starts; the proportional formula and cap set the slope and the floor; the all-or-nothing patient rule and keeping dropouts in the denominator make data completeness part of attainment.

## Anchor 3: other precedents (context only)

- France, ETAPES (2018, historical): supplier flat fee per patient per semester plus a performance bonus paid in year N+1 (OC France, both rows).
- England: outcome-based agreements in the NHS commercial framework cover branded medicines only; medtech and digital reach evidence-linked access through NICE conditional recommendations, which is not outcome-linked payment (OC England rows; [WF] rows must be re-read on the live page).
- United States Medicaid: the 2020 VBP rule defines value-based purchasing for covered outpatient drugs only (OC United States "Medicaid VBP rule: scope").

## Budget impact

`analytics.budget-impact-model` is the library's calculator for net budget impact on the person's inputs. Its output is a hypothesis about the person's inputs, never a forecast, and never a price. In live calls on 19 October 2026 it returned an error (422) for every argument shape tried (`tools.md`). Until it works, compute the same arithmetic by hand from the person's inputs and label it "hypothesis, person's inputs".

## Rows cited from the coding and pricing research pass

These rows come from the Market Access coding and pricing research pass (`research_ma2/CODING_PRICING.md`, 19 October 2026). They are cited here, not copied; the quotes below are as recorded in that file.

| Row | Source URL | Verbatim quote | Read on |
|---|---|---|---|
| US31 | https://www.cms.gov/priorities/innovation/files/access-payments-amts-perf-targets.pdf | "Effective Period: July 5, 2026 – December 31, 2027" | 19 October 2026 |
| US32 | same | "The sum of monthly payments may not exceed 50 percent of the Medicare portion of the annual OAP allowed amount." | 19 October 2026 |
| US33 | same | "During the Effective Period, the OAT will be 50 percent for all ACCESS Participants." / "During the Effective Period, the SST will be 90 percent for all ACCESS Participants." | 19 October 2026 |
| US34 | same | "DHMT: Supply of digital device and monthly treatment G0552, G0553" / "Remote Therapeutic Monitoring (RTM): Patient education and device set-up 98975" | 19 October 2026 |
| US35 | https://www.cms.gov/priorities/innovation/files/access-oap-billing-guidelines.pdf | "Claims are processed as zero-paid claims by Medicare Administrative Contractors (MACs). Payments are issued by CMS" / "G0675 BH $7.50" | 19 October 2026 |
| US36 | https://www.cms.gov/priorities/innovation/innovation-models/access | "Only ACCESS G-codes may be billed for aligned beneficiaries during active care periods." | 19 October 2026 |
| DE4 | https://www.gesetze-im-internet.de/sgb_5/__134.html | "Die Verhandlungen und deren Vorbereitung ... sind vertraulich." (the termination point in that row's fact column is not in its quote) | 19 October 2026 |
