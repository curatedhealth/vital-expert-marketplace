# Task TR-8.1.1 Break text into checkable claims (Part A)

Absorbs the claim-decomposition method of the earlier vital-verify plugin.

## Formula

| Slot | For this task |
|---|---|
| Worker | Evidence lead |
| Workflow | Take the text as submitted, split it into claims, rank them, pair each with its quoted passage, then stop before deciding support |
| Skill | TR-8.1.1 |
| Knowledge | `references/patterns.md` (C1–C4, C8, C11, C13, C14), `references/rules.md` (R1–R5) |
| Tool | VERIFY `extract_claims`; without it, `scripts/split_claims.py` or a split by hand |
| Prompt | This guide |
| Template | `assets/claim-list.md` |
| Input | The finished text exactly as submitted, and the supplied material (paper, registry summary, label, report, notes) |
| Governance | TR-H1, TR-H4, TR-H7, TR-H12 |

## What counts as one claim

A claim is one thing the text says is the case that a reader could ask to see in a
source. One subject, one thing said about it, and, for a figure, one frame (who, which
group, which period, which unit).

- **Keep the words.** A claim is quoted from the text as written, never cleaned up.
- **A sentence with two facts that rest on different passages is two claims for pairing.**
  "Admissions fell 40% in the registry of nearly 2,000 patients" carries an effect and a
  size. VERIFY's `extract_claims` works by sentence, so it returns this as one claim; you
  note both parts so you can read a `partial` result later.
- **A figure inside a sentence is part of that claim**, not a separate one, unless the
  figure is the only new point.
- **No citation marker does not mean no claim.** A sentence without a reference is still
  checked. A reference marker is copied, not treated as evidence.
- **Still a claim:** a fact dressed as an opinion ("we believe it cuts admissions by
  40%"), a fact attributed to an unnamed authority ("experts agree"), a fact in a chart
  title or a slide headline.
- **Not a claim about the world:** headings, a recommendation ("payers should…"), an
  opinion with no factual content, a definition the text sets for itself, and reference
  lines. List these as "opinion, recommendation or definition". They are not checked
  against a passage, and they still go to the person's review.

## Which claims matter most

Rank before pairing, so a short check covers the right sentences (TR-H12).

| Priority | Kind of claim | Why it goes first |
|---|---|---|
| 1 | Numbers: rates, counts, percentages, prices, savings, dates, durations | Reviewers check them first; one wrong figure discredits the page |
| 1 | Efficacy and safety statements: what the product does, side effects, tolerability | Highest consequence for patients and for review |
| 1 | Quotations and named people or organizations | Words in someone's mouth must be exact and attributable |
| 1 | Compliance or performance claims: "approved", "recommended", "guideline", "certified" | VERIFY keeps these only when a quoted passage states them (R5) |
| 2 | Comparisons and superlatives: more, less, better, first, only, largest | Often in no source at all |
| 2 | Causes: "because", "due to", "led to", "reduces" from an association | Turn timing or association into a claim of effect |
| 2 | Study description: design, population, size, endpoint | A registry described as a trial changes what the result means |
| 3 | Background statements | Check when the work leaves the company |

## Steps

1. **Freeze the text.** Take it exactly as submitted, including spaces. Do not correct
   typos or rephrase first. If it is over 20,000 characters, split it at paragraph
   breaks and say so.
2. **Split it.**
   - VERIFY connected: call `extract_claims` with the frozen text
     (`references/tools.md`). Keep what it returns, including offsets.
   - Not connected: where code can run, `python scripts/split_claims.py text.txt`;
     otherwise split by hand at sentence ends. Label the split "manual, not
     tool-checked".
3. **Rank** each claim with the table above. At light depth, keep priority 1 and 2 only.
4. **List the supplied material.** One line per source. If nothing was supplied, stop
   here: ask for the material. Do not search for it and do not use what you remember.
5. **Pair each claim with its passage.** Find the words in the supplied material that
   the claim rests on and quote them exactly, with a locator (page, section, table,
   paragraph or line). Rules:
   - Quote, never paraphrase. A summary you wrote is not a passage (pattern C3).
   - Take the passage from the source the text cites, not from another one that happens
     to agree (C13).
   - The passage must cover the whole claim. If one passage covers half, note which
     half.
   - If the supplied material says nothing about the claim, record "no passage found".
     Do not stretch a nearby sentence to fit.
   - If two supplied passages disagree, pair both and flag it for the person.
6. **Stop.** Return the claim list (`assets/claim-list.md`) or go straight to Part B. Part
   A never gives a support result.

## Checks before handing to Part B

- Every claim is quoted from the text as submitted.
- Every factual sentence of the right priority appears once.
- Every passage is a word-for-word quote with a locator, or "no passage found".
- No support word is attached to any claim yet.

## Companion slot

| | |
|---|---|
| What VERIFY would do | Split the text into claims with exact offsets, so every result maps back to its place in the text |
| Tool call | `extract_claims` with `text` (and `granularity: "sentence"`, the only value and the default) |
| Without it | Manual split by script or by hand, labeled "manual, not tool-checked" |
| Never | Describe a split as VERIFY's when the tool did not run |

## Boundaries

- Part A does not decide support, grade the source or count the result.
- Do not drop a claim because it is hard to check. A hard claim is a priority claim.
- Do not add a claim the text does not make, even one the person "meant".
