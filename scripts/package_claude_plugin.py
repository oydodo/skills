#!/usr/bin/env python3
"""Package the shared oydodo-skills contents for Claude web or Claude Code.

Usage:
  python3 scripts/package_claude_plugin.py
  python3 scripts/package_claude_plugin.py --output dist/custom-name.zip

The archive root contains .claude-plugin/plugin.json, skills/, and licenses/.
No external downloads, third-party Python packages, or machine-specific paths.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "oydodo-skills"
REQUIRED = {
    "crux-first-reasoning",
    "grilling",
    "independent-judgment",
    "interview-me",
    "ponytail",
    "technical-documentation",
    "technical-language",
    "technical-writing",
}
PARTS = (".claude-plugin", "skills", "licenses")
EXTRA_FILES = ("README.md", "SOURCES.md")


def package(output: Path) -> None:
    manifest_path = PLUGIN / ".claude-plugin" / "plugin.json"
    meta = json.loads(manifest_path.read_text(encoding="utf-8"))
    if meta.get("name") != "oydodo-skills":
        raise ValueError("Claude plugin manifest name mismatch")

    skill_files = list((PLUGIN / "skills").glob("*/SKILL.md"))
    names = {p.parent.name for p in skill_files}
    if names != REQUIRED:
        raise ValueError(
            f"Expected eight independent skills; missing={sorted(REQUIRED - names)}, "
            f"extra={sorted(names - REQUIRED)}"
        )
    for path in skill_files:
        body = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", body, re.S)
        if not match or not re.search(r"^name:\s*", match[1], re.M) or not re.search(
            r"^description:\s*", match[1], re.M
        ):
            raise ValueError(f"Missing valid SKILL.md frontmatter: {path}")

    files = []
    for part in PARTS:
        directory = PLUGIN / part
        if not directory.is_dir():
            raise ValueError(f"Missing plugin directory: {directory}")
        files.extend(p for p in directory.rglob("*") if p.is_file())
    files.extend(PLUGIN / name for name in EXTRA_FILES)
    if any(not p.is_file() or p.is_symlink() for p in files):
        raise ValueError("Missing or symlinked plugin file")

    output = output.resolve()
    if PLUGIN in output.parents:
        raise ValueError("Output ZIP must not be within plugin source tree")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(files, key=lambda p: p.relative_to(PLUGIN).as_posix()):
            name = path.relative_to(PLUGIN).as_posix()
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 << 16)
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)

    with zipfile.ZipFile(output) as check:
        entrypoints = {Path(n).parent.name for n in check.namelist()
                       if re.fullmatch(r"skills/[^/]+/SKILL.md", n)}
        if entrypoints != REQUIRED or ".claude-plugin/plugin.json" not in check.namelist():
            raise ValueError("Archive validation failed")
        if check.testzip() is not None:
            raise ValueError("ZIP CRC validation failed")
    print(f"OK: {output} ({len(files)} files, {len(names)} skills)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=ROOT / "dist" / "oydodo-skills-claude.zip")
    args = parser.parse_args()
    package(args.output)
