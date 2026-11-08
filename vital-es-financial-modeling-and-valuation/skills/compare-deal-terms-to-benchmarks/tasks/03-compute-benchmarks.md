Input:    deals and subject in one JSON file
Atom:     rank-by-consequence (orders positions by distance from the range); a scripted step
Tool:     python3 scripts/benchmarks.py input.json --pretty (fixture: evals/fixtures/good-benchmarks-input.json)
Template: none
Output:   ranges, leave-one-out and subject positions
Check:    exit 0; n beside every range; no verdict wording. Rules: FV-MIN-N, FV-POSITION-NOT-VERDICT
Human:    the deal lead confirms the inputs
