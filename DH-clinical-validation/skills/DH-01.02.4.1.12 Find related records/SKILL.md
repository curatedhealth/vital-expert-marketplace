---
name: "DH-01.02.4.1.12 Find related records"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-01.02.4.1 is chosen, to do Find related records. Catalogue job evidence-table. Tool literature.find_related."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.4.1.12 Find related records

Worker: not bound.
Skill: CF-12.01.02.4.1.12 Find related records.
Prompt: not bound.
Template: not bound.
Tool: `literature.find_related`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the record already opened. A related hit the source does not return is a gap.

Catalogue job: `evidence-table`.

