Input:    commitments and contingencies note, guarantees, off-balance-sheet arrangements; income tax note; ownership-shift facts (intake items 7 and 8)
Atom:     extract-requirements-from-source
Tool:     scripts/runway.py (tax block of the input)
Template: none
Output:   contingent commitments table; tax attributes rows with the flag text and the specialist question; the Section 382 ownership flag with its inputs
Check:    the flags name section 382 (VP-E-022, VP-E-023), the 80 percent limit (VP-E-024) and the IRS rate source (VP-E-025) without computing a limitation; IPR&D treatment and contingencies are specialist questions (VP-E-030 to VP-E-034, practitioner sources); every row sourced; the 3-year testing period and the more-than-50-points test named by rule id; the limitation amount not computed. Rule: a tax specialist decides; asset mode leaves tax out
Human:    the named accountant (tax specialist for tax flags, counsel for license obligations) reviews the output
