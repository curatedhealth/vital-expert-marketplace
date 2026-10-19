---
name: "DH Diligence Read company changes"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH Diligence Watch companies is chosen, to do Read company changes. Catalogue job market-screen. Tool diligence-dh.get_deltas."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence Read company changes

Worker: not bound.
Skill: not a CF-12 row. Library tool `diligence-dh.get_deltas`.
Prompt: not bound.
Template: not bound.
Tool: `diligence-dh.get_deltas`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

What the store recorded for the watch since a date. State when the watch has no later sweep. Do not invent an event.

Catalogue job: `market-screen`.

