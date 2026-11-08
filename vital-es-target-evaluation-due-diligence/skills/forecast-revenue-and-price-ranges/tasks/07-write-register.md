Input:    the output of task 05, the screen and questions of task 06, and templates/revenue-register.md
Atom:     compose-draft (structure = templates/revenue-register.md; answer first, then evidence rows)
Tool:     python3 scripts/validate_register.py register.json
Template: templates/revenue-register.md
Output:   the revenue and price register: answer in three lines, per-country ranges, sensitivity, probability of success beside the ranges, Market Access columns, failure-mode screen, gaps, questions, decisions needed
Check:    validate_register exit 0; adopted_forecast HUMAN ONLY and recommended_forecast null; no single figure, no risk-adjusted or discounted figure, no EU price, no merged Market Access value. Rule: the register is UNSIGNED until a named reviewer signs
Human:    the named reviewer signs; the deal lead decides which forecast, if any, the team adopts
