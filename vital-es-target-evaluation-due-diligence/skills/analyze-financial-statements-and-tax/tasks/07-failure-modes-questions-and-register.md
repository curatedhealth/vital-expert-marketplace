Input:    the outputs of tasks 01 to 06; references/failure-modes.md
Atom:     compare-against-criteria (triggered / not triggered / cannot tell); compose-draft
Tool:     python3 scripts/validate_register.py register.json (fixture: evals/fixtures/good-register.json)
Template: none
Output:   failure-mode screen for FE-01 to FE-04, questions for the accountant, tax specialist and counsel, the gaps with consequences, the register written to templates/financial-register.md
Check:    validator exit 0; status UNSIGNED until a named reviewer signs; options to close each gap listed with effort and risk. Rule: "triggered" points to a register row; "not triggered" has a written reason; "cannot tell" has a gap
Human:    the named accountant (tax specialist for tax flags, counsel for license obligations) reviews the output
