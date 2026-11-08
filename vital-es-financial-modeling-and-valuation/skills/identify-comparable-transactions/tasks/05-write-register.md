Input:    tasks 01 to 04 and templates/comparables-register.md
Atom:     compose-draft
Tool:     python3 scripts/validate_register.py register.json
Template: templates/comparables-register.md
Output:   the comparables register: answer in three lines, criteria, screen, flags, questions
Check:    validate_register exit 0; HUMAN ONLY fields
Human:    the named reviewer signs
