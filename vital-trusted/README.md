# VITAL TRUSTED

Nineteen skills for people across a life-sciences company who use an AI assistant for daily work: general management, brand, market access, medical and other teams. TRUSTED supports the company's own SOPs and review processes. It never replaces them.

## Status

**Status:** Pilot → Pilot after VERIFY gates (version 0.3.0). Hybrid B + Standard upgrade, 8 November 2026. Not yet signed by a medical, legal or regulatory practitioner for customer Released. License terms are still to be set (`UNLICENSED` in plugin metadata; see LICENSE).

## Tier

**Tier:** Standard. Authored functional evals and known-answer cases ship with each skill. Full public back-tests are out of scope for this release.

## Known-answer status

Each skill carries authored `evals/known-answer/` cases with fixtures and expected behaviours. Functional `evals/evals.json` holds at least three cases per skill. Sealed suite material lives outside the install tree under `mcps/trusted/eval-kit/`.

## [CHECK] means

- **[CHECK]:** a rule, period or fact not traced to a registered passage that was quote-checked against a saved copy of its source, or a team-set default.
- **[GAP]:** a fact or source missing; never filled.

## Depends on

- `vital-core-atoms` (CF05 atoms bound where task cards name them).
- Optional: TRUSTED Prove live tools (MCP server id `trusted-prove`, URL `https://mcp.vital.expert/api/mcp/verify`) when a `vvfy_` key is pasted. Offline Prove path does not require it. The separate `vital-verify` plugin is **retired** — do not install it.

## Healthcare oversight (directory disclosure)

TRUSTED is high-risk healthcare-adjacent software. Outputs are decision support for trained life-sciences professionals. A named human must review claim-bearing work through the company's SOPs before anything leaves the team. The pack does not clear promotional, medical or regulatory materials.

## Offline-first Prove

Without a `vvfy_` key, Prove skills run with the plugin `tools/` suite and label every result **not tool-checked**. With a key pasted into this pack, they may call live Prove tools (fetch, admission, currency); citations still require human review.

## Not covered

| Work | Owner |
|---|---|
| Live URL/DOI fetch, retraction lookup, tenant document ingest, usage metering | TRUSTED Prove live MCP (optional key in this pack) |
| Medical, legal or regulatory sign-off | Named human reviewers |
| Company SOP text and approved labels | The customer's own systems |
| Extra agents, slash commands, automations | Deferred to factory re-cut |
| Separate `vital-verify` skill pack | **Retired** 8 November 2026 |

## The standard

| Letter | Need | The question it asks |
|---|---|---|
| T | Tangible | Is it useful to this reader, for this job? |
| R | Rule-compliant | Is it allowed, for this audience, in this market? |
| U | Unbiased | Is the evidence shown in proportion? |
| S | Safe | Could it lead to harm? |
| T | True | Is it correct, and can it be shown? |
| E | Ethical | Is AI being used responsibly for this work? |
| D | Defensible | Can the organization stand behind it? |

## The skills

| Code | Skill | Family | Letter |
|---|---|---|---|
| TR-0.1 | trusted-capability-map | Core | All |
| TR-0.2 | trusted-intake | Core | All |
| TR-0.3 | trusted-check | Core | All |
| TR-1.1 | substance-and-usefulness | Build | Tangible |
| TR-1.2 | fit-for-reader | Build | Tangible |
| TR-2.1 | claims-and-label | Build | Rule-compliant |
| TR-2.2 | market-rules-and-data | Build | Rule-compliant |
| TR-3.1 | balanced-evidence | Build | Unbiased |
| TR-3.2 | honest-framing | Build | Unbiased |
| TR-4.1 | patient-safety | Build | Safe |
| TR-5.1 | grounded-statements | Build | True |
| TR-5.2 | sourced-claims | Build | True |
| TR-6.1 | responsible-inputs | Build | Ethical |
| TR-6.2 | responsible-use | Build | Ethical |
| TR-7.1 | work-record | Build | Defensible |
| TR-8.1 | claim-assessment | Prove | True |
| TR-8.2 | source-assessment | Prove | True |
| TR-8.3 | confidence-scoring | Prove | True |
| TR-8.4 | citation-and-record | Prove | True and Defensible |

## Installing

In Cowork, add the marketplace and install **vital-trusted** only. Paste a `vvfy_` key into this pack only if you want live Prove tools. Do **not** install `vital-verify` (retired). Ask "what can TRUSTED do?" or start an everyday task such as a board update.

## What is in this plugin

| Part | Path | Role |
|---|---|---|
| Steward agent | `agents/trusted-steward-agent.md` | Map-first owner; evidence rules; human gates |
| Why this agent | `references/why-this-agent.md` | Rationale (anatomy R10) |
| Connectors | `connectors.md` | Offline tools + live Prove MCP use / never / cite |
| Offline tools | `tools/` | Deterministic Prove helpers |
| Capability map | `skills/trusted-capability-map/` | Missions and routing |
| Job skills | `skills/*/` | Full CF04 kits |

## Claims rule

No sentence states a rule, rate, period or number without a registered passage id, `[CHECK]` or `[GAP]`. Offline tool results are local and labeled not tool-checked; they are not a verdict that a sentence is true in the world.
