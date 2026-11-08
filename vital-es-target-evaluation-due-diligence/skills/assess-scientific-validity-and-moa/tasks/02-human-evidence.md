Input:    genetic, natural-history and early clinical pharmacology evidence (intake item 4)
Atom:     extract-requirements-from-source; classify-text-labels (human_genetic, clinical_pharmacology, other)
Tool:     scripts/mechanism_check.py (evidence_chain)
Template: none
Output:   human_evidence rows (kind, cohort, size, direction of effect, source); the evidence-chain grade (human_genetic, clinical_pharmacology, preclinical_only, none)
Check:    every row sourced; an unsourced statement is not counted; the consequence of a thin chain stated as a GAP. Rule: population-level statistics from the literature are context, never an asset probability
Human:    the named scientist reviews the evidence-chain grade
