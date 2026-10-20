# Task TR-5.2.1 Every claim sourced or marked as a gap

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced colleague with an evidence background |
| Workflow | Sort statements into claims and non-claims, attach a supplied source to each claim, gap the rest |
| Skill | TR-5.2.1 |
| Knowledge | `references/rules.md` (R1, R2, R5, R6), `references/patterns.md` (S1–S8) |
| Tool | `scripts/find_source_cues.py` where code can run. Companion slot: none at launch; VERIFY `check_claim` through `claim-assessment` tests a claim against its passage after drafting |
| Prompt | This guide |
| Template | `assets/check-line.md`, `assets/source-note.md` |
| Input | The draft or request, the supplied sources, the audience from intake |
| Governance | TR-H1, TR-H2, TR-H3, TR-H7, TR-H11 |

## Which statements need a source

| Needs a source | Examples |
|---|---|
| Any figure | Sales, share, market size, prevalence, response rate, cost, price, patient numbers |
| Any comparison | "Better than", "faster than", "fewer side effects than", "similar to" |
| Efficacy and safety | What the product does, how well, for whom, its side effects and risks |
| Competitor facts | A competitor's results, launch, price, pipeline, label, strategy |
| Market and environment facts | Payer positions, guideline recommendations, treatment patterns, policy changes |
| Quotes and attributed views | What a doctor, payer, advisory board or author said or thinks |
| Superlatives and firsts | "Leading", "only", "first", "most prescribed", "gold standard" |
| Time-bound statements | "Current", "latest", "now", "recently approved", "new" |
| Collective authority | "Studies show", "experts agree", "guidelines recommend", "data suggest", "per FDA guidance" |

| Does not need a source | Condition |
|---|---|
| The person's own plan | Framed as a plan: "We will launch in two regions first" |
| The person's own opinion or recommendation | Framed as theirs: "We recommend prioritizing the payer channel" |
| Questions, objectives, agenda items | "Objective: understand payer concerns" |
| Definitions the reader shares | Common terms used in their ordinary sense |

A plan or opinion that contains a fact still needs a source for the fact: "We recommend
the payer channel, because payers now cover 70% of prescriptions" carries a figure.

## Guard (while drafting)

1. **List the supplied sources** in one line each, with what kind of source each is
   (see `tasks/source-type-fit.md`).
2. **For each claim you write, know its source** before you write it. Show it in short
   form beside the claim at leadership depth and above ("(Q3 IQVIA extract, supplied)").
3. **Where a claim has no supplied source, write the gap inline:**
   `[GAP: not supplied — source for <claim> — <what would close it>]`. Keep the claim only
   if the person wants it kept with the gap visible; otherwise leave it out and say so.
4. **Turn collective authority into a name.** "Studies show" becomes the named study or a
   gap. "Experts agree" becomes the named panel, survey or guideline, or a gap. "Per FDA
   guidance" becomes the guidance title and date, or a gap.
5. **Keep opinions framed as opinions.** Do not convert "we believe" into a fact, and do
   not add a source to a recommendation to make it look like evidence.

## Repair (existing draft)

1. **Scan for cues.** Where code can run, use `scripts/find_source_cues.py <draft.txt>` to
   list vague attributions, superlatives, undated "current" claims and weak citations.
   Then read the whole draft: the script finds wording, not claims.
2. **Classify each statement:** claim with a named supplied source; claim with a source
   named but not supplied; claim with no source; not a claim (plan, opinion, question).
3. **Fix:** keep sourced claims; for named-but-not-supplied sources, ask for the document
   (do not confirm it from memory); replace unsourced claims with a gap or remove them;
   reword collective authority.
4. **Never delete silently.** Every removed or gapped claim appears in the source note.

## Check line

See `assets/check-line.md`.

## Boundaries

- Whether the claim says what the source says is `grounded-statements` (while drafting)
  and `claim-assessment` (with tools). This task checks that a source is named and
  supplied.
- Whether a comparative or superlative claim is allowed at all in this market is
  `claims-and-label`. This task asks only what would source it.
- An absent source does not make a claim false. It makes it unsourced here.
