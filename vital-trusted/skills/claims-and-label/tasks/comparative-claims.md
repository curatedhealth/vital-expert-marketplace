# Task TR-2.1.3 Comparative claims

Makes sure every comparison, superlative or absolute claim rests on data that compared
like with like, says exactly what was compared, and does not disparage a competitor.

## Formula

| Slot | For this task |
|---|---|
| Worker | Regulatory and promotional reviewer who helps drafts through review |
| Workflow | Find every comparison and absolute claim, find the data each rests on, test it against the five questions, rewrite or mark the gap |
| Skill | TR-2.1.3 |
| Knowledge | `references/rules.md` (R17 to R24), `references/patterns.md` (C1–C8) |
| Tool | None. Companion slot: VERIFY `check_claim` through `claim-assessment`, to test the comparison against its passage |
| Prompt | This guide |
| Template | `assets/claims-note.md`, `assets/check-line.md` |
| Input | The request, the draft, the supplied studies or data, the label, the context card (reader, market) |
| Governance | TR-H1, TR-H2, TR-H3, TR-H8, TR-H11 |

## What counts as a comparative or absolute claim

- explicit comparison with a named product or class: "better", "faster", "more
  effective", "safer", "better tolerated", "more convenient", "superior", "versus",
  "compared with"
- comparison with "standard care", "current treatments" or "older therapies"
- absolute and superlative claims: "first", "only", "leading", "best", "number one",
  "unique", "unmatched", "gold standard"
- implied comparison: "finally, a treatment that works", "no more daily injections",
  "patients deserve better"
- "safe", "well tolerated", "no side effects" used as a claim
- "new", in markets that limit how long it can be used

`scripts/find_claim_cues.py` lists this wording in a longer draft.

## The five questions for every comparison

Ask them in this order. A "no" or "not supplied" on any of them is a flag.

| Question | What a reviewer will look for | Rules |
|---|---|---|
| 1. Was it compared directly? | A study in which both products (or the product and the named comparator) were given to comparable patients and the stated outcome was measured. Two placebo-controlled trials are not a direct comparison | R17, R18, R23 |
| 2. Is it like with like? | Same population, endpoint, dose, time point and setting; products for the same need | R18, R19, R21, R22, R23 |
| 3. Is the feature material and representative? | The compared feature matters to the reader and reflects the whole picture, not one favorable endpoint | R18, R21 |
| 4. Does the wording match the data? | "Faster" means time to an outcome was compared; "more effective" means efficacy was; a secondary or subgroup result is labeled as such | R17, R20 |
| 5. Is it fair to the competitor? | Factual, no mockery or blame, no confusion of brands | R18, R19, R21 |

For absolute claims ("first", "only", "leading"): the claim needs a stated scope (what,
where, since when), a date, and a source the person supplied. Without all three it is
rewritten without the absolute, or gapped (R20, R21, R22).

## Guard (while drafting)

1. **Do not write a comparison the supplied data does not make.** When asked to "say we
   are better than X" with no direct comparison supplied, decline in one plain line and
   offer what can be said: each product's own result with its own comparator, a
   factual difference the label states (dosing, route), or a gap for the study that
   would be needed.
2. **Name the comparator and the measure** in every comparison you do write: "in
   KESTREL-3, time to response was shorter with Brevanzo than with Kelandro (median 4
   versus 7 weeks)", as supplied.
3. **Scope every absolute** with what, where and since when, from a supplied source, or
   leave it out.
4. **Keep competitors factual.** No adjectives about their product.
5. **Patient and public material carries no comparison with another treatment** until
   the review process decides; several markets exclude it outright (R24) or exclude
   public promotion of prescription medicines altogether (R11, R15).

## Repair (existing draft)

1. **List every comparative and absolute claim** with the data it rests on, if any.
2. **Run the five questions** on each.
3. **Fix:** keep a comparison that has a direct, like-for-like source, with comparator
   and measure stated; rewrite a comparison resting on two separate trials into two
   separate statements with no "versus" between them; scope or remove absolutes;
   remove disparaging language; gap any comparison with no source.
4. **Cross-trial comparisons:** do not decide whether one can be shown at all. Present
   the results separately and route the question to medical review (pattern C2).
5. **Never delete silently.** Every change appears in the claims note.

## "Make it more competitive"

People often want a sharper competitive message. Sharpen with what is supported: lead
with the product's own strongest supported result, state a factual difference the label
supports, make the reason it matters to this reader explicit. Do not add a comparison,
a superlative or a competitor weakness to make it sharper, and say so in one line if the
request implied it.

## Check line

See `assets/check-line.md`. Disparaging language and unscoped absolutes go in the notes
under the comparisons line.

## Boundaries

- Whether the comparison's source says what is claimed is `grounded-statements` while
  drafting and `claim-assessment` with VERIFY. This task asks whether a direct,
  like-for-like source exists and whether the wording matches it.
- Which kind of source can carry a comparison for this reader is `sourced-claims`.
- Whether benefits and risks are shown in proportion is `balanced-evidence`.
- Whether a comparison may be used at all in a market is decided by the review process
  (TR-H11). This task never calls a comparison fair, valid or permitted (TR-H3).
