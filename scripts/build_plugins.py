#!/usr/bin/env python3
"""Build both platform plugins from the single curated Skill registry.

Source of truth: registry/skills.yaml + skills/ + core/{always-on.md,hooks.json} + CHANGELOG.md + pinned upstream submodules.
Generated outputs: plugins/oydodo-skills/{skills,licenses,core,hooks,SOURCES.md,CHANGELOG.md}.
Only generated contents change; platform-specific manifests keep their identities.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "plugins" / "oydodo-skills"
MANIFESTS = ("plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json")
GENERATED_DIRS = ("skills", "licenses", "core", "hooks")
GENERATED_FILES = ("SOURCES.md", "CHANGELOG.md")
MAX_SIZE = 25 * 1024 * 1024


def catalog() -> tuple[dict, list[dict]]:
    data = yaml.safe_load((ROOT / "registry" / "skills.yaml").read_text(encoding="utf-8"))
    entries = data["skills"]
    names = [entry["name"] for entry in entries]
    if not names or len(names) != len(set(names)):
        raise ValueError("Skill registry must contain distinct named entries")
    for item in entries:
        if not re.fullmatch(r"[a-z][a-z0-9-]*", item["name"]):
            raise ValueError(f"Invalid skill name: {item['name']}")
        if item["source"] != "maintained" and item["source"] not in data["upstreams"]:
            raise ValueError(f"Unrecognized source for {item['name']}")
    return data, entries


def source_modules() -> list[str]:
    data, entries = catalog()
    return sorted({data["upstreams"][e["source"]]["module_path"]
                   for e in entries if e["source"] != "maintained"})


def run_git(*args: str, at: Path = ROOT) -> str:
    return subprocess.check_output(["git", "-C", str(at), *args],
                                   text=True, stderr=subprocess.PIPE).strip()


def pinned_commit(module_path: str) -> str:
    row = run_git("ls-tree", "HEAD", "--", module_path)
    if not row or "\t" not in row:
        raise ValueError(f"Not a pinned Git submodule: {module_path}")
    parts = row.split("\t", 1)[0].split()
    if len(parts) != 3 or parts[:2] != ["160000", "commit"]:
        raise ValueError(f"Not a submodule gitlink: {module_path}")
    path = ROOT / module_path
    if not (path / ".git").exists() and not (path / ".git").is_file():
        raise ValueError(f"Initialize pinned submodule first: {module_path}")
    installed = run_git("rev-parse", "HEAD", at=path)
    if installed != parts[2]:
        raise ValueError(f"Submodule {module_path} checked out at {installed}, "
                         f"but repository pins {parts[2]}")
    return installed


def files_under(source: Path):
    if not source.is_dir() or source.is_symlink():
        raise ValueError(f"Missing or unsafe Skill source: {source}")
    ignored = {".git", ".github", ".gitignore", ".DS_Store",
               "__pycache__", "node_modules", ".pytest_cache", ".venv"}
    for path in sorted(source.rglob("*")):
        rel = path.relative_to(source)
        if any(part in ignored for part in rel.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"Symlink in Skill source: {path}")
        if path.is_file() and path.name not in {"LICENSE", "LICENSE.md"}:
            yield path, rel


def normalized_skill(original: bytes, name: str, description_override: str | None) -> bytes:
    value = original.decode("utf-8")
    m = re.match(r"\A---[ \t]*\r?\n([\s\S]*?)\r?\n---[ \t]*\r?\n", value)
    if not m:
        raise ValueError(f"Missing YAML frontmatter: {name}")
    header = yaml.safe_load(m.group(1))
    if not isinstance(header, dict) or header.get("name") != name:
        raise ValueError(f"Source SKILL.md name mismatch: {name}")
    description = description_override or header.get("description")
    if not isinstance(description, str) or not description.strip():
        raise ValueError(f"Skill {name} has no description")
    # Keep original body; preserve Claude user-only metadata when supplied.
    # Codex reads the equivalent invocation policy from agents/openai.yaml.
    manual = header.get("disable-model-invocation", False)
    if not isinstance(manual, bool):
        raise ValueError(f"Skill {name} has invalid disable-model-invocation")
    front = "---\nname: " + name + "\ndescription: " + json.dumps(
        description, ensure_ascii=False) + "\n"
    if manual:
        front += "disable-model-invocation: true\n"
    front += "---\n"
    return (front + value[m.end():]).encode("utf-8")

def copy_core(stage: Path) -> None:
    """Package one canonical core policy plus its fail-open SessionStart hook."""
    rules = ROOT / "core" / "always-on.md"
    hooks = ROOT / "core" / "hooks.json"
    if any(not p.is_file() or p.is_symlink() for p in (rules, hooks)):
        raise ValueError("Missing or unsafe core/always-on.md or core/hooks.json")
    content = rules.read_text(encoding="utf-8")
    for name in ("philosophical-foundation", "independent-judgment", "crux-first-reasoning"):
        if f"skills/{name}/SKILL.md" not in content:
            raise ValueError(f"Always-on core is missing reference: {name}")
    payload = json.loads(hooks.read_text(encoding="utf-8"))
    groups = payload.get("hooks", {}).get("SessionStart", [])
    if len(groups) != 1 or len(groups[0].get("hooks", [])) != 1:
        raise ValueError("Expected one fail-open SessionStart command hook")
    handler = groups[0]["hooks"][0]
    command = handler.get("command")
    if (handler.get("type") != "command" or not isinstance(command, str)
            or "core/always-on.md" not in command or "exit 0" not in command):
        raise ValueError("Core Hook must read the packaged rules and fail open")
    for source, relative in ((rules, "core/always-on.md"), (hooks, "hooks/hooks.json")):
        dest = stage / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)


def make_tree(stage: Path) -> list[str]:
    data, entries = catalog()
    pins = {module: pinned_commit(module) for module in source_modules()}
    copy_core(stage)
    history = ROOT / "CHANGELOG.md"
    if not history.is_file() or history.is_symlink():
        raise ValueError("Missing or unsafe canonical CHANGELOG.md")
    shutil.copy2(history, stage / "CHANGELOG.md")
    origin = []
    for entry in entries:
        name = entry["name"]
        rel = Path(entry["skill_path"])
        if rel.is_absolute() or ".." in rel.parts:
            raise ValueError(f"Unsafe source path: {rel}")
        source = ROOT / rel
        if entry["source"] != "maintained":
            module = Path(data["upstreams"][entry["source"]]["module_path"])
            if not source.is_relative_to(ROOT / module):
                raise ValueError(f"Skill {name} is outside its declared submodule")
        destination = stage / "skills" / name
        count = 0
        for item, relfile in files_under(source):
            dest = destination / relfile
            dest.parent.mkdir(parents=True, exist_ok=True)
            content = item.read_bytes()
            if relfile.as_posix() == "SKILL.md":
                content = normalized_skill(content, name,
                                           entry.get("description_override"))
            dest.write_bytes(content)
            count += 1
        if not (destination / "SKILL.md").is_file():
            raise ValueError(f"Skill has no SKILL.md: {name}")
        if not (destination / "agents" / "openai.yaml").is_file():
            metadata = {"interface": {
                "display_name": name.replace("-", " ").title(),
                "short_description": " ".join(
                    (entry.get("description_override") or name.replace("-", " ")).split())[:110]
            }}
            dest = destination / "agents" / "openai.yaml"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(yaml.safe_dump(metadata, allow_unicode=True,
                                           sort_keys=False), encoding="utf-8")
        # Align Claude explicit-only flag and Codex invocation policy.
        skill_text = (destination / "SKILL.md").read_text(encoding="utf-8")
        skill_match = re.match(r"\A---[ \t]*\n([\s\S]*?)\n---[ \t]*\n", skill_text)
        if not skill_match:
            raise ValueError(f"Missing generated frontmatter: {name}")
        skill_header = yaml.safe_load(skill_match.group(1))
        if skill_header.get("disable-model-invocation", False):
            meta_path = destination / "agents" / "openai.yaml"
            meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
            if not isinstance(meta, dict):
                raise ValueError(f"Invalid OpenAI metadata for {name}")
            policy = meta.setdefault("policy", {})
            if not isinstance(policy, dict):
                raise ValueError(f"Invalid invocation policy for {name}")
            if policy.get("allow_implicit_invocation") is not False:
                policy["allow_implicit_invocation"] = False
                meta_path.write_text(yaml.safe_dump(
                    meta, allow_unicode=True, sort_keys=False), encoding="utf-8")
        if entry["source"] == "maintained":
            url = "https://github.com/oydodo/skills"
            pin = "maintained in this repository"
        else:
            u = data["upstreams"][entry["source"]]
            url = u["url"].removesuffix(".git")
            pin = pins[u["module_path"]]
            license_file = ROOT / u["module_path"] / "LICENSE"
            if not license_file.is_file() or license_file.is_symlink():
                raise ValueError(f"Upstream license missing for {name}")
            out = stage / "licenses" / f"{name}-LICENSE"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(license_file.read_bytes())
        note = "Curated trigger description; body unmodified" if entry.get(
            "description_override") else "Body unmodified"
        origin.append(f"| {name} | [{entry['source']}]({url}) | {pin} | {note} |")
    provenance = (
        "# Source provenance (generated)\n\n"
        "DO NOT edit here. Edit registry/skills.yaml, maintained skills, or the pinned "
        "submodule commits; the publish workflow regenerates this file.\n\n"
        "| Skill | Source | Pinned source | Packaging note |\n"
        "| --- | --- | --- | --- |\n"
        + "\n".join(origin)
        + "\n\nThird-party licenses are included under licenses/. "
        "No MCP servers are installed. An optional fail-open SessionStart hook "
        "loads the core principles on supported local Agent runtimes.\n"
    )
    (stage / "SOURCES.md").write_text(provenance, encoding="utf-8")
    return [e["name"] for e in entries]


def signature(folder: Path) -> dict[str, str]:
    result = {}
    for part in (*GENERATED_DIRS, *GENERATED_FILES):
        path = folder / part
        if path.is_file():
            result[part] = hashlib.sha256(path.read_bytes()).hexdigest()
        elif path.is_dir():
            for child in path.rglob("*"):
                if child.is_file():
                    key = child.relative_to(folder).as_posix()
                    result[key] = hashlib.sha256(child.read_bytes()).hexdigest()
    return result


def versions() -> tuple[str, list[tuple[Path, dict]]]:
    manifests = []
    for name in MANIFESTS:
        path = BUNDLE / name
        info = json.loads(path.read_text(encoding="utf-8"))
        if info.get("name") != "oydodo-skills":
            raise ValueError(f"Wrong plugin identity in {path}")
        manifests.append((path, info))
    found = {info["version"] for _, info in manifests}
    if len(found) != 1:
        raise ValueError(f"Plugin manifest versions disagree: {found}")
    version = found.pop()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Expected stable X.Y.Z plugin version")
    return version, manifests


def release_notes_for(version: str) -> str:
    """Return the exact versioned notes for GitHub Releases and handoff."""
    history = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    first = re.search(
        rf"(?m)^## \[{re.escape(version)}\] - [0-9]{{4}}-[0-9]{{2}}-[0-9]{{2}}\s*$",
        history,
    )
    if first is None:
        raise ValueError(f"No CHANGELOG.md notes for release v{version}")
    next_release = re.search(
        r"(?m)^## \[[0-9]+\.[0-9]+\.[0-9]+\] - ",
        history[first.end():],
    )
    end = first.end() + next_release.start() if next_release else len(history)
    return history[first.start():end].strip() + "\n"


def sync(check: bool) -> None:
    old_version, manifests = versions()
    with tempfile.TemporaryDirectory(prefix="oydodo-build-") as temp:
        staging = Path(temp)
        names = make_tree(staging)
        size = sum(p.stat().st_size for p in staging.rglob("*") if p.is_file())
        if size > MAX_SIZE:
            raise ValueError(f"Skill content exceeds 25MB: {size}")
        before, after = signature(BUNDLE), signature(staging)
        changed = before != after
        if check:
            if changed:
                missing = sorted(set(after) - set(before))
                removed = sorted(set(before) - set(after))
                modified = sorted(k for k in before.keys() & after.keys()
                                  if before[k] != after[k])
                raise SystemExit(f"OUT OF SYNC: missing={missing}, "
                                 f"removed={removed}, changed={modified}")
            print(f"OK: generated files match source; {len(names)} skills; v{old_version}")
            return
        if changed:
            major, minor, patch = map(int, old_version.split("."))
            next_version = f"{major}.{minor}.{patch + 1}"
            history = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
            latest = re.search(r"(?m)^## \[([0-9]+\.[0-9]+\.[0-9]+)\] - [0-9]{4}-[0-9]{2}-[0-9]{2}\s*$", history)
            if latest is None or latest.group(1) != next_version:
                raise ValueError(
                    f"CHANGELOG.md must start its release history with [{next_version}] "
                    "before publishing a changed Plugin"
                )
            for name in GENERATED_DIRS:
                shutil.rmtree(BUNDLE / name, ignore_errors=True)
                shutil.copytree(staging / name, BUNDLE / name)
            for name in GENERATED_FILES:
                shutil.copy2(staging / name, BUNDLE / name)
            for path, info in manifests:
                info["version"] = next_version
                path.write_text(json.dumps(info, indent=2, ensure_ascii=False) + "\n",
                                encoding="utf-8")
            print(f"UPDATED: {len(names)} skills; v{old_version} -> v{next_version}")
        else:
            print(f"UNCHANGED: {len(names)} skills; v{old_version}")


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true", help="Generate into the plugin")
    group.add_argument("--check", action="store_true", help="Fail on generated drift")
    group.add_argument("--list-submodules", action="store_true",
                       help="Print only selected pinned upstream submodule paths")
    group.add_argument("--release-notes", metavar="VERSION",
                       help="Print the matching CHANGELOG.md section for GitHub Releases")
    args = parser.parse_args()
    if args.list_submodules:
        print("\n".join(source_modules()))
    elif args.release_notes:
        print(release_notes_for(args.release_notes), end="")
    else:
        sync(check=args.check or not args.write)


if __name__ == "__main__":
    main()
