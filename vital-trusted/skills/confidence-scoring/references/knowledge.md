# Knowledge: confidence-scoring

## Migrated rules

# Rules this skill applies

Each rule names its source, the date and its status (TR-H8). The confidence line is
VERIFY's own definition, not a regulatory or industry requirement. No primary document
known to this skill sets a faithfulness threshold for releasing material, and this skill
sets none.

Last reviewed: 20 October 2026.

| Id | Rule | Source | Status |
|---|---|---|---|
| C1 | Faithfulness percent = (supported + 0.5 × partial) ÷ (supported + partial + unsupported + contradicted + unverifiable), as a whole percent. out_of_scope is left out of the denominator. | VERIFY connector server instruction, as exposed to this session on 20 October 2026. The same formula is restated in the earlier vital-verify `support-decision` skill (version 2026-10-19.2). | Confirmed against the connector instruction on 20 October 2026. The connector tool schemas do not state it. |
| C2 | Rounding to a whole percent is half up (12.5 becomes 13). | None. Chosen by this skill so the result is reproducible. | `[CHECK]`: VERIFY's own rounding convention is not stated in the instruction or the schemas. Owner to confirm. |
| C3 | The six statuses: supported, partial, unsupported, contradicted, unverifiable, out_of_scope. Open items are partial, unsupported, contradicted and unverifiable. | VERIFY connector instruction, 20 October 2026 (names the statuses in the formula and the open items). | Confirmed for the names on 20 October 2026. The `check_claim` schema says it "returns a status" but does not list the values; `[CHECK]` against a real return. |
| C4 | Status meanings: supported means the passage states the claim or a stricter version; partial means part is stated and the rest can be named; unsupported needs admissible sources to have been checked; contradicted needs a passage stating the opposite; unverifiable is a refusal (no source, inadmissible source, empty passage) and not a finding that the claim is false; out_of_scope is for normative and definitional statements. A bronze-tier passage yields at most partial. | vital-verify `support-decision` skill, `references/statuses.md`, restated 19 October 2026 from the VERIFY method. | `[CHECK]`: a document, not the connector. To be re-established against `check_claim` returns before being stated as fact. |
| C5 | A status measures word overlap between the statement and the passage. It is not a verdict that the statement is true in the world. | VERIFY connector instruction, 20 October 2026 ("A status is word overlap with that passage, not a verdict that the sentence is true in the world"). | Confirmed on 20 October 2026. |
| C6 | Under each reference, print the source_score total and the axes whose values are numbers; omit an axis whose value is null. Then the confidence line, then a short card: counts by status, the open items, one recommendation. No evidence table unless asked. | VERIFY connector instruction, 20 October 2026. | Confirmed on 20 October 2026. |
| C7 | Source score axes are authority, recency, relevance, provenance and currency (weights 25, 25, 30, 10, 10); null axes are dropped and the rest rescaled to 100; relevance is null when no question was passed; currency is null until a currency check runs. | vital-verify `source-grading` skill, `references/tiers-and-score.md`, 19 October 2026. The `qualify_source` schema says only that it returns "a tier and a source_score". | `[CHECK]`: axis names, weights and null behavior to be confirmed against a real `qualify_source` return. Print what comes back; do not recompute. |

## How to use these rules in output

- Do the arithmetic of C1 in the open. Never describe it as an industry standard.
- When a rule is `[CHECK]`, apply it as this skill's practice and do not cite it as
  VERIFY behavior to the person.
- Never add a threshold, a band or a label to the percent. None of these sources defines
  one.

## Migrated patterns

# Misuse patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching; no real product, trial or person.

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

**P1 The percent as a verdict.** The number is presented as a grade or a release signal.
Why: the percent counts overlap with supplied passages. It says nothing about truth,
balance, permission or whether the right sources were supplied.
Before: "Faithfulness 96%: high confidence, safe to send to the payer."
After: "Faithfulness 96%: of the 12 factual statements checked, 11 are backed by the
passages supplied and 1 is partly backed. Open: 1 statement on cost. Your market access
review decides whether it goes." (TR-H3, TR-H5, C5)

**P2 The simulated percent.** A figure computed from the assistant's own reading, or
estimated, when VERIFY did not run.
Why: it looks like a tool result and is not one. It is a fabricated record.
Before: "I've checked it: about 80% faithful."
After: "No confidence figure: VERIFY is not connected. Read, not tool-checked: 5
statements match your material, 1 does not appear in it." (TR-H1, TR-H4)

**P3 Out of scope in the denominator.** Normative or definitional statements counted.
Why: they cannot be backed by a passage, so counting them lowers the figure for no
reason; leaving them off the card hides that they exist.
Before: 6 supported, 2 partial, 1 unsupported, 1 unverifiable, 3 out of scope → "54%".
After: (6 + 1) ÷ 10 = 70%; "3 statements are not factual and are not counted". (C1)

**P4 Unverifiable dropped to lift the figure.** "Leave out the ones it couldn't check."
Why: a statement nobody could check is still in the text. Dropping it from the count but
not from the draft overstates support.
After: keep it in the denominator, or remove the statement from the text and check
again. (C1, TR-H1)

**P5 Unverifiable read as false.** "Two claims are wrong."
Why: unverifiable means no usable source or passage, not that the statement is false.
After: "2 statements could not be checked: no source was supplied for them." (C4)

**P6 Source score called confidence.** "Source confidence 78", or the faithfulness
percent averaged with the source scores.
Why: the source score is about the page; the percent is about the statements. Mixing
them produces a number that means nothing.
After: print the source score under its reference and the faithfulness line once, apart.
(C6, C7)

**P7 The empty axis as zero.** A null relevance or currency axis printed as 0.
Why: zero says the check ran and scored nothing; null says it did not run.
After: leave the axis out; if it matters, say "currency not checked". (C6)

**P8 Two recommendations, or a send decision.** "Fix the cost line, add a reference,
check the subgroup, then it's good to go."
Why: one recommendation keeps the next action clear; a send decision is not the card's
to make.
After: "Recommendation: remove the cost-savings statement or supply the analysis that
backs it, and check again." (C6, TR-H5)

**P9 Zero denominator printed as a number.** "0%" or "100%" when nothing factual was
checked.
After: "No confidence figure: nothing factual was checked." (C1)

**P10 Comparing drafts without the counts.** "Version 2 is better: 85% against 70%."
Why: the two drafts may have had different statements checked.
After: show both counts side by side and say what changed.

# Failure modes

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-CS-01 | Faithfulness as truth % | Was faithfulness treated as probability the claim is true? | Meaning | RAGAS / VERIFY | VERIFIED |
| FM-CS-02 | Invented counts | Were statuses invented that claim-assessment did not return? | Provenance | TR-H4 | VERIFIED practice |
| FM-CS-03 | Clearance from % alone | Was high % used to clear a pack? | Clearance | TR-H5 | VERIFIED practice |
| FM-08 | Tool status treated as world-truth | Is a local or Verify status described as "true in the world"? | Prove honesty | VERIFY / TRUSTED Prove | VERIFIED |

Skill-specific rows for `confidence-scoring`. Shared FM-08 is universal Prove honesty.
