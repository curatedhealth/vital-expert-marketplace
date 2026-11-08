Input:    the target product profile, the clinical evidence register (A) and the mechanism register (F) (intake items 2 and 7)
Atom:     compare-against-criteria (state set: supported / not counted)
Tool:     scripts/market_check.py (differentiation block)
Template: none
Output:   differentiation rows: claim, TPP attribute, comparison type (head_to_head, indirect, cross_trial, none), basis rows, state, reason
Check:    "supported" names an A or F row and a head-to-head or indirect comparison; every other claim shows why it is not counted. Rule: a sponsor statement or a cross-trial comparison never counts
Human:    the named reviewer with market and clinical knowledge reviews the output
