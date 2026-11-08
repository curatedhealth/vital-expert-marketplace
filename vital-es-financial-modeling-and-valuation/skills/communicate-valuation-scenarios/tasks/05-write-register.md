Input:    tasks 01 to 04 and templates/scenario-communication.md
Atom:     compose-draft
Tool:     python3 scripts/validate_register.py register.json
Template: templates/scenario-communication.md
Output:   the register: answer in three lines, range, what would change the call, decisions, questions
Check:    validate_register exit 0; HUMAN ONLY fields
Human:    the named reviewer signs
