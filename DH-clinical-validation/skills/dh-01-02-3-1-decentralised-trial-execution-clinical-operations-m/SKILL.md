---
name: dh-01-02-3-1-decentralised-trial-execution-clinical-operations-m
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.02.3.1 Decentralised Trial Execution & Clinical Operations Management. Use when the user asks for Decentralised Trial Setup, Remote Data Capture Operations, Trial Data Integrity Management. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.3.1 Decentralised Trial Execution & Clinical Operations Management

Heading: DH-01.02.3 Clinical Operations.
Core: DH-01.02 Clinical Validation & Evidence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.02.3.1.1 Decentralised Trial Setup

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 11 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.3.1.1 Decentralised Trial Setup.
Prompt: PS-DH.01.02.3.1.1 DH-01.02.3.1.1 Decentralised Trial Setup.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

## DH-01.02.3.1.1 Decentralised Trial Setup

### Task
Draft the decentralized-trial setup brief for {product} from the protocol the operator already has.

### Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.02.3`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

### Output
A bounded ops brief: sites/remote paths already named; data-capture owners; [GAP] missing ops facts. Do not invent enrollment. Mark unresolved facts [GAP].

### Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a trial result, endpoint, or regulatory evidence claim. Protocol design stays on DH-01.02.1 Clinical Study Design. Digital endpoint capture stays on DH-01.02.4 Digital Evidence Generation. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Use the protocol and site plan the buyer supplied.


## DH-01.02.3.1.2 Remote Data Capture Operations

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 22 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.3.1.2 Remote Data Capture Operations.
Prompt: PS-DH.01.02.3.1.2 DH-01.02.3.1.2 Remote Data Capture Operations.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

## DH-01.02.3.1.2 Remote Data Capture Operations

### Task
Run remote data-capture operations for the digital-evidence study without silent data loss.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for DH-01.02.3.1.2 Remote Data Capture Operations. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Use the capture plan the buyer supplied.


## DH-01.02.3.1.3 Trial Data Integrity Management

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 23 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.3.1.3 Trial Data Integrity Management.
Prompt: PS-DH.01.02.3.1.3 DH-01.02.3.1.3 Trial Data Integrity Management.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

## DH-01.02.3.1.3 Trial Data Integrity Management

### Task
Keep trial data integrity from first capture through lock, with an audit trail.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for DH-01.02.3.1.3 Trial Data Integrity Management. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Check the data checks the buyer supplied.
