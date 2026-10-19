---
name: "DH-02.01.2.1.6 List commercial sources"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-02.01.2.1 is chosen, to do List commercial sources. Catalogue job competitor-landscape. Tool commercial-dh.list_commercial_dh_sources."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.2.1.6 List commercial sources

Worker: not bound.
Skill: CF-12.02.01.2.1.6 List commercial sources.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.list_commercial_dh_sources`. This call is not counted. Do not close it with Verify.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Free list of the diligence, regulatory, and market-access feeds this suite reads. Do not recount those feeds as new calls.

Catalogue job: `competitor-landscape`.

