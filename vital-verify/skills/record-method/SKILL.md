---
name: record-method
description: >-
  Files the check as a draft or as a record a named person cleared, and exports the memo and the source list. Use when someone asks to save, clear, or export the verification. Do not use it to grade a link, to decide a sentence, or to sign without the person's name.
compatibility: >-
  VITAL Verify connector. The method steps run without a key. build_record and build_citation need a Verify key.
metadata:
  framework_code: "[GAP]"
  register_code: "[GAP]"
  framework_path: "[GAP] no CF04 binding was confirmed for this method"
  worker: clearance-officer
  pack: verify
  version: "2026-10-19.2"
  route:
    - "save this"
    - "export the"
    - "i am"
    - "record has"
    - "source register"
    - "use my"
    - "i asked"
    - "not sign"
    - "every claim"
    - "line with"
---

# Record method

You bind what was checked to the person who decided. You never decide for them.

## Task router

| The person is asking | Read |
|---|---|
| Save, clear, or export | [tasks/build-record.md](tasks/build-record.md) |

## Rules for every task

- Zero decisions means a draft. The memo says so on the first line.
- The name is a person's name. It is not the connector and not the model.
- Citation lines are the formatted line, with no caption.
- Before anything is filed, read [references/governance.md](references/governance.md).

## Load when needed

- Exports: [references/exports.md](references/exports.md)
- Calls: [references/tools.md](references/tools.md)
- A miss: [references/gap-rules.md](references/gap-rules.md)
