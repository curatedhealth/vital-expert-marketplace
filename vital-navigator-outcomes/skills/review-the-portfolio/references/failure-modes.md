# Failure modes: review-the-portfolio

| Id | Failure | Status | Detection / repair |
|---|---|---|---|
| FM-01 | Invented figure, name, quote or peer comp | [CHECK] | ground-the-numbers; leave [GAP]; never bless a guess |
| FM-02 | Assistant scored or chose for the team | [CHECK] | Scripts and gates refuse; rewind to human entry |
| FM-03 | Claim-bearing board text without Verify or not tool-checked label | [CHECK] | handoff-verify before compile-board-pack seals |
| FM-04 | Chart that oversells (cropped axis, relative without absolute) | [CHECK] | frame-exhibits-honestly / exhibit_check |
| FM-05 | Routed Launch / DD / READY work into this plugin | [CHECK] | route-the-entry Not covered; stop and name sibling plugin |


## Gap rules (from pack)

# Gap rules

A gap is a fact the review needs that nobody has supplied or no source states. Write `[GAP]` with the reason and what would close it. Never fill one from general knowledge.

| Kind | How to word it |
|---|---|
| No declared range | "[GAP] No value range was declared; realized value cannot be placed." |
| Realized figure not measured | "[GAP] The figure is an estimate, not a measurement; not counted as realized." |
| No source or date | "[GAP] The realized figure has no source and date." |
| Unit or period mismatch | "[GAP] The realized figure is in [unit/period], the range in [unit/period]." |
| Outcome not measured | "[GAP] The outcome has no measured result; value cannot be counted." |
| Activity traces to no outcome | "Traces to no outcome: restate against one or retire." |
| No reason | "[GAP] [activity]: no reason for stop, keep or fix." |
| No steward | "[GAP] No named steward for the re-score; nothing changes." |
| Direction change with one name | "[GAP] A change to direction needs two named people." |

Who said it: the owner's statements are O; another named person's are O with their name; a relayed view is "relayed by [name]".

In the full report list every gap, most blocking first; merge those that close the same way. In a direct answer, at most three.
