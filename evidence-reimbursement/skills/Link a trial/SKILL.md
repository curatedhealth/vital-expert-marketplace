---
name: "Link a trial"
description: "Only while the Digital Health Library connector is connected. Use only after the job Digital Endpoint Capture & RWE Platform Management is chosen, to do Link a trial."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Link a trial

## Execution formula
Worker: not bound.
Skill: CF-12.01.02.4.1.6 Link a trial.
Prompt: not bound.
Template: not bound.
Tool: `literature.find_trial`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Link a registry entry for the study already opened.
