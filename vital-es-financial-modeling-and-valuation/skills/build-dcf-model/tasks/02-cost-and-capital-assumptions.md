Input:    the deal team's statement of the cost structure (intake item 4)
Atom:     extract-requirements-from-source (the team's statement is the source; one row per line with owner and date)
Tool:     none
Template: none
Output:   cost structure per scenario with source or owner; a missing structure is a GAP and the value is labelled revenue-only
Check:    no line is invented; every line has a source or a named owner; shares are between 0 and 1. Rule: FV-CASHFLOW-ARITHMETIC
Human:    the finance lead (named) supplies the values; the deal lead confirms
