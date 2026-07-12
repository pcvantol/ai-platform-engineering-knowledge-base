from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import re


KNOWLEDGE_DIRS = {
    "sources": "KS",
    "observations": "EO",
    "candidates": "KC",
    "concepts": "KCN",
    "generalized": "GK",
    "certified": "CK",
}


@dataclass(frozen=True)
class ValidateConfig:
    knowledge: bool = False
    publications: bool = False
    sources: bool = False
    output: Path | None = None


@dataclass(frozen=True)
class ValidationFinding:
    identifier: str
    severity: str
    category: str
    title: str
    object_id: str
    object_path: Path | None
    evidence: str
    recommendation: str


@dataclass(frozen=True)
class ValidationResult:
    report: str
    report_path: Path | None
    finding_count: int
    qualification: dict[str, str]


class KnowledgeBaseValidator:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root

    def validate(self, config: ValidateConfig) -> ValidationResult:
        scopes = self._scopes(config)
        objects = self._knowledge_objects()
        findings: list[ValidationFinding] = []
        if "repository" in scopes:
            findings.extend(self._validate_repository_structure())
        if "sources" in scopes:
            findings.extend(self._validate_sources(objects))
        if "knowledge" in scopes:
            findings.extend(self._validate_knowledge(objects))
        if "publications" in scopes:
            findings.extend(self._validate_publications(objects))
        qualification = self._qualification(findings, scopes)
        report = self._render_report(scopes, objects, findings, qualification)
        report_path = None
        if config.output:
            report_path = config.output.resolve()
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(report, encoding="utf-8")
        return ValidationResult(
            report=report,
            report_path=report_path,
            finding_count=len(findings),
            qualification=qualification,
        )

    def _scopes(self, config: ValidateConfig) -> set[str]:
        selected = set()
        if config.knowledge:
            selected.add("knowledge")
        if config.publications:
            selected.add("publications")
        if config.sources:
            selected.add("sources")
        if not selected:
            return {"repository", "sources", "knowledge", "publications"}
        return selected

    def _knowledge_objects(self) -> dict[str, Path]:
        objects: dict[str, Path] = {}
        for folder in KNOWLEDGE_DIRS:
            root = self.repository_root / folder
            if not root.exists():
                continue
            for path in root.glob("**/*.md"):
                if path.name == "README.md" and not (
                    folder == "sources" and path.parent != root
                ):
                    continue
                text = path.read_text(encoding="utf-8")
                identifier = self._metadata(text).get("Identifier", "").strip("`")
                if not identifier and folder == "sources":
                    metadata = self._metadata(text)
                    identifier = metadata.get("Knowledge Source identifier", "").strip("`")
                if not identifier and folder == "sources":
                    match = re.search(r"\b(KS-[A-Z0-9-]+)\b", text)
                    identifier = match.group(1) if match else ""
                if not identifier:
                    identifier = path.stem
                objects[identifier] = path
        return objects

    def _validate_repository_structure(self) -> list[ValidationFinding]:
        required = [
            "README.md",
            "sources/README.md",
            "observations/README.md",
            "candidates/README.md",
            "concepts/README.md",
            "generalized/README.md",
            "certified/README.md",
            "publications/README.md",
            "quality-health/README.md",
        ]
        findings = []
        for relative in required:
            path = self.repository_root / relative
            if not path.exists():
                findings.append(
                    self._finding(
                        "repository",
                        "ERROR",
                        "repository consistency",
                        "Required repository area is missing.",
                        relative,
                        path,
                        f"Expected path `{relative}` does not exist.",
                        "Restore the required repository area through governed repository maintenance.",
                    )
                )
        return findings

    def _validate_sources(self, objects: dict[str, Path]) -> list[ValidationFinding]:
        findings = []
        sources_root = self.repository_root / "sources"
        source_ids = self._ids_with_prefix(objects, "KS-")
        observations_text = self._combined_text(self.repository_root / "observations")
        for source_id in source_ids:
            source_path = objects[source_id]
            if source_id not in observations_text:
                findings.append(
                    self._finding(
                        source_id,
                        "WARN",
                        "source coverage",
                        "Knowledge Source has no downstream observations.",
                        source_id,
                        source_path,
                        f"`{source_id}` is registered but was not found in observation records.",
                        "Review source coverage and extract observations when evidence exists.",
                    )
                )
        for source_dir in sources_root.glob("*"):
            if not source_dir.is_dir():
                continue
            if not (source_dir / "README.md").exists():
                findings.append(
                    self._finding(
                        source_dir.name,
                        "ERROR",
                        "source structure",
                        "Knowledge Source directory is missing README.",
                        source_dir.name,
                        source_dir,
                        f"`{source_dir}` has no README.md.",
                        "Restore the source profile README.",
                    )
                )
        return findings

    def _validate_knowledge(self, objects: dict[str, Path]) -> list[ValidationFinding]:
        findings: list[ValidationFinding] = []
        findings.extend(self._validate_required_metadata(objects))
        findings.extend(self._validate_relationship_targets(objects))
        findings.extend(self._validate_traceability(objects))
        findings.extend(self._validate_certification(objects))
        findings.extend(self._validate_duplicates(objects))
        return findings

    def _validate_required_metadata(self, objects: dict[str, Path]) -> list[ValidationFinding]:
        findings = []
        for object_id, path in objects.items():
            text = path.read_text(encoding="utf-8")
            metadata = self._metadata(text)
            if object_id.startswith(("EO-", "KC-", "KCN-", "GK-", "CK-")):
                for field in ["Identifier", "Lifecycle state"]:
                    if field not in metadata:
                        findings.append(
                            self._finding(
                                object_id,
                                "ERROR",
                                "metadata completeness",
                                f"Missing required metadata field `{field}`.",
                                object_id,
                                path,
                                f"`{object_id}` does not define `{field}` in its metadata table.",
                                "Add the missing metadata through governed knowledge maintenance.",
                            )
                        )
        return findings

    def _validate_relationship_targets(self, objects: dict[str, Path]) -> list[ValidationFinding]:
        findings = []
        known_ids = set(objects)
        for object_id, path in objects.items():
            text = path.read_text(encoding="utf-8")
            for target in self._referenced_ids(text):
                if target == object_id or target.startswith("KS-PREP-"):
                    continue
                if target not in known_ids and self._is_knowledge_id(target):
                    findings.append(
                        self._finding(
                            object_id,
                            "ERROR",
                            "relationship integrity",
                            "Referenced Knowledge Object does not resolve.",
                            target,
                            path,
                            f"`{object_id}` references `{target}`, but no matching object file was found.",
                            "Review the relationship target or restore the missing Knowledge Object.",
                        )
                    )
        return findings

    def _validate_traceability(self, objects: dict[str, Path]) -> list[ValidationFinding]:
        findings = []
        requirements = {
            "KC-": "EO-",
            "KCN-": "KC-",
            "GK-": "KCN-",
            "CK-": "GK-",
        }
        for object_id, path in objects.items():
            text = path.read_text(encoding="utf-8")
            refs = self._referenced_ids(text)
            for prefix, required_prefix in requirements.items():
                if object_id.startswith(prefix) and not any(ref.startswith(required_prefix) for ref in refs):
                    findings.append(
                        self._finding(
                            object_id,
                            "ERROR",
                            "traceability completeness",
                            f"Missing upstream `{required_prefix}` traceability.",
                            object_id,
                            path,
                            f"`{object_id}` does not reference any `{required_prefix}` object.",
                            "Restore lifecycle traceability before relying on this object.",
                        )
                    )
            if object_id.startswith("EO-") and "Commit" not in text:
                findings.append(
                    self._finding(
                        object_id,
                        "WARN",
                        "evidence completeness",
                        "Observation may be missing commit evidence.",
                        object_id,
                        path,
                        f"`{object_id}` does not contain a visible `Commit` evidence field.",
                        "Review observation evidence metadata.",
                    )
                )
        return findings

    def _validate_certification(self, objects: dict[str, Path]) -> list[ValidationFinding]:
        findings = []
        for object_id, path in objects.items():
            if not object_id.startswith("CK-"):
                continue
            text = path.read_text(encoding="utf-8")
            metadata = self._metadata(text)
            if metadata.get("Certification status") != "Certified":
                findings.append(
                    self._finding(
                        object_id,
                        "ERROR",
                        "certification validity",
                        "Certified Knowledge has invalid certification status.",
                        object_id,
                        path,
                        f"`{object_id}` status is `{metadata.get('Certification status', 'missing')}`.",
                        "Review certification metadata and certification history.",
                    )
                )
            if "Source Evidence" not in text:
                findings.append(
                    self._finding(
                        object_id,
                        "ERROR",
                        "certification evidence",
                        "Certified Knowledge is missing Source Evidence section.",
                        object_id,
                        path,
                        f"`{object_id}` has no `Source Evidence` section.",
                        "Restore evidence traceability before using this knowledge as canonical.",
                    )
                )
        return findings

    def _validate_duplicates(self, objects: dict[str, Path]) -> list[ValidationFinding]:
        findings = []
        by_title: dict[tuple[str, str], list[tuple[str, Path]]] = {}
        for object_id, path in objects.items():
            if not object_id.startswith(("KCN-", "CK-")):
                continue
            title = self._title(path.read_text(encoding="utf-8")).lower()
            key = (object_id.split("-", 1)[0], title)
            by_title.setdefault(key, []).append((object_id, path))
        for (_, title), items in by_title.items():
            if len(items) <= 1:
                continue
            ids = ", ".join(f"`{item[0]}`" for item in items)
            findings.append(
                self._finding(
                    items[0][0],
                    "WARN",
                    "duplicate knowledge",
                    "Potential duplicate concept or Certified Knowledge title.",
                    items[0][0],
                    items[0][1],
                    f"Title `{title}` appears in {ids}.",
                    "Review whether these objects should be related, merged, split, or left distinct.",
                )
            )
        return findings

    def _validate_publications(self, objects: dict[str, Path]) -> list[ValidationFinding]:
        findings = []
        publications_root = self.repository_root / "publications"
        known_ck = {object_id for object_id in objects if object_id.startswith("CK-")}
        for path in publications_root.glob("**/*.md"):
            if path.name == "README.md":
                continue
            text = path.read_text(encoding="utf-8")
            refs = {ref for ref in self._referenced_ids(text) if ref.startswith("CK-")}
            if not refs:
                findings.append(
                    self._finding(
                        path.stem,
                        "WARN",
                        "publication consistency",
                        "Publication has no Certified Knowledge references.",
                        path.stem,
                        path,
                        f"`{path.relative_to(self.repository_root)}` does not reference Certified Knowledge.",
                        "Review publication traceability to Certified Knowledge.",
                    )
                )
            for ref in refs - known_ck:
                findings.append(
                    self._finding(
                        path.stem,
                        "ERROR",
                        "publication consistency",
                        "Publication references missing Certified Knowledge.",
                        ref,
                        path,
                        f"`{path.relative_to(self.repository_root)}` references `{ref}`, which does not resolve.",
                        "Refresh the publication from current Certified Knowledge.",
                    )
                )
        return findings

    def _qualification(self, findings: list[ValidationFinding], scopes: set[str]) -> dict[str, str]:
        categories_with_errors = {finding.category for finding in findings if finding.severity == "ERROR"}
        categories_with_warnings = {finding.category for finding in findings if finding.severity == "WARN"}

        def decision(categories: set[str]) -> str:
            if categories & categories_with_errors:
                return "FAIL"
            if categories & categories_with_warnings:
                return "REVIEW"
            return "PASS"

        qualification = {
            "KNOWLEDGE_VALID": decision({
                "metadata completeness",
                "traceability completeness",
                "duplicate knowledge",
            }),
            "TRACEABILITY_VALID": decision({
                "traceability completeness",
                "evidence completeness",
                "certification evidence",
            }),
            "RELATIONSHIPS_VALID": decision({"relationship integrity"}),
            "CERTIFICATION_VALID": decision({"certification validity", "certification evidence"}),
            "PUBLICATION_VALID": decision({"publication consistency"}),
            "REPOSITORY_VALID": decision({"repository consistency", "source structure", "source coverage"}),
        }
        return qualification

    def _render_report(
        self,
        scopes: set[str],
        objects: dict[str, Path],
        findings: list[ValidationFinding],
        qualification: dict[str, str],
    ) -> str:
        timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        return f"""# Knowledge Base Validation Report

## Validation Metadata

| Field | Value |
| --- | --- |
| Repository | `{self.repository_root}` |
| Timestamp | {timestamp} |
| Scopes | {", ".join(sorted(scopes))} |
| Finding count | {len(findings)} |

## Qualification Decisions

{self._qualification_table(qualification)}

## Knowledge Scorecard

{self._scorecard(objects, findings)}

## Findings

{self._findings(findings)}

## Repository Qualification

Validation results are evidence for governance review. They do not modify Certified Knowledge, publications, repositories or lifecycle records.
"""

    def _qualification_table(self, qualification: dict[str, str]) -> str:
        rows = ["| Decision | Result |", "| --- | --- |"]
        for key, value in qualification.items():
            rows.append(f"| `{key}` | {value} |")
        return "\n".join(rows)

    def _scorecard(self, objects: dict[str, Path], findings: list[ValidationFinding]) -> str:
        counts = {
            "Knowledge Objects": len(objects),
            "Certified Knowledge": len([item for item in objects if item.startswith("CK-")]),
            "Traceability": self._score_status(findings, {"traceability completeness", "evidence completeness"}),
            "Relationship Integrity": self._score_status(findings, {"relationship integrity"}),
            "Knowledge Quality": self._score_status(findings, {"metadata completeness", "duplicate knowledge"}),
            "Repository Health": self._score_status(findings, {"repository consistency", "source structure", "source coverage"}),
            "Publication Health": self._score_status(findings, {"publication consistency"}),
            "Knowledge Drift": "not evaluated by validation command",
            "Validation Coverage": "repository snapshot",
            "Findings": len(findings),
            "Errors": len([item for item in findings if item.severity == "ERROR"]),
            "Warnings": len([item for item in findings if item.severity == "WARN"]),
            "Traceability Findings": len([item for item in findings if "traceability" in item.category]),
            "Relationship Findings": len([item for item in findings if "relationship" in item.category]),
            "Publication Findings": len([item for item in findings if "publication" in item.category]),
            "Repository Health Findings": len([
                item for item in findings if item.category in {"repository consistency", "source coverage", "source structure"}
            ]),
        }
        rows = ["| Metric | Value |", "| --- | --- |"]
        for key, value in counts.items():
            rows.append(f"| {key} | {value} |")
        return "\n".join(rows)

    def _score_status(self, findings: list[ValidationFinding], categories: set[str]) -> str:
        scoped = [finding for finding in findings if finding.category in categories]
        if any(finding.severity == "ERROR" for finding in scoped):
            return "fail"
        if scoped:
            return "review"
        return "pass"

    def _findings(self, findings: list[ValidationFinding]) -> str:
        if not findings:
            return "No findings."
        sections = []
        for finding in findings:
            path = (
                finding.object_path.relative_to(self.repository_root).as_posix()
                if finding.object_path and finding.object_path.exists()
                else "not available"
            )
            sections.append(
                f"""### {finding.identifier}: {finding.title}

| Field | Value |
| --- | --- |
| Severity | {finding.severity} |
| Category | {finding.category} |
| Knowledge Object | `{finding.object_id}` |
| Object path | `{path}` |

Evidence: {finding.evidence}

Recommendation: {finding.recommendation}
"""
            )
        return "\n".join(sections)

    def _finding(
        self,
        seed: str,
        severity: str,
        category: str,
        title: str,
        object_id: str,
        object_path: Path | None,
        evidence: str,
        recommendation: str,
    ) -> ValidationFinding:
        digest = hashlib.sha1(
            "|".join([seed, severity, category, title, object_id]).encode("utf-8")
        ).hexdigest()
        number = int(digest[:8], 16) % 100000
        return ValidationFinding(
            identifier=f"VF-{number:05d}",
            severity=severity,
            category=category,
            title=title,
            object_id=object_id,
            object_path=object_path,
            evidence=evidence,
            recommendation=recommendation,
        )

    def _metadata(self, text: str) -> dict[str, str]:
        values: dict[str, str] = {}
        for line in text.splitlines():
            if not line.startswith("| "):
                continue
            parts = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(parts) != 2 or parts[0] == "---":
                continue
            values[parts[0]] = parts[1]
        return values

    def _referenced_ids(self, text: str) -> set[str]:
        return set(re.findall(r"\b(?:KS|EO|KC|KCN|GK|CK)-[A-Z0-9-]+\b", text))

    def _is_knowledge_id(self, value: str) -> bool:
        return bool(re.match(r"^(KS|EO|KC|KCN|GK|CK)-", value))

    def _ids_with_prefix(self, objects: dict[str, Path], prefix: str) -> list[str]:
        return sorted(object_id for object_id in objects if object_id.startswith(prefix))

    def _combined_text(self, root: Path) -> str:
        if not root.exists():
            return ""
        return "\n".join(path.read_text(encoding="utf-8") for path in root.glob("**/*.md"))

    def _title(self, text: str) -> str:
        for line in text.splitlines():
            if line.startswith("# "):
                return line.split(": ", 1)[-1].strip()
        return ""
