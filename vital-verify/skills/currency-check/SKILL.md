---
name: currency-check
description: >-
  Says whether a paper or catalogue document has been retracted, corrected, superseded, or withdrawn. Use when someone asks if a source is still in force before they rely on it. Do not use it to grade a page, to decide whether a sentence is supported, or to treat a bare web link as a literature check.
compatibility: >-
  VITAL Verify connector. The method steps run without a key. check_currency need a Verify key.
metadata:
  framework_code: "[GAP]"
  register_code: "[GAP]"
  framework_path: "[GAP] no CF04 binding was confirmed for this method"
  worker: source-qualifier
  pack: verify
  version: "2026-10-19.2"
  route:
    - "has this"
    - "doi still"
    - "guidance withdrawn"
    - "the currency"
    - "a press"
    - "this catalogue"
    - "record when"
    - "a correction"
    - "i treat"
    - "that the"
---

# Currency check

You ask whether a resolved source is still in force. You do not grade support, and you do not sign.

## Task router

| The person is asking | Read |
|---|---|
| Is this paper or document retracted, corrected, superseded, or withdrawn | [tasks/check-currency.md](tasks/check-currency.md) |

## Rules for every task

- A URL with no literature id is not checked. Say that. Do not call the page current.
- A retracted paper is out, except when the sentence is about the retraction.
- When the connector is absent, say the currency was not checked. Do not guess from the year.
- Before the answer leaves, read [references/governance.md](references/governance.md).

## Load when needed

- Notices: [references/notices.md](references/notices.md)
- Calls: [references/tools.md](references/tools.md)
- A miss: [references/gap-rules.md](references/gap-rules.md)
