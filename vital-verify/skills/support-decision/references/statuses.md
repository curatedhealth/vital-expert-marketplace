# Support decision reference

Code: `check_claim` in `mcps/verify/service.py`. Gold and silver passages go to the faithfulness scorer, which measures word overlap. Bronze never reaches that scorer.

## Boundaries

- `supported` means the passage states the claim or a stricter version. A stricter passage ("at least 12 weeks") supports "12 weeks." A looser passage does not support a stronger claim.
- `partial` means you can point at the supported half and name the rest. "The trial enrolled adults" does not support "the trial enrolled 412 adults with type 2 diabetes" beyond the adult half.
- `unsupported` requires that admissible sources were checked. Skipping the check is `unverifiable`, not `unsupported`.
- `contradicted` requires an admissible passage that states the opposite, not a passage that is silent.
- `unverifiable` is the refusal: missing source, missing source id, tier `inadmissible`, or an empty passage. It is not a statement that the claim is false.
- `out_of_scope` is for `normative` and `definitional` claims. Leave those counts out of the faithfulness denominator.

## Three numbers that must stay apart

| Number | What it measures | Where it is printed |
|---|---|---|
| Faithfulness percent | Status counts on the claims in this answer | One line under the reference list |
| Source score | The page: authority, recency, relevance, provenance, currency | Under that source's citation line |
| Rail F score | 0.50 verified facts + 0.25 cross-source consistency + 0.25 × (100 − hallucination risk) | The evidence rail, not this connector's card |

Do not average them. Do not label the source score "confidence."

## Open items

Open items are `partial`, `unsupported`, `contradicted`, and `unverifiable`. The card lists those counts and one recommendation. It does not include an evidence table unless the user asks.


Restated 19 October 2026 from the Verify method. No separate primary source was added.
