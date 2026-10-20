# Tools and companion slot

## Companion slot

No companion exists for this skill yet. Do not imitate one (TR-H4).

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Jurisdiction | An MLR preparation companion would hold the company's market templates and the approved label per market, and return which market's wording, approval and channels apply | None yet | Ask the market; work from the label the person supplies; check line says "not tool-checked" |
| Required statements | The same companion would return the company's element list for this material and market, and draw the job code, date and current PI link from the approval system | None yet | Placeholders for the person to fill; `[GAP: not checkable here — current approved version — your approval system]` |
| Privacy in the output | A privacy companion could apply the company's minimum-count rule and its consent records | None yet | Ask the privacy function; never set a threshold |

VERIFY does not fill these slots. It checks sentences against supplied passages; it does
not hold market rules, templates, codes or consent records.

When the person supplies a template, element list or minimum count from their company,
use it as given, with its date, and do not extend it. That is the person's input, not a
companion result.

## Script

### `scripts/scan_output.py`

A cue scan of a draft, run where the host can execute code.

```
python scripts/scan_output.py draft.txt --statements --market UK
python scripts/scan_output.py draft.txt --data
python scripts/scan_output.py draft.txt --statements --data --market CH --json
cat draft.txt | python scripts/scan_output.py - --data --small-count 10
```

`--statements` lists, for the market given (UK, EU, CH, US or unknown), the elements
usually expected from `references/rules.md`, and for each the lines where a cue word was
found or "no cue found". `--data` lists formats that can point to a person (a title
followed by a name, dates, ages, record-like numbers, email addresses, phone numbers)
and small counts next to words like "patients" or "cases", masked.

`--small-count` sets the cutoff for listing counts (default 10). It is a listing
cutoff for the person to read, not a privacy threshold; the privacy function sets that.

Pitfalls:

- It finds words, not meaning. "Prescribing information" in a sentence is not a PI. A
  "no cue found" is a place to look, not a finding that the element is missing, and a
  cue found is not a finding that the element is there or correct.
- Names without a title, a bare age ("67,"), villages, jobs and patient stories are
  not found. A clean data scan does not make a text anonymous; say so when reporting
  it.
- It never prints a full identifier. Read the masked hits in the draft itself.
- Tests: `python scripts/test_scan_output.py`.
