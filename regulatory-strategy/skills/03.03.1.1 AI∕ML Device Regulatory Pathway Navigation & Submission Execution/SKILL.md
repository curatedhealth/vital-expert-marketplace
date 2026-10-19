---
name: dh-03-03-1-1
description: "Only while the Digital Health Library connector is connected. Run one task in 03.03.1.1 AI/ML Device Regulatory Pathway Navigation & Submission Execution. Use when the user asks for AI/ML Pathway Selection, Predetermined Change Control Plan Authoring, AI/ML Submission Assembly. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# 03.03.1.1 AI/ML Device Regulatory Pathway Navigation & Submission Execution

Heading: 03.03.1 AI/ML Regulatory.
Core: DH-03.03 Regulatory Strategy & Submissions.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## 03.03.1.1.1 AI/ML Pathway Selection

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 18 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.1.1.1 AI/ML Pathway Selection.
Prompt: PS-DH.03.03.1.1.1 AI/ML Pathway Selection.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Select the AI/ML device pathway, including whether a Predetermined Change Control Plan is required.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for AI/ML Pathway Selection. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## 03.03.1.1.2 Predetermined Change Control Plan Authoring

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 14 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.1.1.2 Predetermined Change Control Plan Authoring.
Prompt: PS-DH.03.03.1.1.2 Predetermined Change Control Plan Authoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Author a Predetermined Change Control Plan for {product}'s AI-enabled device software function: Description of Modifications, Modification Protocol, and Impact Assessment.

### Inputs
- Product, intended use, and the AI-enabled device software function in scope.
- Pathway if named (510(k), De Novo, or PMA). Do not invent a pathway or a predicate.
- Planned modification types, data and retraining methods, and any performance or labeling facts the operator already has.

### Output
A bounded FDA PCCP draft: Description of Modifications (what may change, inside intended-use bounds); Modification Protocol (data, retraining, performance evaluation, update and labeling steps); Impact Assessment (safety and effectiveness of the listed changes). Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, performance, predicates, or authorization status. `[GAP]` when inputs are missing. Quality-system and cybersecurity work stay on `PS-DH.03.02`. EU MDR / AI Act stay on `PS-DH.03.03.2`. Generic class and predicate stay on `PS-DH.03.03.3`. Generic dossier and CER stay on `PS-DH.03.03.4`. Access AMCP stays on `PS-04.02`. Not a CF05 skill.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## 03.03.1.1.3 AI/ML Submission Assembly

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 18 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.1.1.3 AI/ML Submission Assembly.
Prompt: PS-DH.03.03.1.1.3 AI/ML Submission Assembly.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Assemble the AI/ML submission so the first pass does not bounce.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for AI/ML Submission Assembly. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.
