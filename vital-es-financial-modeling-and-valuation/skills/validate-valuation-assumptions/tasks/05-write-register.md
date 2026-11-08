Input:    tasks 01 to 04 and templates/assumption-register.md
Atom:     compose-draft
Tool:     python3 scripts/validate_register.py register.json
Template: templates/assumption-register.md
Output:   the assumption register: answer in three lines, assumptions with traces, checks, gaps, questions, decisions
Check:    validate_register exit 0; HUMAN ONLY fields; no validation claim
Human:    the named reviewer signs
