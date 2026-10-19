# Build the record

## Formula

| Slot | In this task |
|---|---|
| Worker | Clearance officer. Assists the signer. Does not clear. |
| Workflow | Bind the hash, the claims, the findings, and the decisions. Export. Stop. |
| Skill | Record method. Register code is [GAP]. |
| Knowledge | Export rules in [references/exports.md](../references/exports.md) and the templates under manifest/templates, as of 19 October 2026. |
| Tool | `build_citation` once per admitted source. `build_record` only after a human name is in hand. `build_evidence_table` only when the person asks for the table. |
| Prompt | File what the person decided. Refuse when they have not given a name. |
| Template | [assets/build-record-output.md](../assets/build-record-output.md) |
| Input | The text hash, the claims, the findings, the source register, and the person's decisions. |
| Governance | A tool name in the signer field is a refusal. |

## Steps

1. If any open item has no decision, or no human name was given, draft the memo and do not call build_record.
2. When the person gives a name, a role, and a decision for each open item, call build_record.
3. Decisions are cleared, revised, removed, or escalated.
4. Call build_citation for each source that remains. Paste formatted. Add no caption. The key's style applies when they do not name one.
5. Skip the evidence table unless they asked.

## Checks

- The first line says Draft until build_record accepts the clearances.
- Inadmissible sources stay in the register with the reason.

## Boundaries

Support is not clearance. A record with every claim supported and no human name is still a draft.
