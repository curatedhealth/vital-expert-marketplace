Input:    the inputs of tasks 01 to 04 in one JSON file (the calculator input)
Atom:     none (no atom: a scripted step)
Tool:     python3 scripts/forecast_range.py input.json --pretty (fixture: evals/fixtures/good-forecast-input.json)
Template: none
Output:   per country: peak-year and cumulative revenue as low, mid and high (gross and net apart), cumulative to the exclusivity end, the sensitivity table for all seven drivers, the probability of success beside the ranges, disabled-rule [CHECK] messages, gaps and flags; a total only for one currency or with a dated rate
Check:    exit 0; the calculator rejects discount and risk-adjustment inputs, "EU", mixed currencies and a net above list; no figure is risk-adjusted or discounted. Rule: a person confirms the inputs; the output stays UNSIGNED
Human:    the deal lead confirms the inputs before the numbers are used
