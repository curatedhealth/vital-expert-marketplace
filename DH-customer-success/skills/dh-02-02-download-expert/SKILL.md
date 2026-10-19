---
name: dh-02-02-download-expert
description: "Only while the Digital Health Library connector is connected. Start the job DH-02.02 Customer Success & Implementation Download a digital health expert. Use when the user wants an expert file, a system prompt, or a digital health agent pack for their own assistant."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.02 Customer Success & Implementation Download a digital health expert

This job returns a file for the buyer's own assistant. It does not run the expert here.

Ask which one task to run, then follow that section.

- Find digital health experts. Skill `DH-02.02 Customer Success & Implementation Find digital health experts`. agent-pack.list_experts. Not counted.
- Download one digital health expert. Skill `DH-02.02 Customer Success & Implementation Download one digital health expert`. agent-pack.download_agent. One counted call.

A team of three to five experts is not in this pack. Do not call `agent-pack.download_team`.
