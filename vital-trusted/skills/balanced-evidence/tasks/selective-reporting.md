# Task TR-3.1.2 Selective reporting

## Formula

| Slot | For this task |
|---|---|
| Worker | Medical reviewer (an experienced colleague; not the company's medical review) |
| Workflow | Inventory everything the material reports, mark what the draft uses, restore what changes the picture, and state the scope of the rest |
| Skill | TR-3.1.2 |
| Knowledge | `references/rules.md` (R3, R4, R7, R9, R10), `references/patterns.md` (SR1–SR8) |
| Tool | `scripts/balance_cues.py --source material.txt` where code can run. Companion slot: none yet (`references/tools.md`) |
| Prompt | This guide |
| Template | `assets/check-line.md`, `assets/balance-note.md`, `assets/evidence-inventory.md` |
| Input | The draft or request and all supplied material: every study, results table, abstract or registry extract |
| Governance | TR-H1, TR-H3, TR-H6, TR-H7, TR-H11 |

## What can be selected

- **Studies:** two trials of the same product and use, where one met its primary
  endpoint and one did not; a pivotal trial and its extension; a trial and a real-world
  study.
- **Endpoints:** the primary endpoint, key secondary endpoints, exploratory endpoints.
- **Subgroups:** pre-specified and post hoc, and the overall population they sit in.
- **Time points:** the pre-specified time point and the early or late ones; the point
  where the effect was largest and where it was smallest.
- **Analysis sets:** everyone randomized, completers only, responders only.

## Guard (while drafting)

1. **Fill the evidence inventory first** (`assets/evidence-inventory.md`) from the
   supplied material only: every study, its primary endpoint and result, its
   pre-specified time point, key secondary endpoints, subgroups, harms and
   discontinuations. Leave a field as a gap rather than inferring it.
2. **Lead with the primary result** of each study used, at its pre-specified time point,
   in everyone it was planned for. Secondary, subgroup and exploratory results follow,
   labeled as such.
3. **Use every study of the same question in the material**, or say why one is left out
   ("ZELORA-3, in a different population, is not covered here"). A study that did not
   meet its primary endpoint is not dropped because it is unhelpful.
4. **Report time points fairly.** Use the pre-specified one. If an earlier or later one
   is shown, show the pre-specified one too. Do not choose the week where the effect
   peaked.
5. **State the scope** when the draft is deliberately narrow: "This slide covers the
   primary endpoint of ZELORA-2. Secondary endpoints and safety are on slide 3." A stated
   scope is fair; an unstated one reads as the whole picture.
6. **Ask about what was not supplied.** If the draft rests on one study and you cannot see
   whether others exist, ask: "Are there other studies of this product for this use? A
   summary that leaves one out will be read as selective." Never name a study from
   memory (TR-H1) and never say "no other studies exist".

## Repair (existing draft)

1. **Build the inventory** from the material. Where code can run,
   `scripts/balance_cues.py draft.txt --source material.txt` lists study names and time
   points that appear in the material but not in the draft. It matches words, not
   meaning: check the inventory by hand as well.
2. **Mark each inventory item** as: in the draft as reported; in the draft but
   demoted or buried (for example, the primary result after the secondary, or in a
   footnote); left out; not supplied.
3. **Decide what changes the picture.** A left-out item changes the picture when the
   reader would draw a different conclusion with it: a negative or neutral study, a
   missed primary endpoint, a fading effect, a higher dropout rate, a subgroup that went
   the other way. Restore those. For the rest, state the scope.
4. **Fix** by restoring, reordering so the primary result leads, labeling subgroups and
   time points, and stating scope. Leave gaps for what is missing. When the person must
   choose which study or time point leads, ask (`needs a decision`).
5. **Never delete silently.** Every change appears in the balance note.

## Check line

See `assets/check-line.md`.

## Boundaries

- Whether a subgroup, endpoint or design is described correctly (pre-specified or post
  hoc, surrogate or clinical outcome, observational or randomized) is
  `grounded-statements`. Here, the question is whether it was chosen fairly and given its
  proper place.
- Whether a study is good enough, peer reviewed, retracted or superseded is
  `source-assessment`.
- Whether an effect is large, certain or clinically meaningful, and how it is worded, is
  `honest-framing` and the reviewer.
- Finding studies not supplied is a literature search, outside this skill. Ask the person
  or their literature or medical information team.
