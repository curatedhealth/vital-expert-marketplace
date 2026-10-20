#!/usr/bin/env python3
"""Plain-language scan for patient-facing or lay text.

Reports, for a text a patient or member of the public will read:
  - sentence lengths (median, mean, longest) and the sentences over a working threshold
  - long words (four or more syllables, by a simple heuristic)
  - abbreviations, and whether each is spelled out at first use
  - symbols lay readers often misread (<, >, <=, >=, +/-, ~)
  - words from a short list of clinician terms
  - words to reread for tone (alarming or falsely reassuring)

It finds features, not meaning. Every hit is a prompt to read the sentence. Nothing it
returns is a readability score or a verdict. The sentence-length threshold (default 20
words) is a working threshold chosen by this skill, not a figure from any guideline.

Usage:
  python plain_language_scan.py text.txt
  python plain_language_scan.py text.txt --json
  python plain_language_scan.py text.txt --max-words 15 --terms extra_terms.txt
  cat text.txt | python plain_language_scan.py -
"""

import argparse
import json
import re
import statistics
import sys

CLINICIAN_TERMS = [
    "adverse event", "adverse reaction", "efficacy", "contraindicated", "contraindication",
    "hepatic", "renal", "titrate", "titration", "subcutaneous", "intravenous",
    "intramuscular", "placebo", "randomized", "randomised", "endpoint", "hazard ratio",
    "confidence interval", "comorbidity", "comorbidities", "prophylaxis", "prophylactic",
    "etiology", "aetiology", "dyspnea", "dyspnoea", "hypertension", "hypotension",
    "hypoglycemia", "hypoglycaemia", "myocardial infarction", "tolerability",
    "pharmacokinetic", "monotherapy", "adjunctive", "baseline", "statistically significant",
    "dose-dependent", "incidence", "concomitant", "oral administration", "indicated for",
    "first-line", "second-line", "regimen", "sequelae", "idiopathic", "asymptomatic",
    "symptomatic", "exacerbation", "remission", "prognosis", "pruritus", "edema", "oedema",
    "nausea and emesis", "emesis", "arrhythmia", "anaphylaxis", "hematologic",
    "haematologic", "neutropenia", "thrombocytopenia", "glycemic", "glycaemic",
]

TONE_TERMS = [
    # can alarm
    "fatal", "deadly", "dangerous", "life-threatening", "catastrophic", "devastating",
    "severe risk", "toxic",
    # can falsely reassure
    "nothing to worry about", "no need to worry", "completely safe", "totally safe",
    "perfectly safe", "risk-free", "risk free", "no side effects", "harmless",
    "guaranteed", "always works", "cure", "cures", "100% effective",
]

SYMBOL_PATTERN = re.compile(r"(<=|>=|≤|≥|±|\+/-|(?<![\w-])~(?=\s?\d)|(?<=\s)[<>](?=\s?\d)|^[<>](?=\s?\d))", re.M)

ABBREV_PATTERN = re.compile(r"\b(?=[A-Za-z0-9]*[A-Z][A-Za-z0-9]*[A-Z])[A-Za-z][A-Za-z0-9]{1,7}\b")

# Words that look like abbreviations but are ordinary in text.
ABBREV_IGNORE = {"I", "OK", "TV", "US", "UK", "EU"}

NO_SPLIT = ["e.g.", "i.e.", "Dr.", "Mr.", "Mrs.", "Ms.", "vs.", "etc.", "approx.", "No.", "Fig."]


def split_sentences(text):
    protected = text
    for i, abbr in enumerate(NO_SPLIT):
        protected = protected.replace(abbr, f"\x00{i}\x00")
    protected = re.sub(r"(\d)\.(\d)", "\\1\x01\\2", protected)
    # Bullet lines and blank lines end a sentence too.
    chunks = re.split(r"(?<=[.!?])\s+|\n\s*\n|\n\s*[-*•]\s+|\n(?=\s*\d+[.)]\s)", protected)
    sentences = []
    for chunk in chunks:
        if chunk is None:
            continue
        restored = chunk.replace("\x01", ".")
        for i, abbr in enumerate(NO_SPLIT):
            restored = restored.replace(f"\x00{i}\x00", abbr)
        restored = " ".join(restored.split()).lstrip("-*• ").strip()
        if restored and re.search(r"[A-Za-z]", restored):
            sentences.append(restored)
    return sentences


def words_of(sentence):
    return re.findall(r"[A-Za-z][A-Za-z'’-]*|\d+(?:[.,]\d+)?", sentence)


def syllables(word):
    w = word.lower().strip("'’-")
    if not w.isalpha():
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    groups = re.findall(r"[aeiouy]+", w)
    return max(1, len(groups))


def find_terms(text, terms):
    hits = []
    lower = text.lower()
    for term in terms:
        pattern = r"(?<![a-z])" + re.escape(term.lower()) + r"(?:s|es)?(?![a-z])"
        count = len(re.findall(pattern, lower))
        if count:
            hits.append({"term": term, "count": count})
    return hits


def find_abbreviations(text):
    results = {}
    for match in ABBREV_PATTERN.finditer(text):
        token = match.group(0)
        if token in ABBREV_IGNORE or token.isdigit():
            continue
        if token in results:
            results[token]["count"] += 1
            continue
        start, end = match.span()
        before = text[max(0, start - 2):start]
        after = text[end:end + 2]
        # Spelled out at first use: "full words (ABC)" or "ABC (full words)".
        in_parens_after_words = before.endswith("(") and re.search(r"[a-z]{3,}\s*\($", text[max(0, start - 40):start] or "")
        followed_by_expansion = after.startswith(" (") and re.match(r"\s\([a-z]", text[end:end + 4] or "")
        results[token] = {
            "abbreviation": token,
            "count": 1,
            "spelled_out_at_first_use": bool(in_parens_after_words or followed_by_expansion),
        }
    return list(results.values())


def scan(text, max_words=20, extra_terms=None):
    sentences = split_sentences(text)
    lengths = [len(words_of(s)) for s in sentences]
    long_sentences = [
        {"words": n, "sentence": s} for s, n in zip(sentences, lengths) if n > max_words
    ]
    all_words = [w for s in sentences for w in words_of(s)]
    long_words = {}
    for w in all_words:
        if syllables(w) >= 4:
            key = w.lower()
            long_words[key] = long_words.get(key, 0) + 1
    terms = CLINICIAN_TERMS + (extra_terms or [])
    return {
        "note": "Features to reread, not findings. No readability score is given.",
        "sentences": len(sentences),
        "words": len(all_words),
        "sentence_length": {
            "median": statistics.median(lengths) if lengths else 0,
            "mean": round(statistics.mean(lengths), 1) if lengths else 0,
            "longest": max(lengths) if lengths else 0,
            "working_threshold": max_words,
            "over_threshold": len(long_sentences),
        },
        "long_sentences": long_sentences,
        "long_words": [{"word": k, "count": v} for k, v in sorted(long_words.items())],
        "abbreviations": find_abbreviations(text),
        "symbols": sorted({m.group(0).strip() for m in SYMBOL_PATTERN.finditer(text)}),
        "clinician_terms": find_terms(text, terms),
        "tone_terms": find_terms(text, TONE_TERMS),
    }


def report(result):
    sl = result["sentence_length"]
    lines = [
        f"{result['sentences']} sentences, {result['words']} words.",
        f"Sentence length: median {sl['median']}, mean {sl['mean']}, longest {sl['longest']}; "
        f"{sl['over_threshold']} over {sl['working_threshold']} words (working threshold, not a rule).",
    ]
    for item in result["long_sentences"]:
        lines.append(f"  - ({item['words']} words) {item['sentence']}")
    if result["long_words"]:
        lines.append("Long words to reread: " + ", ".join(
            f"{w['word']} ({w['count']})" for w in result["long_words"]))
    unexplained = [a for a in result["abbreviations"] if not a["spelled_out_at_first_use"]]
    if result["abbreviations"]:
        lines.append(f"Abbreviations: {len(result['abbreviations'])}, "
                     f"{len(unexplained)} not spelled out at first use: "
                     + ", ".join(a["abbreviation"] for a in unexplained))
    if result["symbols"]:
        lines.append("Symbols lay readers often misread: " + " ".join(result["symbols"]))
    if result["clinician_terms"]:
        lines.append("Clinician terms: " + ", ".join(
            f"{t['term']} ({t['count']})" for t in result["clinician_terms"]))
    if result["tone_terms"]:
        lines.append("Words to reread for tone: " + ", ".join(
            f"{t['term']} ({t['count']})" for t in result["tone_terms"]))
    lines.append(result["note"])
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("path", help="text file, or - for standard input")
    parser.add_argument("--max-words", type=int, default=20)
    parser.add_argument("--terms", help="file with one extra term per line")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()
    extra = []
    if args.terms:
        with open(args.terms, encoding="utf-8") as fh:
            extra = [line.strip() for line in fh if line.strip()]
    result = scan(text, args.max_words, extra)
    print(json.dumps(result, indent=2, ensure_ascii=False) if args.json else report(result))


if __name__ == "__main__":
    main()
