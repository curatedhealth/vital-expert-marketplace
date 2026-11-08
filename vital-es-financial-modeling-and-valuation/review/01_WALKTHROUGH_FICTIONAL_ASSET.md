# Walkthrough on a fictional asset

Written 7 November 2026. Every name, figure and source is fictional and comes from the plugin's own test fixtures; nothing is a statement about a real product. The numbers are the output of the offline scripts run when this pack was built.

## 1. The request
A business-development team is looking at an in-licence of a fictional oral drug (asset VX-100). The due diligence registers exist. The lead asks for a valuation as a range, what moves it, and how it sits against comparable deals.

## 2. What each skill hands over (in chain order)

1. **V1, DCF**: unrisked present values by scenario and rate. For the fixture the range is 57.8 to 407.9 million USD; the rate is a human choice and no probability is applied.
2. **V2, rNPV**: the probability applied once, stage by stage. The fixture's rNPV range is -21.9 to 97.4 million across three scenarios and three rates.
3. **V3, assumption checks**: nine checks per assumption; the register never says "validated".
4. **V4, scenarios**: the standard low / mid / high by the stated pairing rule and the named scenarios the team defines; no probability is invented.
5. **V5, sensitivity**: base case 7.7 million; the drivers ranked by absolute swing: pos (36.1), revenue (15.1), cost (-12.1), discount_rate (9.5), launch_delay (7.7); switching values for revenue and probability.
6. **V6, memo**: starts from the range with its pointer, lists the decisions with owners and refuses recommendation and fairness language.
7. **V7 to V9, comparables**: a screen of supplied deals, ranges per term with n and leave-one-out, and the benchmark range beside the model range, never merged.
   Benchmarks on the fixture: upfront 100 to 250 (n = 4); the subject's upfront is "within" the range, an arithmetic position and not a verdict.

## 3. The valuation summary

Run on the all-clear fixture: 9 of 9 valuation registers supplied; proposed red workstreams: none. Model range -21.9 to 97.4 USD m [V6:rnpv_range]; it is a range, not a value.
Run on the conflict fixture: Model range -21.9 to 97.4 USD m [V6:rnpv_range]; it is a range, not a value. 0 open gaps; 1 conflicts shown side by side; the adopted valuation is HUMAN ONLY. The two ranges are shown side by side and not reconciled.

## 4. Where a person decides
- the discount rate or rates; the final probability of success; the scales and the threshold of the sensitivity; the scenario set and any weights;
- whether each comparable counts; which range informs a negotiation; the adopted valuation; any fairness or solvency view; deal terms.

## 5. What to look at as a reviewer
Open one register, follow one row to its passage, and check the item against the checklist in 03. The sources are registered verbatim in each skill's references/verbatim-passages.json. The WIPO valuation text is a guide, not a standard.
