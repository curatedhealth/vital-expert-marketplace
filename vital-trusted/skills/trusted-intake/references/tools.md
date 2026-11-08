# Companion slot

No companion exists for intake today. The method runs fully on what the person says and
what the request shows. Never describe a lookup that did not run (TR-H4).

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Work context | Read the approved label for the named market so product status is read, not asked (candidate: label source) | No companion yet | Status recorded as the person states it or as the supplied label shows; otherwise asked or left as a gap |
| Data and policy context | Read the company's AI use policy and approved-tool list so the data question becomes a lookup with a quoted passage (candidate: AI policy companion) | No companion yet | The policy question is asked; the answer is recorded as "person states", never as checked |

VERIFY does not fill an intake slot. It checks finished text against passages; it does
not read company policies or labels for status. [CHECK: owner to confirm VERIFY has no
intake role when the Prove skills are cross-checked.]

## Detecting a future companion

A companion is present only when its tools appear in the assistant's tool list. Do not
assume one because the person mentions it (`trusted-capability-map`,
`references/tools.md`).
