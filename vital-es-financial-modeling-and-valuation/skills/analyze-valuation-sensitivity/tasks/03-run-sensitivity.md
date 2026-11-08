Input:    the input of tasks 01 and 02 in one JSON file
Atom:     rank-by-consequence (orders the drivers by absolute swing); a scripted step
Tool:     python3 scripts/sensitivity.py input.json --pretty (fixture: evals/fixtures/good-sensitivity-input.json)
Template: none
Output:   base case, swings, tornado ranks, switching values
Check:    exit 0; probability applied once inside the model. Rules: FV-OAT, FV-TORNADO-RANK, FV-SWITCHING
Human:    the deal lead confirms the inputs
