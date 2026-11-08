# Failure modes: size-value-at-stake

| Id | Failure | Status | Detection / repair |
|---|---|---|---|
| FM-01 | Invented figure, name, quote or peer comp | [CHECK] | ground-the-numbers; leave [GAP]; never bless a guess |
| FM-02 | Assistant scored or chose for the team | [CHECK] | Scripts and gates refuse; rewind to human entry |
| FM-03 | Claim-bearing board text without Verify or not tool-checked label | [CHECK] | handoff-verify before compile-board-pack seals |
| FM-04 | Chart that oversells (cropped axis, relative without absolute) | [CHECK] | frame-exhibits-honestly / exhibit_check |
| FM-05 | Routed Launch / DD / READY work into this plugin | [CHECK] | route-the-entry Not covered; stop and name sibling plugin |


## Gap rules (from pack)

# Gap rules

A gap is a fact the value case needs that nobody has supplied or no source states. Write `[GAP]` with the reason and what would close it. Never fill a gap from general knowledge; never let a gap become an assumption silently.

| Kind | Example | How to word it |
|---|---|---|
| No basis for a figure | "We think it's big" with no number | "[GAP] No basis for the range yet. A baseline measurement or a small pilot would give one." |
| External figure without a primary source | "Industry says 30% savings" | "[GAP] External figure removed: no primary source named." |
| Not scored | A scorer did not return the sheet | "[GAP] Not scored by [name]; no score was filled in." |
| Not in the library | No driver matches | "[GAP] No library driver matched; kept in the person's words." |
| Not readable by the connector | Outcome links at levels 1 and 2 | "[GAP] The library's outcome links are readable only at driver level." |
| No outcome for a driver | A chosen driver with no outcome | "[GAP] No outcome yet contributes to [driver]; its value cannot be proven." |

Rules:

- A missing library row is never evidence that the value does not exist.
- A wide range is not a gap; it is honest. A range with no basis is a gap.
- In the full report list every gap, most blocking first. In a direct answer, at most three.
