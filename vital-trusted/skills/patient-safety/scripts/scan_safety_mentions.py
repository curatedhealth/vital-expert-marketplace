#!/usr/bin/env python3
"""Find words that may signal a possible safety report, or patient-wording problems.

A backstop for reading, never a decision. It finds words, not meaning: every hit must
be read in context, and a clean scan does not mean there is nothing to flag.

Usage:
    python scan_safety_mentions.py notes.txt
    python scan_safety_mentions.py notes.txt --json
    python scan_safety_mentions.py --patient leaflet.txt
    cat transcript.txt | python scan_safety_mentions.py -
"""
import argparse
import json
import re
import sys

# Kinds of possible safety report (Part B). Terms are lowercase regex fragments.
SAFETY_KINDS = {
    "possible side effect": [
        r"side[- ]effects?", r"adverse (?:event|reaction|effect)s?", r"\breactions?\b",
        r"\brash(?:es)?\b", r"\bitch(?:y|ing)?\b", r"\bhives\b", r"\bswell(?:ing|ed)\b",
        r"\bnause(?:a|ous)\b", r"\bvomit(?:ing|ed)?\b", r"\bdiarrh?oea\b|\bdiarrhea\b",
        r"\bdizz(?:y|iness)\b", r"\bheadaches?\b", r"\bfaint(?:ed|ing)?\b",
        r"\bseizures?\b|\bfits?\b", r"\bbleed(?:ing)?\b|\bbruis(?:e|ing|ed)\b",
        r"\bpalpitations?\b", r"\bshort(?:ness)? of breath\b", r"\bjaundice\b",
        r"liver (?:tests?|enzymes?|function)", r"\b(?:alt|ast)\b (?:rose|raised|up|high)",
        r"kidney (?:tests?|function|problems?)", r"\bfatigue\b|\bexhausted\b",
        r"\bfell ill\b|\bgot ill\b|\bfelt (?:ill|unwell|awful|sick)\b",
        r"\bsince (?:starting|taking|switching)\b", r"\bafter (?:starting|taking|the first dose)\b",
        r"\bdeveloped\b", r"\ballerg(?:y|ic)\b", r"\banaphyla",
    ],
    "hospital or death": [
        r"\bhospitali[sz]ed\b|\bhospital\b|\badmitted\b|\bemergency (?:room|department)\b|\b(?:a&e|er)\b",
        r"\bintensive care\b|\bicu\b", r"\bdied\b|\bdeath\b|\bpassed away\b|\bfatal\b",
        r"\bdisabilit(?:y|ies)\b", r"\bbirth defect\b|\bcongenital\b",
    ],
    "pregnancy or breastfeeding": [
        r"\bpregnan(?:t|cy|cies)\b", r"\bexpecting a baby\b", r"\bbreast-?feed(?:ing)?\b",
        r"\bnursing\b", r"\blactat(?:ing|ion)\b", r"\bmiscarr(?:y|iage)\b", r"\bconceiv",
        r"\bpartner (?:is|was|became) pregnant\b",
    ],
    "overdose, misuse or abuse": [
        r"\boverdos(?:e|ed|ing)\b", r"\btoo (?:much|many)\b", r"\bdouble(?:d)? (?:the )?dose\b",
        r"\btook (?:two|2|extra|more)\b", r"\bwhole (?:pack|box|bottle)\b",
        r"\bmisus(?:e|ed|ing)\b", r"\babus(?:e|ed|ing)\b", r"\bnot prescribed (?:to|for)\b",
        r"\bsomeone else'?s\b", r"\bcrush(?:ed|ing)\b", r"\bsnort", r"\brecreational",
    ],
    "medication error": [
        r"\bwrong (?:dose|drug|medicine|product|patient|strength|tablet|pen)\b",
        r"\bmix(?:ed)?[- ]up\b", r"\bgiven by mistake\b", r"\bdispens(?:ed|ing) (?:error|the wrong)\b",
        r"\bnear miss\b", r"\bmedication error\b",
    ],
    "lack of effect": [
        r"\bstopped working\b", r"\b(?:didn'?t|did not|doesn'?t|does not) (?:work|help)\b",
        r"\bno (?:effect|difference|improvement)\b", r"\black of (?:effect|efficacy)\b",
        r"\bnot working\b", r"\bwore off\b", r"\bineffective\b",
    ],
    "off-label use as reported": [
        r"\boff[- ]label\b", r"\bnot (?:approved|licensed) for\b", r"\bunlicensed\b",
    ],
    "product quality": [
        r"\bbroken\b", r"\bleak(?:ing|ed|s)?\b", r"\bdiscolou?r(?:ed|ation)\b",
        r"\bcrumbl(?:ed|ing)\b", r"\bparticles?\b", r"\bcloudy\b", r"\bdamaged\b",
        r"\bmissing (?:leaflet|label|tablets?|parts?)\b", r"\bcounterfeit\b|\bfake\b|\bfalsified\b",
        r"\btasted? (?:different|strange|odd)\b", r"\bsmell(?:ed|s)? (?:different|strange|odd)\b",
        r"\b(?:pen|device|inhaler|pump|injector) (?:failed|jammed|didn'?t work|did not work|broke)\b",
        r"\bfaulty\b|\bmalfunction",
    ],
    "interaction": [
        r"\binteract(?:ion|ed|s)?\b", r"\btogether with\b", r"\bat the same time as\b",
        r"\bwith (?:alcohol|grapefruit)\b",
    ],
}

# Patient-wording checks (Part A, patient language).
PATIENT_KINDS = {
    "reassurance not to state unless the leaflet does": [
        r"\bcompletely safe\b", r"\b(?:totally|perfectly|100%) safe\b", r"\bis safe\b",
        r"\bno side[- ]effects?\b", r"\bnothing to worry\b", r"\bno need to worry\b",
        r"\bharmless\b", r"\bgentle\b", r"\bnatural\b", r"\beveryone tolerates\b",
        r"\bhardly notice\b", r"\brisk[- ]free\b", r"\bno risks?\b",
    ],
    "advice about treatment": [
        r"\byou can (?:stop|skip|reduce|increase|double|take)\b", r"\bstop taking\b",
        r"\btake (?:two|2|an extra|a double)\b", r"\bdouble (?:up|the dose)\b",
        r"\bno need to (?:see|call|ask|tell) (?:your|a) (?:doctor|gp|pharmacist|nurse)\b",
        r"\bfine (?:with|to drink) alcohol\b", r"\bsafe to (?:drive|drink|combine)\b",
        r"\binstead of your\b", r"\bswitch (?:to|from)\b",
    ],
    "alarming framing": [
        r"\bdeadly\b", r"\blethal\b", r"\bcould (?:kill|die)\b", r"\bdangerous\b",
        r"\bterrifying\b", r"\bdon'?t risk\b", r"\bbefore it'?s too late\b",
        r"\bwill (?:fail|die)\b",
    ],
}

ROUTE = re.compile(
    r"\b(?:ask|talk to|speak (?:to|with)|tell|contact|check with|call) (?:your |a )?"
    r"(?:doctor|gp|physician|nurse|pharmacist|healthcare professional|care team)",
    re.IGNORECASE,
)


def compile_kinds(kinds):
    return {k: [re.compile(p, re.IGNORECASE) for p in pats] for k, pats in kinds.items()}


def snippet(line, start, end, width=50):
    a = max(0, start - width)
    b = min(len(line), end + width)
    text = line[a:b].strip()
    return ("..." if a > 0 else "") + text + ("..." if b < len(line) else "")


def scan(text, kinds):
    compiled = compile_kinds(kinds)
    hits = []
    for n, line in enumerate(text.splitlines(), start=1):
        for kind, pats in compiled.items():
            seen = set()
            for pat in pats:
                for m in pat.finditer(line):
                    key = (m.start(), m.end())
                    if key in seen:
                        continue
                    seen.add(key)
                    hits.append({
                        "line": n,
                        "kind": kind,
                        "match": m.group(0),
                        "context": snippet(line, m.start(), m.end()),
                    })
    hits.sort(key=lambda h: (h["line"], h["kind"]))
    return hits


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("path", help="text file, or - for standard input")
    ap.add_argument("--patient", action="store_true",
                    help="scan a patient-facing draft for wording problems instead")
    ap.add_argument("--json", action="store_true", help="print JSON")
    args = ap.parse_args(argv)

    if args.path == "-":
        text = sys.stdin.read()
    else:
        with open(args.path, encoding="utf-8") as fh:
            text = fh.read()

    kinds = PATIENT_KINDS if args.patient else SAFETY_KINDS
    hits = scan(text, kinds)
    counts = {k: sum(1 for h in hits if h["kind"] == k) for k in kinds}
    result = {"mode": "patient wording" if args.patient else "possible safety mentions",
              "counts": counts, "hits": hits,
              "note": "Words found, not meaning. Read every hit in context. "
                      "A clean scan does not mean there is nothing to flag."}
    if args.patient:
        result["route_to_clinician_lines"] = [
            n for n, line in enumerate(text.splitlines(), start=1) if ROUTE.search(line)
        ]

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"Scan: {result['mode']}")
    for k, c in counts.items():
        print(f"  {k}: {c}")
    if args.patient:
        lines = result["route_to_clinician_lines"]
        print("  route to a doctor, nurse or pharmacist: "
              + (f"found on line(s) {', '.join(map(str, lines))}" if lines else "none found"))
    for h in hits:
        print(f"line {h['line']:>4}  {h['kind']}: \"{h['match']}\"  | {h['context']}")
    print(result["note"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
