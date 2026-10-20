# Task VR-4.1 Build the record

## Formula

| Slot | In this task |
|---|---|
| Worker | Clearance officer. Assists the signer. Does not clear. |
| Workflow | Bind the hash, the claims, the findings, and the decisions. Export. Stop. |
| Skill | VR-4.1 Record method |
| Knowledge | `references/rules.md`, `references/exports.md`, `references/patterns.md` |
| Tool | `build_citation`, `build_record`, optional `build_evidence_table`; see companion |
| Prompt | File what the person decided. Refuse when they have not given a name. |
| Template | `assets/build-record-output.md` |
| Input | The text hash, the claims, the findings, the source register, and the person's decisions. |
| Governance | A tool name in the signer field is a refusal. VR-H4, VR-H5, VR-H11 |

## Companion

| State | What to do |
|---|---|
| VERIFY + human name + decisions | Call `build_record`; `build_citation` per remaining source. |
| Missing name or open decisions | Draft memo only; first line says Draft. |
| VERIFY absent | Draft method-only memo; label not tool-filed. |

## Steps

1. If any open item has no decision, or no human name was given, draft the memo and do not call build_record.
2. When the person gives a name, a role, and a decision for each open item, call build_record.
3. Decisions are cleared, revised, removed, or escalated.
4. Call build_citation for each source that remains. Paste formatted. Add no caption.
5. Skip the evidence table unless they asked.

## Checks

- The first line says Draft until build_record accepts the clearances.
- Inadmissible sources stay in the register with the reason.

## Boundaries

Support is not clearance.
