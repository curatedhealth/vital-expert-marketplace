Input:    all rows and the screen
Atom:     compose-draft
Tool:     python3 scripts/validate_register.py register.json (fixture: evals/fixtures/good-register.json); templates/market-register.md
Template: templates/market-register.md
Output:   the written register with the answer first, options to close each gap (effort, risk), the decisions needed and their owner, the access-inputs GAP, and the hand-off to determine-commercial-viability
Check:    validator exit 0; status UNSIGNED until a named reviewer signs; no sales, price or access figure. Rule: nothing in the register reads as a sales forecast
Human:    the named reviewer with market and clinical knowledge reviews the output
