# Tools and companion slot

## Companion slot

No companion exists for this skill and none is planned (product concept §10.2:
"Tangible: no candidate, stays method only"). Do not imitate one (TR-H4).

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Audience and literacy | None planned. A hypothetical companion could hold a company's approved lay glossary and patient wording, so plain terms are looked up rather than chosen | None | Method runs in full; plain-language scan where code can run; check line says "not tool-checked" |
| Deliverable fit | None planned. Nothing here needs a tool beyond counting | None | Method runs in full; "not tool-checked" |
| Translation fidelity | None planned. A hypothetical companion could look up approved product information and approved local terms by product, language and date, so flagged terms become lookups | None | Approved wording comes only from the person; terms without it are flagged for a qualified translator; "not tool-checked" |

VERIFY does not fill these slots. It checks sentences against supplied passages; it does
not judge reader fit, format or translation.

## Scripts

Run them where the host can execute code. Where it cannot, do the same steps by hand.
Tests: `python scripts/test_scripts.py` (12 tests, standard library only).

### `scripts/plain_language_scan.py`

For patient or lay text. Lists sentence lengths (median, mean, longest, and sentences
over a working threshold), long words, abbreviations and whether each is spelled out at
first use, symbols such as < and >, words from a short list of clinician terms, and
words to reread for tone (alarming or falsely reassuring).

```
python scripts/plain_language_scan.py leaflet.txt
python scripts/plain_language_scan.py leaflet.txt --json
python scripts/plain_language_scan.py leaflet.txt --max-words 15 --terms our_terms.txt
cat leaflet.txt | python scripts/plain_language_scan.py -
```

Pitfalls:

- It finds features, not meaning. A short sentence can still be unclear; a listed term
  can be right ("high blood pressure (hypertension)" lists "hypertension" on purpose).
- The 20-word threshold is a working threshold chosen by this skill, not from a
  guideline. The EU guideline says only that long sentences should not be used.
- English only. It gives no readability score or grade level, by design (TR-H3).
- The clinician and tone lists are short prompts, not a dictionary. Add the person's
  own terms with `--terms`.

### `scripts/compare_numbers.py`

For a translation. Reads every number in the original and the translation, each with
its own language's notation (English 1,000.5; German 1.000,5), and lists values missing,
added or with a changed symbol unit.

```
python scripts/compare_numbers.py original.txt translation.txt --source-locale en --target-locale de
python scripts/compare_numbers.py original.txt translation.txt --json
```

Pitfalls:

- Digits and symbol units only (mg, µg, mcg, g, kg, mL, L, mmol/L, mg/dL, IU, %). Word
  units (weeks, Wochen) and numbers written as words (two, zwei) are not compared.
- A clean result means the digits match, not that the meaning matches. Read the
  sentences.
- Supported notations: en, and de / fr / it / es read as decimal comma with dot, space
  or apostrophe grouping (the apostrophe covers Swiss usage, 1'200).
- Values that legitimately appear only once in one language (a footnote number, a
  section number) show as differences; read them before reporting.
