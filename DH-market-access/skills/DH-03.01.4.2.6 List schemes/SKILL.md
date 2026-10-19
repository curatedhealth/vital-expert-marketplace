---
name: "DH-03.01.4.2.6 List schemes"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-03.01.4.2 is chosen, to do List schemes. Catalogue job scheme-precedents. Tool market-access-dh.list_schemes."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.01.4.2.6 List schemes

Worker: not bound.
Skill: CF-12.03.01.4.2.6 List schemes.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.list_schemes`. This call is not counted. Do not close it with Verify.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

List schemes the connector serves. This call is free. An empty scheme stays empty.

Catalogue job: `scheme-precedents`.

