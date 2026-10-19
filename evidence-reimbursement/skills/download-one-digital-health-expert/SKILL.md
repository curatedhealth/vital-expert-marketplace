---
name: "Download one digital health expert"
description: "Only while the Digital Health Library connector is connected. Use only after the job Download a digital health expert is chosen and one expert slug is known, to download that expert. Call agent-pack.download_agent once."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Download one digital health expert

Job: Download a digital health expert.

Run this only when that job is already chosen and the buyer has named one slug from Find digital health experts.

Call only `agent-pack.download_agent` with that slug. This is one counted call on the library key.

Return the system prompt and the skill methods for the buyer's own assistant. A hosted tool named in the file is a Digital Health Library tool, called on the connector already connected. It does not need a second key. Do not download a team.
