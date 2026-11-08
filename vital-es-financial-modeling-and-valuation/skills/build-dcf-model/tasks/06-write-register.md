Input:    the output of task 04, the screen of task 05 and templates/dcf-register.md
Atom:     compose-draft (structure = the template; answer first, then evidence rows)
Tool:     python3 scripts/validate_register.py register.json
Template: templates/dcf-register.md
Output:   the DCF register: answer in three lines, revenue and cost inputs with pointers, present values by scenario and rate, terminal share, gaps, questions, decisions needed
Check:    validate_register exit 0; adopted valuation HUMAN ONLY; no single present value as the value; no fairness view. Rule: UNSIGNED until a named reviewer signs
Human:    the named reviewer signs; the deal lead decides whether any rate or value is adopted
