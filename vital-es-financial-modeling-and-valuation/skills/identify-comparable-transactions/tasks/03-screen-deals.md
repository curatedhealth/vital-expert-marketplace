Input:    candidate list and criteria in one JSON file
Atom:     classify-text-labels (stage and modality labels); compare-against-criteria (gap cases); a scripted step
Tool:     python3 scripts/comparables.py input.json --pretty (fixture: evals/fixtures/good-comparables-input.json)
Template: none
Output:   screen table, included and excluded ids, flags
Check:    exit 0; counts add up; selection flag when completed only. Rules: FV-SELECTION-FLAG, FV-GAP-ALLOWANCE
Human:    the valuation reviewer confirms every exclusion
