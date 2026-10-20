# Output format: review and repair plan

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line.

## Short mode (default for a direct question)

1. **Ranked by your scores:** one or two sentences naming the top findings and the close call.
2. **Ranking:** Finding · Value estimate · Largest contributing criterion · Owner you named.
3. **Release under your rule:** findings where your rule is not met: "release waits under your rule: owner decides".
4. **Responding work and review:** one line per finding: the responding work with its row (risk file update QS22, EU15; change control QS34; CAPA proportional to risk QS18; validation EU19) and the review that accepts it, as the person named it, or "not named".
5. **Record:** "Review draft. Scores, weights, rule and owners are yours. Uncleared AI-assisted draft." or the clearer's name.

## Full mode

### What this ranks
Findings considered (from A1 and A2), the person's criteria and that the scores are theirs.

### Criteria, anchors and weights
| Criterion (higher = more urgent) | 0 means | 2 means | 4 means | Weight |
|---|---|---|---|---|

### Facts behind the scores
| Finding | Criterion 1 | Criterion 2 | ... |
|---|---|---|---|
Each cell: the fact with its source, then the person's score in brackets.

### Ranking
| Finding | Value estimate | Contributions by criterion |
|---|---|---|
Method: as returned by the tool, with its citation.

### How robust
For adjacent pairs, the weight at which they swap. The close call named.

### Repair plan
| Finding | Responding work | Owner you named | Your release rule met? | Review that accepts the repair | Depends on |
|---|---|---|---|---|---|

Sequenced by dependency, not by date.

### Record
Release, CAPA and audit-response decisions stop for the owner. Cleared by NAME, or uncleared. AI-assisted draft.
