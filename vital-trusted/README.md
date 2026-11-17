# Vital TRUSTED

Nineteen skills for people across a life-sciences company who use an AI assistant
for daily work: general management, brand, market access, medical and other teams.
TRUSTED supports the company's own SOPs and review processes. It never replaces them.

**Product of Crossroads Catalyst GmbH (Vital Expert).**  
**Status:** version **0.3.11** · `release_state: Pilot` (demoted 9 November 2026; do not install for new work until owner publishes 0.3.3).  
**License:** Proprietary — see `LICENSE` (`LicenseRef-CrossroadsCatalyst-Proprietary`).

Outputs remain uncleared drafts until a named human clears them under your process.
`[CHECK]` markers inside skill standards still mean "confirm against the primary PDF
before treating as settled doctrine."

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

Build skills make the work good by design. Prove skills carry claim/source/confidence/
citation method and label results **not tool-checked**.

Deterministic offline checks ship as **data + instructions** (`references/check-rules.json`
plus `references/tools.md`, and shared `templates/offline-checks/`), not as Python programs.
This directory build has no remote MCP connector.

## Installing (Claude Cowork)

1. Add marketplace: `curatedhealth/vital-expert-marketplace`
2. Install: `/plugin install vital-trusted@vital-expert-marketplace`

Do **not** install retired `vital-verify`. Ask "what can TRUSTED do?" or start an everyday
task such as a board update.

## Choosing letters

All seven letters are on by default. Ask "turn off Ethical" or "use only True and
Safe" to change this for a conversation.

## Inside each skill

`SKILL.md`, `tasks/`, `references/` (`method.md`, `method-standards.md`, `knowledge.md`,
`failure-modes.md`, `tools.md`), skill `templates/`, shared `../../templates/` cards,
`examples/`, `evals/`, and offline `tools/` at the plugin root.
