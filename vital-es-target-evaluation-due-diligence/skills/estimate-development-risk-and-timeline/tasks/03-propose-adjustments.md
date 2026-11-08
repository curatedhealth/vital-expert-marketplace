Input:    signed register, failure-mode screen from skill A, benchmark
Atom:     compare-against-criteria (criteria = register findings and triggered failure modes; states: moves probability down / up / no move / cannot tell)
Tool:     none
Template: none
Output:   per adjustment: id, transition, multiplier low / mid / high, reason, ref (register row id or FM id), upward_basis if above 1
Check:    every triggered failure mode and every register row with a high or some-concerns risk of bias has either an adjustment or a written no-move reason. Rule: no adjustment from general impression; a person confirms each one. The bounds are the proposer's, shown with the reason
Human:    the BD or investment lead confirms each adjustment and its bounds
