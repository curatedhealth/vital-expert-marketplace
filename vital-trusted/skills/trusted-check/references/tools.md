# Tools and companion slot

## Companion slot per task

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Run the active letters | Each letter skill's own slot (label source, MLR preparation, safety routing, AI policy) would let that letter check instead of ask | No companion yet for any Build letter | Each letter runs as method; checks that need a missing companion read "not checked" in the summary |
| Write the summary | None needed | `scripts/scan_verdicts.py` where code can run | Read the summary once for the words in `references/patterns.md` P1 |
| Run Prove by hand | Compare factual claims with supplied sources, write source cards, count results and list open items, write reference lines and a record note | None. The four Prove skills, run by hand | Name what could not be checked; never invent a result (TR-H4) |

## "Could not be checked" lines for empty slots

Use these plain lines when the letter is active and the check needed the companion:

| Empty slot | Plain line |
|---|---|
| Label source (Rule-compliant, Safe) | "Whether statements about the product match the approved label: no label tool yet, and no label was supplied." (Drop the first half if the person supplied the label and the letter compared it.) |
| MLR preparation | Not listed; promotional review is named as the next process instead |
| Safety routing | Not listed; the safety reporting procedure is named in open items |
| AI policy | "Whether the tool and data use fit your AI policy: checked only against what you told me about it." |
| No sources supplied | See `tasks/prove-handoff.md`, section "When no sources are supplied" |

## Prove order (all by hand)

`trusted-check` calls no tool. It sends the packet to the Prove skills, in this order, and
collects their lines. Every line is labeled "not tool-checked".

| Order | Prove skill | What it does by hand | Gives back |
|---|---|---|---|
| 1 | `source-assessment` | One source card per source: kind, peer review (from evidence), funders and interests, fit, can carry, cannot carry, date in full, currency | A line of counts; no tier, no score |
| 2 | `claim-assessment` | Splits the text into claims and pairs each with an exact quoted passage | The six hand-check results per claim (`claim-assessment/references/statuses.md`) |
| 3 | `confidence-scoring` | Counts by result, open items in order of risk, one recommendation | The open-items summary and the fixed line "No confidence figure: these results were not tool-checked." |
| 4 | `citation-and-record` | Plain reference lines from supplied details; a record note | Reference lines; the record note, cleared only by a named person who reviewed it |
| on request | `citation-and-record` | Evidence table built by hand | The table |

## Script

### `scripts/scan_verdicts.py`

Scans a summary for verdict words and phrases (`references/patterns.md` P1, P2, P3) and
for leaked codes (P8): rule ids, framework codes, skill names, raw gap syntax. Letter
words such as "Safe" and "True" at the start of a row are allowed.

```
python scripts/scan_verdicts.py summary.txt
python scripts/scan_verdicts.py summary.txt --json
python scripts/test_scan_verdicts.py
```

Exit code 0 when nothing is found, 1 when there are hits. Each hit gives the line
number, the words found and why. It also reports a missing or altered closing statement.

Pitfalls:

- It finds words, not meaning. A clean scan is not a clean summary; read it once.
- It allows "Safe" and "True" only as row labels. "Safe to send" is a hit.
