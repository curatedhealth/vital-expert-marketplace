Input:    tasks 01 to 04 and templates/benchmark-register.md
Atom:     compose-draft
Tool:     python3 scripts/validate_register.py register.json
Template: templates/benchmark-register.md
Output:   the benchmark register: answer in three lines, ranges, leave-one-out, positions, gaps, questions
Check:    validate_register exit 0; HUMAN ONLY fields
Human:    the named reviewer signs
