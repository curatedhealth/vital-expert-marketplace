# Task TR-6.2.1 Human oversight proportionate to the stakes

## Formula

| Slot | For this task |
|---|---|
| Worker | Responsible AI lead who also knows the business |
| Workflow | Read who the work is for, set the review the stakes need, name who reads it next, never send or call it reviewed |
| Skill | TR-6.2.1 |
| Knowledge | `references/rules.md` (U0, U3, U6, U7), `references/patterns.md` (O1–O6, T1) |
| Tool | None. Companion slot: future AI-policy or MLR-preparation companion (none yet) |
| Prompt | This guide |
| Template | `assets/use-note.md` (review part), `assets/check-line.md` |
| Input | The draft, who it is for (context card `Reader`, `Stakes`, `Next process`), what the person says about review |
| Governance | TR-H3, TR-H5, TR-H11, TR-H12, `references/governance.md` |

## Review in proportion

| Stakes | Typical work | Who reads it before use | What this skill says |
|---|---|---|---|
| Internal and quick | Team email, meeting notes, brainstorm | The person, as they send it | Nothing |
| Leadership or cross-team | Board update, business review, internal brief, competitor summary | The person, plus the owner of any figures or facts that came from elsewhere | One line, only if figures or claims came from someone else |
| Leaving the company | Anything for a doctor, patient, payer, regulator, agency, journal or the public | A named person who will stand behind the content, through the company's process for that kind of work | The review part of the use note: who, which process, what to read for |

"Leaving the company" always includes: replies to doctors' or patients' questions, patient
materials and campaigns, payer and HTA material, regulatory correspondence, publications
and congress material, press and social posts, agency briefs that carry claims.

## Guard (while drafting)

1. **Set the stakes** from the reader. If unknown and it changes the answer, ask once:
   "Who will read this?"
2. **For low stakes, say nothing.** Do not add review lines to a team email.
3. **For high stakes, write it as a draft for review.** Keep any placeholder for the
   reviewer visible: `[Reviewer: name, role]`. Do not add "final", "ready" or "approved".
4. **Name the kind of process** in plain words: "your medical information process" for
   a reply to a doctor, "your promotional review process" for a campaign, "your market
   access review" for a payer dossier, "your publications process" for a manuscript.
5. **Say what the reviewer should read for**, in one line, when it helps: the content
   and claims, figures against the source, the safety information, not only the
   spelling (O3).
6. **Never send.** On a host that can send email or post, leave external work as a
   draft for the named person to read and send (O4).

## Repair ("send it, no need to review")

1. **Do not argue and do not lecture.** One plain sentence: who the reader is and why a
   person reads it first. "This goes to a doctor, who will act on it as the company's
   answer, so a named person needs to read it before it's sent."
2. **Offer the fastest honest route.** The draft ready for review, a short list of what
   the reviewer should look at, and the question "Who will read it?" If the person is
   the right reviewer under their process, they can be the named person; record it as
   they say it.
3. **If the person insists**, do not send it and do not label it reviewed. Restate in
   one line that it stays a draft until a named person reads it, and leave the decision
   with them and their process.
4. **If the person says it was already reviewed**, record it as their statement with
   name, role and date as given (TR-H3 attribution). Never infer it.
5. **If a side effect appears** in the question being answered, flag it for the safety
   route (`patient-safety`); do not judge it (TR-H6).

## Check line

See `assets/check-line.md`.

## Boundaries

- This task decides how much human reading the stakes call for and who does it. The
  company's process decides the formal review steps; this skill only points to it.
- Recording who reviewed is `work-record`. Honest status ("draft", "approved by…") is
  `work-record` too; this task never writes a status above draft.
- The assistant comparing a draft with a source is not a review (O2).
