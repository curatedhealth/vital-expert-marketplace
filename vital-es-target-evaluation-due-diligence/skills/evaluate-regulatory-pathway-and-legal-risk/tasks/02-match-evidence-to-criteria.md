Input:    task 01 routes; the signed clinical evidence register (skill A); the ranges (skill B)
Atom:     compare-against-criteria (criteria = each route criterion; state set: met / not met / gap)
Tool:     none
Template: none
Output:   per route, per criterion: state, evidence_ref (register row id), note
Check:    "met" names a register row; a criterion no row speaks to is a gap with the consequence; validate_pathway.py E_CRITERIA is clean. Rule: the register is the evidence; a seller's claim is not
Human:    the named regulatory reviewer (counsel for legal rows) reviews the output
