Input:    all rows, the options and the screen
Atom:     compose-draft
Tool:     python3 scripts/validate_register.py register.json (fixture: evals/fixtures/good-register.json); templates/viability-register.md
Template: templates/viability-register.md
Output:   the written register with the answer first (the range and the state counts, not a verdict), options to close each gap (effort, risk), the decisions needed and their owner, and what the Market Access pack and the valuation capability own
Check:    validator exit 0; status UNSIGNED until a named reviewer signs; commercial_decision HUMAN ONLY; recommended_option null. Rule: no sentence recommends an option or says the asset is or is not viable
Human:    the named reviewer with commercial experience decides; the skill states no opinion
