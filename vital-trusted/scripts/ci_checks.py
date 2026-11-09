#!/usr/bin/env python3
"""Release checks for the vital-trusted plugin.

Usage (from anywhere):
    python3 scripts/ci_checks.py            static checks only
    python3 scripts/ci_checks.py --tests    static checks, then every script test
    python3 scripts/ci_checks.py --only pointers,em-dash
    python3 scripts/ci_checks.py --list

Exit code 0 when every check passes, 1 when any check fails.

Standard library only. The checks read the plugin folder that holds this script's
parent directory and never write to it.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")

MAX_FILES = 512
MAX_DESCRIPTION = 1024
PACK_VERSION = "0.3.4"
TEXT_SUFFIXES = (".md", ".json", ".txt", ".py")
EM_DASH = "\u2014"

# Files that describe the retired VERIFY companion on purpose. They are the only
# shipped text allowed to name its tools; each is listed with its reason.
VERIFY_EXEMPT = {
    "CHANGELOG.md": "history of releases, names what was retired",
}

VERIFY_TOOL_NAMES = [
    "qualify_source", "check_claim", "verify_text", "build_citation",
    "build_evidence_table", "generate_report", "extract_claims", "check_currency",
    "ingest_document", "build_record", "my_usage", "check_provenance",
]
VERIFY_STATUS_NAMES = ["out_of_scope", "not_checked", "partially_supported", "not_supported"]
DO_NOT_USE = re.compile(
    r"\b(never|do not|don't|must not|not use|no longer|forbidden|banned|reserved|retired|"
    r"not a result|never appear)\b",
    re.I,
)

PATH_PREFIXES = ("references", "tasks", "templates", "examples", "evals", "scripts",
                 "tools", "agents", "skills")
REPO_PATH = re.compile(r"(?<![\w./:-])(mcps|manifest|docs)/[\w.-]")


# Generic names that stand for "any skill's file of that name" or for a file kept
# outside the skill folders, so they have no single path to resolve.
GENERIC_NAMES = {"SKILL.md", "plugin.json"}

# No file is exempt from the pointer check. The changelog names removed scripts
# without a file extension so it names no path that is missing.
POINTER_EXEMPT = {}


def rel(path):
    return os.path.relpath(path, ROOT)


def shipped_files():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in ("__pycache__", ".git")]
        for name in filenames:
            if name == ".DS_Store" or name.endswith(".pyc"):
                continue
            out.append(os.path.join(dirpath, name))
    return sorted(out)


def read(path):
    with open(path, encoding="utf-8", errors="replace") as handle:
        return handle.read()


def skill_dir_of(path):
    """The skill folder a file belongs to, or None for plugin-level files."""
    parts = os.path.relpath(path, SKILLS).split(os.sep) if path.startswith(SKILLS + os.sep) else None
    if parts and len(parts) > 1:
        return os.path.join(SKILLS, parts[0])
    return None


def frontmatter(text):
    """Return the raw frontmatter block of a markdown file, or ''."""
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end > 0 else ""


def quoted_value(block, key):
    """Value of a double-quoted scalar `key: "..."` that may span lines."""
    match = re.search(r'(?m)^[ ]*' + re.escape(key) + r':\s*"', block)
    if not match:
        return None
    i = match.end()
    chars = []
    while i < len(block):
        ch = block[i]
        if ch == "\\" and i + 1 < len(block):
            nxt = block[i + 1]
            chars.append({"n": "\n", "t": "\t", '"': '"', "\\": "\\"}.get(nxt, nxt))
            i += 2
            continue
        if ch == '"':
            return "".join(chars)
        chars.append(ch)
        i += 1
    return "".join(chars)


# ---------------------------------------------------------------- checks

def check_file_count():
    count = len(shipped_files())
    problems = [] if count <= MAX_FILES else [f"{count} files, cap is {MAX_FILES}"]
    return problems, f"{count} files (cap {MAX_FILES})"


def check_descriptions():
    problems, seen = [], 0
    targets = [os.path.join(SKILLS, d, "SKILL.md") for d in sorted(os.listdir(SKILLS))
               if os.path.isfile(os.path.join(SKILLS, d, "SKILL.md"))]
    agents = os.path.join(ROOT, "agents")
    if os.path.isdir(agents):
        targets += [os.path.join(agents, f) for f in sorted(os.listdir(agents)) if f.endswith(".md")]
    for path in targets:
        value = quoted_value(frontmatter(read(path)), "description")
        if value is None:
            match = re.search(r"(?m)^description:\s*(.+)$", frontmatter(read(path)))
            value = match.group(1) if match else None
        if value is None:
            if path.startswith(SKILLS):
                problems.append(f"{rel(path)}: no description")
            continue
        seen += 1
        if len(value) > MAX_DESCRIPTION:
            problems.append(f"{rel(path)}: description is {len(value)} characters")
    plugin = os.path.join(ROOT, ".claude-plugin", "plugin.json")
    if os.path.isfile(plugin):
        with open(plugin, encoding="utf-8") as handle:
            text = json.load(handle).get("description", "")
        seen += 1
        if len(text) > MAX_DESCRIPTION:
            problems.append(f"{rel(plugin)}: description is {len(text)} characters")
    longest = 0
    for path in targets:
        value = quoted_value(frontmatter(read(path)), "description") or ""
        longest = max(longest, len(value))
    return problems, f"{seen} descriptions, longest skill description {longest} (cap {MAX_DESCRIPTION})"


def check_versions():
    problems, count = [], 0
    for name in sorted(os.listdir(SKILLS)):
        path = os.path.join(SKILLS, name, "SKILL.md")
        if not os.path.isfile(path):
            continue
        count += 1
        match = re.search(r'(?m)^\s+version:\s*"?([\w.]+)"?', frontmatter(read(path)))
        if not match:
            problems.append(f"{rel(path)}: no metadata version")
        elif match.group(1) != PACK_VERSION:
            problems.append(f"{rel(path)}: version {match.group(1)}, expected {PACK_VERSION}")
        folder = quoted_value(frontmatter(read(path)), "name") or re.search(
            r"(?m)^name:\s*(\S+)", frontmatter(read(path))).group(1)
        if folder != name:
            problems.append(f"{rel(path)}: name {folder!r} differs from folder {name!r}")
    plugin = os.path.join(ROOT, ".claude-plugin", "plugin.json")
    with open(plugin, encoding="utf-8") as handle:
        meta = json.load(handle)
    if meta.get("version") != PACK_VERSION:
        problems.append(f"plugin.json version {meta.get('version')}, expected {PACK_VERSION}")
    if meta.get("release_state") != "Pilot":
        problems.append(f"plugin.json release_state {meta.get('release_state')}, expected Pilot")
    return problems, f"{count} skills and plugin.json at {PACK_VERSION}, release_state {meta.get('release_state')}"


def check_depends_on():
    problems = []
    shipped_skills = {d for d in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, d, "SKILL.md"))}
    for path in shipped_files():
        if not path.endswith((".md", ".json")):
            continue
        text = read(path)
        for match in re.finditer(r"depends_on\s*[:=]\s*(.+)", text):
            names = re.findall(r"[\w-]+", match.group(1))
            missing = [n for n in names if n not in shipped_skills]
            if missing:
                problems.append(f"{rel(path)}: depends_on names {missing}, not shipped")
    return problems, "no depends_on that is not shipped"


PATH_TOKEN = re.compile(
    r"(?<![\w/.:@~-])((?:\.\./)*(?:(?:%s)/)[\w./*-]*[\w*]|[\w-]+\.(?:md|py|json|txt))(?![\w/-])"
    % "|".join(PATH_PREFIXES)
)


def resolve_candidates(path, token):
    bases = [os.path.dirname(path)]
    skill = skill_dir_of(path)
    if skill:
        bases.append(skill)
    else:
        bases.append(ROOT)
    return [os.path.normpath(os.path.join(base, token)) for base in bases]


def check_pointers():
    problems, checked = [], 0
    for path in shipped_files():
        if not path.endswith(".md") or rel(path) in POINTER_EXEMPT:
            continue
        text = read(path)
        for lineno, line in enumerate(text.split("\n"), 1):
            for match in PATH_TOKEN.finditer(line):
                token = match.group(1).rstrip(".,;:")
                if token in GENERIC_NAMES:
                    continue
                if re.match(r"^[\w-]+\.(?:txt|json)$", token):
                    continue  # a file the person supplies, not one the plugin ships
                if "<" in token or ">" in token or "://" in token or token.startswith("www"):
                    continue
                if re.match(r"^[\w-]+\.(?:md|py|json|txt)$", token) and token in (
                        "e.g.md", "i.e.md"):
                    continue
                checked += 1
                found = False
                for candidate in resolve_candidates(path, token):
                    if "*" in token:
                        import glob
                        if glob.glob(candidate):
                            found = True
                    elif os.path.exists(candidate):
                        found = True
                    if found:
                        break
                if not found:
                    problems.append(f"{rel(path)}:{lineno}: {token}")
    return problems, f"{checked} path mentions resolved"


def check_repo_paths():
    problems = []
    for path in shipped_files():
        if not path.endswith(TEXT_SUFFIXES) or os.path.basename(path) in ("ci_checks.py", "test_ci_checks.py"):
            continue
        for lineno, line in enumerate(read(path).split("\n"), 1):
            if REPO_PATH.search(line):
                problems.append(f"{rel(path)}:{lineno}: {line.strip()[:90]}")
    return problems, "no mcps/, manifest/ or docs/ paths"


def check_verify_words():
    problems = []
    tool_re = re.compile(r"\b(%s)\b" % "|".join(VERIFY_TOOL_NAMES))
    status_re = re.compile(r"\b(%s)\b" % "|".join(VERIFY_STATUS_NAMES))
    plain_re = re.compile(r"`(supported|partial|unsupported|contradicted|unverifiable)`")
    name_re = re.compile(r"\bVERIFY\b|\bvital-verify\b|\bvvfy_|\btrusted-prove\b|\bmcp__")
    for path in shipped_files():
        name = rel(path)
        if name in VERIFY_EXEMPT or os.path.basename(path) in ("ci_checks.py", "test_ci_checks.py"):
            continue
        if not path.endswith(TEXT_SUFFIXES):
            continue
        is_python = path.endswith(".py")
        lines = read(path).split("\n")
        for lineno, line in enumerate(lines, 1):
            hits = []
            for regex in (name_re, tool_re):
                hits += [m.group(0) for m in regex.finditer(line)]
            if not is_python:
                hits += [m.group(0) for m in status_re.finditer(line)]
                hits += [m.group(0) for m in plain_re.finditer(line)]
            if not hits:
                continue
            window = " ".join(lines[max(0, lineno - 2):lineno])
            if DO_NOT_USE.search(window):
                continue
            problems.append(f"{name}:{lineno}: {sorted(set(hits))}")
    return problems, f"no VERIFY tool, key or status name outside a do-not-use rule ({len(VERIFY_EXEMPT)} history files exempt)"


def gap_stripped(text):
    return re.sub(r"\[GAP:.*?\]", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)


def check_em_dash():
    problems = []
    for path in shipped_files():
        if not path.endswith(".md"):
            continue
        name = rel(path)
        in_scope = ("/templates/" in "/" + name or "/examples/" in "/" + name
                    or name.startswith("templates" + os.sep))
        if not in_scope:
            continue
        for lineno, line in enumerate(read(path).split("\n"), 1):
            if EM_DASH in line:
                problems.append(f"{name}:{lineno}: {line.strip()[:90]}")
    return problems, "no em dash in templates or examples anywhere, gap markers included"


def check_duplicates():
    groups = {}
    for path in shipped_files():
        with open(path, "rb") as handle:
            digest = hashlib.sha256(handle.read()).hexdigest()
        groups.setdefault(digest, []).append(rel(path))
    problems = [f"identical: {', '.join(sorted(v))}" for v in groups.values() if len(v) > 1]
    return problems, "no two shipped files are byte-identical"


def check_files_tables():
    """Each SKILL.md 'Files in this skill' table lists exactly the files the skill ships."""
    problems = []
    for name in sorted(os.listdir(SKILLS)):
        skill = os.path.join(SKILLS, name)
        path = os.path.join(skill, "SKILL.md")
        if not os.path.isfile(path):
            continue
        match = re.search(r"(?ms)^## Files in this skill\s*\n(.*?)(?=^## |\Z)", read(path))
        if not match:
            problems.append(f"{rel(path)}: no 'Files in this skill' table")
            continue
        listed = set()
        for line in match.group(1).split("\n"):
            if line.startswith("|") and not line.startswith("|---") and not line.startswith("| File"):
                listed.update(re.findall(r"`([^`]+)`", line.split("|")[1]))
        shipped = set()
        for dirpath, dirnames, filenames in os.walk(skill):
            dirnames[:] = [d for d in dirnames if d != "__pycache__"]
            for fname in filenames:
                if fname == ".DS_Store" or fname.endswith(".pyc"):
                    continue
                relpath = os.path.relpath(os.path.join(dirpath, fname), skill)
                if relpath != "SKILL.md":
                    shipped.add(relpath)
        for extra in sorted(listed - shipped):
            problems.append(f"{rel(path)}: lists {extra}, which is not shipped")
        for missing in sorted(shipped - listed):
            problems.append(f"{rel(path)}: does not list {missing}")
    return problems, "every Files table matches the files shipped"


def run_tests():
    problems, count = [], 0
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    tests = []
    for path in shipped_files():
        base = os.path.basename(path)
        if base.startswith("test_") and base.endswith(".py"):
            tests.append(path)
    for path in tests:
        count += 1
        proc = subprocess.run([sys.executable, os.path.basename(path)], cwd=os.path.dirname(path),
                              env=env, capture_output=True, text=True, timeout=300)
        if proc.returncode != 0:
            tail = (proc.stdout + proc.stderr).strip().split("\n")[-3:]
            problems.append(f"{rel(path)}: exit {proc.returncode}: {' | '.join(tail)[:200]}")
    return problems, f"{count} test files pass"


# ---------------------------------------------------------------- checks added in 0.3.4

ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
SAFETY_STEP = "0. **Safety first (TR-H14).**"
SUPERLATIVES = re.compile(r"\b(world-class|best-in-class|seamless|cutting-edge|game-changing|revolutionary)\b", re.I)
DERIVED = re.compile(r"(percentage[- ]points?|\brelative (?:change|reduction|increase)\b|\babout \d+(?:\.\d+)?\s?%|\b\d+(?:\.\d+)?-fold\b|\btimes (?:more|higher|lower)\b)", re.I)


def skill_mds():
    for name in sorted(os.listdir(SKILLS)):
        path = os.path.join(SKILLS, name, "SKILL.md")
        if os.path.isfile(path):
            yield name, path


def check_frontmatter():
    """Agent Skills frontmatter: valid YAML when PyYAML is present, allowed keys,
    name equals folder, name syntax, description cue and characters."""
    problems = []
    try:
        import yaml  # optional
    except ImportError:
        yaml = None
    for name, path in skill_mds():
        block = frontmatter(read(path))
        if yaml is not None:
            try:
                data = yaml.safe_load(block) or {}
            except Exception as exc:  # noqa: BLE001
                problems.append(f"{rel(path)}: frontmatter is not valid YAML ({str(exc).splitlines()[0][:60]})")
                continue
        else:
            data = {k: True for k in re.findall(r"(?m)^([A-Za-z_-]+):", block)}
            data["name"] = (re.search(r"(?m)^name:\s*(\S+)", block) or [None, None])[1]
            data["description"] = quoted_value(block, "description") or ""
        extra = set(data) - ALLOWED_KEYS
        if extra:
            problems.append(f"{rel(path)}: frontmatter keys not allowed: {sorted(extra)}")
        skill_name = str(data.get("name", "")).strip('"')
        if skill_name != name:
            problems.append(f"{rel(path)}: name '{skill_name}' differs from folder '{name}'")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", skill_name or "-") or len(skill_name) > 64 \
                or "claude" in skill_name or "anthropic" in skill_name:
            problems.append(f"{rel(path)}: name '{skill_name}' breaks the naming rule")
        desc = str(data.get("description", ""))
        if "<" in desc or ">" in desc:
            problems.append(f"{rel(path)}: description contains < or >")
        if not re.search(r"\bUse (it )?when(ever)?\b", desc):
            problems.append(f"{rel(path)}: description has no 'Use it when' cue")
        if re.search(r"\b(I can|you can)\b", desc):
            problems.append(f"{rel(path)}: description is not in the third person")
    return problems, "every SKILL.md frontmatter is valid, named for its folder and cues its use"


def check_body_size():
    problems = []
    for name, path in skill_mds():
        lines = read(path).count("\n")
        if lines >= 500:
            problems.append(f"{rel(path)}: {lines} lines (keep under 500)")
    for path in shipped_files():
        if "/references/" in path and path.endswith(".md"):
            text = read(path)
            if text.count("\n") > 100 and not re.search(r"(?im)^(#+\s*|\*\*)?contents\b", text[:4000]):
                problems.append(f"{rel(path)}: over 100 lines with no contents list near the top")
    return problems, "SKILL.md bodies under 500 lines; long references open with contents"


def check_safety_first():
    problems = []
    for name in sorted(os.listdir(SKILLS)):
        path = os.path.join(SKILLS, name, "references", "method.md")
        if not os.path.isfile(path):
            problems.append(f"skills/{name}: no references/method.md")
            continue
        steps = [l for l in read(path).split("\n") if re.match(r"\d+\.\s", l)]
        if not steps or not steps[0].startswith(SAFETY_STEP):
            problems.append(f"{rel(path)}: first numbered step is not the TR-H14 safety step")
    hard = os.path.join(SKILLS, "trusted-capability-map", "references", "hard-rules.md")
    if os.path.isdir(os.path.dirname(os.path.dirname(hard))) and (not os.path.isfile(hard) or "TR-H14" not in read(hard)):
        problems.append(f"{rel(hard)}: TR-H14 missing")
    return problems, "every method.md opens with the TR-H14 safety step; hard rule present"


def ka_expected_blocks(text):
    for block in re.findall(r"```json\s*\n(.*?)```", text, re.S):
        try:
            yield json.loads(block)
        except ValueError:
            continue


def check_eval_rules():
    """Evals never require a gap marker; known-answer cases parse and carry must_include."""
    problems = []
    for path in shipped_files():
        name = rel(path)
        if "/evals/" not in "/" + name:
            continue
        if path.endswith("evals.json"):
            try:
                data = json.loads(read(path))
            except ValueError as exc:
                problems.append(f"{name}: not valid JSON ({exc})")
                continue
            ids = [e.get("id") for e in data.get("evals", [])]
            if len(ids) < 3:
                problems.append(f"{name}: fewer than 3 evals")
            if len(ids) != len(set(ids)):
                problems.append(f"{name}: duplicate eval ids")
            for e in data.get("evals", []):
                for key in ("must_include", "expectations", "assertions"):
                    for item in e.get(key, []) or []:
                        if "[GAP" in json.dumps(item):
                            problems.append(f"{name}: eval {e.get('id')} {key} requires a gap marker")
        elif "/known-answer/" in name and path.endswith(".md"):
            blocks = list(ka_expected_blocks(read(path)))
            if not blocks:
                problems.append(f"{name}: no parseable expected JSON block")
            for b in blocks:
                if not b.get("must_include"):
                    problems.append(f"{name}: expected block has no must_include")
                if any("[GAP" in str(x) for x in b.get("must_include", [])) \
                        and b.get("gap_marker_expected_in") != "drafted deliverable":
                    problems.append(f"{name}: must_include requires a gap marker")
    return problems, "evals parse, have 3 or more cases, unique ids, and never require a gap marker"


def check_rule_contradictions():
    problems = []
    banned = {
        "including when True is off": "C9 off-letter contradiction",
        "Open for you": "heading is 'Open for a person'",
        "Record cleared by": "record status is 'Cleared by <name>, <role>, <date>'",
        "pregnancy exposure, overdose": "TR-H14 list is 'pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person'",
        "Part 3) of": "gap rules are Part 2 of the capability map's knowledge.md",
    }
    for path in shipped_files():
        if not path.endswith(".md") or rel(path) == "CHANGELOG.md":
            continue
        for lineno, line in enumerate(read(path).split("\n"), 1):
            for phrase, why in banned.items():
                if phrase in line:
                    problems.append(f"{rel(path)}:{lineno}: '{phrase}' ({why})")
    return problems, "no known contradictory phrasing"


def check_voice():
    """Templates and examples: no superlatives and no exclamation marks in our own text.
    Quoted input lines (starting with '>') are the person's material and are skipped."""
    problems = []
    for path in shipped_files():
        name = rel(path)
        if not path.endswith(".md"):
            continue
        in_scope = ("/templates/" in "/" + name or "/examples/" in "/" + name)
        for lineno, line in enumerate(read(path).split("\n"), 1):
            unquoted = re.sub(r'"[^"]*"|\'[^\']*\'|`[^`]*`', "", line)
            speaks = in_scope or name in ("README.md",) or name.startswith("agents") or name.endswith("SKILL.md")
            if speaks and SUPERLATIVES.search(unquoted) and not re.search(r"(?i)\b(cut|avoid|never|not|no|such as|claims?)\b", line):
                problems.append(f"{name}:{lineno}: superlative: {line.strip()[:80]}")
            if in_scope and not line.lstrip().startswith(">") and re.search(r"[A-Za-z]\!(\s|$)", line) \
                    and '"' not in line:
                problems.append(f"{name}:{lineno}: exclamation mark: {line.strip()[:80]}")
    return problems, "no superlatives; no exclamation marks in templates or examples"


def report_derived_figures():
    """Report only: lines in examples that state a derived figure, for a person to confirm."""
    hits = []
    for path in shipped_files():
        name = rel(path)
        if "/examples/" not in "/" + name or not path.endswith(".md"):
            continue
        for lineno, line in enumerate(read(path).split("\n"), 1):
            if DERIVED.search(line):
                labeled = "calculated from the two figures you supplied" in line
                hits.append(f"{name}:{lineno}: {'LABELED ' if labeled else ''}{line.strip()[:110]}")
    return hits


SAFETY_LIST = ("possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or "
               "off-label use reported for a person, medication error, lack of effect or product quality problem")


def check_safety_list():
    """Every copy of the TR-H14 list is identical (whitespace folded)."""
    problems, copies = [], 0
    pat = re.compile(r"possible\s+side\s+effect,\s+pregnancy[^.;:]*?problems?", re.S)
    for path in shipped_files():
        if not path.endswith(".md") or rel(path) == "CHANGELOG.md":
            continue
        for m in pat.finditer(read(path)):
            copies += 1
            text = re.sub(r"\s+", " ", m.group(0))
            if text.rstrip("s") != SAFETY_LIST:
                line = read(path)[:m.start()].count("\n") + 1
                problems.append(f"{rel(path)}:{line}: {text[:110]}")
    return problems, f"{copies} copies of the TR-H14 list, all identical"


def check_agents():
    problems = []
    folder = os.path.join(ROOT, "agents")
    if os.path.isdir(folder):
        for name in sorted(os.listdir(folder)):
            if name.endswith(".md"):
                block = frontmatter(read(os.path.join(folder, name)))
                if not re.search(r"(?m)^name:\s*\S", block) or not re.search(r"(?m)^description:\s*\S", block):
                    problems.append(f"agents/{name}: frontmatter needs name and description")
    return problems, "every agent has a name and a description"


CHECKS = [
    ("file-count", check_file_count),
    ("descriptions", check_descriptions),
    ("versions", check_versions),
    ("depends-on", check_depends_on),
    ("pointers", check_pointers),
    ("files-tables", check_files_tables),
    ("repo-paths", check_repo_paths),
    ("verify-words", check_verify_words),
    ("em-dash", check_em_dash),
    ("duplicates", check_duplicates),
    ("frontmatter", check_frontmatter),
    ("body-size", check_body_size),
    ("safety-first", check_safety_first),
    ("eval-rules", check_eval_rules),
    ("contradictions", check_rule_contradictions),
    ("voice", check_voice),
    ("safety-list", check_safety_list),
    ("agents", check_agents),
]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--tests", action="store_true", help="also run every test_*.py")
    parser.add_argument("--only", help="comma-separated check names")
    parser.add_argument("--list", action="store_true", help="list check names")
    parser.add_argument("--derived-report", action="store_true",
                        help="print every example line with a derived figure (report, not pass or fail)")
    args = parser.parse_args(argv)
    checks = list(CHECKS) + ([("tests", run_tests)] if args.tests else [])
    if args.list:
        print("\n".join(name for name, _ in CHECKS + [("tests", run_tests)]))
        return 0
    if args.derived_report:
        hits = report_derived_figures()
        print(f"Derived-figure report: {len(hits)} line(s) for a person to confirm")
        print("\n".join(hits))
        return 0
    if args.only:
        wanted = set(args.only.split(","))
        checks = [c for c in CHECKS + [("tests", run_tests)] if c[0] in wanted]
    failed = 0
    for name, fn in checks:
        problems, summary = fn()
        if problems:
            failed += 1
            print(f"FAIL {name}: {len(problems)} problem(s)")
            for line in problems[:60]:
                print(f"     {line}")
            if len(problems) > 60:
                print(f"     ... {len(problems) - 60} more")
        else:
            print(f"PASS {name}: {summary}")
    print(f"{len(checks) - failed} of {len(checks)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
