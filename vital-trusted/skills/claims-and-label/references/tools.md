# Tools and companion slot

## Companion slot

No companion exists for this skill at launch. The method runs fully on the label or
intended-purpose statement the person supplies. This skill never calls VERIFY directly
and never describes a label or review check that did not run (TR-H4).

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Label and intended use | Fetch the current approved label for the named market and version, and compare each product statement with its indication, population and dose wording | No companion yet. Candidate: label source (`trusted-capability-map`, `references/tools.md`) | Method runs on the supplied label; whether that label is current and approved in the market is `[GAP: not checkable here — …]`; check line says "not tool-checked" |
| Promotional boundary | Prepare the piece for the company's promotional or medical review: route it, attach the label and references, record reviewer comments | No companion yet. Candidate: MLR preparation | Method runs; the note names the kind of process; "not tool-checked" |
| Comparative claims | Test the comparison against the passage of the head-to-head study it rests on | VERIFY `check_claim`, through `claim-assessment`, when VERIFY is connected | Method runs (five questions); whether the study says what the comparison claims is "not tool-checked" |

Hand-off rule: a comparison that has a supplied direct study goes to `claim-assessment`
for the support check, which owns the VERIFY contract. This skill did not read VERIFY's
argument or return contracts `[CHECK]` that the hand-off matches the final
`claim-assessment` scope.

## Script

### `scripts/find_claim_cues.py`

Lists wording that usually marks a statement this skill should look at. It finds words,
not claims or uses, and makes no judgment: read the whole draft against the label as
well.

```
python scripts/find_claim_cues.py draft.txt
python scripts/find_claim_cues.py draft.txt --json
cat draft.txt | python scripts/find_claim_cues.py -
```

Cue groups:

| Group | Examples it finds | Task |
|---|---|---|
| comparison | better, faster, more effective, safer, superior, outperforms, versus, vs, compared with, head-to-head | Comparative claims |
| absolute or superlative | first, only, leading, best, number one, unique, unmatched, gold standard (not "first-line") | Comparative claims |
| safety absolute | safe, safely, no side effects, harmless, risk-free, well tolerated | Comparative claims; then `patient-safety` |
| device function | diagnose, detect, predict, prevent, cure, rule out, screen for, replaces a visit | Label and intended use |
| population or line of therapy | children, adolescents, teenagers, pediatric, elderly, pregnant, first-line, second-line, monotherapy, in combination with, mild, all patients | Label and intended use |
| unapproved status | off-label, unlicensed, unapproved, not approved, investigational, coming soon | Label and intended use; Promotional boundary |
| promotional tone | game-changing, breakthrough, revolutionary, proven, guaranteed, miracle, switch to, ask your doctor about, don't wait, exclamation mark | Promotional boundary |

Each row: line number, group, the matched words, and the line.

Tested on 20 October 2026 against `scripts/test_input.txt` with
`python3 scripts/test_find_claim_cues.py` (expected groups per line asserted).
