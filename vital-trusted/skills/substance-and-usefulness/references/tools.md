# Tools and companion slot

## Companion slot

No companion exists for this skill and none is planned (product concept v0.4, §10.2:
Tangible stays method only). Usefulness is judged by reading against the reader's job;
there is nothing for a tool to verify. Do not imitate one (TR-H4).

| Task | What a companion would do, if one were ever built | Tool | Without it |
|---|---|---|---|
| Specificity | Fetch the person's own figures, owners and dates from systems they name (plan, CRM, project tracker), so a specific comes from a source rather than a question | None | Ask the person; leave gaps; check line says "not tool-checked" |
| No fluff | Nothing beyond the script below | None | Method and script run |
| So what | Read the person's plan or objectives document to know the reader's job | None | Read the context card; ask once |
| Actionability | Read the action log or tracker to find owners and dates already agreed | None | Ask; leave `needs a decision` gaps |
| Structure integrity | Read the company's standard templates, so a mandated structure is not flagged | None | Ask whether a template applies |

VERIFY does not fill these slots. It checks sentences against supplied passages; when a
new specific or "so what" is added and VERIFY is connected, it goes to
`claim-assessment` like any other sentence, through `trusted-check`.

## Script

### `scripts/scan_fluff.py`

A deterministic scan of a draft, run where the host can execute code. It lists, with
line numbers:

- buzzword hits from a fixed list (`leverage`, `synergies`, `holistic`, `robust`,
  `landscape`, `ecosystem`, `unlock`, `best practices`, `paradigm shift`, and others in
  the script);
- throat-clearing openings at the start of a sentence ("in today's…", "it is important
  to note", "as we all know", "this document aims to");
- vague words that often hide a missing who, how much or by when ("stakeholders",
  "significant", "strong", "soon", "going forward", "various");
- stacked hedges (two or more of "may", "might", "potentially", "possibly", "somewhat"
  in one sentence);
- near-duplicate sentence pairs (word overlap at or above a threshold, default 0.6).

```
python scripts/scan_fluff.py draft.txt
python scripts/scan_fluff.py draft.txt --json
python scripts/scan_fluff.py draft.txt --dup-threshold 0.5
cat draft.txt | python scripts/scan_fluff.py -
python scripts/test_scan_fluff.py
```

Pitfalls:

- It finds words, not meaning. "Robust" in a statistics sentence and "landscape" as a
  slide title are hits that are not fluff. Read every hit; never report raw counts as
  findings (TR-H9).
- It does not find a missing "so what", a missing owner or an invented framework. Those
  need reading.
- The near-duplicate check compares word sets; it misses a point repeated in different
  words and can pair two sentences that share many common words. Read each pair.
- A clean scan does not mean the draft is useful.
