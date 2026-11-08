Input:    the signed revenue register (net revenue by scenario and year), the exclusivity register (intake items 2 and 3)
Atom:     extract-requirements-from-source (the registers are the source; one row per series with its pointer)
Tool:     none
Template: none
Output:   net revenue series by scenario with pointers; launch years; exclusivity end per market; fields a register lacks are GAP
Check:    every figure points to a register row or is GAP; nothing from another market is a proxy. Rule: upstream gaps stay gaps
Human:    the deal lead confirms the series
