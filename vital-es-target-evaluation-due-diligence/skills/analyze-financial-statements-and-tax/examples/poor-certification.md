# What not to produce (FICTIONAL, for the poor-example screen)

Financial register: FICTIONAL Aurelian Bio Inc.

- The company has no going concern issue and its quality of earnings is strong.   <- certifies two things only an accountant may state; the 10-Q in the data room contains substantial-doubt language.
- Net debt is 12 million.   <- a definition choice that is human only, and no definition was given.
- Runway is about two years.   <- no burn basis, no source, no scenario; the filing's own sufficiency statement is "into the second quarter of 2027".
- Licensor: unknown.   <- "unknown" instead of a GAP; the change-of-control clause was never looked for.
- The NOLs are fully usable.   <- a tax conclusion; ownership shifts of 62 points were supplied.
- The financial statements are fairly presented.   <- an accounting opinion.

Why it fails: validate_register.py returns E_OPINION_TEXT, E_UNKNOWN, E_GOING_CONCERN, E_OBLIGATION, E_FM_UNRESOLVED and E_QUESTIONS (evals/fixtures/poor-register.json is the machine-readable version). A register must quote the filed language, state a basis for every runway, record each clause and ask the specialist.

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json` (or of the skill named); the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| "no going concern issue" | the going-concern evaluation is the auditor's, with a one-year horizon | VP-E-050, VP-E-051 |
| "the NOLs are fully usable"; 62 points of shifts | section 382 ownership change threshold of more than 50 points; the 80 percent limit | VP-E-022, VP-E-024 |
| "net debt is 12 million"; "quality of earnings is strong" | no source defines them for diligence; human only | none (E13 [CHECK]) |
| "Licensor: unknown" | a redacted or missing term is a GAP, never "unknown" | VP-E-012 |
