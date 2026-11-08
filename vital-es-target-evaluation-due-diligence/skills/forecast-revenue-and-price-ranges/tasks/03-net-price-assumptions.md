Input:    the list prices from task 02 and the deal team's statement of net-to-list ratios (intake items 6 and 10)
Atom:     extract-requirements-from-source (the deal team's own statement is the source; one row per country: ratio low, mid and high, the name of the person who set it, the date)
Tool:     none
Template: none
Output:   per country: net-to-list ratio range labelled ASSUMPTION with the setter's name and date; a country without a statement is GAP and its net revenue is not computed
Check:    no ratio is above 1 or below 0; no default ratio is used (rule FC-NET-DEFAULT-RATIO is [CHECK]); the evidence that net is not public is cited (VP-R-021, VP-R-022, VP-R-040, VP-R-024). Rule: net is an assumption, never a fact
Human:    the named deal-team member sets the ratios; the deal lead confirms
