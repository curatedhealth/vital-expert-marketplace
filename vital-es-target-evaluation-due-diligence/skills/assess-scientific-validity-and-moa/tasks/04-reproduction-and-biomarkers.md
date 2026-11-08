Input:    reproductions and biomarker data (intake items 6 and 7)
Atom:     extract-requirements-from-source
Tool:     scripts/mechanism_check.py (reproduction, biomarkers)
Template: none
Output:   independent_reproduction rows (finding, performing organization, independent or not, result, source); biomarker rows with the human target-engagement flag
Check:    a reproduction needs its own data (new_data_collected true; National Academies definition, VP-F-100) and its result is a degree, not a pass/fail (VP-F-101); "independent" only for a different organization (ENGINEERING RULE: no source defines independence by organization); a pharmacodynamic biomarker counts for humans only if it shows target engagement in a human study and is sourced. Rule: a reproduction by the originator is recorded as such
Human:    the named scientist confirms the inputs (who performed each reproduction)
