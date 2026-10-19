---
name: digital-endpoint-instrumentation
description: "Use only after the job Digital Endpoint Capture & RWE Platform Management is chosen, to do Digital Endpoint Instrumentation."
---

# Digital Endpoint Instrumentation

## Execution formula
Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 30 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.02.4.1.1 Digital Endpoint Instrumentation.
Prompt: PS-DH.01.02.4.1.1 Digital Endpoint Instrumentation.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Prompt

# Digital Endpoint Instrumentation — Prompt (PS05)

## Task
Draft the digital-endpoint instrumentation brief for {product} from measures the operator already named.

## Inputs
- Product, indication, and geography the operator already has.
- Decisions already taken in the parent suite `PS-DH.01.02.4`. Named owners if present.
- Do not invent a trial, coverage, price, class, or agency outcome.

## Output
A bounded instrumentation brief: endpoints already named; capture path; [GAP] missing sensors or sources. Do not invent a signal. Mark unresolved facts [GAP].

## Guardrails
No invented evidence, coverage, price, or agency outcome. [GAP] when inputs are missing. No off-label instruction. Do not invent a trial result, endpoint, or regulatory evidence claim. Protocol design stays on Clinical Study Design. Trial ops stay on Clinical Operations. Not a CF05 skill. Access AMCP stays on `PS-04.02`. Patient hubs stay on `PS-06.01`. Commercial Launch Excellence stays on `PS-04.01.04`.

## Template

## Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## Boundary

Use the endpoint and device the buyer named.
