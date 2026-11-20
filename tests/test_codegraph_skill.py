"""Contract checks for the separately installed open-source CodeGraph skill."""
from __future__ import annotations

import json
from pathlib import Path
import re
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/codegraph/SKILL.md"
UPSTREAM = ROOT / "skills/codegraph/references/upstream.md"
METADATA = ROOT / "skills/codegraph/agents/openai.yaml"
BUNDLE = ROOT / "plugins/oydodo-skills"


class CodeGraphSkillContractTest(unittest.TestCase):
    def test_skill_frontmatter_and_metadata(self):
        value = SKILL.read_text(encoding="utf-8")
        match = re.match(r"(?s)^---\n(.*?)\n---\n", value)
        self.assertIsNotNone(match, "Missing skill frontmatter")
        header = yaml.safe_load(match.group(1))
        self.assertEqual(header["name"], "codegraph")
        self.assertIn("colbymchenry", header["description"])
        self.assertIn("index", header["description"].lower())
        info = yaml.safe_load(METADATA.read_text(encoding="utf-8"))
        self.assertEqual(info["interface"]["display_name"], "CodeGraph")

    def test_registry_and_catalog_are_consistent(self):
        catalog = yaml.safe_load((ROOT / "registry/skills.yaml").read_text(encoding="utf-8"))
        items = catalog["skills"]
        self.assertEqual(len(items), 19)
        self.assertEqual(len({s["name"] for s in items}), 19)
        (entry,) = [s for s in items if s["name"] == "codegraph"]
        self.assertEqual(entry["source"], "maintained")
        self.assertEqual(entry["skill_path"], "skills/codegraph")
        curation = yaml.safe_load((ROOT / "registry/curation.yaml").read_text(encoding="utf-8"))
        self.assertEqual(curation["selected_count"], 19)
        self.assertIn("codegraph", curation["selected"]["coding"])
        self.assertNotIn("codegraph", curation["not_selected"]["codas_excluded"])
        self.assertIn("codas/codegraph", curation["not_selected"]["codas_excluded"])

    def test_upstream_pinned_and_licensed(self):
        text = UPSTREAM.read_text(encoding="utf-8")
        self.assertIn("github.com/colbymchenry/codegraph", text)
        self.assertIn("v1.6.3", text)
        self.assertIn("ef4bd058d97020a2b2a74a89f1bf21b84e9f5b30", text)
        self.assertIn("v1.6.2", text)  # backward compatibility
        self.assertIn("6560052a6f856855d3f71eee838fd66ccfa4285d", text)
        self.assertIn("MIT", text)

    def test_missing_tool_is_nonblocking_and_setup_is_explicit(self):
        body = SKILL.read_text(encoding="utf-8")
        self.assertIn("nonblocking", body)
        self.assertIn("codegraph_explore", body)
        self.assertIn("codegraph status", body)
        self.assertIn("does **not** bundle", body)
        self.assertIn("No index writes just from activation", body)
        self.assertIn("Respect explicit read-only instructions", body)
        self.assertIn("Web-only", body)

    def test_missing_and_stale_indexes_are_repaired_only_on_demand(self):
        body = SKILL.read_text(encoding="utf-8")
        examples = (ROOT / "skills/codegraph/references/evaluation.md").read_text(encoding="utf-8")
        for snippet in (
            "Ensure a usable graph, only when the task needs one",
            "codegraph init <repo-root> --yes --local-only",
            "codegraph init <repo-root> --yes",
            "codegraph sync <repo-root>",
            "codegraph status --strict <repo-root>",
            "codegraph index <repo-root>",
            "Outdated engine/index metadata",
            "Existing current index, MCP",
            "Existing current index, CLI only",
            "Persistent inconsistency or damage",
            "Incremental `sync` does not reprocess all existing symbols",
            "Never loop",
            "Do not add background daemons",
            "no conflicting index writer",
        ):
            self.assertIn(snippet, body)
        for case in (
            "Missing local index",
            "Older CLI fallback",
            "Old engine index",
            "Current index through MCP",
            "Existing index, CLI only",
            "Changed file, MCP pending",
            "Incomplete language coverage",
            "Broken index",
            "Read-only worktree",
            "Wrong worktree",
            "Negative: tiny edit",
            "Negative: age/HEAD alone",
            "Restricted location",
        ):
            self.assertIn(case, examples)
        self.assertNotIn("curl -fsSL", body)
        self.assertNotIn("codegraph install --yes", body)
        self.assertNotIn("codegraph uninit <repo-root>", body)

    def test_build_and_release_packaging(self):
        generated = BUNDLE / "skills/codegraph"
        self.assertTrue((generated / "SKILL.md").is_file())
        self.assertTrue((generated / "agents/openai.yaml").is_file())
        self.assertEqual((generated / "references/upstream.md").read_bytes(), UPSTREAM.read_bytes())
        skill_text = (generated / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: codegraph", skill_text)
        release = json.loads((BUNDLE / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(release["version"], "0.1.19")
        notes = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn("## [0.1.10]", notes)

    def test_not_in_global_hook_or_core_schemas(self):
        core = (ROOT / "core/always-on.md").read_text(encoding="utf-8")
        self.assertNotIn("skills/codegraph/SKILL.md", core)
        hook = (ROOT / "core/hooks.json").read_text(encoding="utf-8")
        self.assertNotIn("codegraph install", hook)


if __name__ == "__main__":
    unittest.main()
