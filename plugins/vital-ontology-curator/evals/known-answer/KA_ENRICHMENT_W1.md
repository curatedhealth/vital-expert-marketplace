# Known-answer evals — enrichment W1/W2

## KA-CUR-VP-01 — refuse VP-less bound tip

Input: propose tip `subject_family=ph`, `subject_code=PH-01`, empty `vp_code`.  
Expect: `error=missing_vp_code`.

## KA-CUR-PRIV-01 — refuse private shared-queue

Input: capture lead `public_flag=private`.  
Expect: `non_public_source_refused`.

## KA-CUR-ODI-01 — opportunity math

Input: I=8, S=4.  
Expect: opportunity=12 (`I + max(I-S,0)`).

## KA-CUR-APQC-01 — missing scope → queue not approve

Input: APQC tip without formula/unit/normalization_basis.  
Expect: `evaluate_record_eligibility` → `eligible=false`, reason `apqc_scope_incomplete:…`; fast-track `applied=false`. Named decide may still approve.

## KA-CUR-READ-01 — polymorphic evidence read

Input: approved tip `subject_family=ph`, empty `vd_code`.  
Expect: `curator_evidence_for_driver(vd_code=PH-…)` count 0; `subject_family+subject_code` count 1.
