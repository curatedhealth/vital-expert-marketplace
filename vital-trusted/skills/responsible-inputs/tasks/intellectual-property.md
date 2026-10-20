# Task TR-6.1.2 Intellectual property

## Formula

| Slot | For this task |
|---|---|
| Worker | Responsible AI lead who also knows the business |
| Workflow | Recognize whose work it is and what the request does with it, prefer summary over reproduction, point to licensing |
| Skill | TR-6.1.2 |
| Knowledge | `references/rules.md` (I9, I10, I12), `references/patterns.md` (P1–P7) |
| Tool | `scripts/scan_inputs.py` (copyright and license markers) where code can run. Companion slot: future AI-policy companion (none yet) |
| Prompt | This guide |
| Template | `assets/input-note.md`, `assets/check-line.md` |
| Input | The request, the material, where the result will go, any license terms the person supplies |
| Governance | TR-H1, TR-H3, TR-H7, TR-H11, `references/governance.md` |

## What to recognize

| Kind | Typical signs | The question |
|---|---|---|
| Copyrighted text | A full journal article, a book chapter, a paid newsletter, a guideline document, a publisher PDF with a copyright line | Is the request to reproduce or closely rework it, or to understand and summarize it? |
| Paid or licensed reports and data | Market research reports, syndicated sales or prescription data, analyst reports, database exports with license terms | Do the license terms allow this use, and this tool? |
| Client-owned material | A client's documents in an agency, consultancy or CRO | Does the client agreement allow it? |
| Agency or third-party creative work | Agency concepts, copy, images, campaign assets, stock images | Who owns it, and was it licensed for this use? |
| The person's own company's work | Their own published press release, their own approved materials | Usually nothing to raise; other letters may still apply |

## Guard (before or as material comes in)

1. **Set the depth.** Reading or summarizing for one's own understanding, from material
   the company has access to: usually one line at most, or nothing. Reproducing or
   reworking a whole work, or anything going outside the company: continue.
2. **Say what it looks like and what the request does with it.** "This is a full paid
   journal article; the request is to rewrite it for an external newsletter."
3. **Prefer summary over reproduction.** Offer a summary in new words, with the citation
   and a link to the original, and at most short, attributed quotations. A close
   rewrite that follows the article paragraph by paragraph is still built on the
   article.
4. **Respect licenses.** Licensed reports and data are used as their terms allow. Ask
   whether the terms cover this use, this tool and this audience. Do not guess the
   terms and do not assume a subscription covers external use or use in an AI tool.
5. **Point to the company's process** in plain words: the library or licensing team for
   publications and paid reports, the contract owner for client or partner material,
   the brand or legal team for agency work. Whether a use is fair, a fair dealing or
   covered by an exception is a legal judgment; it belongs there (I9, I10).
6. **Proceed on the safer route** the person picks. For a summary, use the
   `grounded-statements` discipline: only what the article says, cited.

## Repair (existing draft reproduces material)

1. **Find the reproduced passages:** long verbatim runs, close paraphrase that follows
   the source sentence by sentence, copied tables or figures, unattributed quotations.
2. **Rewrite as a summary** in new words with a citation, or cut to a short quotation
   with attribution, or mark `[GAP: needs a decision — permission to reproduce <item> —
   your licensing process]` where the person wants the reproduction kept.
3. **Never remove the attribution** to make text look original, and never present
   someone else's figure or table as the company's own.
4. **List what changed** in the note, sized to the stakes.

## Check line

See `assets/check-line.md`.

## Boundaries

- Whether a source is good enough as evidence is `source-assessment`; whether a claim
  needs a citation is `sourced-claims`.
- Authorship and AI disclosure on the result is `responsible-use`.
- Licensing, fair use and contract interpretation belong to the company's legal or
  licensing function. This task flags and asks.
