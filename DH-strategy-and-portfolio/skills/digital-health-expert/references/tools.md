# Tools: measured behavior (19 October 2026)

All calls below were made live on 19 October 2026. Keys were never printed. Trimmed outputs are in `examples/live/`.

## Two connectors carry the expert tools

| Connector | Tools | Notes |
|---|---|---|
| VITAL Digital Health Library (mcp.vital.expert library) | `agent-pack.list_experts`, `agent-pack.download_agent` | No team download on this connector. |
| VITAL agent-pack | `list_experts`, `download_agent`, `download_team`, `my_usage` | Server instructions: "download_team is 3 to 5 experts and exists only on a team key." |

Both `list_experts` and both `download_agent` returned the same structure.

## list_experts

Arguments: `function` (department slug), `query` (matched against slug, name, remit), `limit` 1 to 50, default 25.

| Call | Result |
|---|---|
| no arguments | `experts: []`, `needs_filter: true`, message "Pass function or query. A full-workforce key does not receive the catalogue in one call." |
| `function: "digital-regulatory-evidence"`, `limit: 50` | 11 experts, all department "Digital Regulatory & Evidence": real-world-evidence-director-digital, cybersecurity-architect-digital-health, quality-assurance-manager-software, quality-systems-director-software, samd-regulatory-affairs-director, digital-health-consultant, regulatory-submission-manager-samd, digital-health-evidence-regulatory-director, head-digital-therapeutics, software-test-engineer-samd, regulatory-intelligence-analyst-digital |
| `query: "regulatory"`, `limit: 10` | `matched: 15`, `returned: 10`, `truncated: true`; includes experts from Digital Product and Digital Health Leadership |
| `query: "quality"`, `limit: 10` | 10 experts, including data-engineering-manager-health and service-design-director (the word appears in their remit) |
| `query: "quality-systems"`, `limit: 5` (agent-pack connector) | 1 expert: quality-systems-director-software |

Each row: `slug`, `display_name`, `description` (cut at about 280 characters, sometimes mid-word), `department` (display name, not slug). Every response carries the note: "Files for the buyer model. VITAL does not answer. A hosted tool named in the file is a Digital Health Library tool. Call it on the library connector the buyer already connected. It does not need a second key."

Department slugs: only `digital-regulatory-evidence` was measured. Department display names seen in results: Digital Regulatory & Evidence, Digital Product, Digital Health Leadership, Data & Interoperability, AI/ML & Data Science. The tool description gives `digital-commercial` as an example slug. Other slugs are [GAP]; use `query` when unsure.

Pitfalls: word queries match the remit text, so filter by department first; read `truncated`; the remit is cut.

## download_agent

Argument: `expert` (slug). Measured on `samd-regulatory-affairs-director` (library connector) and `quality-systems-director-software` (agent-pack connector).

Top-level fields: `pack: "agent"`, `version: "2026-10-16"`, `run_on: "buyer_model"`, `install`, `agent` {slug, display_name, description, function, department, system_prompt}, `skills` [{code, name, body_md}], `skill_count`, `skills_capped`, `tools` [{tool_id, name, description, and for some: hosted_product, how_to_call}], `does_not_include`, `note`.

| Field | samd-regulatory-affairs-director | quality-systems-director-software |
|---|---|---|
| Response size | 65,961 characters | 76,920 characters |
| System prompt | 5,287 characters | 5,885 characters |
| Skills | 49 (`skills_capped: false`) | 67 |
| Skill families | CF-12.03.03 (24), CF-12.01.02 (18), CF-12.03.02 (6), CF-EV-05 (1) | CF-12.03.02 (24), CF-12.03.03 (24), CF-12.01.02 (18), CF-EV-05 (1) |
| Tools | 32 | 32 (same list) |
| `does_not_include` | corpus, runners, memory, model, tool implementations | same |

`install` text (verbatim): "Load agent.system_prompt as the assistant instructions. Load each skills entry as its own skill file. tools lists hosted VITAL connectors by name. They do nothing until the buyer connects that connector with its own key. This pack does not run on a VITAL model."

Tools: of 32, 7 name `hosted_product: literature`, 4 `regulatory-dh`, 1 `regulatory`, and 20 carry no hosted product and no `how_to_call`. Each hosted entry says "Connect the VITAL <product> MCP with its own key. Do not copy this tool into the pack." This conflicts with the `note` ("does not need a second key").

Pitfall: the response is too large to paste into most chat windows; save it as a file.

## download_team (agent-pack connector only)

Argument: `experts`, three to five slugs. Measured with samd-regulatory-affairs-director, quality-systems-director-software, regulatory-submission-manager-samd.

Result: 214,786 characters. Top level: `pack: "team"`, `version: "2026-10-16"`, `run_on: "buyer_model"`, `method`, `agents` (each a full single-expert download), `agent_count: 3`, `does_not_include`, `note`. The SaMD director's prompt in the team file is identical to its single download. All three agents carry the same 32 tools.

`method` (verbatim): "Seat each packed agent separately. Give each agent only its own system prompt and skills. Ask the same question. Keep each answer, including disagreement. Then write one synthesis that does not erase a minority position. This is not a VITAL Panel. VITAL Panel is the workforce connector ask_team."

The call succeeded on the agent-pack key used in this build (plan `pack_monthly`). A refusal on another key was not observed; its wording is [GAP].

## my_usage (agent-pack connector, free)

Returns `callsThisMonth`, `monthlyCallCap`, `remaining`, `plan`, and a key label. Before the build's agent-pack calls: 4 of 500. After one list_experts, one download_team and one download_agent: 6. That fits list being free and each download counting once; it was measured once, on one key.
