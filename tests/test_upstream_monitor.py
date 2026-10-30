"""Contract: scheduled upstream updates must track exactly curated submodules."""
from __future__ import annotations

from configparser import ConfigParser
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]


class UpstreamMonitorContractTest(unittest.TestCase):
    def test_dependabot_tracks_only_selected_upstreams(self):
        config = yaml.safe_load((ROOT / ".github/dependabot.yml").read_text(encoding="utf-8"))
        self.assertEqual(config["version"], 2)
        (job,) = config["updates"]
        self.assertEqual(job["package-ecosystem"], "gitsubmodule")
        self.assertEqual(job["directory"], "/")
        self.assertEqual(job["schedule"]["interval"], "weekly")
        self.assertEqual(job["schedule"]["timezone"], "Asia/Taipei")

        # Dependabot Git Submodules dependency names are .gitmodules paths.
        wanted = {entry["dependency-name"] for entry in job["allow"]}
        self.assertEqual(len(wanted), len(job["allow"]))
        catalog = yaml.safe_load((ROOT / "registry/skills.yaml").read_text(encoding="utf-8"))
        sources = {item["source"] for item in catalog["skills"] if item["source"] != "maintained"}
        selected = {catalog["upstreams"][source]["module_path"] for source in sources}
        self.assertEqual(wanted, selected, "Dependabot allow list drifted from selected sources")

        module_config = ConfigParser(interpolation=None)
        module_config.read(ROOT / ".gitmodules", encoding="utf-8")
        declared_paths = {module_config[section]["path"] for section in module_config.sections()}
        self.assertTrue(wanted <= declared_paths)
        self.assertNotIn("upstream/deepseek-harness", wanted)

    def test_no_unattended_merge(self):
        # Auto-PR creation is permitted; auto-merge remains a human decision.
        job = yaml.safe_load((ROOT / ".github/dependabot.yml").read_text(encoding="utf-8"))["updates"][0]
        self.assertNotIn("auto-merge", job)
        self.assertGreater(job["open-pull-requests-limit"], 0)


if __name__ == "__main__":
    unittest.main()
