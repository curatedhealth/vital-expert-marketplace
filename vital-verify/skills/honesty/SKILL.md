---
name: honesty
description: >-
  Takes numbers, names, quotations, and performance claims out of an answer when no quoted passage states them. Use when a draft sounds specific and the sources are silent, or when someone asks what must be cut before the answer is shown. Do not use it to grade a link, to compute a new score, or to restyle the prose.
compatibility: >-
  VITAL Verify connector. The method steps run without a key. No extra call. This task reads findings that check_claim already returned. need a Verify key.
metadata:
  framework_code: "[GAP]"
  register_code: "[GAP]"
  framework_path: "[GAP] no CF04 binding was confirmed for this method"
  worker: claim-checker
  pack: verify
  version: "2026-10-19.2"
  route:
    - "of this"
    - "experts say"
    - "source is"
    - "the soc"
    - "a quotation"
    - "draft ends"
    - "keep the"
    - "a plausible"
    - "sentences have"
    - "not let"
---

# Honesty

You delete what no finding supports. You do not add a score, and you do not sign.

## Task router

| The person is asking | Read |
|---|---|
| What must leave this draft | [tasks/drop-unsupported-detail.md](tasks/drop-unsupported-detail.md) |

## Rules for every task

- Empty is better than a specific-looking fabrication.
- An unnamed authority is not a source.
- The method runs with or without a key, because it reads findings already in hand.
- Before the answer leaves, read [references/governance.md](references/governance.md).

## Load when needed

- The drop list: [references/drop-list.md](references/drop-list.md)
- Which calls this task does not make: [references/tools.md](references/tools.md)
- A miss: [references/gap-rules.md](references/gap-rules.md)
