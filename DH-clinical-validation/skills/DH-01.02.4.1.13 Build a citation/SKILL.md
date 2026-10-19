---
name: "DH-01.02.4.1.13 Build a citation"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-01.02.4.1 is chosen, to do Build a citation. Catalogue job evidence-table. Tool literature.build_citation."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.4.1.13 Build a citation

Worker: not bound.
Skill: CF-12.01.02.4.1.13 Build a citation.
Prompt: not bound.
Template: not bound.
Tool: `literature.build_citation`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Build the citation for one record already in hand. Do not invent an identifier.

Catalogue job: `evidence-table`.

