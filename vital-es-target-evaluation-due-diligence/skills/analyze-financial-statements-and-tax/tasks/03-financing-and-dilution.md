Input:    financing documents and equity notes: rounds, facilities, warrants, convertibles, share counts (intake item 5)
Atom:     extract-requirements-from-source
Tool:     scripts/runway.py (dilution block of the input)
Template: none
Output:   financing history table (date, type, amount, source); per-round dilution and the retained share of the starting holders; total gross proceeds of priced rounds
Check:    fully diluted share counts used; every row sourced; investor mode shows the financing path (what is closed, what is only expected). Rule: arithmetic only; no valuation; asset mode leaves this out
Human:    the named accountant (tax specialist for tax flags, counsel for license obligations) reviews the output
