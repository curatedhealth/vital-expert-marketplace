# Escalate one open item

## Formula

| Slot | In this task |
|---|---|
| Worker | Clearance officer, preparing the packet. Does not decide. |
| Workflow | Copy the claim, the status, the passage, and write one question. Stop. |
| Skill | Escalation. Register code is [GAP]. |
| Knowledge | Packet fields in [references/packet.md](../references/packet.md), from the Verify method as of 19 October 2026. |
| Tool | None. Do not call build_record. |
| Prompt | Ask the question the person can answer. Do not clear the claim. |
| Template | [assets/escalate-open-item-output.md](../assets/escalate-open-item-output.md) |
| Input | One finding that is partial, unsupported, contradicted, bronze-only, or a disagreement between two admissible sources. |
| Governance | Unverifiable is escalated only to ask which source to fetch. It is not escalated so someone can bless a guess. |

## Steps

1. Copy the claim in the wording from the split.
2. State the status and the tier.
3. Quote the passage and the locator. If there is no passage, say not covered.
4. Write one question.
5. Leave the signer blank.

## Checks

- The question can be answered without re-running the tools.
- The packet does not say cleared.

## Boundaries

Do not change the status while writing the packet.
