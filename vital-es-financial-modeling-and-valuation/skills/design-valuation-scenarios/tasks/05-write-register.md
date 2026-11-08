Input:    tasks 01 to 04 and templates/scenario-register.md
Atom:     compose-draft
Tool:     python3 scripts/validate_register.py register.json
Template: templates/scenario-register.md
Output:   the scenario register: answer in three lines, drivers, table, named scenarios, gaps, questions
Check:    validate_register exit 0; HUMAN ONLY fields
Human:    the named reviewer signs
