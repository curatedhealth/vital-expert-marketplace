---
name: claim-decomposition
description: >-
  Splits a draft into the sentences a reader could ask to see in a source, and keeps each sentence where it sat in the text. Use when someone pastes an answer, a paragraph, or a report and asks what can be checked. Do not use it to grade a link, to decide support, or to sign a record.
compatibility: >-
  VITAL Verify connector. The method steps run without a key. extract_claims need a Verify key.
metadata:
  framework_code: "[GAP]"
  register_code: "[GAP]"
  framework_path: "[GAP] no CF04 binding was confirmed for this method"
  worker: claim-checker
  pack: verify
  version: "2026-10-19.2"
  route:
    - "what in"
    - "answer into"
    - "list the"
    - "sentences are"
    - "pull out"
    - "mark the"
    - "the claims"
    - "this report"
    - "separate the"
    - "extract claims"
---

# Claim decomposition

You split text. You do not decide whether a sentence is true, and you do not sign.

## Task router

| The person is asking | Read |
|---|---|
| What in this text can be checked | [tasks/split-claims.md](tasks/split-claims.md) |

## Rules for every task

- Keep the person's wording. Do not merge two sentences into a smoother one.
- A sentence with no citation marker is still a claim.
- When the connector is absent, split on sentence boundaries and say the split is manual.
- Before the answer leaves, read [references/governance.md](references/governance.md).

## Load when needed

- Kinds and offsets: [references/claim-kinds.md](references/claim-kinds.md)
- Calls: [references/tools.md](references/tools.md)
- A miss: [references/gap-rules.md](references/gap-rules.md)
