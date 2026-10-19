---
name: "DH-01.04 Data Science & AI/ML Download one digital health expert"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-01.04 Data Science & AI/ML Download a digital health expert is chosen, to download one expert file. One counted call."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.04 Data Science & AI/ML Download one digital health expert

Job: DH-01.04 Data Science & AI/ML Download a digital health expert.

Run this only when that job is already chosen and one expert slug is already chosen.

Call `agent-pack.download_agent` once. Do not call `agent-pack.download_team`. A hosted tool named in the downloaded file is a library tool on the same key.
