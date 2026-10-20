# Tools and companion slot

## Companion slot

No companion exists for this skill yet. Do not imitate one (TR-H4). VERIFY does not fill
these slots: it checks sentences against supplied passages; it does not hold approved
labels or route safety reports.

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Clinical safety statements | A label-source companion would return the current approved label for a named product, market and formulation, with its revision date, section by section | None yet | Ask the person for the label; quote only what they supply; mark currency `[GAP: not checkable here — whether this is the current approved label — confirm with your regulatory function]` |
| Patient safety language | The same label-source companion, for the approved patient leaflet | None yet | Ask for the leaflet; method runs; "not tool-checked" |
| Side-effect flag | A safety-routing companion would open an intake in the company's safety system with the quoted text and source, and return a receipt reference. It would never assess the case | None yet | Write the flag for the person to pass on; never say it was sent |

When the person quotes their safety procedure, a contact route or a label in the
conversation, use their words as supplied, with their date, and do not extend them. That
is the person's input, not a companion result.

VERIFY may still check, through `claim-assessment`, that a quoted label sentence matches
the supplied label passage. That is a support check on wording, not a safety check.

## Scripts

Run them where the host can execute Python 3. Where it cannot, do the same steps by hand.
Both scripts read files the person supplied; neither sends anything anywhere.

### `scripts/scan_safety_mentions.py`

Lists words and phrases in a text that may signal a possible safety report, by kind
(possible side effect, pregnancy or breastfeeding, overdose or misuse, medication error,
lack of effect, product quality, interaction, hospital or death), with line numbers and
the surrounding words.

With `--patient`, it scans a patient-facing draft instead: phrases of reassurance, advice
about treatment, alarming framing, and whether any route to a doctor, nurse or
pharmacist appears.

```
python scripts/scan_safety_mentions.py notes.txt
python scripts/scan_safety_mentions.py notes.txt --json
python scripts/scan_safety_mentions.py --patient leaflet.txt
cat transcript.txt | python scripts/scan_safety_mentions.py -
```

Pitfalls:

- It finds words, not meaning. "No rash" and "rash" both show. Read each hit.
- It misses paraphrases, other languages, misspellings and symptoms not in its list. A
  clean scan does not mean there is nothing to flag; say so if reporting it.
- It never decides anything. A hit is a reason to read, not a finding, and never a
  grade.
- Its snippets repeat the input, which may hold personal or health details. Keep scan
  output out of any deliverable.

### `scripts/label_match.py`

Compares safety sentences in a draft with the supplied label text. For each draft
sentence that mentions dose, contraindication, warning, interaction or a special
population, it finds the closest label sentence and reports one of: word for word (after
normalizing spaces, case and punctuation), close (similar wording, with any numbers or
units that differ listed), or not found in the supplied label.

```
python scripts/label_match.py label.txt draft.txt
python scripts/label_match.py label.txt draft.txt --json
python scripts/label_match.py label.txt draft.txt --threshold 0.55
```

Pitfalls:

- It compares text only. A word-for-word match does not mean the statement fits the
  reader, the market or the question, and does not mean the label is current.
- "Close" covers both harmless rewording and dangerous changes ("must not" to "should
  not"); read every close match.
- "Not found" means not found in the supplied text, not that the label lacks it, unless
  the complete label was supplied.
- It splits sentences simply; tables pasted as text may split oddly. Check table cells by
  hand.
- An exact part of a longer label sentence counts as word for word and is marked "part
  of a longer label sentence". Check that the part quoted did not drop a condition.

### `scripts/test_scripts.py`

Tests both scripts on invented fixtures (a doctor's email, a market research extract, two
leaflets, a label and a draft). Run `python scripts/test_scripts.py` after any change.
