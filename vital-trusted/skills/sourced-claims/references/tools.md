# Tools and companion slot

## Companion slot

This skill uses no tool. It hands finished work to the Prove skills, which run by hand.

| Task | What a companion would do | Handed to | Without it |
|---|---|---|---|
| Every claim sourced | Compare each sourced claim with the quoted passage it rests on | `claim-assessment`, by hand | Method runs; check line says "not tool-checked" |
| Right type of source | Qualify a specific source (type, peer review, funding, fit for the question) and check whether it is current or superseded | `source-assessment`, by hand (a source card) | Method names the type and whether it fits; anything about the specific source beyond its type is left open in plain words; "not tool-checked" |
| Specific citations | Build a plain citation from a supplied source | `citation-and-record`, by hand | Method lists fields from the supplied source; "citation not tool-checked" |

## Script

### `scripts/find_source_cues.py`

Lists wording that usually marks a claim needing a source or a citation needing work.
It finds wording, not claims: read the whole draft as well.

```
python scripts/find_source_cues.py draft.txt
python scripts/find_source_cues.py draft.txt --json
cat draft.txt | python scripts/find_source_cues.py -
```

Cue groups:

| Group | Examples it finds |
|---|---|
| vague authority | studies show, research suggests, experts agree, data suggest, it is well known, guidelines recommend |
| unnamed regulator or guidance | per FDA guidance, EMA guidelines, according to NICE (with no title or year nearby) |
| superlative or first | leading, first, only, best, most prescribed, gold standard, number one |
| undated current | current, latest, now, recently, new (with no year on the same line) |
| weak source type | press release, blog, news, preprint, abstract, poster, data on file, internal |
| incomplete citation | "Name et al." or "Name 2023" with no DOI or PMID on the line; bare "data on file" |
| figure | a number with % or a ratio such as "1 in 20" with no bracketed source on the line |

Each row: line number, group, the matched words, and the line. It makes no judgment.

Tested on 20 October 2026 against `scripts/test_input.txt` with
`python3 scripts/test_find_source_cues.py` (expected groups per line asserted).
