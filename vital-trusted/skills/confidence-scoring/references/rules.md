# Rules this skill applies

Each rule names its source, the date and its status (TR-H8). The confidence line is
VERIFY's own definition, not a regulatory or industry requirement. No primary document
known to this skill sets a faithfulness threshold for releasing material, and this skill
sets none.

Last reviewed: 20 October 2026.

| Id | Rule | Source | Status |
|---|---|---|---|
| C1 | Faithfulness percent = (supported + 0.5 × partial) ÷ (supported + partial + unsupported + contradicted + unverifiable), as a whole percent. out_of_scope is left out of the denominator. | VERIFY connector server instruction, as exposed to this session on 20 October 2026. The same formula is restated in the earlier vital-verify `support-decision` skill (version 2026-10-19.2). | Confirmed against the connector instruction on 20 October 2026. The connector tool schemas do not state it. |
| C2 | Rounding to a whole percent is half up (12.5 becomes 13). | None. Chosen by this skill so the result is reproducible. | `[CHECK]`: VERIFY's own rounding convention is not stated in the instruction or the schemas. Owner to confirm. |
| C3 | The six statuses: supported, partial, unsupported, contradicted, unverifiable, out_of_scope. Open items are partial, unsupported, contradicted and unverifiable. | VERIFY connector instruction, 20 October 2026 (names the statuses in the formula and the open items). | Confirmed for the names on 20 October 2026. The `check_claim` schema says it "returns a status" but does not list the values; `[CHECK]` against a real return. |
| C4 | Status meanings: supported means the passage states the claim or a stricter version; partial means part is stated and the rest can be named; unsupported needs admissible sources to have been checked; contradicted needs a passage stating the opposite; unverifiable is a refusal (no source, inadmissible source, empty passage) and not a finding that the claim is false; out_of_scope is for normative and definitional statements. A bronze-tier passage yields at most partial. | vital-verify `support-decision` skill, `references/statuses.md`, restated 19 October 2026 from the VERIFY method. | `[CHECK]`: a document, not the connector. To be re-established against `check_claim` returns before being stated as fact. |
| C5 | A status measures word overlap between the statement and the passage. It is not a verdict that the statement is true in the world. | VERIFY connector instruction, 20 October 2026 ("A status is word overlap with that passage, not a verdict that the sentence is true in the world"). | Confirmed on 20 October 2026. |
| C6 | Under each reference, print the source_score total and the axes whose values are numbers; omit an axis whose value is null. Then the confidence line, then a short card: counts by status, the open items, one recommendation. No evidence table unless asked. | VERIFY connector instruction, 20 October 2026. | Confirmed on 20 October 2026. |
| C7 | Source score axes are authority, recency, relevance, provenance and currency (weights 25, 25, 30, 10, 10); null axes are dropped and the rest rescaled to 100; relevance is null when no question was passed; currency is null until a currency check runs. | vital-verify `source-grading` skill, `references/tiers-and-score.md`, 19 October 2026. The `qualify_source` schema says only that it returns "a tier and a source_score". | `[CHECK]`: axis names, weights and null behavior to be confirmed against a real `qualify_source` return. Print what comes back; do not recompute. |

## How to use these rules in output

- Do the arithmetic of C1 in the open. Never describe it as an industry standard.
- When a rule is `[CHECK]`, apply it as this skill's practice and do not cite it as
  VERIFY behavior to the person.
- Never add a threshold, a band or a label to the percent. None of these sources defines
  one.
