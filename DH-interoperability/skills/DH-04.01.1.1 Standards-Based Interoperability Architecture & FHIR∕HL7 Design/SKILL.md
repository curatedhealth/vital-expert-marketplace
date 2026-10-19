---
name: "DH-04.01.1.1 Standards-Based Interoperability Architecture & FHIR/HL7 Design"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.01.1.1 Standards-Based Interoperability Architecture & FHIR/HL7 Design. Use when the user asks for Implementation guide selection, Exchange pattern design, Conformance gap record. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.01.1.1 Standards-Based Interoperability Architecture & FHIR/HL7 Design

Heading: DH-04.01.1 Interoperability Architecture.
Core: DH-04.01 Clinical Integration & Interoperability.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.01.1.1.1 Implementation guide selection

Worker: FHIR Integration Specialist (`fhir-integration-specialist`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.1.1.1 Implementation guide selection.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.1.1. The other skills under this competency do a different job.

### What it does
Choose the FHIR implementation guide this exchange will conform to, and name what the guide does not cover.

### Method
1. Name the exchange (who sends, who receives, and the clinical purpose).
2. Select one base guide (US Core, IPS, or a national IG) and list the profiles this exchange will use.
3. Write the elements the guide leaves open, and mark each one as a local profile or as out of scope.

### Do not
Do not invent a profile for an element the chosen guide already constrains.

### Output
A one-page guide choice: guide name and version, profiles in use, and elements left open.

A missing fact stays [GAP].

## DH-04.01.1.1.2 Exchange pattern design

Worker: FHIR Integration Specialist (`fhir-integration-specialist`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.1.1.2 Exchange pattern design.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.1.1. The other skills under this competency do a different job.

### What it does
Decide how the two systems exchange those profiles: query, subscription, or bulk.

### Method
1. For each profile, state whether the receiver queries, subscribes, or takes a bulk export.
2. Name the FHIR interaction (search, read, $export, Subscription) and the authorization scope it needs.
3. Reject a second pattern for the same profile unless the first pattern cannot carry a named element.

### Do not
Do not specify REST, messaging, and bulk for the same payload.

### Output
A pattern table: profile, interaction, scope, and why the other patterns were set aside.

A missing fact stays [GAP].

## DH-04.01.1.1.3 Conformance gap record

Worker: FHIR Integration Specialist (`fhir-integration-specialist`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.1.1.3 Conformance gap record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.1.1. The other skills under this competency do a different job.

### What it does
Compare the current payloads to the chosen guide and record each miss.

### Method
1. Take one real or sandbox payload per profile.
2. Check must-support elements, cardinality, and terminology bindings.
3. Record each miss as the element path, the rule, and whether it blocks go-live.

### Do not
Do not mark a payload conformant because it is valid JSON.

### Output
A gap list tied to the guide version. An empty list is allowed only after every must-support element was checked.

A missing fact stays [GAP].
