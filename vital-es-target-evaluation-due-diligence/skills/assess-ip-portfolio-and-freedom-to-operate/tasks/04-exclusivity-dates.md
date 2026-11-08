Input:    patent family table, regulatory milestones and designations (intake items 2, 4, 5), the pte and spc blocks naming the patent
Atom:     none (no atom: a scripted or reading step)
Tool:     python3 scripts/exclusivity_dates.py input.json --pretty (fixture: evals/fixtures/good-exclusivity-input.json)
Template: none
Output:   per market: regulatory periods, patent final expiries with extension, effective dates (all patents; composition only), gaps, flags, disabled-rule [CHECK] messages
Check:    biologics with accepted pediatric studies add six months to the 12-year and 4-year periods (42 U.S.C. 262(m)(2), VP-C-033); a qualified infectious disease product that is not a section 262(a) biologic adds 5 years (21 U.S.C. 355f, VP-C-040 to VP-C-042) and stacks with pediatric exclusivity; exit 0; every date names its rule id; conventions (whole days, calendar months) shown; diligence reduction, issue date and SPC reference date gaps listed. Rule: a person confirms the inputs; the output stays UNSIGNED; no freedom-to-operate statement
Human:    the named patent counsel (or named IP reviewer) reviews the output
