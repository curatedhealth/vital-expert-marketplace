#!/usr/bin/env python3
"""Check a downloaded VITAL Digital Health expert file before installing it.

Usage:
    python3 check_expert_file.py <download.json> [--connected regulatory-dh,literature]

Accepts the JSON returned by agent-pack.download_agent (one expert) or
download_team (an "agents" list). Prints, per expert, the findings a person
should fix or accept before loading the system prompt on their assistant:
plumbing lines left in the prompt, counts in the prompt that disagree with the
file, tools with no hosted product, tools outside the person's connectors,
skill entries with empty sections, and the skill families bound.
It reports facts about the file only; whether to keep or remove a line is the
person's decision.
"""
import json
import re
import sys
from collections import Counter

PLUMBING = [
    ("foreign key", r"trust the foreign key"),
    ("[GAP] field marker", r"\[GAP\] \([a-z_]+\)"),
    ("work-product titled None", r"None \(WP[^)]*\)"),
    ("archetype code", r"AL0\d-[A-Z]{3}"),
    ("internal id", r"de21_function_id"),
]
FAMILIES = {
    "CF-12.03.03": "regulatory strategy and submissions",
    "CF-12.03.02": "quality management and compliance",
    "CF-12.01.02": "clinical validation and evidence",
}


def agents_of(doc):
    if "agents" in doc:
        return doc["agents"]
    return [doc]


def check(a, connected):
    out = []
    ag = a["agent"]
    sp = ag.get("system_prompt", "")
    out.append(f"Expert: {ag.get('display_name')} ({ag.get('slug')}), department {ag.get('department')}")
    out.append(f"  System prompt: {len(sp)} characters. Skills: {len(a.get('skills', []))}. Tools: {len(a.get('tools', []))}.")
    out.append(f"  Not included (per file): {', '.join(a.get('does_not_include', []))}")

    for label, rx in PLUMBING:
        hits = re.findall(rx, sp)
        if hits:
            out.append(f"  PLUMBING in prompt: {label}, {len(hits)} occurrence(s), e.g. '{hits[0]}'")

    m = re.search(r"Bound competencies \((\d+)\): ([^\n]*)", sp)
    if m:
        stated = int(m.group(1))
        listed = [x for x in re.split(r"; ", m.group(2).split(" \u2014 ")[0].rstrip(".")) if x.strip()]
        if stated != len(listed):
            out.append(f"  COUNT MISMATCH: prompt says {stated} bound competencies, lists {len(listed)}")
        out.append("  Competencies named in prompt: " + "; ".join(listed))
    m = re.search(r"Tools you can operate \((\d+)\)", sp)
    if m and int(m.group(1)) != len(a.get("tools", [])):
        out.append(f"  COUNT MISMATCH: prompt says {m.group(1)} tools, file lists {len(a.get('tools', []))}")

    tools = a.get("tools", [])
    unhosted = [t["name"] for t in tools if not t.get("hosted_product")]
    if unhosted:
        out.append(f"  TOOLS with no hosted product or call route ({len(unhosted)}): {', '.join(unhosted)}")
    hosted = Counter(t.get("hosted_product") for t in tools if t.get("hosted_product"))
    if hosted:
        out.append("  Hosted products named: " + ", ".join(f"{k} ({v})" for k, v in sorted(hosted.items())))
    if connected is not None:
        missing = sorted({t["hosted_product"] for t in tools if t.get("hosted_product") and t["hosted_product"] not in connected})
        if missing:
            out.append(f"  NOT CONNECTED for you: {', '.join(missing)}")
    if any("own key" in (t.get("how_to_call") or "") for t in tools) and "second key" in (a.get("note") or ""):
        out.append("  KEY TEXT CONFLICT: tool entries say 'with its own key'; the note says no second key is needed")

    fam = Counter()
    empty = 0
    for s in a.get("skills", []):
        fam[FAMILIES.get(s["code"][:11], s["code"][:11])] += 1
        body = s.get("body_md", "")
        if re.search(r"### Prompt\s*\n\s*###", body) or re.search(r"### Template\s*\n\s*###", body) or "Prompt: not bound." in body:
            empty += 1
    out.append("  Skill families: " + ", ".join(f"{k} ({v})" for k, v in fam.most_common()))
    if empty:
        out.append(f"  SKILLS with an empty or unbound Prompt or Template section: {empty}")
    if any("ST05-PHARMA" in s.get("body_md", "") for s in a.get("skills", [])):
        out.append("  TEMPLATE CODE: skills reference ST05-PHARMA-DH-OVERLAY (register C16)")
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    connected = None
    if "--connected" in sys.argv:
        connected = set(sys.argv[sys.argv.index("--connected") + 1].split(","))
    doc = json.load(open(sys.argv[1], encoding="utf-8"))
    for a in agents_of(doc):
        print("\n".join(check(a, connected)))
        print()


if __name__ == "__main__":
    main()
