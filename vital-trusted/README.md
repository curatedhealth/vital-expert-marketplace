# VITAL TRUSTED

Nineteen skills for people across a life-sciences company who use an AI assistant
for daily work: general management, brand, market access, medical and other teams.
TRUSTED supports the company's own SOPs and review processes. It never replaces them.

Status: version 0.2.1 on `curatedhealth/vital-expert-marketplace`. Not yet reviewed by
medical, legal or regulatory reviewers. Rules the skills could not trace to a dated
primary document are marked `[CHECK]` inside the skill files and are described, not
enforced. License terms are still to be set (`UNLICENSED` in plugin metadata).

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

Build skills make the work good by design. Prove skills carry the method behind the
VITAL Verify tools: fact checking, source quality, confidence, citation and record.

## Installing

In Cowork, add the marketplace `curatedhealth/vital-expert-marketplace` and install
**vital-trusted**. In other assistants that load Agent Skills, add the folders under
`skills/`. To try it, ask "what can TRUSTED do?" or start an everyday task such as a
board update.

## VITAL Verify

The connector is `https://mcp.vital.expert/api/mcp/verify` — the same host as the
`vital-verify` pack. Paste a `vvfy_` key when Cowork asks (optional). Do not add a
second Verify connector by hand, and do not install `vital-verify` only to get tools if
this pack is already installed.

Without a key, Prove skills still run by hand, label output "not tool-checked", and give
no confidence figure. With the key, they call the VERIFY tools on that host.

## Choosing letters

All seven letters are on by default. Ask "turn off Ethical" or "use only True and
Safe" to change this for a conversation.

## Inside each skill

`SKILL.md` (instructions), `tasks/` (one guide per task), `references/` (rules,
patterns, gap rules, governance, tools), `assets/` (output formats), `examples/`,
`evals/evals.json` (test requests) and `scripts/` (small helpers with their own tests).
`evals/suite-evals.json` at the plugin root holds cross-skill daily-user requests.
