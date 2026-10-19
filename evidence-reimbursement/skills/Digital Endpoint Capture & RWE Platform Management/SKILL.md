---
name: digital-endpoint-capture-and-rwe-platform-management
description: "Only while the Digital Health Library connector is connected. Start the job Digital Endpoint Capture & RWE Platform Management in Clinical Validation & Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Digital Endpoint Capture & RWE Platform Management

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Digital Endpoint Instrumentation. Skill `digital-endpoint-instrumentation`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 30 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.4.1.1 Digital Endpoint Instrumentation. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- RWE Data Pipeline Management. Skill `rwe-data-pipeline-management`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 32 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.4.1.2 RWE Data Pipeline Management. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Signal Detection Analysis. Skill `signal-detection-analysis`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 30 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.4.1.3 Signal Detection Analysis. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Search literature. Skill `search-literature`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.search_literature`.
- Open a literature record. Skill `open-a-literature-record`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.get_record`.
- Link a trial. Skill `link-a-trial`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.find_trial`.
- Grade evidence. Skill `grade-evidence`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.grade_evidence`.
- Check a retraction. Skill `check-a-retraction`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.check_retraction`.
- Build an evidence table. Skill `build-an-evidence-table`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.build_evidence_table`.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
