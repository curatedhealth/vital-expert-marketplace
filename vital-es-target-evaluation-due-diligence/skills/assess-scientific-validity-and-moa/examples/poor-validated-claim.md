# What not to produce (FICTIONAL, for the poor-example screen)

Mechanism register: FICTIONAL FX-701

- The target is validated and the mechanism is proven; we recommend proceeding.   <- a scientific go/no-go; only the named scientist may state it.
- Strong human genetics.   <- one cohort, unsourced in the register; no source entry, so it is not counted.
- Reproduced in two species.   <- both by the originating laboratory; independence needs a different organization.
- Animal data are robust.   <- ARRIVE items were never listed; blinding is not reported and the exclusion criteria cannot be assessed.
- Class: no issues.   <- a failed class member and a class safety warning exist.
- Biomarker: unknown.   <- "unknown" instead of a GAP.

Why it fails: validate_register.py returns E_GONOGO_FIELD, E_GONOGO_TEXT, E_UNKNOWN, E_SECTION, E_SOURCE, E_ARRIVE, E_PRECEDENT, E_FM_UNRESOLVED and E_QUESTIONS (evals/fixtures/poor-register.json is the machine-readable version).

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json`; the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Wrong statement | Pattern documented in | Passage ids |
|---|---|---|
| "validated and proven" from one cohort and animal work | population-level genetic finding is context only; animal discordance | VP-F-001 to VP-F-003, VP-F-070 to VP-F-072 |
| "reproduced in two species", both by the originating laboratory | independence and replication evidence | VP-F-030 to VP-F-032, VP-F-040 to VP-F-043 |
| "animal data are robust" with no ARRIVE items | the ARRIVE Essential 10 | VP-F-010 to VP-F-021 |
| "class: no issues" with a failed member and a class warning | class-wide warning | VP-F-050, VP-F-051 |
