Input:    the driver table and named scenarios in one JSON file
Atom:     none (a scripted step)
Tool:     python3 scripts/scenarios.py input.json --pretty (fixture: evals/fixtures/good-scenario-input.json)
Template: none
Output:   standard table by pairing, named scenarios, coverage gaps, weights check
Check:    exit 0; the low scenario takes adverse ends; no expected value. Rules: FV-SCENARIO-PAIRING, FV-NO-INVENTED-PROBABILITY
Human:    the deal lead confirms the inputs
