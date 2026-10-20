#!/usr/bin/env python3
"""Compare the numbers and units in an original text and its translation.

Reads both texts with their own number conventions (for example English 1,000.5 and
German 1.000,5), so a change of notation is not reported as a change of value. Reports:
  - values in the original that do not appear in the translation
  - values in the translation that do not appear in the original
  - values that appear with a different symbol unit (mg vs µg, % vs nothing)

Only symbol units that do not change between languages are compared (mg, µg, mcg, g,
kg, mL, L, mmol/L, mg/dL, IU, %). Word units (weeks, Wochen) and numbers written as words
(two, zwei) are not compared; read them by hand.

A clean comparison means the digits match. It does not mean the meaning matches.

Usage:
  python compare_numbers.py original.txt translation.txt --source-locale en --target-locale de
  python compare_numbers.py original.txt translation.txt --json
"""

import argparse
import json
import re
import sys
from collections import Counter

UNITS = ["mmol/L", "mmol/l", "mg/dL", "mg/dl", "mg/kg", "µg", "μg", "mcg", "mg", "kg", "g",
         "mL", "ml", "L", "IU", "I.E.", "%"]
UNIT_CANON = {"mmol/l": "mmol/L", "mg/dl": "mg/dL", "μg": "µg", "mcg": "µg", "ml": "mL",
              "I.E.": "IU"}

UNIT_RE = "|".join(re.escape(u) for u in sorted(UNITS, key=len, reverse=True))

NUMBER_RE = {
    # English: 1,234.5 or 1234.5 or 0.5
    "en": re.compile(r"(?<![\w.,])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)(?![\d])\s?(" + UNIT_RE + r")?(?![A-Za-z])"),
    # German and most continental European: 1.234,5 or 1234,5 or 0,5 (also space and Swiss apostrophe groups)
    "de": re.compile(r"(?<![\w.,])(\d{1,3}(?:[.   '’]\d{3})+(?:,\d+)?|\d+(?:,\d+)?)(?![\d])\s?(" + UNIT_RE + r")?(?![A-Za-z])"),
}
NUMBER_RE["fr"] = NUMBER_RE["de"]
NUMBER_RE["it"] = NUMBER_RE["de"]
NUMBER_RE["es"] = NUMBER_RE["de"]


def to_value(raw, locale):
    if locale == "en":
        clean = raw.replace(",", "")
    else:
        clean = re.sub(r"[.   '’]", "", raw).replace(",", ".")
    value = float(clean)
    return int(value) if value.is_integer() else value


def extract(text, locale):
    pattern = NUMBER_RE[locale]
    items = []
    for match in pattern.finditer(text):
        raw, unit = match.group(1), match.group(2)
        unit = UNIT_CANON.get(unit, unit) if unit else ""
        items.append({"raw": raw, "value": to_value(raw, locale), "unit": unit,
                      "context": " ".join(text[max(0, match.start() - 30):match.end() + 30].split())})
    return items


def compare(source_text, target_text, source_locale="en", target_locale="de"):
    src = extract(source_text, source_locale)
    tgt = extract(target_text, target_locale)
    src_vals = Counter(i["value"] for i in src)
    tgt_vals = Counter(i["value"] for i in tgt)
    missing = src_vals - tgt_vals
    added = tgt_vals - src_vals
    unit_changes = []
    src_units = Counter((i["value"], i["unit"]) for i in src if i["unit"])
    tgt_units = Counter((i["value"], i["unit"]) for i in tgt)
    for (value, unit), count in src_units.items():
        if tgt_units.get((value, unit), 0) < count and value in tgt_vals:
            found = sorted({i["unit"] or "(none)" for i in tgt if i["value"] == value})
            unit_changes.append({"value": value, "original_unit": unit, "translation_units": found})
    return {
        "note": "Digits and symbol units only. Matching digits do not mean the meaning matches.",
        "original_numbers": len(src),
        "translation_numbers": len(tgt),
        "missing_from_translation": [
            {"value": v, "count": c, "context": [i["context"] for i in src if i["value"] == v][:2]}
            for v, c in missing.items()],
        "added_in_translation": [
            {"value": v, "count": c, "context": [i["context"] for i in tgt if i["value"] == v][:2]}
            for v, c in added.items()],
        "unit_changes": unit_changes,
    }


def report(result):
    lines = [f"Original: {result['original_numbers']} numbers. Translation: {result['translation_numbers']} numbers."]
    if not (result["missing_from_translation"] or result["added_in_translation"] or result["unit_changes"]):
        lines.append("Every number in the original appears in the translation with the same symbol unit.")
    for item in result["missing_from_translation"]:
        lines.append(f"  - In the original, not in the translation: {item['value']} (x{item['count']}) ... {item['context'][0]}")
    for item in result["added_in_translation"]:
        lines.append(f"  - In the translation, not in the original: {item['value']} (x{item['count']}) ... {item['context'][0]}")
    for item in result["unit_changes"]:
        lines.append(f"  - Unit differs for {item['value']}: original {item['original_unit']}, translation {', '.join(item['translation_units'])}")
    lines.append(result["note"])
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("original")
    parser.add_argument("translation")
    parser.add_argument("--source-locale", default="en", choices=sorted(NUMBER_RE))
    parser.add_argument("--target-locale", default="de", choices=sorted(NUMBER_RE))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    with open(args.original, encoding="utf-8") as fh:
        source = fh.read()
    with open(args.translation, encoding="utf-8") as fh:
        target = fh.read()
    result = compare(source, target, args.source_locale, args.target_locale)
    print(json.dumps(result, indent=2, ensure_ascii=False) if args.json else report(result))


if __name__ == "__main__":
    sys.exit(main())
