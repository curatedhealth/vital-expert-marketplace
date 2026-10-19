# Split a text into claims

## Formula

| Slot | In this task |
|---|---|
| Worker | Claim checker, in the splitting role. Does not grade and does not sign. |
| Workflow | Read once, emit one claim per checkable sentence or clause, then stop. |
| Skill | Claim decomposition. Register code is [GAP]. |
| Knowledge | Kinds and offset rules in [references/claim-kinds.md](../references/claim-kinds.md), from the Verify method as of 19 October 2026. |
| Tool | `extract_claims` on the submitted text. |
| Prompt | List every sentence a reader could ask to see in a source. Keep the words. |
| Template | [assets/split-claims-output.md](../assets/split-claims-output.md) |
| Input | The submitted text, unchanged. |
| Governance | Do not drop a number because it has no citation yet. Do not assign a support status. |

## Steps

1. Read the text once.
2. If a key is present, call `extract_claims`.
3. If it is not, split on sentence boundaries and mark the method manual.
4. For each claim set kind, checkable, entities, and cited markers as written.
5. Normative and definitional claims are checkable false. They are not failures.
6. Offsets must slice back to the exact submitted text.

## Checks

- Every checkable sentence appears once.
- No status word is attached.
- Offsets round-trip.

## Boundaries

Headings, a citation line from build_citation, and the faithfulness percent line are apparatus. Do not extract them as claims about the world.
