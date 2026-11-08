# Task TR-3.2.3 Conflict disclosure

## Formula

| Slot | For this task |
|---|---|
| Worker | Medical reviewer with a statistics background |
| Workflow | List every interest the material shows, check the draft carries each where the result is used, and remove any "independent" or neutral label the material does not support |
| Skill | TR-3.2.3 |
| Knowledge | `references/rules.md` (R8, R9), `references/patterns.md` (IN1–IN7) |
| Tool | `scripts/find_framing_cues.py` (independence and sponsor words). No companion yet |
| Prompt | This guide |
| Template | `assets/check-line.md`, `assets/disclosure-line.md`, `assets/framing-note.md` |
| Input | The draft, the supplied sources (funding statement, author disclosures, sponsor role, methods), the context card |
| Governance | TR-H1, TR-H3, TR-H6, TR-H11 |

## What counts as an interest here

Only what the material shows. Typical interests, as the source states them:

- the study was sponsored or funded by the company that makes the product, or by a
  competitor;
- authors are employees, hold stock, or received consulting fees, honoraria or grants
  from either;
- the sponsor designed the study, held or analyzed the data, or wrote or reviewed the
  report;
- a medical writer or agency was paid by the company;
- the figure is company data: "data on file", an internal analysis, company-run market
  research, a company-funded survey or advisory board;
- the person writing works for the company whose product is described (the draft
  itself is company material).

`source-assessment` records what a source discloses. This task makes sure the draft
carries that disclosure to its reader.

## Guard (while drafting)

1. **Inventory the interests** from the supplied material, one line each, with where
   the material says so (funding statement, disclosures section, methods). If the
   material carries no funding or interest statement, record "not stated in the
   source". That is not the same as "independent".
2. **Carry the interest with the result.** Where a sponsored study's result is used,
   say who sponsored it in the same place, in plain words ("a trial funded by the
   maker of X"; "company data on file"). For a slide, on the slide that uses it.
3. **Never re-label an interest away.** Do not call a sponsored study "independent",
   a company survey "physicians' views", a company analysis "real-world evidence shows",
   or a paid advisory board "expert consensus". Name the source as it is.
4. **"Independent" only when the material says so**, and attributed: "the authors state
   the funder had no role in design, analysis or writing". Never in the draft's own
   voice.
5. **Disclose the writer's side when it matters.** When company material describes a
   competitor's study or the company's own, it is the company speaking; do not present
   it as a neutral overview. The company's own process decides the exact declaration.
6. **Build the disclosure line from the material only** (`assets/disclosure-line.md`).
   Missing pieces become gaps; never fill a funder, role or author tie from memory.

## Repair (existing draft)

1. **Inventory the interests** in the material, as above.
2. **Find every use** of each interested source in the draft and every "independent",
   "unbiased", "objective", "neutral", "real-world doctors", "experts agree" or similar
   label. `python scripts/find_framing_cues.py draft.txt` lists the words; read each.
3. **Classify:** disclosed where used; disclosed only far away (end note, last slide,
   footnote); not disclosed; labeled independent or neutral without support in the
   material.
4. **Fix:** add the disclosure where the result is used; remove unsupported labels;
   attribute "no role" statements to the authors.
5. **If the person asks to drop or soften a disclosure the material shows**, stop and
   explain in plain words why it stays (`references/governance.md`). Offer shorter
   wording, not removal.

## Check line

See `assets/check-line.md` (interests line).

## Boundaries

- No legal determination (TR-H6): do not decide whether a payment, transfer of value
  or relationship must be reported under a law or code (for example a transparency
  register), or whether a declaration meets a code's wording. Say what the material
  shows; point to the company's promotional review or compliance process.
- Do not judge whether the sponsor's involvement biased the result. Readers judge that
  from the disclosure; the job is that they can see it.
- Grading the source itself (peer review, funding, fit) is `source-assessment`. Which
  claims need a reference is `sourced-claims`. How AI use is disclosed is
  `responsible-use`.
