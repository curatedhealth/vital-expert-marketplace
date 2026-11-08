# Commercial viability register: FICTIONAL FX-801 (bd, asset, markets US and EU; reference date 7 November 2026)

Reviewer: UNSIGNED    Commercial decision: HUMAN ONLY (owner: to be named)    Recommended option: none    Status: Draft
(Every name, figure and source here is FICTIONAL. Amounts are millions of USD, nominal peak annual sales.)

## Answer first
- Peak-sales range from 4 included analogs (US, USD, nominal): low 400, median 775, high 1,500. It is a range from analogs, not a forecast, not a point estimate and not a deal value; it is not adjusted for price, coverage or access. Leaving out each analog in turn moves the median between 650 and 900.
- Conditions: 6 met, 2 not met, 2 straddle a threshold, 1 gap. Not met: two class flags on the mechanism are not addressed (C-CL); 1 supported differentiation claim against the buyer's minimum of 2 (C-DF). Straddle: the buyer's hurdle of 700 lies inside the range 400 to 1,500 (C-HU); exclusivity wanted to 30 June 2037 is covered by the all-patents date of 31 December 2038 but not by the composition-only date of 1 March 2036 (C-EX). Gap: price, coverage and access (C-MA).
- What blocks: the Market Access pack is draft 0.1.0 and not Released, so the range may be overstated. The decision owner has not been named.

## Options (none is recommended)
### GO
Conditions that would have to hold: all eleven. Evidence for: C-A, C-F, C-B, C-D, C-G, C-AN. Evidence against: C-CL, C-DF, C-EX, C-HU. What would change the call: C-CL and C-DF resolved; the buyer decides which patents count (C-EX) and whether 700 is the right hurdle (C-HU); Market Access records (C-MA).
### CONDITIONAL GO
Conditions in place: the six that are met. Conditions precedent: C-EX, C-HU, C-MA. Conditions that would end it: C-CL, C-DF.
### NO-GO
Conditions present: C-CL and C-DF. What would change the call: the straddling and gap conditions resolved the other way.

## Market Access hand-off
Pack: vital-pharma-market-access; state: draft 0.1.0 (not Released); records: 0. State: GAP. Consequence: the analog range is not adjusted for price, coverage or access and may be overstated.

## Failure-mode screen
| Mode | State | Register ref or reason | Gap |
|---|---|---|---|
| MH-01 | triggered | analog_range | |
| MH-02 | triggered | access_interface | |
| MH-03 | triggered | conditions[6] | |
| MH-04 | triggered | conditions[7] | |

## Questions for the decision owner
1. Is a hurdle of 700 the right test given the range runs from 400 to 1,500?
2. Counsel: which patents count toward the effective exclusivity end?

## Open items
[CHECK]: no forecast-error band applied (results not read).  [GAP]: Released Market Access records; a reviewer's view on analog comparability.  Hand-offs: price, coverage and access to the Market Access pack; revenue forecasting and deal value to the valuation capability.

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json` (or of the skill named); the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| peak sales as a range from four dated analogs with n and leave-one-out | practitioner analog-selection criteria (not a standard) | VP-H-030 to VP-H-032 |
| forecast optimism is context; no band applied | forecast error in Austrian dossiers (one country) | VP-H-001 to VP-H-005 |
| the Cha band is disabled | article body paywalled | none ([CHECK] row H1a) |
| access conditions: GAP until the Market Access pack is Released; access failure evidence has scope | withdrawals after AMNOG (Germany); ATMP withdrawals (ATMPs only) | VP-H-020 to VP-H-022 |
| option dimensions: strategy fit and the landscape at launch | practitioner in-licensing framework (not a standard) | VP-H-040, VP-H-041 |
| exclusivity conditions read from skill C; EU ten years | Directive 2001/83/EC Art 10(1) | VP-H-050, VP-C-071, VP-C-072 |
| all three options shown, none recommended; the decision is human only | a practitioner closing recommendation of three options (not a standard) | VP-A-143 |
