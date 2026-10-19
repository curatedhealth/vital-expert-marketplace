---
name: download-a-digital-health-expert
description: "Only while the Digital Health Library connector is connected. Start the job Download a digital health expert. Use when the user wants an expert file, a system prompt, or a digital health agent pack for their own assistant."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Download a digital health expert

This job returns a file for the buyer's own assistant. It does not run the expert here.

Ask which one task to run, then load that task skill.

- Find digital health experts. Skill `find-digital-health-experts`. agent-pack.list_experts. Not counted.
- Download one digital health expert. Skill `download-one-digital-health-expert`. agent-pack.download_agent. One counted call.

A team of three to five experts is not in this pack. Do not call `agent-pack.download_team`.
