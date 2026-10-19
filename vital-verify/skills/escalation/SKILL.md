---
name: escalation
description: >-
  Hands an open claim to a named person, with the passage and the question they have to answer. Use when a finding is partial, unsupported, or contradicted, when the only passage is bronze, or when two admissible sources disagree. Do not use it to decide the claim yourself or to file a signed record.
compatibility: >-
  VITAL Verify connector. The method steps run without a key. No write call. build_record is the record task, after the person decides. need a Verify key.
metadata:
  framework_code: "[GAP]"
  register_code: "[GAP]"
  framework_path: "[GAP] no CF04 binding was confirmed for this method"
  worker: clearance-officer
  pack: verify
  version: "2026-10-19.2"
  route:
    - "this finding"
    - "two sources"
    - "the only"
    - "is contradicted"
    - "the packet"
    - "failed ask"
    - "leave the"
    - "i need"
    - "unsupported claim"
    - "not clear"
---

# Escalation

You prepare the question. You do not answer it, and you do not sign.

## Task router

| The person is asking | Read |
|---|---|
| What does a person need to decide | [tasks/escalate-open-item.md](tasks/escalate-open-item.md) |

## Rules for every task

- The question does not contain the decision you prefer.
- A tool name is not a clearer.
- This task runs without a key. It writes no record.
- Before the packet leaves, read [references/governance.md](references/governance.md).

## Load when needed

- Packet fields: [references/packet.md](references/packet.md)
- Calls: [references/tools.md](references/tools.md)
- A miss: [references/gap-rules.md](references/gap-rules.md)
