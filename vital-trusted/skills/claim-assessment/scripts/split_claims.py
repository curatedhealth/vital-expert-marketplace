#!/usr/bin/env python3
"""Manual claim split for claim-assessment (VITAL TRUSTED, TR-8.1.1).

Splits a text into sentences with start and end offsets that slice back to the exact
input, and flags priority signals for ranking. It is a manual aid used when the VERIFY
connector is not connected. It never decides support. Output is labeled
"manual split, not tool-checked".

Usage:
    python split_claims.py text.txt
    python split_claims.py text.txt --json
    python split_claims.py --self-test
"""
import json
import re
import sys

LABEL = "manual split, not tool-checked"

# Words after which a period does not end a sentence.
ABBREVIATIONS = {
    "e.g", "i.e", "vs", "etc", "dr", "prof", "mr", "mrs", "ms", "no", "fig", "approx",
    "al", "ca", "cf", "inc", "ltd", "st", "jan", "feb", "mar", "apr", "jun", "jul",
    "aug", "sep", "sept", "oct", "nov", "dec",
}

FLAGS = {
    "number": re.compile(r"\d"),
    "comparison": re.compile(
        r"\b(more|less|fewer|greater|higher|lower|better|worse|superior|inferior|"
        r"first|only|largest|leading|best|than|versus|vs\.?|compared)\b", re.I),
    "quote": re.compile(r"[\"“”]"),
    "efficacy_or_safety": re.compile(
        r"\b(efficac\w*|effective\w*|improv\w*|reduc\w*|cuts?|response|remission|"
        r"surviv\w*|safe\w*|toleran?\w*|tolerated|side[- ]effects?|adverse|"
        r"discontinu\w*|risk\w*|admissions?|events?)\b", re.I),
    "causal": re.compile(
        r"\b(because|due to|caused?|leads? to|led to|results? in|thanks to|drives?)\b",
        re.I),
    "named_title": re.compile(r"\b(Dr|Prof|Professor|Mr|Mrs|Ms)\.?\s+[A-Z]"),
    "compliance_or_performance": re.compile(
        r"\b(approved|approval|recommended|guidelines?|certified|compliant|validated|"
        r"standard of care|saves?|savings?)\b", re.I),
    "unnamed_authority": re.compile(
        r"\b(experts? (agree|say|believe)|studies (show|suggest)|research shows|"
        r"it is (well )?known)\b", re.I),
    "recommendation": re.compile(r"\b(should|must|ought to|we recommend)\b", re.I),
}

PRIORITY_1 = {"number", "quote", "efficacy_or_safety", "named_title",
              "compliance_or_performance"}
PRIORITY_2 = {"comparison", "causal", "unnamed_authority"}


def _is_boundary(text, i):
    """True if the terminator at text[i] ends a sentence."""
    ch = text[i]
    if ch in "!?":
        return True
    if ch != ".":
        return False
    # Decimal point: digit on both sides.
    if 0 < i < len(text) - 1 and text[i - 1].isdigit() and text[i + 1].isdigit():
        return False
    # Abbreviation: the word immediately before the period.
    m = re.search(r"([A-Za-z.]+)$", text[:i])
    if m and m.group(1).lower().rstrip(".") in ABBREVIATIONS:
        return False
    # Must be followed by whitespace (optionally after closing quotes/brackets) or end.
    j = i + 1
    while j < len(text) and text[j] in "\"'”)]":
        j += 1
    return j >= len(text) or text[j].isspace()


def split(text):
    """Return a list of (start, end) spans covering each sentence, trimmed of
    surrounding whitespace, so that text[start:end] is the sentence exactly."""
    spans = []
    start = 0
    n = len(text)
    i = 0
    while i < n:
        if text[i] in ".!?" and _is_boundary(text, i):
            end = i + 1
            while end < n and text[end] in "\"'”)]":
                end += 1
            spans.append((start, end))
            start = end
            i = end
            continue
        if text[i] == "\n" and i + 1 < n and text[i + 1] == "\n":
            spans.append((start, i))
            start = i
        i += 1
    if start < n:
        spans.append((start, n))
    out = []
    for s, e in spans:
        while s < e and text[s].isspace():
            s += 1
        while e > s and text[e - 1].isspace():
            e -= 1
        if e > s:
            out.append((s, e))
    return out


def flags_for(sentence):
    return [name for name, rx in FLAGS.items() if rx.search(sentence)]


def priority(flags):
    if PRIORITY_1 & set(flags):
        return 1
    if PRIORITY_2 & set(flags):
        return 2
    if "recommendation" in flags:
        return "recommendation"
    return 3


def analyze(text):
    claims = []
    for k, (s, e) in enumerate(split(text), 1):
        sent = text[s:e]
        f = flags_for(sent)
        claims.append({"id": k, "start": s, "end": e, "text": sent,
                       "flags": f, "priority": priority(f)})
    return {"method": LABEL, "characters": len(text), "claims": claims}


def render(result):
    lines = [f"Claims ({result['method']}); {len(result['claims'])} sentences"]
    for c in result["claims"]:
        fl = ", ".join(c["flags"]) or "none"
        lines.append(f"{c['id']:>3}. [{c['start']}:{c['end']}] priority {c['priority']} "
                     f"({fl})")
        lines.append(f"     {c['text']}")
    lines.append("Flags are signals for ranking, not a support result.")
    return "\n".join(lines)


def self_test():
    sample = ('Velostra cuts admissions by 40%, as shown in the NORLA trial of 1,850 '
              'patients. Prof. Anna Keller calls it "a new standard of care". '
              'Mean age was 71.5 years, e.g. older adults vs. younger ones.\n\n'
              'Payers should prioritize Velostra. Experts agree it is well tolerated!')
    r = analyze(sample)
    texts = [c["text"] for c in r["claims"]]
    assert len(texts) == 5, texts
    for c in r["claims"]:
        assert sample[c["start"]:c["end"]] == c["text"]
    assert texts[2].startswith("Mean age was 71.5 years, e.g. older"), texts[2]
    assert "named_title" in r["claims"][1]["flags"]
    assert "quote" in r["claims"][1]["flags"]
    assert r["claims"][0]["priority"] == 1
    assert r["claims"][3]["priority"] == "recommendation"
    assert "unnamed_authority" in r["claims"][4]["flags"]
    assert analyze("")["claims"] == []
    assert analyze("No terminator here")["claims"][0]["text"] == "No terminator here"
    print("self-test passed: 5 sentences, offsets round-trip, flags as expected")


def main(argv):
    if "--self-test" in argv:
        self_test()
        return 0
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    with open(paths[0], encoding="utf-8") as fh:
        text = fh.read()
    result = analyze(text)
    if "--json" in argv:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(render(result))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
