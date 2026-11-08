# Poor example (fictional; do not copy)

"FX-101 showed a statistically significant and clinically meaningful benefit across the full population
and especially in patients under 50 (p<0.01). Safety was unknown. The endpoint is accepted by FDA and EMA
as a surrogate. Replication is expected in the phase 3."

What is wrong, row by row:
1. Source is a press release; no regulatory document, no flag, no gap (breaks FM-07 and the source-tier rule).
2. "Especially in patients under 50" is a subgroup claim with no prespecification or interaction test (FM-03).
3. "Safety was unknown" uses the banned word; absence must be GAP with what is missing and why it matters.
4. "Accepted by FDA and EMA as a surrogate" is from memory: the EU has no surrogate table, and the US claim needs the table row.
5. "Replication is expected" treats a plan as a result.
6. No risk-of-bias domains, no estimand, no failure-mode screen, no reviewer.
The validator rejects it: E_UNKNOWN, E_PRESS_ONLY, E_SUBGROUP, E_PRECEDENT, E_MODE_NOT_SCREENED.

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json`; the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Wrong statement | Pattern documented in | Passage ids |
|---|---|---|
| the source is a press release alone | FM-07 | VP-A-083 to VP-A-085 |
| "especially in patients under 50" | FM-03 | VP-A-088, VP-A-089 |
| "accepted by FDA and EMA as a surrogate" | FDA surrogate table is the US source; the EU claim is [CHECK] | VP-A-050, VP-A-053 |
| "replication is expected in the phase 3" | phase 2 results not confirmed in phase 3 (FM-02) | VP-A-080, VP-A-081 |
