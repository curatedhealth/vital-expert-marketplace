Input:    tasks 03 to 05 and templates/rnpv-register.md
Atom:     compose-draft
Tool:     python3 scripts/validate_register.py register.json
Template: templates/rnpv-register.md
Output:   the rNPV register: answer in three lines, stage table, rNPV and unrisked NPV by scenario and rate, gaps, questions, decisions
Check:    validate_register exit 0; HUMAN ONLY fields; no fairness view. Rule: UNSIGNED until a reviewer signs
Human:    the named reviewer signs; the deal lead decides what, if anything, is adopted
