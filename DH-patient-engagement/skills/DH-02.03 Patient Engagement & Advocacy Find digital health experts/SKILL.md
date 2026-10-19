---
name: "DH-02.03 Patient Engagement & Advocacy Find digital health experts"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-02.03 Patient Engagement & Advocacy Download a digital health expert is chosen, to find experts. Call agent-pack.list_experts with a department or a query. This call is free."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.03 Patient Engagement & Advocacy Find digital health experts

Job: DH-02.03 Patient Engagement & Advocacy Download a digital health expert.

Run this only when that job is already chosen.

Ask for a department or a name. The jobs in this pack are owned by Patient Experience Designer. Call only `agent-pack.list_experts` with `function` or `query`. An empty call returns no roster. This call is not counted.

Show the slug, the display name, and the remit. Ask which one expert to download.
