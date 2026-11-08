Input:    the team's stage costs and years (intake item 3)
Atom:     extract-requirements-from-source
Tool:     none
Template: none
Output:   stage table: name, years, cost low / mid / high, owner
Check:    stages sequential and not overlapping; costs non-negative; every cost has an owner. Rule: FV-STAGE-LAYOUT
Human:    the finance lead supplies the values
