Input:    intake, signed register
Atom:     compare-against-criteria (criteria = the strata in references/benchmarks/bio-2011-2020.json; states: fits / does not fit / cannot tell)
Tool:     none
Template: none
Output:   one benchmark_key and benchmark_basis (why this stratum), with its n per transition and any LOW_N flag
Check:    biomarker stratum only when patients are selected by a biomarker, not when a new biomarker is being evaluated (VP-B-061, VP-B-065); a biomarker or orphan stratum outside oncology is flagged as resting on few data points (VP-B-064, VP-B-066). exactly one stratum; the most specific stratum with adequate n is used; other attributes are held for adjustments. Rule: strata are not combinable; the human confirms the stratum
Human:    the BD or investment lead confirms the stratum
