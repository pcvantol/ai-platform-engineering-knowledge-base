from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import json

from .assistant import CertifiedKnowledge, EngineeringAssistant


@dataclass(frozen=True)
class EvolveConfig:
    target: str | None = None
    program_path: Path | None = None
    output: Path | None = None


@dataclass(frozen=True)
class EvolveResult:
    program_identifier: str
    drift_level: str
    recommendation_count: int
    report: str
    report_path: Path | None = None


@dataclass(frozen=True)
class EvolutionRecommendation:
    identifier: str
    evolution_type: str
    title: str
    affected_artifacts: list[str]
    affected_knowledge: list[CertifiedKnowledge]
    rationale: str
    implementation_impact: str
    estimated_effort: str
    dependencies: list[str]
    risk_assessment: str


class EngineeringProgramEvolution:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root
        self.assistant = EngineeringAssistant(repository_root)

    def evolve(self, config: EvolveConfig) -> list[EvolveResult]:
        manifest_paths = self._manifest_paths(config)
        current_knowledge = self.assistant._load_certified_knowledge()
        results: list[EvolveResult] = []
        for manifest_path in manifest_paths:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            result = self._evolve_program(manifest_path, manifest, current_knowledge)
            if config.output:
                output_path = self._output_path(config.output, result, len(manifest_paths) > 1)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(result.report, encoding="utf-8")
                result = EvolveResult(
                    program_identifier=result.program_identifier,
                    drift_level=result.drift_level,
                    recommendation_count=result.recommendation_count,
                    report=result.report,
                    report_path=output_path,
                )
            results.append(result)
        return results

    def _manifest_paths(self, config: EvolveConfig) -> list[Path]:
        if config.program_path:
            return [self._manifest_from_path(config.program_path)]
        if config.target:
            target_path = Path(config.target)
            if target_path.exists():
                return [self._manifest_from_path(target_path)]
            generated_path = self.repository_root / "generated-programs" / config.target
            if generated_path.exists():
                return [self._manifest_from_path(generated_path)]
            matches = [
                path
                for path in self._all_program_manifests()
                if config.target.lower() in path.read_text(encoding="utf-8").lower()
            ]
            if matches:
                return matches
            raise RuntimeError(f"No Engineering Program manifest found for target: {config.target}")
        manifests = self._all_program_manifests()
        if not manifests:
            raise RuntimeError(
                "No Engineering Program manifests found. Use --program <path> or generate a program first."
            )
        return manifests

    def _manifest_from_path(self, path: Path) -> Path:
        resolved = path.resolve()
        if resolved.is_file():
            return resolved
        manifest = resolved / ".aikb" / "engineering-program-manifest.json"
        if manifest.exists():
            return manifest
        raise RuntimeError(f"No Engineering Program manifest found at: {path}")

    def _all_program_manifests(self) -> list[Path]:
        roots = [
            Path.cwd() / "generated-programs",
            self.repository_root / "generated-programs",
        ]
        manifests: list[Path] = []
        for root in roots:
            if root.exists():
                manifests.extend(root.glob("*/.aikb/engineering-program-manifest.json"))
        return sorted(set(manifests))

    def _evolve_program(
        self,
        manifest_path: Path,
        manifest: dict[str, object],
        current_knowledge: list[CertifiedKnowledge],
    ) -> EvolveResult:
        program = manifest.get("program", {})
        if not isinstance(program, dict):
            program = {}
        program_identifier = str(program.get("identifier", manifest_path.parent.parent.name))
        program_type = str(program.get("type", "unknown"))
        generated_artifacts = [
            str(item)
            for item in manifest.get("generated_artifacts", [])
            if isinstance(item, str)
        ]
        program_records = [
            item
            for item in manifest.get("traceability_references", [])
            if isinstance(item, dict)
        ]
        program_ids = {
            str(item.get("certified_knowledge"))
            for item in program_records
            if item.get("certified_knowledge")
        }
        current_by_id = {item.identifier: item for item in current_knowledge}
        current_ids = set(current_by_id)
        new_ids = sorted(current_ids - program_ids)
        missing_ids = sorted(program_ids - current_ids)
        changed_ids = self._changed_ids(program_records, current_by_id)
        drift_level = self._drift_level(new_ids, missing_ids, changed_ids, len(program_ids))
        recommendations = self._recommendations(
            program_type,
            generated_artifacts,
            current_knowledge,
            new_ids,
            missing_ids,
            changed_ids,
        )
        report = self._render_report(
            manifest_path,
            manifest,
            current_knowledge,
            new_ids,
            missing_ids,
            changed_ids,
            drift_level,
            recommendations,
        )
        return EvolveResult(
            program_identifier=program_identifier,
            drift_level=drift_level,
            recommendation_count=len(recommendations),
            report=report,
        )

    def _changed_ids(
        self,
        program_records: list[dict[str, object]],
        current_by_id: dict[str, CertifiedKnowledge],
    ) -> list[str]:
        changed: list[str] = []
        for record in program_records:
            identifier = str(record.get("certified_knowledge", ""))
            current = current_by_id.get(identifier)
            if not current:
                continue
            manifest_evidence = {
                (
                    str(item.get("observation", "")),
                    str(item.get("repository", "")),
                    str(item.get("evidence", "")),
                    str(item.get("commit", "")),
                )
                for item in record.get("evidence", [])
                if isinstance(item, dict)
            }
            current_evidence = {
                (
                    item.get("observation", ""),
                    item.get("repository", ""),
                    item.get("evidence", ""),
                    item.get("commit", ""),
                )
                for item in current.evidence_rows
            }
            if manifest_evidence != current_evidence:
                changed.append(identifier)
        return sorted(changed)

    def _drift_level(
        self,
        new_ids: list[str],
        missing_ids: list[str],
        changed_ids: list[str],
        program_count: int,
    ) -> str:
        if not new_ids and not missing_ids and not changed_ids:
            return "no drift"
        if missing_ids:
            return "critical drift"
        total = len(new_ids) + len(changed_ids)
        if program_count and total >= max(5, program_count):
            return "major drift"
        if total >= 3:
            return "moderate drift"
        return "minor drift"

    def _recommendations(
        self,
        program_type: str,
        artifacts: list[str],
        current_knowledge: list[CertifiedKnowledge],
        new_ids: list[str],
        missing_ids: list[str],
        changed_ids: list[str],
    ) -> list[EvolutionRecommendation]:
        recommendations: list[EvolutionRecommendation] = []
        affected_new = [item for item in current_knowledge if item.identifier in new_ids]
        if affected_new:
            recommendations.append(
                self._recommendation(
                    "ER-001",
                    "knowledge integration",
                    "Review newly certified knowledge for program integration.",
                    artifacts or ["README.md"],
                    affected_new,
                    "Current Certified Knowledge contains items not present in the program manifest.",
                    "Review generated artifacts and decide whether to regenerate or patch the program under governance.",
                    "Medium",
                    ["Engineering review", "Program owner approval"],
                    "Medium risk if ignored; the program may miss current canonical knowledge.",
                )
            )
        affected_changed = [item for item in current_knowledge if item.identifier in changed_ids]
        if affected_changed:
            recommendations.append(
                self._recommendation(
                    "ER-002",
                    "documentation evolution",
                    "Review knowledge traceability changes.",
                    [".aikb/engineering-program-manifest.json"],
                    affected_changed,
                    "The evidence recorded in the program manifest differs from current Certified Knowledge.",
                    "Refresh traceability references after human review.",
                    "Low",
                    ["Traceability review"],
                    "Low to medium risk; rationale may still be valid but traceability is stale.",
                )
            )
        if missing_ids:
            recommendations.append(
                EvolutionRecommendation(
                    identifier="ER-003",
                    evolution_type="governance evolution",
                    title="Resolve Certified Knowledge no longer present in the Knowledge Base.",
                    affected_artifacts=["GOVERNANCE.md", ".aikb/engineering-program-manifest.json"],
                    affected_knowledge=[],
                    rationale="The program references Certified Knowledge that is not available in the current Knowledge Base.",
                    implementation_impact="Escalate to governance before using the program for engineering decisions.",
                    estimated_effort="High",
                    dependencies=["Knowledge steward review", "Certification history review"],
                    risk_assessment="Critical risk; program authority may rely on unavailable canonical knowledge.",
                )
            )
        for domain, artifact, evolution_type in [
            ("Architecture", "ARCHITECTURE.md", "architecture improvements"),
            ("Verification", "VERIFICATION_STRATEGY.md", "verification improvements"),
            ("Software Assurance", "SOFTWARE_ASSURANCE_STRATEGY.md", "software assurance improvements"),
            ("Release", "RELEASE_STRATEGY.md", "roadmap evolution"),
            ("Governance", "GOVERNANCE.md", "governance evolution"),
            ("Engineering", "ROADMAP.md", "roadmap evolution"),
            ("Engineering", "BACKLOG.md", "backlog evolution"),
        ]:
            domain_knowledge = self._filter(current_knowledge, domain)
            if artifact in artifacts and domain_knowledge:
                recommendations.append(
                    self._recommendation(
                        f"ER-{len(recommendations) + 1:03d}",
                        evolution_type,
                        f"Review {artifact} against current {domain} knowledge.",
                        [artifact],
                        domain_knowledge[:4],
                        f"The program should remain aligned with Certified Knowledge in {domain}.",
                        "Review artifact content; apply changes only after engineering approval.",
                        "Low",
                        ["Program maintainer review"],
                        "Low risk; recommendation improves alignment and reduces drift.",
                    )
                )
        if program_type != "unknown":
            recommendations.append(
                self._recommendation(
                    f"ER-{len(recommendations) + 1:03d}",
                    "publication refresh",
                    "Evaluate whether derived publications need refresh after program evolution.",
                    ["README.md"],
                    current_knowledge[:4],
                    "Program evolution can change derived communication needs, but publications remain non-canonical.",
                    "Review publication set separately; do not update publications automatically.",
                    "Low",
                    ["Publication owner review"],
                    "Low risk if tracked; moderate risk if external audiences use stale derived material.",
                )
            )
        return recommendations

    def _recommendation(
        self,
        identifier: str,
        evolution_type: str,
        title: str,
        artifacts: list[str],
        knowledge: list[CertifiedKnowledge],
        rationale: str,
        impact: str,
        effort: str,
        dependencies: list[str],
        risk: str,
    ) -> EvolutionRecommendation:
        return EvolutionRecommendation(
            identifier=identifier,
            evolution_type=evolution_type,
            title=title,
            affected_artifacts=artifacts,
            affected_knowledge=knowledge,
            rationale=rationale,
            implementation_impact=impact,
            estimated_effort=effort,
            dependencies=dependencies,
            risk_assessment=risk,
        )

    def _render_report(
        self,
        manifest_path: Path,
        manifest: dict[str, object],
        current_knowledge: list[CertifiedKnowledge],
        new_ids: list[str],
        missing_ids: list[str],
        changed_ids: list[str],
        drift_level: str,
        recommendations: list[EvolutionRecommendation],
    ) -> str:
        generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        program = manifest.get("program", {})
        if not isinstance(program, dict):
            program = {}
        program_identifier = str(program.get("identifier", manifest_path.parent.parent.name))
        return f"""# Engineering Program Evolution Report

## Review Metadata

| Field | Value |
| --- | --- |
| Program identifier | `{program_identifier}` |
| Program type | `{program.get('type', 'unknown')}` |
| Program manifest | `{manifest_path}` |
| Review timestamp | {generated_at} |
| Current knowledge version | repository-snapshot |
| Drift level | {drift_level} |

## Knowledge Drift

| Drift class | Certified Knowledge |
| --- | --- |
| New current knowledge not in program | {self._ids(new_ids)} |
| Program knowledge missing from current KB | {self._ids(missing_ids)} |
| Traceability changed | {self._ids(changed_ids)} |

## Gap Analysis

{self._gap_analysis(new_ids, missing_ids, changed_ids)}

## Impact Analysis

{self._impact_analysis(recommendations)}

## Evolution Recommendations

{self._recommendation_sections(recommendations)}

## Manifest Extension Proposal

The program manifest should track the following fields. This report does not update the manifest automatically.

```json
{json.dumps(self._manifest_extension(drift_level, recommendations, generated_at), indent=2)}
```

## Traceability

{self._traceability(recommendations)}

## Governance Boundary

This report is an evolution proposal. It does not modify repositories, generated programs, Certified Knowledge, publications, or engineering history. Apply recommendations only through engineering review and approval.
"""

    def _gap_analysis(
        self,
        new_ids: list[str],
        missing_ids: list[str],
        changed_ids: list[str],
    ) -> str:
        rows = [
            "- Architecture, governance, verification, assurance, roadmap and backlog should be reviewed against current Certified Knowledge.",
        ]
        if new_ids:
            rows.append("- New Certified Knowledge exists outside the program manifest.")
        if missing_ids:
            rows.append("- The program references Certified Knowledge not found in the current Knowledge Base.")
        if changed_ids:
            rows.append("- Some traceability references differ from current Certified Knowledge evidence.")
        if not new_ids and not missing_ids and not changed_ids:
            rows.append("- No knowledge drift detected; routine review may still identify improvement opportunities.")
        return "\n".join(rows)

    def _recommendation_sections(self, recommendations: list[EvolutionRecommendation]) -> str:
        if not recommendations:
            return "No recommendations."
        sections = []
        for recommendation in recommendations:
            sections.append(
                f"""### {recommendation.identifier}: {recommendation.title}

| Field | Value |
| --- | --- |
| Evolution type | {recommendation.evolution_type} |
| Affected artifacts | {", ".join(f"`{item}`" for item in recommendation.affected_artifacts)} |
| Affected knowledge | {self._ids([item.identifier for item in recommendation.affected_knowledge])} |
| Estimated effort | {recommendation.estimated_effort} |
| Dependencies | {", ".join(recommendation.dependencies)} |
| Risk assessment | {recommendation.risk_assessment} |

Engineering rationale: {recommendation.rationale}

Supporting evidence:

{self._supporting_evidence(recommendation.affected_knowledge)}

Implementation impact: {recommendation.implementation_impact}
"""
            )
        return "\n".join(sections)

    def _impact_analysis(self, recommendations: list[EvolutionRecommendation]) -> str:
        if not recommendations:
            return "No program impact detected."
        artifacts = sorted(
            {
                artifact
                for recommendation in recommendations
                for artifact in recommendation.affected_artifacts
            }
        )
        knowledge = sorted(
            {
                item.identifier
                for recommendation in recommendations
                for item in recommendation.affected_knowledge
            }
        )
        risks = sorted({recommendation.risk_assessment for recommendation in recommendations})
        efforts = sorted({recommendation.estimated_effort for recommendation in recommendations})
        return "\n".join(
            [
                f"- Affected artifacts: {self._ids(artifacts)}",
                f"- Affected Certified Knowledge: {self._ids(knowledge)}",
                f"- Estimated effort levels: {', '.join(efforts)}",
                f"- Risk profile: {'; '.join(risks)}",
                "- Dependencies: engineering review, program owner approval, and specialized owner review where listed.",
            ]
        )

    def _manifest_extension(
        self,
        drift_level: str,
        recommendations: list[EvolutionRecommendation],
        timestamp: str,
    ) -> dict[str, object]:
        return {
            "evolution_tracking": {
                "current_knowledge_version": "repository-snapshot",
                "last_synchronization": None,
                "last_evolution_review": timestamp,
                "accepted_recommendations": [],
                "rejected_recommendations": [],
                "pending_recommendations": [
                    recommendation.identifier for recommendation in recommendations
                ],
                "knowledge_drift": drift_level,
            }
        }

    def _traceability(self, recommendations: list[EvolutionRecommendation]) -> str:
        blocks = []
        seen: set[str] = set()
        for recommendation in recommendations:
            for item in recommendation.affected_knowledge:
                if item.identifier in seen:
                    continue
                seen.add(item.identifier)
                blocks.append(
                    "```text\n"
                    f"{recommendation.identifier}\n"
                    "->\n"
                    f"{item.identifier}\n"
                    "->\n"
                    f"{item.generalized}\n"
                    "->\n"
                    f"{', '.join(item.concepts)}\n"
                    "->\n"
                    f"{', '.join(item.candidates)}\n"
                    "->\n"
                    f"{', '.join(item.observations)}\n"
                    "->\n"
                    f"{item.knowledge_source}\n"
                    "->\n"
                    "supporting evidence recorded in Certified Knowledge\n"
                    "```"
                )
        return "\n\n".join(blocks) if blocks else "No Certified Knowledge traceability available."

    def _supporting_evidence(self, knowledge: list[CertifiedKnowledge]) -> str:
        rows = [
            "| Certified Knowledge | Observation | Repository | Evidence | Commit |",
            "| --- | --- | --- | --- | --- |",
        ]
        count = 0
        for item in knowledge:
            for evidence in item.evidence_rows:
                rows.append(
                    f"| `{item.identifier}` | `{evidence.get('observation', '')}` | "
                    f"`{evidence.get('repository', '')}` | `{evidence.get('evidence', '')}` | "
                    f"`{evidence.get('commit', '')}` |"
                )
                count += 1
                if count >= 6:
                    rows.append("| More evidence available | See Certified Knowledge |  |  |  |")
                    return "\n".join(rows)
        if count == 0:
            rows.append("| No direct evidence listed | Review governance record |  |  |  |")
        return "\n".join(rows)

    def _filter(self, knowledge: list[CertifiedKnowledge], term: str) -> list[CertifiedKnowledge]:
        needle = term.lower()
        return [
            item
            for item in knowledge
            if needle in item.title.lower()
            or needle in item.category.lower()
            or needle in item.domains.lower()
            or needle in item.summary.lower()
        ]

    def _ids(self, ids: list[str]) -> str:
        if not ids:
            return "`none`"
        return ", ".join(f"`{item}`" for item in ids)

    def _output_path(self, output: Path, result: EvolveResult, multiple: bool) -> Path:
        if output.suffix:
            return output
        if multiple:
            return output / f"{result.program_identifier.lower()}-evolution-report.md"
        return output / "evolution-report.md"
