Input:    the draft in one JSON file
Atom:     none (a scripted step)
Tool:     python3 scripts/scenario_summary.py input.json --pretty (fixture: evals/fixtures/good-summary-input.json)
Template: none
Output:   the assembled summary in the fixed order
Check:    exit 0; refusals E_RECOMMEND, E_FAIRNESS, E_POINT, E_POINTER; range with low below high
Human:    the deal lead reviews
