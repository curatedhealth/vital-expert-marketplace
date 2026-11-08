Input:    cash items, burn basis and source, scheduled and contingent outflows, closed and expected inflows, debt maturities, scenarios (intake items 3 and 4)
Atom:     none
Tool:     python3 scripts/runway.py input.json --pretty (fixture: evals/fixtures/good-runway-input.json)
Template: none
Output:   per scenario: runway months, cash-out date, flags with rule ids; gaps; disabled-rule [CHECK] messages
Check:    exit 0; burn basis and source stated; contingent outflows and expected inflows appear only in the scenarios that name them; the convention line (calendar months, month-end events) shown. Rule: a person confirms the burn basis; the output is arithmetic on supplied inputs, not a forecast; investor mode runs three or more scenarios
Human:    the named accountant (tax specialist for tax flags, counsel for license obligations) reviews the output
