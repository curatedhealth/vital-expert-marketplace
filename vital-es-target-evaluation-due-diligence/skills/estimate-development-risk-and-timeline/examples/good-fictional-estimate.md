# Good example (fictional asset FX-101; not a real product)

Inputs: signed register (evals/fixtures/good-register.json); phase 2; neurology; BD; US and EU.

**Answer first**
- Overall probability from phase 2 to approval (US benchmark basis): low 5.9%, mid 8.9%, high 11.7%; unadjusted benchmark 12.3% (technical 14.2%, regulatory 86.7%). EU approval probability [GAP]. [numbers: scripts/pos_chain.py on evals/fixtures/good-input.json]
- Timeline from phase 2 start to an approval decision: low 78, mid 114, high 144 months (scripts/timeline_range.py; low and high start from the spread of disease-area averages, not a confidence interval). EU assessment 150 or 210 days excluding clock stops; clock stops [GAP].
- Drivers: A1 phase 2 reliability (register R1) moves overall mid most; A2 manufacturing evidence (FM-08).
- Final number: UNSIGNED.

Benchmark first: neurology, Fig 2 p.7 of B1: phase 2 to 3 26.8% (n=504), phase 3 to NDA/BLA 53.1% (n=226), NDA/BLA to approval 86.7% (n=165). Then adjustments with reasons and references, sensitivity per adjustment.
BD implications (options): tie a milestone to confirmation of the phase 2 effect with complete week-12 data; ask for the manufacturing section before signing.

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json`; the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| the neurology stratum is the benchmark: phase 2 to 3 26.8% (n=504), phase 3 to NDA/BLA 53.1% (n=226), NDA/BLA to approval 86.7% (n=165) | the benchmark's disease-area table | VP-B-010 |
| the benchmark success is advanced divided by advanced plus suspended | the report's definition | VP-B-004 |
| an overall benchmark of the order of 8% from phase 1 across all indications, 10.5 years to approval | the report's overall figures | VP-B-001, VP-B-003 |
| EU assessment 150 or 210 days excluding clock stops | EMA accelerated assessment page | VP-B-031 |
| the phase 2 adjustment sized to the register's replication status | phase 2 results not confirmed in phase 3 | VP-A-080, VP-A-081 (skill A register) |
| a manufacturing-evidence adjustment (A2) | trade-press report of complete response letters; a secondary source, so the pattern is flagged SUMMARY-ONLY in skill A and the adjustment is labeled a judgement | none |
