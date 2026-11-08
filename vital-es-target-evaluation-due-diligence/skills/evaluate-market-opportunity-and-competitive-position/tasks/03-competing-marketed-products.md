Input:    regulator approval pages, labels, company pages, the Market Access pack's competitor signals (intake item 6)
Atom:     extract-requirements-from-source
Tool:     connectors (read-only)
Template: none
Output:   competitors_marketed rows: product, sponsor, mechanism, approved indication, market, source with date
Check:    each row has a source with a date; a product approved in only one of the two markets says so. Rule: no price, coverage or share figure
Human:    the named reviewer with market and clinical knowledge reviews the output
