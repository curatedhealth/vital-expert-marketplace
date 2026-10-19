# Output format: design review pack

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line.

## Short mode (default for a direct question)

1. **Where the review stands:** two sentences: how many items have complete evidence, how many are open, and the decisions the reviewers must take.
2. **Open items:** Item · What is open · Evidence id.
3. **Residual risks against your criteria:** Hazard · Residual (yours) · Your criterion · Where it falls · Decision: for the reviewers.
4. **The decision needed:** one line naming the owner the person gave, or "owner not named" with the question.
5. **Record:** "Review pack, draft for the owner. Decisions are the reviewers'. Uncleared AI-assisted draft." or the clearer's name.

## Full mode

### Scope and people
Stage, release or change under review; reviewers as named; owner as named (or "owner not named").

### Evidence by item
| Item | Requirement or control | Verification or validation | Result | Source | Open? |
|---|---|---|---|---|---|

### Residual risk layout
| Hazard | Controls and type | Residual severity (yours) | Residual probability (yours) | Your criterion | Where it falls | Benefit stated by you | Decision |
|---|---|---|---|---|---|---|---|

### Overall residual risk and benefit
The person's benefit statement beside the residual risks. Conclusion left for the reviewers.

### Record page
| Date | Scope | Reviewers | Item | Outcome (accept / accept with actions / change required) | Action owner | Filed at |
|---|---|---|---|---|---|---|

Outcome and owner cells are empty or hold what the person said. "Filed at" is the design and development file location, or `[GAP]`.

### Record
Draft for the owner. Risk acceptance, review outcome and release decisions are the reviewers' and the owner's. Cleared by NAME, or uncleared. AI-assisted draft.
