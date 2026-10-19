---
name: "DH-01.02.4.1 Digital Endpoint Capture & RWE Platform Management"
description: "Only while the Digital Health Library connector is connected. Start the job DH-01.02.4.1 Digital Endpoint Capture & RWE Platform Management in DH-01.02 Clinical Validation & Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.4.1 Digital Endpoint Capture & RWE Platform Management

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- DH-01.02.4.1.1 Digital Endpoint Instrumentation. Skill `digital-endpoint-instrumentation`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 30 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.4.1.1 DH-01.02.4.1.1 Digital Endpoint Instrumentation. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- DH-01.02.4.1.2 RWE Data Pipeline Management. Skill `rwe-data-pipeline-management`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 32 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.4.1.2 DH-01.02.4.1.2 RWE Data Pipeline Management. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- DH-01.02.4.1.3 Signal Detection Analysis. Skill `signal-detection-analysis`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 30 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.4.1.3 DH-01.02.4.1.3 Signal Detection Analysis. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- DH-01.02.4.1.4 Search literature. Skill `search-literature`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.search_literature`.
- DH-01.02.4.1.5 Open a literature record. Skill `open-a-literature-record`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.get_record`.
- DH-01.02.4.1.6 Link a trial. Skill `link-a-trial`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.find_trial`.
- DH-01.02.4.1.7 Grade evidence. Skill `grade-evidence`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.grade_evidence`.
- DH-01.02.4.1.8 Check a retraction. Skill `check-a-retraction`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.check_retraction`.
- DH-01.02.4.1.9 Build an evidence table. Skill `build-an-evidence-table`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.build_evidence_table`.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
