---
name: "DH-01.02.4.1.11 Classify a study"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-01.02.4.1 is chosen, to do Classify a study. Catalogue job evidence-table. Tool literature.classify_study."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.4.1.11 Classify a study

Worker: not bound.
Skill: CF-12.01.02.4.1.11 Classify a study.
Prompt: not bound.
Template: not bound.
Tool: `literature.classify_study`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Classify a study the opened record already names. Do not invent a design the record does not support.

Catalogue job: `evidence-table`.

