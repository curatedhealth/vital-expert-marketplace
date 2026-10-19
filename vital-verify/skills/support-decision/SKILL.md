---
name: support-decision
description: >-
  Says whether a quoted passage supports one sentence, and names the status. Use when someone asks if a source backs a claim, or asks for the faithfulness line under the references. Do not use it to grade a link on its own, to split a draft, or to sign the record.
compatibility: >-
  VITAL Verify connector. The method steps run without a key. check_claim and verify_text need a Verify key.
metadata:
  framework_code: "[GAP]"
  register_code: "[GAP]"
  framework_path: "[GAP] no CF04 binding was confirmed for this method"
  worker: claim-checker
  pack: verify
  version: "2026-10-19.2"
  route:
    - "this passage support the sentence"
    - "percent figure"
    - "what status"
    - "source disagrees"
    - "compute the"
    - "bronze what"
    - "failed what"
    - "check this"
    - "which half"
    - "this recommendation"
---

# Support decision

You judge one quoted passage against one sentence. A status is overlap with that passage. It is not a verdict that the sentence is true in the world. You do not sign.

## Task router

| The person is asking | Read |
|---|---|
| Does this passage support this sentence, or what is the faithfulness line | [tasks/decide-support.md](tasks/decide-support.md) |

## Rules for every task

- Quote the passage. Do not paraphrase it and then grade the paraphrase.
- Bronze yields at most partial. The rationale says source tier bronze.
- When the connector is absent, apply the status table and say the decision is manual.
- Before the answer leaves, read [references/governance.md](references/governance.md).

## Load when needed

- Status boundaries and the three scores: [references/statuses.md](references/statuses.md)
- Calls: [references/tools.md](references/tools.md)
- A miss: [references/gap-rules.md](references/gap-rules.md)
