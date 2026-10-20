# Gap rules

A gap is information: each kind leads to a different next step. Word it so the reader knows what is missing, why, and who can fill it.

## Evidence base

| Situation | How to word it | Next step |
|---|---|---|
| A source the rules require that the library does not query (CENTRAL, Embase, PROSPERO, WHO ICTRP, CTIS, EU-CTR) | "Not searchable through the library `[GAP]`; run in the source itself (row)." | The person's searcher runs it and logs the date (ES-06). |
| No study found for a PICO | "No eligible study found in the sources searched on DATE." Never "no evidence exists." | Check the strategy (PRESS, ES-63) and the sources list before concluding. |
| Library excerpt empty or ends before results | "Results passage not in the library record `[GAP]`." | Read the paper (Europe PMC, publisher) or ask the person for it. |
| Study reported only as a conference abstract or preprint | Say so in the row; it is not a full peer-reviewed report. | Look for the full report; preprints may be included if the protocol allows (ES-53). |
| Registry entry with no results | "Registered, results not posted as of DATE." | Contact authors if the protocol plans it (ES-27). |
| Unpublished company data | "Unpublished; usable only with enough detail to judge it (ES-134); IQWiG cannot use data the submitter will not allow to be published (ES-144)." | The person's owner decides whether to disclose. |

## Records and appraisal

| Situation | How to word it |
|---|---|
| Library design label, not checked | "Draft label from the library (basis: title word or publication type)." Never as the design. |
| Design checked against the paper | "Design from methods section (or registry entry ID)." |
| Risk-of-bias judgment not yet made | "Not yet assessed (reviewers)." Never fill it in. |
| Signalling question with no information in the paper | "No information" is a valid RoB 2 answer (ES-72); write it, do not guess. |
| Retraction status checked only in Crossref | "No retraction found in Crossref on DATE." |
| A rule the research did not read (RoB 1 domains, PROSPERO fields, PRESS checklist text, HTACG reviewer numbers, HAS literature rules) | "`[GAP]` not in the sourced rules; read SOURCE before applying." |

## Synthesis

| Situation | How to word it |
|---|---|
| Pooling not appropriate | "Not pooled: REASON (row)." A narrative synthesis is a valid result (ES-83). |
| Certainty not yet rated | "Certainty: not yet rated (reviewers)." Never "high" from the library's draft. |
| Minimally important difference or decision threshold not given | "Threshold not given by the person `[GAP]`." Never supply one. |
| Flow counts do not reconcile | Quote the failing line from `scripts/prisma_flow.py`; do not adjust counts to make them fit. |

## Open access

When a source is open access (Europe PMC full text, publisher open access), read the full text before marking a field `[GAP]` from an abstract or a library excerpt. Write "abstract only" only when the full text is not openly available, and say where you looked.

## Never

- Never mark a study included, excluded, low risk or high certainty on the model's own judgment.
- Never fill a gap from memory, from a passage without a locator, or from a library label.
- Never call a finding "proven"; never call an absence of found studies an absence of evidence.
