Input:    the output of task 04 and its inputs
Atom:     compare-against-criteria (criteria = the detection question of each failure mode; state set: triggered / not triggered / cannot tell)
Tool:     none
Template: none
Output:   a closed screen with the state of each mode, a register reference for each "triggered", a reason for each "not triggered", a gap for each "cannot tell"; the questions for the reviewer
Check:    all modes screened; at least one question. Rule: a triggered mode goes to the reviewer
Human:    the named valuation reviewer reviews every mode marked triggered or cannot tell
