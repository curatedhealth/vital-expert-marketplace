Input:    documents listed at intake
Atom:     extract-requirements-from-source (here the "requirements" are facts: design, phase, size, control, endpoint, dates), one row per trial or analysis with the passage that states each fact
Tool:     literature_find_trial / get_trial_details to confirm the registered design when an identifier is given
Template: none
Output:   draft rows with a locator per fact; fields without a passage are GAP
Check:    every fact has a locator or is GAP; no fact from memory. Rule: a field not stated in a document is GAP with missing and why_it_matters; never "unknown"
Human:    none (the clinical development reviewer reads the draft rows at task 06)
