---
name: dh-03-03-4-1-regulatory-submission-preparation-dossier-assembly
description: "Only while the Digital Health Library connector is connected. Run one task in DH-03.03.4.1 Regulatory Submission Preparation & Dossier Assembly Execution. Use when the user asks for Clinical Evaluation Report Assembly, Submission Dossier Compilation, Agency Interaction Management, Retrieve guidance, Generate a pathway report. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.03.4.1 Regulatory Submission Preparation & Dossier Assembly Execution

Heading: DH-03.03.4 Submission Excellence.
Core: DH-03.03 Regulatory Strategy & Submissions.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-03.03.4.1.1 Clinical Evaluation Report Assembly

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 24 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.4.1.1 Clinical Evaluation Report Assembly.
Prompt: PS-DH.03.03.4.1.1 Clinical Evaluation Report Assembly.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Assemble the clinical evaluation report so the first pass does not bounce.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Clinical Evaluation Report Assembly. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## DH-03.03.4.1.2 Submission Dossier Compilation

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 20 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.4.1.2 Submission Dossier Compilation.
Prompt: PS-DH.03.03.4.1.2 Submission Dossier Compilation.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Compile the submission dossier for {product} from files the operator already has.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.03.03.4`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded dossier inventory: files already in hand; [GAP] missing pieces. Do not invent a CER finding or write the PCCP. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. FDA PCCP final guidance 4 December 2024 and GMLP. Do not invent a class, predicate, or agency outcome. PCCP stays on DH-03.03.1 AI/ML Regulatory. Class/predicate stay on DH-03.03.3 Regulatory Strategy. Leftover AI/ML Submission Assembly stays named, not gold. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## DH-03.03.4.1.3 Agency Interaction Management

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 20 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.4.1.3 Agency Interaction Management.
Prompt: PS-DH.03.03.4.1.3 Agency Interaction Management.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Plan agency interaction so questions, minutes, and follow-ups stay in one record.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Agency Interaction Management. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## DH-03.03.4.1.4 Retrieve guidance

Worker: not bound.
Skill: CF-12.03.03.4.1.4 Retrieve guidance.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.retrieve_guidance`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the question. These passages are stored guidance or ontology text. They are not register decisions. A passage with no source stays a gap.

## DH-03.03.4.1.5 Generate a pathway report

Worker: not bound.
Skill: CF-12.03.03.4.1.5 Generate a pathway report.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.generate_report`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for a 510(k), De Novo, or PMA number, or a product code. A missing predicate is a gap. UK PARD and swissdamed stay a gap.
