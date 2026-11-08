# Good example (fictional asset FX-101; not a real product)

Buyer mode: BD. Unit: asset. Markets: US, EU. Documents: a regulatory-style review summary, a registry entry and a press release.

**Answer first**
1. The only controlled evidence is one 180-patient phase 2 trial with 22% missing week-12 data and no sensitivity analysis (R1). It puts the efficacy case at risk.
2. The open-label follow-up (R2) is known only from a press release; size, endpoint, safety tables and estimand are GAP. It cannot support the case.
3. Two liver enzyme elevations above 3x upper limit in the treated arm (R1) are not discussed in the seller deck.

| Row | Trial | Design, phase, n, control | Estimand | Risk of bias | Replication | Precedent US / EU | Flags |
|---|---|---|---|---|---|---|---|
| R1 | Randomized phase 2 | double-blind, phase 2, n=180, placebo | adults with Z, as randomized; FX-101 vs placebo as assigned; change in symptom score at week 12; rescue and discontinuation handled with the treatment policy strategy; difference in means | RoB 2: missing outcome data "some concerns" (22% missing, FICTIONAL p. 14); other domains low; overall some concerns | single study | US: clinical endpoint, not on surrogate table; EU: no EU surrogate table exists | none |
| R2 | Open-label extension | open-label, phase 2, n GAP, no control | GAP: the estimand (missing: analysis plan; matters: cannot tell what was measured after discontinuation) | GAP (missing: study report) | GAP | US: GAP; EU: no EU surrogate table exists | NOT_REGULATORY_RECORD; SINGLE_ARM; SUBGROUP_CLAIM; SUBGROUP_UNREPLICATED |

Failure modes triggered: FM-02 (R1), FM-03 (R2), FM-06 (R1), FM-07 (R2). "Cannot tell": FM-05 (no preclinical package), FM-08 (no manufacturing section).
Validated by scripts/validate_register.py: exit 0 (evals/fixtures/good-register.json).

Why it is good: absent evidence is a GAP with the consequence, not "unknown"; the press-release row is not treated as the record; the EU row does not invent a surrogate table.

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json`; the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| a single phase 2 trial carries the efficacy case | phase 2 results not confirmed in phase 3 (FM-02) | VP-A-080, VP-A-081 |
| 22% of week-12 data missing: "some concerns" in the missing-outcome-data domain | RoB 2 domain 3 and the overall rule | VP-A-005, VP-A-009, VP-A-010 |
| rescue and discontinuation handled with the treatment policy strategy; four estimand attributes | ICH E9(R1) attributes and strategies | VP-A-020 to VP-A-025 |
| the open-label follow-up is known only from a press release | press release versus the regulatory record (FM-07) | VP-A-083 to VP-A-085 |
| a subgroup finding with no interaction test or replication | subgroup claims in randomized trial abstracts (FM-03) | VP-A-088, VP-A-089 |
| liver enzyme elevations not discussed in the seller deck | safety evidence that is anecdotal or reaches the record late (FM-06) | VP-A-086, VP-A-087 |
| US precedent: clinical endpoint, not on the surrogate table; EU: no EU surrogate table exists | FDA table of surrogate endpoints; the EU statement is a [CHECK] claim (M12) | VP-A-050, VP-A-053 |
