Input:    the inputs of tasks 01 and 02 in one JSON file
Atom:     none (a scripted step)
Tool:     python3 scripts/rnpv.py input.json --pretty (fixture: evals/fixtures/good-rnpv-input.json)
Template: none
Output:   reach probabilities, cumulative probability, rNPV and unrisked NPV by scenario and rate, expected development cost, [CHECK] message
Check:    exit 0; probability applied once; revenue after the last stage; ranges ordered. Rules: FV-RNPV-STRUCTURE, FV-RISK-ONCE, FV-SCENARIO-PAIRING
Human:    the deal lead confirms the inputs before the figures are used
