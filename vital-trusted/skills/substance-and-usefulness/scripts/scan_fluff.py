#!/usr/bin/env python3
"""Scan a draft for filler, buzzwords, throat-clearing openings, vague words,
stacked hedges and near-duplicate sentences.

Every hit is a prompt to read the sentence, not a finding. A listed word can carry
meaning ("robust to sensitivity analyses"). The script never judges usefulness.

Usage:
    python scan_fluff.py draft.txt
    python scan_fluff.py draft.txt --json
    python scan_fluff.py draft.txt --dup-threshold 0.5
    cat draft.txt | python scan_fluff.py -
"""

import argparse
import json
import re
import sys

BUZZWORDS = [
    "leverage", "leveraging", "leveraged", "synergy", "synergies", "synergistic",
    "holistic", "holistically", "robust", "landscape", "ecosystem", "unlock",
    "unlocking", "best practice", "best practices", "best-in-class", "world-class",
    "paradigm shift", "game changer", "game-changer", "move the needle", "value-add",
    "value add", "end-to-end", "seamless", "seamlessly", "cutting-edge",
    "deep dive", "actionable insights", "drive engagement", "strategic alignment",
    "low-hanging fruit", "circle back", "touch base", "impactful", "transformational",
]

OPENERS = [
    r"in today'?s\b", r"in an? (?:ever|rapidly|increasingly)[- ]\w+",
    r"it is (?:important|worth|critical|essential) to (?:note|mention|highlight|remember)",
    r"as we all know", r"needless to say", r"it goes without saying",
    r"this (?:document|slide|deck|paper|update|note|email) (?:aims|seeks|is intended) to",
    r"the purpose of this (?:document|slide|deck|paper|update|note|email) is",
    r"we are pleased to (?:share|present|provide)",
]

VAGUE = [
    "stakeholders", "key stakeholders", "significant", "significantly", "strong",
    "strongly", "solid", "substantial", "considerable", "various", "numerous",
    "several", "many", "soon", "shortly", "going forward", "near term", "near-term",
    "in due course", "initiatives", "activities", "optimize", "optimise",
    "address gaps", "way forward", "next level",
]

HEDGES = ["may", "might", "could", "potentially", "possibly", "somewhat",
          "perhaps", "arguably", "relatively"]

STOP = set("""a an the and or but of to in on for with at by from as is are was were be
been being this that these those it its we our you your they their he she his her
will would should can do does did has have had not no so than then there here also""".split())


def _phrase_re(phrase):
    parts = [re.escape(p) for p in re.split(r"[\s-]+", phrase)]
    return re.compile(r"(?<![\w-])" + r"[\s-]+".join(parts) + r"(?![\w-])", re.IGNORECASE)


BUZZ_RE = [(w, _phrase_re(w)) for w in BUZZWORDS]
VAGUE_RE = [(w, _phrase_re(w)) for w in VAGUE]
OPENER_RE = [re.compile(r"^\s*(?:[-*•]\s*)?" + p, re.IGNORECASE) for p in OPENERS]
HEDGE_RE = re.compile(r"\b(" + "|".join(HEDGES) + r")\b", re.IGNORECASE)
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(\[])")


def sentences(text):
    """Return (line_number, sentence) pairs. Lines are 1-based."""
    out = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        for s in SENT_SPLIT.split(line):
            s = s.strip()
            if s:
                out.append((lineno, s))
    return out


def _dedupe_overlaps(hits):
    """Drop a hit whose span sits inside a longer hit on the same sentence."""
    hits.sort(key=lambda h: (h[0], -(h[2] - h[1])))
    kept = []
    for h in hits:
        if any(k[0] == h[0] and k[1] <= h[1] and h[2] <= k[2] for k in kept):
            continue
        kept.append(h)
    return kept


def _word_hits(sents, patterns, kind):
    raw = []
    for idx, (lineno, s) in enumerate(sents):
        for word, rx in patterns:
            for m in rx.finditer(s):
                raw.append((idx, m.start(), m.end(), word, lineno, s))
    return [{"kind": kind, "line": h[4], "term": h[3], "sentence": h[5]}
            for h in _dedupe_overlaps(raw)]


def content_words(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2}


def near_duplicates(sents, threshold):
    pairs = []
    words = [content_words(s) for _, s in sents]
    for i in range(len(sents)):
        for j in range(i + 1, len(sents)):
            a, b = words[i], words[j]
            if len(a) < 4 or len(b) < 4:
                continue
            score = len(a & b) / len(a | b)
            if score >= threshold:
                pairs.append({"kind": "near-duplicate", "line": sents[i][0],
                              "other_line": sents[j][0], "overlap": round(score, 2),
                              "sentence": sents[i][1], "other_sentence": sents[j][1]})
    return pairs


def scan(text, dup_threshold=0.6):
    sents = sentences(text)
    hits = []
    hits += _word_hits(sents, BUZZ_RE, "buzzword")
    hits += _word_hits(sents, VAGUE_RE, "vague word")
    for lineno, s in sents:
        if any(rx.search(s) for rx in OPENER_RE):
            hits.append({"kind": "throat-clearing opening", "line": lineno, "sentence": s})
        found = [m.group(1).lower() for m in HEDGE_RE.finditer(s)]
        if len(found) >= 2:
            hits.append({"kind": "stacked hedges", "line": lineno,
                         "term": ", ".join(found), "sentence": s})
    hits += near_duplicates(sents, dup_threshold)
    counts = {}
    for h in hits:
        counts[h["kind"]] = counts.get(h["kind"], 0) + 1
    return {"sentences": len(sents), "counts": counts,
            "hits": sorted(hits, key=lambda h: (h["line"], h["kind"])),
            "note": "Hits are prompts to read, not findings. Read each sentence in context."}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("path", help="text file, or - for standard input")
    p.add_argument("--json", action="store_true", help="print JSON")
    p.add_argument("--dup-threshold", type=float, default=0.6,
                   help="word-overlap threshold for near-duplicate sentences (0 to 1)")
    a = p.parse_args(argv)
    if not 0 < a.dup_threshold <= 1:
        p.error("--dup-threshold must be between 0 and 1")
    text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    result = scan(text, a.dup_threshold)
    if a.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    print(f"{result['sentences']} sentences scanned")
    for kind, n in sorted(result["counts"].items()):
        print(f"  {kind}: {n}")
    for h in result["hits"]:
        if h["kind"] == "near-duplicate":
            print(f"line {h['line']} ~ line {h['other_line']} (overlap {h['overlap']}): "
                  f"{h['sentence']}  |  {h['other_sentence']}")
        else:
            term = f" [{h['term']}]" if "term" in h else ""
            print(f"line {h['line']} {h['kind']}{term}: {h['sentence']}")
    print(result["note"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
