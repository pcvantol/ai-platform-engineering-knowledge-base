from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import re

from .validation import KnowledgeBaseValidator, ValidateConfig


SUPPORTED_IMPROVEMENT_AREAS = (
    "knowledge",
    "generators",
    "publications",
    "repository",
    "cli",
)


@dataclass(frozen=True)
class ImproveConfig:
    area: str | None = None
    output: Path | None = None


@dataclass(frozen=True)
class ImprovementRecommendation:
    identifier: str
    improvement_type: str
    title: str
    priority: str
    engineering_value: str
    affected_area: str
    objective_metrics: dict[str, str]
    supporting_evidence: list[str]
    rationale: str
    estimated_effort: str
    governance_path: str


@dataclass(frozen=True)
class ImproveResult:
    report: str
    report_path: Path | None
    recommendation_count: int


class KnowledgeSystemImprover:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root

    def improve(self, config: ImproveConfig) -> ImproveResult:
        areas = self._areas(config.area)
        metrics = self._metrics()
        validation = KnowledgeBaseValidator(self.repository_root).validate(ValidateConfig())
        recommendations = self._recommendations(areas, metrics, validation)
        report = self._render_report(areas, metrics, validation, recommendations)
        report_path = None
        if config.output:
            report_path = config.output.resolve()
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(report, encoding="utf-8")
        return ImproveResult(
            report=report,
            report_path=report_path,
            recommendation_count=len(recommendations),
        )

    def _areas(self, area: str | None) -> set[str]:
        if not area:
            return set(SUPPORTED_IMPROVEMENT_AREAS)
        if area not in SUPPORTED_IMPROVEMENT_AREAS:
            supported = ", ".join(SUPPORTED_IMPROVEMENT_AREAS)
            raise RuntimeError(f"Unsupported improvement area: {area}. Supported areas: {supported}")
        return {area}

    def _metrics(self) -> dict[str, object]:
        counts = {
            "sources": self._count("sources", "KS-"),
            "observations": self._count("observations", "EO-"),
            "candidates": self._count("candidates", "KC-"),
            "concepts": self._count("concepts", "KCN-"),
            "generalized": self._count("generalized", "GK-"),
            "certified": self._count("certified", "CK-"),
            "publications": len([p for p in (self.repository_root / "publications").glob("**/*.md") if p.name != "README.md"]),
            "generators": len([p for p in (self.repository_root / "generators").glob("*/README.md")]),
            "templates": len([p for p in (self.repository_root / "templates").glob("**/*") if p.is_file()]),
            "cli_modules": len(list((self.repository_root / "cli" / "aikb_cli").glob("*.py"))),
        }
        total_knowledge = sum(counts[key] for key in ["observations", "candidates", "concepts", "generalized", "certified"])
        certified_ratio = self._ratio(counts["certified"], max(total_knowledge, 1))
        candidate_to_concept = self._ratio(counts["concepts"], max(counts["candidates"], 1))
        generalized_to_certified = self._ratio(counts["certified"], max(counts["generalized"], 1))
        publication_coverage = self._ratio(counts["publications"], max(counts["certified"], 1))
        return {
            "counts": counts,
            "certified_ratio": certified_ratio,
            "candidate_to_concept_ratio": candidate_to_concept,
            "generalized_to_certified_ratio": generalized_to_certified,
            "publication_coverage_ratio": publication_coverage,
            "relationship_quality": self._relationship_quality(),
            "knowledge_reuse": self._knowledge_reuse(),
            "generator_effectiveness": self._generator_effectiveness(counts),
            "publication_quality": self._publication_quality(),
            "repository_health": self._repository_health(),
            "knowledge_drift": "available through aikb evolve",
            "user_feedback": "not configured",
        }

    def _recommendations(
        self,
        areas: set[str],
        metrics: dict[str, object],
        validation,
    ) -> list[ImprovementRecommendation]:
        recommendations: list[ImprovementRecommendation] = []
        counts = metrics["counts"]
        assert isinstance(counts, dict)

        if "knowledge" in areas:
            recommendations.append(
                self._recommendation(
                    "IR-001",
                    "knowledge quality",
                    "Add trend history for lifecycle throughput.",
                    "Medium",
                    "Improves visibility into promotion rate and certification throughput.",
                    "knowledge",
                    {
                        "Observations": str(counts["observations"]),
                        "Candidates": str(counts["candidates"]),
                        "Concepts": str(counts["concepts"]),
                        "Generalized Knowledge": str(counts["generalized"]),
                        "Certified Knowledge": str(counts["certified"]),
                        "Certified ratio": str(metrics["certified_ratio"]),
                    },
                    ["lifecycle object counts", "validation qualification decisions"],
                    "Current lifecycle counts are available, but trend history is not yet captured as a reusable improvement input.",
                    "Medium",
                    "Quality review -> operating model backlog -> governed implementation.",
                )
            )
            if validation.finding_count == 0:
                recommendations.append(
                    self._recommendation(
                        "IR-002",
                        "knowledge completeness",
                        "Introduce positive validation evidence retention.",
                        "Low",
                        "Preserves proof that zero-finding validation was performed at a point in time.",
                        "knowledge",
                        {
                            "Validation findings": str(validation.finding_count),
                            "Relationship qualification": validation.qualification.get("RELATIONSHIPS_VALID", ""),
                            "Traceability qualification": validation.qualification.get("TRACEABILITY_VALID", ""),
                        },
                        ["aikb validate report", "qualification decisions"],
                        "The repository validates cleanly; preserving validation snapshots would make qualification history easier to audit.",
                        "Low",
                        "Governance review -> decide whether validation reports become retained evidence artifacts.",
                    )
                )

        if "generators" in areas:
            recommendations.append(
                self._recommendation(
                    "IR-003",
                    "generator improvements",
                    "Add generator regression fixtures for generated artifacts.",
                    "High",
                    "Improves repeatability and detects generator drift before generated programs are used.",
                    "generators",
                    {
                        "Implemented generators": str(counts["generators"]),
                        "Template files": str(counts["templates"]),
                        "Generator effectiveness": str(metrics["generator_effectiveness"]),
                    },
                    ["generators/README.md", "templates/", "aikb generate validation runs"],
                    "Generators are operational and deterministic, but fixture-based regression evidence is not yet retained.",
                    "Medium",
                    "Generator owner review -> test fixture design -> governed implementation.",
                )
            )

        if "publications" in areas:
            recommendations.append(
                self._recommendation(
                    "IR-004",
                    "publication improvements",
                    "Track publication freshness against current Certified Knowledge.",
                    "Medium",
                    "Reduces stale publication risk while preserving Certified Knowledge authority.",
                    "publications",
                    {
                        "Publications": str(counts["publications"]),
                        "Certified Knowledge": str(counts["certified"]),
                        "Publication coverage ratio": str(metrics["publication_coverage_ratio"]),
                        "Publication quality": str(metrics["publication_quality"]),
                    },
                    ["publications/README.md", "Certified Knowledge index"],
                    "Publications are derived from Certified Knowledge, but freshness review is not yet an operational metric.",
                    "Medium",
                    "Publication governance review -> refresh policy -> future publish command.",
                )
            )

        if "repository" in areas:
            recommendations.append(
                self._recommendation(
                    "IR-005",
                    "repository structure",
                    "Create retained repository health scorecard snapshots.",
                    "Low",
                    "Improves repository sustainability and long-term health review.",
                    "repository",
                    {
                        "Repository health": str(metrics["repository_health"]),
                        "Validation findings": str(validation.finding_count),
                        "Repository qualification": validation.qualification.get("REPOSITORY_VALID", ""),
                    },
                    ["quality-health/README.md", "aikb validate scorecard"],
                    "The scorecard is generated on demand; retained snapshots would support historical trend review.",
                    "Low",
                    "Operating model review -> decide retention policy -> implement report archive if approved.",
                )
            )

        if "cli" in areas:
            recommendations.append(
                self._recommendation(
                    "IR-006",
                    "CLI usability",
                    "Add machine-readable JSON output options for reporting commands.",
                    "Medium",
                    "Improves automation quality without changing canonical knowledge.",
                    "cli",
                    {
                        "CLI modules": str(counts["cli_modules"]),
                        "Reporting commands": "ask, generate, evolve, validate, improve",
                    },
                    ["cli/README.md", "reporting command outputs"],
                    "Current reports are human-readable Markdown. JSON output would support dashboards and automation while preserving governance.",
                    "Medium",
                    "CLI owner review -> output contract design -> backward-compatible implementation.",
                )
            )

        return recommendations

    def _render_report(
        self,
        areas: set[str],
        metrics: dict[str, object],
        validation,
        recommendations: list[ImprovementRecommendation],
    ) -> str:
        timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        return f"""# Continuous Knowledge System Improvement Report

## Report Metadata

| Field | Value |
| --- | --- |
| Repository | `{self.repository_root}` |
| Timestamp | {timestamp} |
| Improvement areas | {", ".join(sorted(areas))} |
| Recommendation count | {len(recommendations)} |

## Repository Metrics

{self._metrics_table(metrics)}

## Validation Evidence

| Qualification | Result |
| --- | --- |
{self._qualification_rows(validation.qualification)}

Validation findings: {validation.finding_count}

## Improvement Analysis

{self._analysis(metrics, validation)}

## Improvement Recommendations

{self._recommendation_sections(recommendations)}

## Governance Boundary

This report proposes improvements. It does not modify repositories, Certified Knowledge, publications, governance, generator outputs, templates or engineering history.
"""

    def _metrics_table(self, metrics: dict[str, object]) -> str:
        counts = metrics["counts"]
        assert isinstance(counts, dict)
        rows = ["| Metric | Value |", "| --- | --- |"]
        for key, value in counts.items():
            rows.append(f"| {key.replace('_', ' ').title()} | {value} |")
        for key in [
            "certified_ratio",
            "candidate_to_concept_ratio",
            "generalized_to_certified_ratio",
            "publication_coverage_ratio",
            "relationship_quality",
            "knowledge_reuse",
            "generator_effectiveness",
            "publication_quality",
            "repository_health",
            "knowledge_drift",
            "user_feedback",
        ]:
            rows.append(f"| {key.replace('_', ' ').title()} | {metrics[key]} |")
        return "\n".join(rows)

    def _qualification_rows(self, qualification: dict[str, str]) -> str:
        return "\n".join(f"| `{key}` | {value} |" for key, value in qualification.items())

    def _analysis(self, metrics: dict[str, object], validation) -> str:
        return "\n".join(
            [
                f"- Knowledge quality is supported by validation result `{validation.qualification.get('KNOWLEDGE_VALID')}`.",
                f"- Relationship quality is `{metrics['relationship_quality']}`.",
                f"- Publication quality is `{metrics['publication_quality']}`.",
                f"- Generator effectiveness is `{metrics['generator_effectiveness']}`.",
                f"- Repository health is `{metrics['repository_health']}`.",
                "- Recommendations remain proposals and require engineering review before implementation.",
            ]
        )

    def _recommendation_sections(self, recommendations: list[ImprovementRecommendation]) -> str:
        if not recommendations:
            return "No recommendations."
        sections = []
        for item in recommendations:
            sections.append(
                f"""### {item.identifier}: {item.title}

| Field | Value |
| --- | --- |
| Improvement type | {item.improvement_type} |
| Priority | {item.priority} |
| Engineering value | {item.engineering_value} |
| Affected area | {item.affected_area} |
| Estimated effort | {item.estimated_effort} |
| Governance path | {item.governance_path} |

Objective metrics:

{self._dict_table(item.objective_metrics)}

Supporting evidence:

{self._list(item.supporting_evidence)}

Engineering rationale: {item.rationale}
"""
            )
        return "\n".join(sections)

    def _dict_table(self, values: dict[str, str]) -> str:
        rows = ["| Metric | Value |", "| --- | --- |"]
        for key, value in values.items():
            rows.append(f"| {key} | {value} |")
        return "\n".join(rows)

    def _list(self, values: list[str]) -> str:
        return "\n".join(f"- {value}" for value in values)

    def _recommendation(
        self,
        identifier: str,
        improvement_type: str,
        title: str,
        priority: str,
        engineering_value: str,
        affected_area: str,
        metrics: dict[str, str],
        evidence: list[str],
        rationale: str,
        effort: str,
        governance_path: str,
    ) -> ImprovementRecommendation:
        enriched_metrics = {
            "Certified Knowledge baseline": str(self._count("certified", "CK-")),
            "Repository health": self._repository_health(),
            **metrics,
        }
        enriched_evidence = [
            "certified/README.md",
            "repository health metrics",
            *evidence,
        ]
        return ImprovementRecommendation(
            identifier=identifier,
            improvement_type=improvement_type,
            title=title,
            priority=priority,
            engineering_value=engineering_value,
            affected_area=affected_area,
            objective_metrics=enriched_metrics,
            supporting_evidence=enriched_evidence,
            rationale=rationale,
            estimated_effort=effort,
            governance_path=governance_path,
        )

    def _count(self, folder: str, prefix: str) -> int:
        root = self.repository_root / folder
        if not root.exists():
            return 0
        count = 0
        for path in root.glob("**/*.md"):
            if path.name == "README.md" and folder != "sources":
                continue
            if prefix in path.read_text(encoding="utf-8"):
                count += 1
        return count

    def _relationship_quality(self) -> str:
        validation = KnowledgeBaseValidator(self.repository_root).validate(
            ValidateConfig(knowledge=True)
        )
        if validation.qualification.get("RELATIONSHIPS_VALID") == "PASS":
            return "pass"
        return "review"

    def _knowledge_reuse(self) -> str:
        publications_text = self._combined_text(self.repository_root / "publications")
        certified_ids = re.findall(r"\bCK-[A-Z0-9-]+\b", publications_text)
        return f"{len(set(certified_ids))} certified references in publications"

    def _generator_effectiveness(self, counts: dict[str, int]) -> str:
        if counts["generators"] >= 2 and counts["templates"] > 0:
            return "operational"
        return "review"

    def _publication_quality(self) -> str:
        validation = KnowledgeBaseValidator(self.repository_root).validate(
            ValidateConfig(publications=True)
        )
        return "pass" if validation.qualification.get("PUBLICATION_VALID") == "PASS" else "review"

    def _repository_health(self) -> str:
        validation = KnowledgeBaseValidator(self.repository_root).validate(ValidateConfig())
        return "pass" if validation.qualification.get("REPOSITORY_VALID") == "PASS" else "review"

    def _ratio(self, numerator: int, denominator: int) -> str:
        return f"{numerator / denominator:.2f}"

    def _combined_text(self, root: Path) -> str:
        if not root.exists():
            return ""
        return "\n".join(path.read_text(encoding="utf-8") for path in root.glob("**/*.md"))
