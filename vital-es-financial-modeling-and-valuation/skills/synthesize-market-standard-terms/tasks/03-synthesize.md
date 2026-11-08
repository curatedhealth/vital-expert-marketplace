Input:    both blocks in one JSON file
Atom:     none (a scripted step)
Tool:     python3 scripts/market_standard.py input.json --pretty (fixture: evals/fixtures/good-synthesis-input.json)
Template: none
Output:   synthesis per term, cross-check, caveats, decisions
Check:    exit 0; merged is false; no verdict wording. Rules: FV-NO-MERGE, FV-THIN-DATA
Human:    the deal lead confirms the inputs
