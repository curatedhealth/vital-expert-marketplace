#!/usr/bin/env python3
"""READY world-class grade meter — measure, do not assume.

Exit 0 only if all hard gates PASS.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
FORBIDDEN = (
    "approved for use",
    "mlr approved",
    "cleared for promotion",
    "cleared for use",
)
# mlr_reviewed allowed only with negation nearby is handled in scan script;
# good drafts must not contain the bare token at all for this meter.
HARD_FORBIDDEN = FORBIDDEN + ("mlr_reviewed",)

MAX_PAIR_JACCARD = 0.45
MIN_GOOD_CHARS = 2500
MIN_UNIQUE_LINE_RATIO = 0.85
MAX_REPEATED_PARAGRAPH = 1  # identical non-trivial paragraphs


def _lines(text: str) -> set[str]:
    return {l.strip() for l in text.splitlines() if l.strip()}


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    return len(a & b) / max(len(a | b), 1)


def _paragraph_repeat_count(text: str) -> int:
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if len(p.strip()) > 80]
    counts: dict[str, int] = {}
    for p in paras:
        counts[p] = counts.get(p, 0) + 1
    return max(counts.values(), default=0)


def main() -> int:
    fails: list[str] = []
    warns: list[str] = []

    # A. CF04 + stamp + offline tools.md
    need = [
        "SKILL.md",
        "intake.md",
        "governance.md",
        "references/method.md",
        "references/method-standards.md",
        "references/knowledge.md",
        "references/failure-modes.md",
        "references/tools.md",
        "references/without-connector.md",
        "examples/good-sourced-draft.md",
        "evals/evals.json",
        "evals/known-answer/expected.json",
    ]
    goods: dict[str, str] = {}
    expected_hashes: dict[str, str] = {}
    ms_hashes: dict[str, list[str]] = {}
    wc_hashes: dict[str, list[str]] = {}

    for skill in SKILLS:
        name = skill.name
        for rel in need:
            p = skill / rel
            if not p.exists() or p.stat().st_size < 40:
                fails.append(f"CF04 missing/thin: {name}/{rel}")
        skill_md = (skill / "SKILL.md").read_text(encoding="utf-8")
        if "stamp_ready_line" not in skill_md:
            fails.append(f"SKILL missing stamp CLI: {name}")
        if "Output cards" not in skill_md:
            fails.append(f"SKILL missing Output cards: {name}")
        tools = (skill / "references" / "tools.md").read_text(encoding="utf-8")
        if "Offline first" not in tools and "offline first" not in tools.lower():
            fails.append(f"tools.md not offline-first heading: {name}")
        if re.search(r"(?i)needs the MLR Review connector|with a `vmlr_` key\.\nWithout", tools):
            # legacy MCP-first opener
            if "Offline first" not in tools:
                fails.append(f"tools.md still MCP-first: {name}")
        if "_offline.py" not in tools and name != "mlr-capability-map":
            # capability-map may only list stamp + list rulesets
            if "stamp_ready_line" not in tools and "mlr_list_rulesets_offline" not in tools:
                fails.append(f"tools.md names no offline CLI: {name}")

        good = (skill / "examples" / "good-sourced-draft.md").read_text(encoding="utf-8")
        goods[name] = good
        if len(good) < MIN_GOOD_CHARS:
            fails.append(f"good draft <{MIN_GOOD_CHARS} chars: {name} ({len(good)})")
        low = good.lower()
        for ph in HARD_FORBIDDEN:
            if ph in low:
                fails.append(f"forbidden in good draft: {name}: {ph}")
        lines = [l.strip() for l in good.splitlines() if l.strip()]
        ratio = len(set(lines)) / max(len(lines), 1)
        if ratio < MIN_UNIQUE_LINE_RATIO:
            fails.append(f"good draft unique_line_ratio {ratio:.2f}<{MIN_UNIQUE_LINE_RATIO}: {name}")
        reps = _paragraph_repeat_count(good)
        if reps > MAX_REPEATED_PARAGRAPH:
            fails.append(f"good draft repeated paragraph x{reps}: {name}")
        if not list((skill / "examples").glob("poor*.md")):
            fails.append(f"missing poor example: {name}")

        exp = skill / "evals" / "known-answer" / "expected.json"
        raw = exp.read_bytes()
        h = hashlib.sha256(raw).hexdigest()
        if h in expected_hashes:
            fails.append(f"identical expected.json: {name} == {expected_hashes[h]}")
        expected_hashes[h] = name
        data = json.loads(raw)
        if data.get("unique_gate") in (None, ""):
            fails.append(f"expected.json missing unique_gate: {name}")

        ms = (skill / "references" / "method-standards.md").read_bytes()
        msh = hashlib.sha256(ms).hexdigest()[:12]
        ms_hashes.setdefault(msh, []).append(name)
        wc = (skill / "references" / "without-connector.md").read_bytes()
        wch = hashlib.sha256(wc).hexdigest()[:12]
        wc_hashes.setdefault(wch, []).append(name)

        std = (skill / "references" / "method-standards.md").read_text(encoding="utf-8")
        if "http://" not in std and "https://" not in std:
            fails.append(f"method-standards missing http: {name}")
        if "8 November 2026" not in std and "Access date" not in std:
            warns.append(f"method-standards missing access date note: {name}")

        # knowledge floor for world-class
        know = (skill / "references" / "knowledge.md").read_text(encoding="utf-8")
        failm = (skill / "references" / "failure-modes.md").read_text(encoding="utf-8")
        if len(know) < 1200:
            fails.append(f"knowledge too thin (<1200 chars): {name} ({len(know)})")
        if len(failm) < 800:
            fails.append(f"failure-modes too thin (<800 chars): {name} ({len(failm)})")

    # B. pairwise Jaccard
    names = list(goods)
    for i, a in enumerate(names):
        for b in names[i + 1 :]:
            j = _jaccard(_lines(goods[a]), _lines(goods[b]))
            if j > MAX_PAIR_JACCARD:
                fails.append(f"good-draft Jaccard {j:.2f}>{MAX_PAIR_JACCARD}: {a} ~ {b}")

    # C. method-standards / without-connector must not be one clone for all
    for h, group in ms_hashes.items():
        if len(group) > 3:
            fails.append(f"method-standards over-cloned ({len(group)}): {group}")
    for h, group in wc_hashes.items():
        if len(group) > 1:
            fails.append(f"without-connector identical clone: {group}")

    # D. packaging
    mcp = (ROOT / ".mcp.json").read_text(encoding="utf-8").strip()
    if mcp not in ("{}", "{\n}"):
        # allow pretty empty object
        try:
            if json.loads(mcp) != {}:
                fails.append(f".mcp.json not empty: {mcp[:80]}")
        except json.JSONDecodeError:
            fails.append(".mcp.json invalid")
    pj = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    if pj.get("release_state") not in ("Pilot", "Released"):
        fails.append(f"release_state unexpected: {pj.get('release_state')!r}")
    elif pj.get("release_state") == "Released":
        warns.append("release_state=Released (owner-promoted)")
    # legacy assets path refs already zero; warn if many asset files remain
    asset_files = list((ROOT / "skills").glob("*/assets/*"))
    if len(asset_files) > 0:
        warns.append(f"legacy assets/ files still on disk: {len(asset_files)} (prefer delete after migrate)")

    # E. fair-balance standards-by-market
    if not (ROOT / "skills" / "mlr-fair-balance-isi" / "references" / "standards-by-market.md").exists():
        fails.append("mlr-fair-balance-isi missing standards-by-market.md")

    print("READY world-class meter")
    print(f"skills={len(SKILLS)}")
    if warns:
        print("WARN:")
        for w in warns:
            print(" -", w)
    if fails:
        print(f"FAIL ({len(fails)}):")
        for f in fails:
            print(" -", f)
        print("GRADE: not-world-class")
        return 1
    print("PASS all hard gates")
    print("GRADE: world-class-pilot-content")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
