---
name: dh-01-07-find-experts
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-01.07 Health Economics & Value Demonstration Download a digital health expert is chosen, to find experts. Call agent-pack.list_experts with a department or a query. This call is free."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.07 Health Economics & Value Demonstration Find digital health experts

Job: DH-01.07 Health Economics & Value Demonstration Download a digital health expert.

Run this only when that job is already chosen.

Ask for a department or a name. The jobs in this pack are owned by Digital Health Access & Reimbursement Lead. Call only `agent-pack.list_experts` with `function` or `query`. An empty call returns no roster. This call is not counted.

Show the slug, the display name, and the remit. Ask which one expert to download.
