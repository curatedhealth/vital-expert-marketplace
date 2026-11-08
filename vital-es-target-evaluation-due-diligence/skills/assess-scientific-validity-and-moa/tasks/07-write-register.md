Input:    all rows and the screen
Atom:     compose-draft
Tool:     python3 scripts/validate_register.py register.json (fixture: evals/fixtures/good-register.json); templates/mechanism-register.md
Template: templates/mechanism-register.md
Output:   the written register with the answer first, options to close each gap (effort, risk), the decisions needed and their owner, the hand-off to review-clinical-data-quality
Check:    validator exit 0; status UNSIGNED until a named reviewer signs; scientific_go_no_go shows HUMAN ONLY. Rule: no sentence says the mechanism is validated, proven or de-risked
Human:    the named scientist signs; the scientific go/no-go is the scientist's alone
