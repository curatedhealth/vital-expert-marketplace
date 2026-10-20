# Task TR-6.2.3 Authorship integrity

## Formula

| Slot | For this task |
|---|---|
| Worker | Responsible AI lead who also knows the business |
| Workflow | Find whose name the work goes out under and what that name claims; keep AI off the byline; turn ghostwriting into acknowledged support the named person makes their own |
| Skill | TR-6.2.3 |
| Knowledge | `references/rules.md` (U1–U5), `references/patterns.md` (A1–A6) |
| Tool | None. Companion slot: future publications or AI-policy companion (none yet) |
| Prompt | This guide |
| Template | `assets/use-note.md` (authorship part), `assets/check-line.md` |
| Input | The work, the named author or signer, who actually drafted it, the venue, the company's role and funding as stated |
| Governance | TR-H1, TR-H3, TR-H5, TR-H11, `references/governance.md` |

## When authorship matters

| Work | What the name claims | Depth |
|---|---|---|
| A manager's own email, memo or slide | "I sent this and stand behind it" | Nothing to raise (A6) |
| A letter to doctors or patients in a physician's name | "This physician wrote or approved this" | The physician reads and approves the final text |
| An article, opinion piece, blog or post for a KOL or external expert | "This independent expert's own view and work" | Full task |
| A journal manuscript, abstract, poster or congress presentation | Authorship under the venue's criteria | Full task, plus disclosure (`tasks/ai-use-disclosure.md`) |
| A quote attributed to a person in a press release or campaign | "This person said this" | The person approves the exact words |

## Guard (while drafting)

1. **Ask whose name it goes out under**, if not stated, when the work is external.
2. **AI never on the byline (U1).** If asked to list AI as an author or cite it as a
   source, decline in one line and say where AI use is described instead.
3. **Draft for an expert as a starting point**, labeled as such: "First draft for
   Dr <name> to rework". Leave the expert's own views as placeholders where the
   material does not give them: `[Dr <name>'s view on …]`. Never invent their opinion,
   experience or patient anecdotes (TR-H1).
4. **Name what makes it honest**, briefly, for anything going out under an expert's or
   author's name:
   - the named person shapes and approves the content and can stand behind all of it
     (U4);
   - writing support, by people and by the assistant, is acknowledged as the venue
     requires (U2, U4, U5);
   - the company's funding or role is disclosed (with `honest-framing`);
   - it goes through the company's publications process (TR-H11).
5. **For manuscripts**, list the authorship criteria in plain words only if the person
   asks or the author list looks wrong (a guest name, a writer listed for drafting
   alone).

## Repair ("write it for Dr X to sign as her own")

1. **One plain line on the problem**: readers will take it as Dr X's own independent
   work; if the company or the assistant wrote it and that is hidden, it misleads them
   and exposes Dr X and the company.
2. **Offer the honest route, not a refusal**: a first draft for Dr X to rework as her
   own, with acknowledgment of writing support and funding, going through the
   publications process. Or the same content published under the company's name.
3. **Do not produce the version framed as her unaided work** ("ready for her to
   submit", "in her voice, no mention of support"). Produce the honest draft instead.
4. **Existing author list:** flag AI listed as author, people listed for drafting alone,
   and names with no stated contribution, as questions for the authors and the
   publications process. Never decide who qualifies.

## Check line

See `assets/check-line.md`.

## Boundaries

- Who the authors are is decided by the authors under the venue's rules and the
  company's publications process. This task asks and points.
- Payments, consulting fees and other interests of the expert are `honest-framing`.
- Whether the content is promotional when an expert speaks for the company is
  `claims-and-label`.
- Copyright in other people's text is `responsible-inputs`.
