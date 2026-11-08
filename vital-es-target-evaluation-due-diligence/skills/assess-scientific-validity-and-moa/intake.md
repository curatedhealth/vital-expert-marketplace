# Intake

Ask for every missing item in one message. For each item, what happens if it is missing is stated.

| # | Input | If missing |
|---|---|---|
| 1 | Buyer mode (bd or investor), unit (asset, or company with the list of pipeline assets; one run per asset, then a roll-up), markets for any regulatory precedent (US, EU or both) | ask; do not start; another market is a [GAP] |
| 2 | The asset: name, modality, target (gene or protein), stated mechanism of action, indication, development stage | ask; do not assume a target, mechanism or indication |
| 3 | The seller's account of the science: deck, target rationale, publications cited, internal reports | ask; without it the register has no claimed mechanism and stops at a gap row |
| 4 | Human evidence: genetic association studies, human genetics of the target, natural-history or clinical pharmacology data, early clinical observations; cohort, size, where published or held | record "not yet set"; the evidence chain is graded no higher than preclinical_only and the gap is stated |
| 5 | Preclinical studies: each with model, species, originating laboratory, dosing, outcome measures and the ARRIVE items as reported (study design, sample size, inclusion and exclusion criteria, randomisation, blinding, outcome measures, statistical methods, experimental animals, experimental procedures, results) | record "not yet set"; an item that cannot be judged from the source is "not assessable" (a GAP) |
| 6 | Reproductions: any repeat of a key finding, by whom, with the result, and whether the performing organization differs from the originator | record "not yet set"; the finding rests on the originating group alone |
| 7 | Biomarkers: what was measured, in which species, whether it shows target engagement, and whether any such measure exists in humans | record "not yet set"; target engagement in humans is then a stated gap |
| 8 | Class: other agents against the same target or mechanism (approved, failed, withdrawn, ongoing) with sources; any class-wide safety warning | record "not yet set"; class risk cannot be judged and the register says so |
| 9 | Differentiation claims: how the asset differs from the class (selectivity, route, patient selection, dose), each with its basis | record "not yet set"; adverse class precedents then carry no differentiation |
| 10 | Name and role of the scientist who will give the scientific judgment | record "not yet set"; the register stays UNSIGNED |

Explicit don'ts: never assume a target, mechanism, indication or model; never infer a study, cohort or reproduction you were not given (it is a [GAP] with the consequence stated); never state or imply that the target is validated; never apply a published population-level finding to the asset as a probability.
The company unit runs one register per asset; the roll-up lists assets side by side and never merges evidence across assets.
