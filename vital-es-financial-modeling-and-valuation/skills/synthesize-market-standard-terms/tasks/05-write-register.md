Input:    tasks 01 to 04 and templates/market-terms-register.md
Atom:     compose-draft
Tool:     python3 scripts/validate_register.py register.json
Template: templates/market-terms-register.md
Output:   the market-terms register: answer in three lines, synthesis, cross-check, caveats, decisions
Check:    validate_register exit 0; HUMAN ONLY fields
Human:    the named reviewer signs
