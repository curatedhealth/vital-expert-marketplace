# Task VR-1.1 Split a text into checkable claims

Maps to TRUSTED Prove `claim-assessment` Part A.

## Formula

| Slot | In this task |
|---|---|
| Worker | Evidence lead (claim checker), in the splitting role. Does not grade and does not sign. |
| Workflow | Read once, emit one claim per checkable sentence or clause, then stop. |
| Skill | VR-1.1 Claim decomposition |
| Knowledge | `references/rules.md`, `references/claim-kinds.md`, `references/patterns.md` |
| Tool | VERIFY `extract_claims`; see companion slot |
| Prompt | List every sentence a reader could ask to see in a source. Keep the words. |
| Template | `assets/split-claims-output.md` |
| Input | The submitted text, unchanged. |
| Governance | Do not drop a number because it has no citation yet. Do not assign a support status. VR-H1, VR-H4, VR-H5 |

## Companion

| State | What to do |
|---|---|
| VERIFY connected | Call `extract_claims` on the submitted text. |
| VERIFY absent | Split on sentence boundaries; mark the method manual / not tool-checked. |

## Steps

1. Read the text once. Do not tidy it first.
2. Call `extract_claims` when a key is present; otherwise split manually.
3. For each claim set kind, checkable, entities, and cited markers as written.
4. Normative and definitional claims are checkable false. They are not failures.
5. Offsets must slice back to the exact submitted text.
6. Hand the list to `support-decision` for pairing and status. Do not decide support here.

## Checks

- Every checkable sentence appears once.
- No status word is attached.
- Offsets round-trip.

## Boundaries

Headings, a citation line from build_citation, and the faithfulness percent line are
apparatus. Do not extract them as claims about the world.
