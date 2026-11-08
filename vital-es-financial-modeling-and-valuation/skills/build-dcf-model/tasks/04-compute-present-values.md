Input:    the inputs of tasks 01 to 03 in one JSON file
Atom:     none (a scripted step)
Tool:     python3 scripts/dcf.py input.json --pretty (fixture: evals/fixtures/good-dcf-input.json)
Template: none
Output:   present values by scenario and rate, terminal value and its share, cash flows by year, gaps and flags, the [CHECK] message for the terminal share
Check:    exit 0; the script rejects probability keys, adopted-valuation keys, a missing rate source and a rate not above the terminal change. Rule: unrisked, undiscounted-by-choice, human-only
Human:    the deal lead confirms the inputs before the figures are used
