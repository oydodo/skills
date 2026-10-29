#!/usr/bin/env python3
"""Backward-compatible Claude-only entrypoint. Prefer package_plugins.py."""
from __future__ import annotations

import argparse
from pathlib import Path

from build_plugins import ROOT
from package_plugins import package


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=ROOT / "dist" / "oydodo-skills-claude.zip")
    args = parser.parse_args()
    package("claude", args.output)
