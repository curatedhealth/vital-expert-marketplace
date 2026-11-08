Input:    tasks 01 to 04 and templates/sensitivity-register.md
Atom:     compose-draft
Tool:     python3 scripts/validate_register.py register.json
Template: templates/sensitivity-register.md
Output:   the sensitivity register: answer in three lines, tornado, switching values, gaps, questions
Check:    validate_register exit 0; HUMAN ONLY fields
Human:    the named reviewer signs
