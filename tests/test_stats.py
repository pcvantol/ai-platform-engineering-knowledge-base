from __future__ import annotations

import json
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import tempfile
import unittest

from cli.aikb_cli.main import main
from cli.aikb_cli.stats import KnowledgeBaseStatistics, StatsConfig
from cli.aikb_cli.status import IMPLEMENTED_COMMANDS


def write(root: Path, relative: str, content: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def record(identifier: str, lifecycle: str, extra: str = "", traceability: str = "") -> str:
    return f"# {identifier}\n\n## Metadata\n\n| Field | Value |\n| --- | --- |\n| Identifier | `{identifier}` |\n| Lifecycle state | {lifecycle} |\n{extra}\n## Traceability\n\n{traceability}\n"


class StatisticsTests(unittest.TestCase):
    def test_empty_valid_repository_is_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            before = sorted(root.rglob("*"))
            result = KnowledgeBaseStatistics(root).run(StatsConfig())
            self.assertEqual(result.data["summary"]["engineering_observations"], 0)
            self.assertEqual(before, sorted(root.rglob("*")))
            self.assertIn("Knowledge Lifecycle Funnel", result.rendered)

    def test_populated_counts_domains_and_json_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(root, "sources/sample/README.md", "# Source\n\n## Metadata\n\n| Field | Value |\n| --- | --- |\n| Identifier | `KS-SAMPLE-001` |\n| Lifecycle status | Active |\n")
            write(root, "observations/sample/EO-SAMPLE-001.md", record("EO-SAMPLE-001", "Repository Observation", "| Knowledge Source | `KS-SAMPLE-001` |\n| Source repository | `owner/sample` |\n| Engineering domain | Platform Engineering |\n| Evidence type | repository documentation |", "Evidence: `README.md`\n\n`KS-SAMPLE-001`"))
            write(root, "candidates/sample/KC-SAMPLE-001.md", record("KC-SAMPLE-001", "Knowledge Candidate", "| Engineering domain | Platform Engineering |", "`EO-SAMPLE-001`"))
            write(root, "concepts/sample/KCN-SAMPLE-001.md", record("KCN-SAMPLE-001", "Knowledge Concept", "| Engineering domain | Platform Engineering |", "`KC-SAMPLE-001`"))
            write(root, "generalized/sample/GK-SAMPLE-001.md", record("GK-SAMPLE-001", "Generalized Knowledge", "| Engineering domains | Platform Engineering |", "`KCN-SAMPLE-001`"))
            write(root, "certified/sample/CK-SAMPLE-001.md", record("CK-SAMPLE-001", "Certified Knowledge", "| Engineering domains | Platform Engineering |\n| Certification status | Certified |", "`GK-SAMPLE-001`\n\n## Source Evidence\n\nEvidence"))
            stats = KnowledgeBaseStatistics(root)
            first = stats.run(StatsConfig(format="json")).rendered
            second = stats.run(StatsConfig(format="json")).rendered
            self.assertEqual(json.loads(first)["summary"]["certified_knowledge"], 1)
            self.assertEqual(json.loads(first)["domains"][0]["domain"], "Platform Engineering")
            self.assertEqual(json.loads(first)["traceability"]["knowledge_objects_with_complete_lineage"], 5)
            self.assertEqual(json.loads(first)["summary"], json.loads(second)["summary"])

    def test_unknown_inventory_metrics_are_not_zero(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            data = KnowledgeBaseStatistics(Path(directory)).collect()
            self.assertIsNone(data["runtime_inventory"]["registered_capabilities"]["count"])
            self.assertFalse(data["runtime_inventory"]["registered_capabilities"]["supported"])

    def test_missing_required_lineage_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(root, "candidates/sample/KC-SAMPLE-001.md", record("KC-SAMPLE-001", "Knowledge Candidate"))
            with self.assertRaisesRegex(RuntimeError, "required lineage"):
                KnowledgeBaseStatistics(root).collect()

    def test_output_is_explicit_and_status_includes_stats(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "reports" / "stats.json"
            result = KnowledgeBaseStatistics(root).run(StatsConfig(format="json", output=output))
            self.assertEqual(result.output_path, output.resolve())
            self.assertTrue(output.exists())
            self.assertIn("aikb stats", [item.command for item in IMPLEMENTED_COMMANDS])

    def test_cli_parser_registration(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with redirect_stdout(StringIO()):
                self.assertEqual(main(["stats", "--format", "json"], repository_root=Path(directory)), 0)


if __name__ == "__main__":
    unittest.main()
