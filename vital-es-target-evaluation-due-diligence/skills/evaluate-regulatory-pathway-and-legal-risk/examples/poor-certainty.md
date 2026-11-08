# Poor example (fictional asset FX-501)

"FX-501 has breakthrough designation, so it will receive accelerated approval in the US and conditional approval in the EU within 18 months. The company is fully compliant and there is no legal risk. Manufacturing is fine."

**What is wrong**
1. States regulatory outcomes as certain ("will receive accelerated approval"). Only the agency decides; validate_pathway.py rejects the text (E_LEGAL_CONCLUSION).
2. Designation is treated as an approval route. Criteria for accelerated approval and for conditional authorisation were not assessed against the register (E_CRITERIA); no confirmatory trial or specific-obligations block (E_CONFIRMATORY); no precedent (E_PRECEDENT).
3. "Fully compliant" and "no legal risk" are legal conclusions for counsel (E_LEGAL_CONCLUSION), made with no document read.
4. "Manufacturing is fine": no site named, no inspection source, no comparability evidence (E_RISK; RL-02 not screened).
5. "18 months" overrides the ranges from the timeline skill without a reason; EU route has no note that the reform is not yet law (E_REFORM); upstream registers not cited (E_UPSTREAM).

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json` (or of the skill named); the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| "will receive accelerated approval"; designation treated as a route | criteria must be assessed; the surrogate table is not a replacement for discussion with review divisions | VP-D-003, VP-D-040 |
| "fully compliant", "no legal risk" | a representation breach can be a material adverse effect; data integrity violations lead to regulatory actions | VP-D-090, VP-D-070 |
| "manufacturing is fine"; no inspection source | public inspection data cannot count all inspections | VP-D-061, VP-D-062 |
| no confirmatory trial plan | FDA draft; conditional authorisation obligations | VP-D-012, VP-D-026 |
