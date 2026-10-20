# Task TR-6.2.2 AI use disclosure

## Formula

| Slot | For this task |
|---|---|
| Worker | Responsible AI lead who also knows the business |
| Workflow | Find who could expect disclosure (policy, venue, law, audience), ask what applies, draft plain wording from what actually happened |
| Skill | TR-6.2.2 |
| Knowledge | `references/rules.md` (U0, U2, U3, U6, U7, U8), `references/patterns.md` (D1–D6) |
| Tool | None. Companion slot: future AI-policy companion (none yet) |
| Prompt | This guide |
| Template | `assets/use-note.md` (disclosure part), `assets/check-line.md` |
| Input | The work, who receives it, the venue, the context card `AI use policy` line, the facts of what the AI did (from `work-record` or the person) |
| Governance | TR-H1, TR-H3, TR-H6, TR-H7, TR-H11, `references/governance.md` |

## Who might expect disclosure

Four places can expect AI help to be stated. This skill works out which are in play and
asks; it never decides what any of them says.

| Place | What to do | Example |
|---|---|---|
| The company's AI use policy | Ask what it says for this kind of work and audience. Use the context card if it already records the answer. | "Does your AI use policy say anything about disclosing AI help in material for payers?" |
| The venue's own rules | Ask which venue; ask for its instructions if not supplied. Where a confirmed rule exists, say it plainly. | A journal following the editors' recommendations asks for AI use in the cover letter and the manuscript (U2). Evidence submitted to NICE: declare AI use and how it was used, including human input (U7). Other HTA bodies, payers and congresses: ask for their rules (U8). |
| The law | Say in plain words what the rule covers and that legal decides whether it applies. | EU: AI-generated text published to inform the public on public-interest matters is labeled, unless a person reviewed it and someone holds editorial responsibility (U6). |
| The audience | Note when readers would reasonably want to know (a patient reading a personal-sounding letter, a doctor reading a reply). The company's policy sets the practice. | "Your policy may say how to handle this for patient letters." |

## Guard (while drafting)

1. **Set the stakes.** Internal and quick: say nothing about disclosure. Leadership:
   only if the person asks or the policy line on the card says something. Leaving the
   company: continue.
2. **Name the places in play** from the table, usually one or two. A payer dossier: the
   policy and the payer's or HTA body's rules. A journal manuscript: the policy, the
   journal, and authorship (`tasks/authorship-integrity.md`). A public campaign: the
   policy and possibly the EU rule.
3. **Ask, once, in one short paragraph.** Name the question and who answers it.
4. **Draft the wording either way**, so the person is not blocked: a disclosure line
   built only from what happened (which parts, which verbs, who reviewed as stated), with
   placeholders for anything not known. Plain, specific, not vague (D3) and not inflated
   (D4).
5. **Put it where the venue expects it**: cover letter and acknowledgments or methods for
   a journal (D6); a methods or declarations section for an HTA submission; a footer or
   first-screen line for public material, as the person's policy or legal team decides.

## Disclosure wording

Build from facts only. Good shape:

```
<An AI assistant | <tool name, if the person wants it named>> was used to <drafted |
summarized | translated | restructured> <which parts> from <the sources>. <Name, role>
reviewed and edited the content and is responsible for it.
```

- Never name a reviewer the person did not give; leave `[name, role]`.
- Never describe the AI as having verified, validated or checked the evidence unless a
  tool check actually ran and the person wants it stated.
- Short is fine. One sentence usually does it.

## Repair (existing disclosure or none)

1. **No disclosure, high stakes:** ask the policy question and offer the wording.
2. **Vague disclosure** ("digital tools were used"): offer the specific version.
3. **Overstated disclosure** ("AI-validated"): replace with plain verbs.
4. **Disclosure in the wrong place** for the venue: say where it goes.
5. **The person wants AI help hidden** where the policy or venue expects it: say in one
   line that the venue or policy asks for it, offer the plain wording, and leave the
   decision with them and their policy owner. Do not draft a statement that says less
   than what happened.

## Check line

See `assets/check-line.md`.

## Boundaries

- `work-record` records what happened; this task decides whether that record should
  appear in the deliverable, by asking the policy and the venue. The record exists
  either way.
- Disclosure of funding or the company's role is `honest-framing` and, for
  publications, `tasks/authorship-integrity.md`.
- Whether a law applies is legal's decision (TR-H6). Say what the rule covers; never
  say "not required" or "required".
