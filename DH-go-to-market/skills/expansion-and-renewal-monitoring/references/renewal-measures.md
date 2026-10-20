# Renewal and expansion measures: what is sourced, what is yours

Interpretive reference for A1, A2 and B1.

## What the sources say, and do not say

The research pass of 19 October 2026 looked for primary or peer-reviewed definitions of customer health scores, renewal rate, gross and net revenue retention, churn, expansion, time to value and NPS as a renewal predictor for digital health. It found none: existing definitions come from vendors, consultancies and blogs, which the research rules exclude. Its instruction to skill builders: ask for the owner's definitions, formulas and thresholds and label them owner-stated (`customer-success-research.md`, "Not sourced"). Renewal and expansion playbooks (business review cadence, success plans, upsell triggers) were not sourced either.

So this skill:

- never states what "NRR" or "churn" means as if there were a standard;
- never gives a typical, good or benchmark rate;
- writes the person's definition down (A1), computes it (A2), and prints the formula beside each figure.

## Sourced facts that bear on how a measure is built

These are not definitions of renewal measures. They are published rules about counting that a person may choose to borrow; say so when they do.

| Fact | Rows | Bearing on a renewal measure |
|---|---|---|
| Reach is computed on a valid denominator of eligible people, not of volunteers who expressed interest; setting-level adoption is the percent of settings approached that participate. | CS27, CS28 | An argument for counting every account due in the period, not only those that engaged. Same logic as the register rule SR18. |
| Penetration has two published calculations, both with a stated denominator. | CS39 | Any usage figure an account quotes as "value seen" needs its denominator named. |
| Implementation outcomes are preconditions for clinical or service outcomes. | CS32 [PAPER] (Proctor 2011, DOI 10.1007/s10488-010-0319-7) | Losses on an open implementation and losses on unseen value should be counted apart (SR17). |
| At setting level, maintenance is a program still running 6 or more months after support ends; sustainability is being part of stable operations. | CS30, CS40 | Definitions a person may borrow for a "sustained account" flag; not renewal definitions. |
| RE-AIM and Proctor define adoption differently; a project should pick one definition per metric and name it. | Research "Changes and conflicts" | The same discipline applies to renewal measures: one named definition per figure. |

## Choices the person must make (A1)

| Choice | Options the person picks from (none is a standard) | Register starter rule |
|---|---|---|
| Cohort | Accounts with a renewal date in the period; accounts active at period start; contracts rather than accounts | SR12 |
| Unit | Account, contract, site, module | |
| What counts as renewed | Signed continuation; written successor contract; purchase order; any of these | SR13, SR15 (verbal intent does not count) |
| What counts as lost | Written notice; renewal date passed without signature; the person's own rule | |
| Open accounts | In the denominator (counted as not retained until signed) or outside it (stated) | SR18 (keep them in) |
| Exclusions | Pilots never on annual contracts; free trials; accounts transferred or merged | SR14 |
| Value basis | Annual contract value, annual recurring revenue, invoiced amount, seats; currency; before and after values per account | |
| Expansion | Value increase on renewed accounts only; also new modules mid-term; also new sites | |
| Contraction | Value decrease on renewed accounts | |
| Offer outcome | What counts as signed, refused, open; a meeting is not an expansion | SR19 to SR22 |
| Owner of the definitions | The person or team that answers for them | |

## Formulas the script applies (`scripts/renewal_metrics.py`)

These are computations on the person's choices, printed beside each figure. They are not sourced definitions.

| Figure | Formula |
|---|---|
| Account renewal rate | renewed / (renewed + lost + open, if open is in the denominator) |
| Starting value | sum of the value-before field over the counted accounts |
| Value lost | sum of value-before over lost accounts |
| Contraction | sum over renewed accounts of max(0, value-before minus value-after) |
| Expansion | sum over renewed accounts of max(0, value-after minus value-before) |
| Value retained without expansion | (start - lost - contraction - open value, if open is in the denominator) / start |
| Value retained with expansion | (start - lost - contraction - open value, if counted, + expansion) / start |
| Offer acceptance | signed / (signed + refused + open, if open is in the denominator) |

If a team calls the last two "gross" and "net" revenue retention, use their names in the output and keep the formula beside them. If their formula differs (for example expansion from accounts outside the cohort, or mid-term changes), the script does not compute it: do it by hand with the formula written out, or ask whether to change the definition.

Status values the person's lists do not cover are counted nowhere and listed for checking. A missing value stops the value figures for the whole cohort and names the accounts (`[GAP]`), rather than computing on a partial base.

## What each figure can and cannot show

| Figure | Can show | Cannot show |
|---|---|---|
| Account renewal rate | The share of the cohort that signed, on the person's definition | Why accounts left; whether the product works |
| Value retained with and without expansion | How much contract value carried over, and how much growth offset losses | Margin; customer health; clinical value |
| Losses by recorded reason | How losses split across the reasons the person records | The true cause (reasons are as recorded) |
| Offer acceptance | The share of offers that became signatures | Whether the offer was right for the account |

## Never

- Never compare a figure with an industry number; none is sourced.
- Never compute a figure on a definition the person has not stated.
- Never present renewal or uptake as evidence that the product is clinically effective.
