# VITAL TRUSTED

Nineteen skills for people across a life-sciences company who use an AI assistant
for daily work: general management, brand, market access, medical and other teams.
TRUSTED supports the company's own SOPs and review processes. It never replaces them.

**Product of Crossroads Catalyst GmbH (Vital Expert).**  
**Status:** version **0.3.4** · `release_state: Pilot`. Not published yet.  
**License:** Proprietary, see `LICENSE` (`LicenseRef-CrossroadsCatalyst-Proprietary`).

Outputs remain uncleared drafts until a named human clears them under your process.
A `[CHECK]` marker inside a skill's standards means the rule has not been read in the
official text yet. The skill applies it as good practice, never as a requirement.

## The standard

| Need | The question it asks |
|---|---|
| Tangible | Is it useful to this reader, for this job? |
| Rule-compliant | Is it allowed, for this audience, in this market? |
| Unbiased | Is the evidence shown in proportion? |
| Safe | Could it lead to harm? |
| True | Is it correct, and can it be shown? |
| Ethical | Is AI being used responsibly for this work? |
| Defensible | Can the organization stand behind it? |

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

Build skills make the work good by design. Prove skills carry the claim, source,
confidence and citation method. There is no connector and no key: Prove checks are done
by hand, by comparing each claim with the passage you supply, and every such result is
labeled **not tool-checked**. Results are counts and plain notes, never a confidence
figure or a verdict.

## Installing

0.3.4 is a Pilot build and has not been published. Do not install `vital-trusted` from
the marketplace for new work; the listing there is the earlier build, 0.3.1, recorded as
Released in the CHANGELOG.
This build will be published only when the owner says so.

## Choosing letters

All seven letters are on by default. Ask "turn off Ethical" or "use only True and
Safe" to change this for a conversation.

## Inside each skill

`SKILL.md` with the intake and governance notes beside it at the skill root, `tasks/`, `references/`
(gap rules, knowledge, method, method standards, patterns, rules and tools notes), the skill's own `templates/`, `examples/`, `evals/`, and
`scripts/` where the skill has a helper script.

At the plugin root: release checks in `scripts/` (see `scripts/README.md`), shared output cards in `templates/` (a skill's own template always
wins over a shared card), a small set of offline helpers in `tools/` (claim splitting,
plain reference lines, letter lines; the counts-only script is in `confidence-scoring`), and the steward in `agents/`.
Helpers run no lookups and label their output not tool-checked.
