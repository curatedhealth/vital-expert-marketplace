---
name: generate-a-pathway-report
description: "Only while the Digital Health Library connector is connected. Use only after the job Regulatory Submission Preparation & Dossier Assembly Execution is chosen, to do Generate a pathway report."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Generate a pathway report

## Execution formula
Worker: not bound.
Skill: CF-12.03.03.4.1.5 Generate a pathway report.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.generate_report`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Ask for a 510(k), De Novo, or PMA number, or a product code. A missing predicate is a gap. UK PARD and swissdamed stay a gap.
