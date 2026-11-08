Input:    preclinical studies with the ARRIVE items as reported (intake item 5)
Atom:     extract-requirements-from-source
Tool:     python3 scripts/mechanism_check.py input.json --pretty (fixture: evals/fixtures/good-mechanism-input.json)
Template: none
Output:   preclinical_evidence rows: model, species, originator, experimental_unit, n_counts_experimental_units, independent_replications_reported, the ten Essential 10 flags (true, false, null), what the model does and does not represent, source; ARRIVE completeness per study
Check:    all ten flags present; each study states its experimental unit and whether n counts experimental units, so that pseudoreplication is visible (ARRIVE E&E, VP-F-110 to VP-F-112); the register lists the strengths and weaknesses of the cited prior research (NIH rigor notice, VP-F-170, VP-F-171; a funder policy, used as a prompt); null means not assessable and becomes a gap; the translatability note names the disease features the model lacks. Rule: ARRIVE shows reporting, not truth; the translatability judgment is the scientist's
Human:    the named scientist reviews the translatability notes and the ARRIVE flags
