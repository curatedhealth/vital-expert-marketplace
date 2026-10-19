---
name: dh-04-01-2-1-ehr-integration-development-smart-on-fhir-deploymen
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.01.2.1 EHR Integration Development & SMART on FHIR Deployment. Use when the user asks for SMART app registration, Screen to FHIR interaction map, Sandbox launch proof. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.01.2.1 EHR Integration Development & SMART on FHIR Deployment

Heading: DH-04.01.2 EHR Integration Delivery.
Core: DH-04.01 Clinical Integration & Interoperability.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.01.2.1.1 SMART app registration

Worker: FHIR Integration Specialist (`fhir-integration-specialist`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.2.1.1 SMART app registration.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.2.1. The other skills under this competency do a different job.

### What it does
Register the app for the launch the EHR actually supports.

### Method
1. Choose EHR launch or standalone launch, and state which one the target EHR supports.
2. List the scopes (patient, user, system) the screens need, and drop scopes no screen uses.
3. Record the client id, redirect URI, and launch endpoint for that EHR.

### Do not
Do not request system/*.read when the app launches as a user in a patient chart.

### Output
A registration note for one named EHR: launch type, scopes, endpoints.

A missing fact stays [GAP].

## DH-04.01.2.1.2 Screen to FHIR interaction map

Worker: FHIR Integration Specialist (`fhir-integration-specialist`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.2.1.2 Screen to FHIR interaction map.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.2.1. The other skills under this competency do a different job.

### What it does
Tie each product screen to the FHIR call it makes and whether it writes back.

### Method
1. List the screens that read or write clinical data.
2. For each screen, name the resource, the interaction, and whether a write returns to the chart.
3. Mark a screen that has no FHIR call as local-only, so it is not described as integrated.

### Do not
Do not claim write-back for a screen that only displays a read.

### Output
A screen map: screen, resource, interaction, write-back yes or no.

A missing fact stays [GAP].

## DH-04.01.2.1.3 Sandbox launch proof

Worker: FHIR Integration Specialist (`fhir-integration-specialist`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.2.1.3 Sandbox launch proof.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.2.1. The other skills under this competency do a different job.

### What it does
Launch the app in a named sandbox and record what the token actually contained.

### Method
1. Launch as a test user into a test patient and a test encounter.
2. Record whether the token carried patient, encounter, and fhirUser.
3. If a context field is missing, record the EHR, the scope requested, and the field that was empty.

### Do not
Do not treat a successful login page as a successful SMART launch.

### Output
A launch log: sandbox, user, patient, context fields present, context fields missing.

A missing fact stays [GAP].
