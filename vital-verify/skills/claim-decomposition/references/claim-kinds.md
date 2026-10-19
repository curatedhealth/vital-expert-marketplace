# Claim kinds

Source: Verify claim-decomposition method, restated 19 October 2026 from the suite skill. No external primary was consulted for the kind list. [GAP] if a register definition differs.

# Claim decomposition reference

`extract_claims` returns claims. It does not return statuses.

## Kinds

| Kind | What the clause does | Default `checkable` |
|---|---|---|
| factual | States that something is the case | true |
| numeric | States a count, rate, date, or threshold | true |
| causal | States that one thing produced another | true |
| comparative | States that one thing is more, less, newer, or different | true |
| normative | States what should be done | false |
| definitional | States what a term means for this text | false |

A sentence can carry one kind. Prefer `numeric` over `factual` when a figure is the point of the sentence. Prefer `comparative` when the point is a difference.

## Offsets

Offsets are Python string indexes into the exact submitted text, including spaces. Do not offset into a cleaned copy. A claim whose offsets do not slice back to `text` is invalid.

## What is not a claim

A heading, a citation line produced by `build_citation`, and the faithfulness percent line are apparatus. Do not extract them as claims about the world.
