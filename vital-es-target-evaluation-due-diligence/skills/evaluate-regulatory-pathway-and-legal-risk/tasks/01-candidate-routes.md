Input:    indication, stage, designations (intake item 3); markets in scope
Atom:     none (no atom: a scripted or reading step)
Tool:     none; reads references/rules/pathway-rules.json (route keys, criteria, clocks, status per rule); references/markets/us.md and eu.md
Template: none
Output:   per market: the standard route and each expedited or conditional route that could apply, each with its criteria list
Check:    every route key exists in the rules file for that market; routes resting on a DRAFT guidance are labelled DRAFT; EU routes carry the reform note. Rule: list routes the evidence might support and routes it clearly cannot; do not rank or choose
Human:    the named regulatory reviewer (counsel for legal rows) reviews the output
