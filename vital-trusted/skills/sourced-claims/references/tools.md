# Tools and companion slot

## Companion slot

No companion is connected to this skill at launch. It hands finished work to the Prove
skills, which own the VERIFY tool calls and their interpretation. This skill never calls
VERIFY directly.

| Task | What a companion would do | Tool (through which skill) | Without it |
|---|---|---|---|
| Every claim sourced | Test each sourced claim against the quoted passage it rests on | VERIFY `check_claim`, `verify_text`, through `claim-assessment` | Method runs; check line says "not tool-checked" |
| Right type of source | Qualify a specific source (type, peer review, funding, fit for the question) and check whether it is current or superseded | VERIFY `qualify_source`, `check_currency`, `ingest_document`, through `source-assessment` | Method names the type and whether it fits; specific grading marked `[GAP: not checkable here — …]`; "not graded with a tool" |
| Specific citations | Build a formatted citation from a supplied or fetched source | VERIFY `build_citation`, through `citation-and-record` | Method lists fields from the supplied source; "citation not built or checked with a tool" |

Tool names are as the VERIFY connector lists them. This skill did not read their
argument or return contracts; those are recorded in the Prove skills. `[CHECK]` that the
three hand-offs above match the final Prove skill scopes.

A future companion that could fill a slot here: a company reference library (approved
references and data on file with their identifiers), which would let the specific
citations task match claims to approved references instead of asking. Candidate, not a
commitment. `[CHECK: not in the concept's candidate list; for the owner to decide]`

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
