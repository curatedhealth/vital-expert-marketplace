#!/usr/bin/env python3
"""Fail if any path named in vital-trusted SKILL.md, tasks/*.md or templates/*.md is missing.

Usage: python3 scripts/check_vital_trusted_pointers.py [plugin_dir]
Exit 0 = all pointers resolve; 1 = missing paths listed on stdout.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

BACKTICK_PATH = re.compile(r"`([^`]+)`")
PATHISH = re.compile(
    r"^(?:\.?\.?/)*(?:references|templates|assets|tasks|examples|evals|scripts|tools|agents)/.+\.(?:md|json|ya?ml|txt|py|csv)$"
    r"|^(?:governance|intake)\.md$"
    r"|^(?:[\w.-]+/)+[\w.-]+\.(?:md|json|ya?ml|txt|py|csv)$"
)


def is_pathish(p: str) -> bool:
    p = p.strip()
    if not p or "*" in p or "://" in p or " " in p:
        return False
    if p.startswith(("http", "mailto")):
        return False
    # Bare filenames like patterns.md are prose, not pointers — require a path or skill-root file.
    if p in {"governance.md", "intake.md"}:
        return True
    if "/" not in p:
        return False
    return bool(PATHISH.match(p) or p.endswith((".md", ".json", ".py", ".txt", ".yaml", ".yml", ".csv")))


def resolve(plugin: Path, skill_dir: Path, mentioned: str) -> Path | None:
    cands = [
        skill_dir / mentioned,
        plugin / mentioned,
        plugin / "skills" / mentioned,
    ]
    # bare check-output etc.
    name = Path(mentioned).name
    if mentioned == name and name.endswith(".md"):
        cands += [skill_dir / "templates" / name, plugin / "templates" / name]
    for c in cands:
        try:
            c = c.resolve()
            if c.is_file() and str(plugin.resolve()) in str(c):
                return c
        except Exception:
            pass
    return None


def iter_sources(skill_dir: Path):
    skill = skill_dir / "SKILL.md"
    if skill.exists():
        yield skill
    tasks = skill_dir / "tasks"
    if tasks.is_dir():
        yield from sorted(tasks.glob("*.md"))
    templates = skill_dir / "templates"
    if templates.is_dir():
        yield from sorted(templates.glob("*.md"))


def main() -> int:
    plugin = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "vital-trusted")
    plugin = plugin.resolve()
    if not (plugin / "skills").is_dir():
        print(f"ERROR: skills/ not found under {plugin}", file=sys.stderr)
        return 2

    missing = []
    checked = 0
    for skill_dir in sorted(p for p in (plugin / "skills").iterdir() if p.is_dir()):
        for src in iter_sources(skill_dir):
            text = src.read_text(errors="replace")
            for m in BACKTICK_PATH.finditer(text):
                raw = m.group(1).strip().split("#")[0].strip()
                # split dual paths "a / b" only when both look like paths
                parts = re.split(r"\s*/\s+(?=references/|templates/|assets/|tasks/|\\.\\./)", raw)
                if len(parts) == 1:
                    parts = [raw]
                for part in parts:
                    part = part.strip()
                    if not is_pathish(part):
                        continue
                    # skill names / ids like trusted-capability-map without slash+file skip unless path
                    if "/" not in part and not part.endswith((".md", ".json", ".py", ".txt")):
                        continue
                    checked += 1
                    if resolve(plugin, skill_dir, part) is None:
                        missing.append((str(src.relative_to(plugin)), part))

    if missing:
        print(f"FAIL: {len(missing)} missing pointer(s) ({checked} path mentions checked)")
        for src, part in missing:
            print(f"  {src}: {part}")
        return 1

    print(f"PASS: {checked} path mentions resolved under {plugin}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
