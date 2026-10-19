---
name: digital-health-expert
description: >
  Find and download a VITAL Digital Health expert (a ready-made role such as the SaMD
  Regulatory Affairs Director, the Quality & Software Lifecycle Director or the Regulatory
  Submission Manager) to run on the person's own assistant. Use it whenever
  someone asks "can I get this expert on my own assistant", "download the regulatory
  expert", "which digital health experts are there", "give me the system prompt for the
  quality director", "I want an agent pack", "set up a team of three experts", or wants a
  VITAL role inside ChatGPT, Gemini, Copilot or Claude. It finds the right expert by
  department or query, downloads one, explains what the file contains and what it does
  not, how to install it, what to check before trusting it, and when a team download needs
  a team key. Shared by every Digital Health pack. Not for running the expert here, not
  for getting regulatory, quality or access answers (use the pack's competency skills),
  and not a VITAL Panel.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Needs the VITAL Digital Health Library connector (mcp.vital.expert) for agent-pack
  list_experts and download_agent. Team downloads need the VITAL agent-pack connector
  with a key that allows download_team.
metadata:
  framework_code: "shared"
  register_code: "agent-pack"
  framework_path: "All Digital Health cores > expert download"
  pack: "shared by all dh-* packs"
  version: "0.1.0-draft"
  replaces: "Find digital health experts; Download one digital health expert; Download a digital health expert (one copy per pack, 3 skills x every dh-* pack)"
---

# Digital Health expert: find, download, install, check

This skill hands the person a file for their own assistant. It does not run the expert here, and it does not answer the expert's questions. Every Digital Health pack shares this one skill; it replaces the three expert shims each pack used to carry.

## What a download is

A download is one VITAL expert as files, built to run on the person's own model. Measured on 19 October 2026 (see [references/tools.md](references/tools.md)), a download contains:

- **A system prompt**: the role, its mandate, what it never does, its stop rules, its evidence rules.
- **Skill methods**: one entry per bound skill (49 for the SaMD Regulatory Affairs Director, 67 for the Quality & Software Lifecycle Director), each a short method in Markdown.
- **A list of hosted tool names**: VITAL connector tools the expert expects. Names only; they do nothing until the matching connector is connected.

The file states that it does **not** include: the corpus, runners, memory, the model, or tool implementations. Say this plainly. The person gets the role and the methods, not VITAL's knowledge base, not a running agent, and not the tools themselves.

## Pick the step

| Step | What it does | Call |
|---|---|---|
| 1 Find | Shortlist experts by department or query | `agent-pack.list_experts` |
| 2 Download one | Get one expert's file | `agent-pack.download_agent` |
| 3 Check | Look for the known defects before installing | read the file; optional `scripts/check_expert_file.py` |
| 4 Install | Load it on the person's assistant | no call |
| Team (optional) | Three to five experts with a seating method | `download_team` on the agent-pack connector |

### 1 Find

Ask what the expert is for: a department, a job, or a name. Then call `agent-pack.list_experts` with `function` (a department slug, for example `digital-regulatory-evidence`) or `query` (a word matched against slug, name and remit), and `limit` up to 50. An empty call returns no roster: the connector answers `needs_filter: true`. Pitfalls, measured:

- A word query matches anywhere in the remit. `query: "quality"` returned a Data Engineering Manager and a Service Design Director next to the quality experts. Prefer `function`, then narrow.
- Results stop at `limit` (default 25); `truncated: true` means there are more. `query: "regulatory"` matched 15 and returned 10 at `limit: 10`.
- The remit text is cut at about 280 characters, sometimes mid-word. Do not read meaning into the cut end.

Show slug, display name, department, and the remit as returned. If the pack's competency skill names a worker (for example `samd-regulatory-affairs-director` for the Regulatory pack), put that one first and say why. Ask which one expert to download. Do not pick for the person when two fit; say what separates them using only the remit text.

### 2 Download one

Call `agent-pack.download_agent` with `expert` set to the chosen slug. One call per expert. The file is large (about 66,000 to 77,000 characters for the two measured), so tell the person to save it as a file rather than paste it into a chat window. Never print or repeat a connector key.

On the vital-agent-pack connector, the usage counter rose by two across one list, one single download and one team download (`my_usage`, 19 October 2026), which fits listing being free and each download counting once. Treat that as measured on one key, not as a price.

### 3 Check before installing (known defects)

Warn the person before they install. Register item C15 records that the downloadable expert prompts leak internal plumbing and list unrelated tools; the 19 October 2026 downloads still show it. Full list and what to do in [references/known-defects.md](references/known-defects.md). After every download, check:

1. **Plumbing lines in the prompt.** Search for "trust the foreign key", "de21_function_id", "[GAP] (", "None (WP", and archetype codes like "AL03-PLN". These are internal fields, not instructions for the person's assistant. The person decides whether to delete them; recommend deleting.
2. **Tools that do not belong.** Each measured expert listed the same 32 tools, including UniProt, ChEMBL, PubChem, MyVariant and Open Targets. 20 of 32 carry no hosted product and no call route. Keep only the tools the person has connected and that fit the role.
3. **Counts that disagree.** The regulatory director's prompt says "Bound competencies (8)" and lists six; every measured prompt says 24 tools while the file lists 32.
4. **Role and skills that do not match.** The Quality & Software Lifecycle Director's prompt names six bound competencies, all regulatory or study-design ones, while its remit is QMS design and its file carries 24 quality skills. Check that the skills match the job the person needs.
5. **Thin skill entries.** 24 skill entries in each measured file have an empty Prompt or Template section or say "Prompt: not bound"; pass-rule and miss-owner entries hold only a header. Several reference the template code `ST05-PHARMA-DH-OVERLAY` (register C16).
6. **Key wording that conflicts.** Tool entries say "Connect the VITAL ... MCP with its own key"; the file's note says a hosted tool runs on the library connector already connected and "does not need a second key". Tell the person to try the library connector they already have first, and to ask VITAL before buying another key.
7. **The escalation line.** The prompt names one escalation peer from VITAL's graph and an owner role. Replace both with the person's own accountable owner. If no owner is named, write "owner not named" and ask; never suggest a job title.

If code execution is available, run `scripts/check_expert_file.py <file> --connected <hosted products the person has>` on the saved download; it prints these findings. Worked output: [examples/check_samd-regulatory-affairs-director.txt](examples/check_samd-regulatory-affairs-director.txt).

### 4 Install

Follow the file's own `install` field: load `agent.system_prompt` as the assistant's standing instructions; load each `skills` entry as its own skill file; treat `tools` as names that do nothing until the person connects that connector. In practice:

- Put the cleaned system prompt where the assistant keeps standing instructions (a project's or custom assistant's instructions field).
- Where the assistant supports Agent Skills, make each skill entry its own skill file; otherwise attach them as reference files.
- Connect the Digital Health Library connector so the hosted tool names resolve. A tool with no hosted product cannot be called through VITAL.
- Keep the prompt's stop rules and "advisory drafts only" lines. They are the expert's governance, and they are why its output still needs a named human to clear it.

### Team downloads

A team is three to five experts, each with its own prompt and skills, plus a seating method: seat each expert separately, ask the same question, keep each answer including disagreement, then write one synthesis that does not erase a minority position. The file says it is not a VITAL Panel.

`download_team` is not on the Digital Health Library connector. It is on the VITAL agent-pack connector, and its instructions say it exists only on a team key. On 19 October 2026 it ran on the agent-pack key used in this build and returned three experts (about 215,000 characters). If the person's key refuses, say a team download needs a team key and offer single downloads instead. Check each expert in the team with step 3.

## Boundaries

- Do not run the expert here or answer as the expert. Route domain questions to the pack's competency skills (for example `regulatory-strategy-capability-map`, `quality-management-capability-map`).
- Do not describe a hosted tool as included in the file.
- Do not edit the file for the person without saying what changed; cleaning the prompt is their decision.
- The downloaded expert produces advisory drafts. Its output is not a regulatory, quality or reimbursement decision, and a named human clears any record.
- AI disclosure: anything the downloaded expert produces for others must be identifiable as AI-produced; its own prompt says so.

## Output

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Answer first (the shortlist, or "downloaded: <name>, saved as a file"), then what is and is not in it, then the check list, then install steps.

## Files in this skill

- `references/tools.md` measured behavior of list_experts, download_agent, download_team and my_usage.
- `references/known-defects.md` the defects observed in downloads, mapped to register items, with what the person should do.
- `scripts/check_expert_file.py` checks a saved download for the known defects.
- `examples/live/` trimmed live outputs from 19 October 2026 (list_experts, two single downloads, one team download).
- `examples/check_samd-regulatory-affairs-director.txt`, `examples/check_team_three.txt` checker output on those downloads.
- `evals/evals.json`, `evals/prompts_only.json` tests, including one request to decline.
