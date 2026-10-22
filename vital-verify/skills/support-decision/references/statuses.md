# Support decision reference

Code: `check_claim` in `mcps/verify/service.py`. Gold, silver, and caller-owned bronze (`ingested` / `supplied`) passages go to the faithfulness scorer. External URL bronze is at most `partial`.

## Boundaries

- `supported` means the passage states the claim or a stricter version. A stricter passage ("at least 12 weeks") supports "12 weeks." A looser passage does not support a stronger claim.
- `partial` means you can point at the supported half and name the rest. "The trial enrolled adults" does not support "the trial enrolled 412 adults with type 2 diabetes" beyond the adult half.
- `unsupported` requires that admissible sources were checked. Skipping the check is `not_checked`, not `unsupported`.
- `contradicted` requires an admissible passage that states the opposite, not a passage that is silent.
- `not_checked` means no source was admitted (missing source, missing source id, inadmissible tier, empty passage, or document not found). Reason: `source not admitted`. It is outside the faithfulness denominator.
- `unverifiable` means an admitted source was checked and the passage can neither support nor refute the claim. It is not a refusal to admit a source.
- `out_of_scope` is for `normative` and `definitional` claims. Leave those counts out of the faithfulness denominator.

## Faithfulness percent

`(supported + 0.5 × partial) ÷ (supported + partial + unsupported + contradicted + unverifiable)`.

`not_checked` and `out_of_scope` are outside the denominator. If every claim is `not_checked`, faithfulness is `null` (never 0 or 100).

## Three numbers that must stay apart

| Number | What it measures | Where it is printed |
|---|---|---|
| Faithfulness percent | Status counts on the claims in this answer | One line under the reference list |
| Source score | The page: authority, recency, relevance, provenance, currency | Under that source's citation line |
| Rail F score | 0.50 verified facts + 0.25 cross-source consistency + 0.25 × (100 − hallucination risk) | The evidence rail, not this connector's card |

Do not average them. Do not label the source score "confidence."

## Open items

Open items are `partial`, `unsupported`, `contradicted`, and `unverifiable`. `not_checked` is listed separately (`summary.not_checked`) and is not an open item.


Restated 22 October 2026 from the Verify method (D2).
