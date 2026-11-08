Input:    the signed registers and ranges of skills A, B, C, D, F, G (intake items 2 and 3) and, when supplied, the signed register of forecast-revenue-and-price-ranges as a revenue_inputs block (intake item 9)
Atom:     compare-against-criteria (state set: met / not met / straddles / gap)
Tool:     python3 scripts/option_set.py input.json --pretty (fixture: evals/fixtures/good-option-input.json)
Template: none
Output:   the eleven conditions (twelve when revenue_inputs is supplied: C-RV) with state, detail, owner skill and consequence
Check:    an unsigned or missing register is "gap"; a threshold the buyer did not supply is "gap"; the exclusivity condition shows when the two effective dates give different answers (straddles). Rule: thresholds are the buyer's; the skill never sets one
Human:    the named reviewer with commercial experience reviews the output
