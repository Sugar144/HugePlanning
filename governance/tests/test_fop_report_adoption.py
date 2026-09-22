from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / ".factory" / "observation-policy.yaml"


class FopReportAdoptionTests(unittest.TestCase):
    def _manifest(self) -> dict:
        value = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertIsInstance(value, dict)
        return value

    def test_partial_report_binding_is_exact(self):
        manifest = self._manifest()
        self.assertEqual(manifest["schemaVersion"], "0.1.0")
        self.assertEqual(manifest["kind"], "factory.observation-adoption")
        self.assertEqual(manifest["repository"], "Sugar144/HugePlanning")
        self.assertEqual(manifest["rolloutMode"], "REPORT")
        self.assertEqual(
            manifest["policy"],
            {
                "id": "factory.observation-policy/0.1.0",
                "sha256": "94f9272972a21e2769c6d6a2ec4ada891c1ad624f79dc7a20fd2cfa006f73b21",
            },
        )
        self.assertEqual(
            manifest["executionClasses"],
            {"DETERMINISTIC_AUTOMATION": {"profile": "OBS-0"}},
        )

    def test_agentic_methodology_runs_remain_unbound(self):
        manifest = self._manifest()
        self.assertNotIn("AI_AGENTIC_HIGH_VALUE", manifest["executionClasses"])
        self.assertEqual(set(manifest["executionClasses"]), {"DETERMINISTIC_AUTOMATION"})


if __name__ == "__main__":
    unittest.main()
