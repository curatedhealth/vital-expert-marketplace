# Claim decomposition examples

Submitted text:

> NICE recommended the treatment in 2024. Response rates were higher in the treated arm. Clinicians should discuss the label with patients.

| Claim | Kind | checkable | Notes |
|---|---|---|---|
| NICE recommended the treatment in 2024. | factual | true | Entity `NICE`. The year is part of the claim, not a separate claim, unless the year is the only thing a later sentence adds. |
| Response rates were higher in the treated arm. | comparative | true | No figure yet. Do not invent one. |
| Clinicians should discuss the label with patients. | normative | false | Later status `out_of_scope`. Leave it out of the faithfulness denominator. |

A sentence with no `[3]` is still extracted. The marker, when present, is copied into `cited_refs` and is not itself evidence.
