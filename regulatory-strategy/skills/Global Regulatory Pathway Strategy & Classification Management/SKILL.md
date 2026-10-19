---
name: global-regulatory-pathway-strategy-and-classification-management
description: "Only while the Digital Health Library connector is connected. Start the job Global Regulatory Pathway Strategy & Classification Management in Regulatory Strategy & Submissions. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Global Regulatory Pathway Strategy & Classification Management

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- SaMD Risk Classification. Skill `samd-risk-classification`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 31 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.3.1.1 SaMD Risk Classification. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Regulatory Pathway Selection. Skill `regulatory-pathway-selection`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 29 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.3.1.2 Regulatory Pathway Selection. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Intended-Use Definition. Skill `intended-use-definition`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 29 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.3.1.3 Intended-Use Definition. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Classify a product. Skill `classify-a-product`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `regulatory-dh.classify_product`.
- Read pathway precedents. Skill `read-pathway-precedents`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `regulatory-dh.get_pathway_precedents`.
- Find predicates. Skill `find-predicates`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `regulatory-dh.find_predicates`.

- Search devices. Skill `search-devices`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `regulatory-dh.search_devices`.
- Open an authorization. Skill `open-an-authorization`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `regulatory-dh.get_authorization`.
- Compare authorizations. Skill `compare-authorizations`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `regulatory-dh.compare_authorizations`.
- Read market status. Skill `read-market-status`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `regulatory-dh.get_market_status`.
Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
