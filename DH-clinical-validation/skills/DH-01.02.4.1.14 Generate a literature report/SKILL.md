---
name: "DH-01.02.4.1.14 Generate a literature report"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-01.02.4.1 is chosen, to do Generate a literature report. Catalogue job evidence-table. Tool literature.generate_report."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.4.1.14 Generate a literature report

Worker: not bound.
Skill: CF-12.01.02.4.1.14 Generate a literature report.
Prompt: not bound.
Template: not bound.
Tool: `literature.generate_report`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Render records this job already holds. Templates are only memo, identity, evidence, grade, and citation. An unknown template is a gap.

Catalogue job: `evidence-table`.

