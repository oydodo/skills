"""Tests for the optional, fail-open SessionStart Hook (POSIX runtime)."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HOOK = ROOT / "core" / "hooks.json"
CORE = ROOT / "core" / "always-on.md"


def command():
    data = json.loads(HOOK.read_text(encoding="utf-8"))
    (group,) = data["hooks"]["SessionStart"]
    (handler,) = group["hooks"]
    assert group["matcher"] == "^(startup|resume|clear|compact|fork)$"
    assert handler["type"] == "command" and handler["timeout"] == 3
    return handler["command"]


class CoreHookTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="oydodo hook test ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def run_hook(self, **extra_env):
        env = dict(os.environ)
        env.pop("CLAUDE_PLUGIN_ROOT", None)
        env.pop("PLUGIN_ROOT", None)
        env.update(extra_env)
        return subprocess.run(
            ["/bin/sh", "-c", command()],
            input="{}", text=True, capture_output=True,
            cwd=self.root, env=env, timeout=5,
        )

    def install_core(self, content=None):
        path = self.root / "core" / "always-on.md"
        path.parent.mkdir(exist_ok=True)
        path.write_text(CORE.read_text(encoding="utf-8") if content is None else content,
                        encoding="utf-8")
        return path

    def assert_silent_success(self, r):
        self.assertEqual((r.returncode, r.stdout, r.stderr), (0, "", ""))

    def test_claude_root_loads_core(self):
        self.install_core()
        r = self.run_hook(CLAUDE_PLUGIN_ROOT=str(self.root))
        self.assertEqual(r.returncode, 0)
        self.assertEqual(r.stdout, CORE.read_text(encoding="utf-8"))

    def test_codex_root_loads_core(self):
        self.install_core()
        r = self.run_hook(PLUGIN_ROOT=str(self.root))
        self.assertEqual(r.returncode, 0)
        self.assertEqual(r.stdout, CORE.read_text(encoding="utf-8"))

    def test_missing_root_is_silent(self):
        self.assert_silent_success(self.run_hook())

    def test_missing_file_is_silent(self):
        self.assert_silent_success(self.run_hook(PLUGIN_ROOT=str(self.root)))

    def test_empty_file_is_silent(self):
        self.install_core("")
        self.assert_silent_success(self.run_hook(PLUGIN_ROOT=str(self.root)))

    def test_directory_instead_of_file_is_silent(self):
        (self.root / "core" / "always-on.md").mkdir(parents=True)
        self.assert_silent_success(self.run_hook(PLUGIN_ROOT=str(self.root)))

    def test_cat_failure_is_silent(self):
        self.install_core()
        shim = self.root / "bin"
        shim.mkdir()
        fake_cat = shim / "cat"
        fake_cat.write_text("#!/bin/sh\nexit 17\n", encoding="utf-8")
        fake_cat.chmod(0o755)
        self.assert_silent_success(self.run_hook(PLUGIN_ROOT=str(self.root), PATH=str(shim)))

    def test_core_links_and_priority(self):
        text = CORE.read_text(encoding="utf-8")
        for skill in ("philosophical-foundation", "independent-judgment",
                      "crux-first-reasoning"):
            self.assertIn(f"skills/{skill}/SKILL.md", text)
            self.assertIn(f"github.com/oydodo/skills/blob/main/skills/{skill}/SKILL.md", text)
        self.assertLess(text.index("主要矛盾优先"), text.index("关键不确定性从属"))

    def test_bundled_assets_match_sources(self):
        bundle = ROOT / "plugins" / "oydodo-skills"
        self.assertEqual((bundle / "core" / "always-on.md").read_bytes(),
                         CORE.read_bytes())
        self.assertEqual((bundle / "hooks" / "hooks.json").read_bytes(),
                         HOOK.read_bytes())


if __name__ == "__main__":
    unittest.main()
