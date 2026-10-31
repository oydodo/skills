#!/usr/bin/env python3
"""Create deterministic portable .agents, Claude, and ChatGPT archives."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import zipfile

from build_plugins import (ROOT, BUNDLE, PORTABLE, PORTABLE_DIRS,
                           PORTABLE_FILES, catalog, signature, versions)

FILE_PARTS = ("skills", "licenses", "core", "hooks")
COMMON_FILES = ("README.md", "SOURCES.md", "CHANGELOG.md")
PLATFORM_FILES = {
    "claude": (".claude-plugin",),
    "chatgpt": (".codex-plugin", "plugin.json"),
}


def package(platform: str, output: Path) -> None:
    expected = {entry["name"] for entry in catalog()[1]}
    version, _ = versions()
    manifest = BUNDLE / (".claude-plugin/plugin.json" if platform == "claude"
                         else "plugin.json")
    data = json.loads(manifest.read_text(encoding="utf-8"))
    if data["name"] != "oydodo-skills" or data["version"] != version:
        raise ValueError(f"Invalid {platform} plugin manifest")
    names = {d.parent.name for d in (BUNDLE / "skills").glob("*/SKILL.md")}
    if names != expected:
        raise ValueError(f"Expected {sorted(expected)}, got {sorted(names)}")

    contents = []
    for folder in (*FILE_PARTS, *PLATFORM_FILES[platform]):
        path = BUNDLE / folder
        if path.is_dir():
            contents.extend(p for p in path.rglob("*") if p.is_file())
        else:
            contents.append(path)
    contents.extend(BUNDLE / name for name in COMMON_FILES)
    if any(not p.is_file() or p.is_symlink() for p in contents):
        raise ValueError("Plugin references a missing or symlinked file")

    output = output.resolve()
    if BUNDLE in output.parents:
        raise ValueError("ZIP must be outside the source plugin directory")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(contents, key=lambda p: p.relative_to(BUNDLE).as_posix()):
            info = zipfile.ZipInfo(path.relative_to(BUNDLE).as_posix(),
                                   date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 << 16)
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)

    with zipfile.ZipFile(output) as verify:
        inside = set(verify.namelist())
        entrypoints = {x.split("/")[1] for x in inside
                       if re.fullmatch(r"skills/[^/]+/SKILL.md", x)}
        if entrypoints != expected or verify.testzip() is not None:
            raise ValueError("ZIP payload verification failed")
        if "CHANGELOG.md" not in inside:
            raise ValueError("Versioned Changelog is missing from the Plugin ZIP")
        notes = verify.read("CHANGELOG.md").decode("utf-8")
        released = re.search(r"(?m)^## \[([0-9]+\.[0-9]+\.[0-9]+)\] - [0-9]{4}-[0-9]{2}-[0-9]{2}\s*$", notes)
        if released is None or released.group(1) != version:
            raise ValueError(f"Changelog version does not match packaged v{version}")
        if not {"core/always-on.md", "hooks/hooks.json"}.issubset(inside):
            raise ValueError("Required always-on policy or SessionStart Hook missing from ZIP")
        hooks = json.loads(verify.read("hooks/hooks.json").decode("utf-8"))
        if not hooks.get("hooks", {}).get("SessionStart"):
            raise ValueError("SessionStart Hook missing from packaged configuration")
        if any(x not in inside for x in
               (".claude-plugin/plugin.json",) if platform == "claude"):
            raise ValueError("Claude manifest missing from ZIP")
        if platform == "chatgpt" and (
            "plugin.json" not in inside or ".codex-plugin/plugin.json" not in inside
        ):
            raise ValueError("ChatGPT plugin manifests missing from ZIP")
    print(f"OK: {platform} {output} ({len(expected)} skills, v{version})")


def package_agents(output: Path) -> None:
    """Portable project-root archive for native Codex, Pi, and DSH discovery.

    Extract at the repository root; deliberately do not package marketplace
    metadata or optional plugin lifecycle hooks as portable skill assets.
    """
    expected = {entry["name"] for entry in catalog()[1]}
    version, _ = versions()
    if signature(PORTABLE, PORTABLE_DIRS, PORTABLE_FILES) != signature(
            BUNDLE, PORTABLE_DIRS, PORTABLE_FILES):
        raise ValueError("Portable .agents skills differ from the plugin source")
    names = {p.parent.name for p in (PORTABLE / "skills").glob("*/SKILL.md")}
    if names != expected:
        raise ValueError(f"Expected portable {sorted(expected)}, got {sorted(names)}")

    contents = []
    for name in PORTABLE_DIRS:
        folder = PORTABLE / name
        if not folder.is_dir() or folder.is_symlink():
            raise ValueError(f"Missing or unsafe portable directory: {folder}")
        contents.extend(p for p in folder.rglob("*") if p.is_file() or p.is_symlink())
    contents.extend(PORTABLE / name for name in PORTABLE_FILES)
    if any(not p.is_file() or p.is_symlink()
           or any(parent.is_symlink() for parent in p.parents if parent != ROOT)
           for p in contents):
        raise ValueError("Portable archive has a missing or symlinked file")
    output = output.resolve()
    if PORTABLE in output.parents or BUNDLE in output.parents:
        raise ValueError("ZIP must be outside generated source directories")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(contents, key=lambda p: p.relative_to(ROOT).as_posix()):
            info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(),
                                   date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 << 16)
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
    with zipfile.ZipFile(output) as verify:
        inside = set(verify.namelist())
        names = {item.split("/")[2] for item in inside
                 if re.fullmatch(r"\.agents/skills/[^/]+/SKILL\.md", item)}
        if names != expected or verify.testzip() is not None:
            raise ValueError("Portable ZIP payload verification failed")
        if not {".agents/SOURCES.md", ".agents/CHANGELOG.md"}.issubset(inside):
            raise ValueError("Portable provenance or release notes missing")
        notes = verify.read(".agents/CHANGELOG.md").decode("utf-8")
        latest = re.search(r"(?m)^## \[([0-9]+\.[0-9]+\.[0-9]+)\] - ", notes)
        if latest is None or latest.group(1) != version:
            raise ValueError("Portable archive version disagrees with plugin release")
        if any(item.startswith(".agents/plugins/") or "hooks/hooks.json" in item
               for item in inside):
            raise ValueError("Portable archive must not install plugin hooks")
    print(f"OK: agents {output} ({len(expected)} skills, v{version})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", choices=("all", "agents", "claude", "chatgpt"),
                        default="all")
    parser.add_argument("--output", type=Path,
                        help="ZIP path for one platform; directory when --platform=all")
    args = parser.parse_args()
    platforms = ("agents", "claude", "chatgpt") if args.platform == "all" else (args.platform,)
    if args.platform == "all" and args.output is not None and args.output.suffix == ".zip":
        parser.error("--platform all requires an output directory, not a ZIP path")
    for platform in platforms:
        path = args.output if len(platforms) == 1 and args.output is not None else (
            (args.output or ROOT / "dist") / f"oydodo-skills-{platform}.zip"
        )
        if platform == "agents":
            package_agents(path)
        else:
            package(platform, path)


if __name__ == "__main__":
    main()
