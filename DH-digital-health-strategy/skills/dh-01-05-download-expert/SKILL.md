---
name: dh-01-05-download-expert
description: "Only while the Digital Health Library connector is connected. Start the job DH-01.05 Digital Health Strategy & Vision Download a digital health expert. Use when the user wants an expert file, a system prompt, or a digital health agent pack for their own assistant."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.05 Digital Health Strategy & Vision Download a digital health expert

This job returns a file for the buyer's own assistant. It does not run the expert here.

Ask which one task to run, then follow that section.

- Find digital health experts. Skill `DH-01.05 Digital Health Strategy & Vision Find digital health experts`. agent-pack.list_experts. Not counted.
- Download one digital health expert. Skill `DH-01.05 Digital Health Strategy & Vision Download one digital health expert`. agent-pack.download_agent. One counted call.

A team of three to five experts is not in this pack. Do not call `agent-pack.download_team`.
