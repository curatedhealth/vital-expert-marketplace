#!/usr/bin/env python3
"""List status and clearance words in a text, for the honest-status task.

Part of the VITAL TRUSTED skill work-record (task TR-7.1.3).

  python status_words.py draft.txt
  python status_words.py draft.txt --json
  cat draft.txt | python status_words.py -

Each row: line number, the word as written, its kind (status or draft marking), whether
a name or a "by ..." phrase sits in the same sentence, and the sentence. It does not
judge whether a status is true. It shows where to ask "who, which event, when".
"""
import argparse
import json
import re
import sys

STATUS = [
    r"approv(?:ed|al|es)",
    r"final(?:i[sz]ed)?",
    r"validat(?:ed|ion)",
    r"verified",
    r"reviewed",
    r"review(?:ed)? complete",
    r"signed[- ]off",
    r"sign[- ]off",
    r"cleared",
    r"certified",
    r"compliant",
    r"ready to (?:send|use|share|publish)",
    r"for distribution",
    r"MLR[- ]approved",
]
DRAFT = [
    r"draft",
    r"uncleared",
    r"not yet reviewed",
    r"for review",
    r"\[GAP[^\]]*\]",
    r"\[Approval[^\]]*\]",
]

STATUS_RE = re.compile(r"\b(?:" + "|".join(STATUS) + r")\b", re.IGNORECASE)
DRAFT_RE = re.compile(r"(?:\b(?:" + "|".join(DRAFT[:4]) + r")\b|" + "|".join(DRAFT[4:]) + ")",
                      re.IGNORECASE)
# A "by <Name>" phrase, or a title plus capitalized surname, in the same sentence.
NAME_RE = re.compile(
    r"\bby\s+(?:(?:Dr|Prof|Mr|Ms|Mrs)\.?\s+)?[A-Z][a-zA-Z.'-]+(?:\s+[A-Z][a-zA-Z.'-]+)*"
    r"|\b(?:Dr|Prof|Mr|Ms|Mrs)\.?\s+[A-Z][a-zA-Z.'-]+"
)
# Split on sentence ends, but not after common title abbreviations.
SENT_SPLIT = re.compile(r"(?<!\bDr\.)(?<!\bMr\.)(?<!\bMs\.)(?<!\bMrs\.)(?<!\bProf\.)(?<!\b[A-Z]\.)(?<=[.!?])\s+")
# Names that are tools or models, not people: a status "by" one of these has no human behind it.
NOT_A_PERSON = re.compile(
    r"^by\s+(?:AI|the AI|the assistant|assistant|ChatGPT|Claude|Copilot|Gemini|GPT\S*|"
    r"TRUSTED|VERIFY|the tool|tool|model)\b",
    re.IGNORECASE,
)
NEGATION = re.compile(r"\b(?:not|not yet|never|un)\s*$", re.IGNORECASE)


def sentences_with_lines(text):
    """Yield (line_number, sentence) pairs."""
    for i, line in enumerate(text.splitlines(), start=1):
        for s in SENT_SPLIT.split(line):
            s = s.strip()
            if s:
                yield i, s


def scan(text):
    rows = []
    for line, sent in sentences_with_lines(text):
        name = NAME_RE.search(sent)
        if name and NOT_A_PERSON.match(name.group(0)):
            name = None
        draft_spans = [m.span() for m in DRAFT_RE.finditer(sent)]
        for m in STATUS_RE.finditer(sent):
            inside_draft = any(a <= m.start() < b for a, b in draft_spans)
            if inside_draft or NEGATION.search(sent[:m.start()]):
                continue
            rows.append({
                "line": line,
                "word": m.group(0),
                "kind": "status",
                "name_in_sentence": bool(name),
                "name_hint": name.group(0) if name else None,
                "sentence": sent,
            })
        for m in DRAFT_RE.finditer(sent):
            rows.append({
                "line": line,
                "word": m.group(0),
                "kind": "draft marking",
                "name_in_sentence": bool(name),
                "name_hint": name.group(0) if name else None,
                "sentence": sent,
            })
    rows.sort(key=lambda r: r["line"])
    return rows


def summary(rows):
    status = [r for r in rows if r["kind"] == "status"]
    return {
        "status_words": len(status),
        "status_words_without_name": sum(1 for r in status if not r["name_in_sentence"]),
        "draft_markings": sum(1 for r in rows if r["kind"] == "draft marking"),
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("path", help="text file, or - for standard input")
    p.add_argument("--json", action="store_true", help="output JSON")
    a = p.parse_args(argv)
    text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    rows = scan(text)
    s = summary(rows)
    if a.json:
        print(json.dumps({"rows": rows, "summary": s}, indent=2))
        return 0
    for r in rows:
        who = f"name nearby: {r['name_hint']}" if r["name_in_sentence"] else "no name in sentence"
        print(f"line {r['line']:>3} | {r['kind']:<13} | {r['word']:<16} | {who} | {r['sentence']}")
    print(
        f"\n{s['status_words']} status words ({s['status_words_without_name']} with no name "
        f"in the sentence), {s['draft_markings']} draft markings. "
        "This lists words; it does not judge whether a status is true."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
