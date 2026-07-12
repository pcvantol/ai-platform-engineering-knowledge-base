from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from typing import Any

from .status import ARCHITECTURE_ONLY_COMMANDS, IMPLEMENTED_COMMANDS


STAGES = (
    ("knowledge_sources", "sources", "KS-"),
    ("engineering_observations", "observations", "EO-"),
    ("knowledge_candidates", "candidates", "KC-"),
    ("knowledge_concepts", "concepts", "KCN-"),
    ("generalized_knowledge", "generalized", "GK-"),
    ("certified_knowledge", "certified", "CK-"),
)
UPSTREAM_PREFIX = {"KC-": "EO-", "KCN-": "KC-", "GK-": "KCN-", "CK-": "GK-"}
ID_RE = re.compile(r"\b(?:KS|EO|KC|KCN|GK|CK)-[A-Z0-9-]+\b")


@dataclass(frozen=True)
class StatsConfig:
    format: str = "markdown"
    output: Path | None = None


@dataclass(frozen=True)
class StatsResult:
    data: dict[str, Any]
    rendered: str
    output_path: Path | None


@dataclass(frozen=True)
class Record:
    identifier: str
    stage: str
    path: Path
    metadata: dict[str, str]
    references: set[str]
    text: str


class KnowledgeBaseStatistics:
    """Derives read-only repository statistics from canonical Markdown records."""

    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root

    def collect(self) -> dict[str, Any]:
        records = self._load_records()
        publications = self._load_publications()
        relationships = self._relationships(records)
        traceability = self._traceability(records, publications)
        stage_records = {stage: [record for record in records.values() if record.stage == stage] for stage, _, _ in STAGES}
        summary = {stage: len(stage_records[stage]) for stage, _, _ in STAGES}
        summary.update({"publications": len(publications), "relationships": relationships["total"]})
        return {
            "report_type": "knowledge-base-statistics",
            "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "repository_root": str(self.repository_root),
            "canonical": False,
            "summary": summary,
            "lifecycle_funnel": self._funnel(stage_records, len(publications)),
            "domains": self._domains(stage_records),
            "classifications": self._classifications(stage_records, publications),
            "traceability": traceability,
            "relationships": relationships,
            "certification": self._certification(stage_records),
            "sources": self._sources(stage_records),
            "publications": self._publication_stats(publications),
            "runtime_inventory": self._runtime_inventory(),
            "warnings": self._warnings(stage_records, publications),
        }

    def run(self, config: StatsConfig) -> StatsResult:
        if config.format not in {"markdown", "json"}:
            raise RuntimeError("Unsupported stats format. Supported formats: markdown, json")
        data = self.collect()
        rendered = self.render_markdown(data) if config.format == "markdown" else self.render_json(data)
        output_path = None
        if config.output:
            output_path = config.output.resolve()
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(rendered, encoding="utf-8")
        return StatsResult(data=data, rendered=rendered, output_path=output_path)

    def _load_records(self) -> dict[str, Record]:
        records: dict[str, Record] = {}
        for stage, directory, prefix in STAGES:
            root = self.repository_root / directory
            if not root.exists():
                continue
            paths = (
                [path for path in sorted(root.glob("**/README.md")) if path.parent != root]
                if stage == "knowledge_sources"
                else sorted(root.glob(f"**/{prefix}*.md"))
            )
            for path in paths:
                text = self._read(path)
                metadata = self._all_table_metadata(text) if stage == "knowledge_sources" else self._metadata(text)
                identifier = (metadata.get("Identifier") or metadata.get("Knowledge Source identifier") or self._id_from_text(text, prefix)).strip("`")
                if not identifier or not identifier.startswith(prefix):
                    raise RuntimeError(f"Invalid required record identifier in {path}: expected {prefix} identifier.")
                if stage != "knowledge_sources" and not metadata.get("Lifecycle state"):
                    raise RuntimeError(f"Invalid required record in {path}: missing Lifecycle state metadata.")
                if identifier in records:
                    raise RuntimeError(f"Duplicate canonical identifier {identifier} in {path} and {records[identifier].path}.")
                records[identifier] = Record(identifier, stage, path, metadata, set(ID_RE.findall(text)), text)
        self._validate_required_lineage(records)
        return records

    def _load_publications(self) -> list[Record]:
        root = self.repository_root / "publications"
        if not root.exists():
            return []
        publications = []
        for path in sorted(root.glob("**/*.md")):
            if path.name == "README.md":
                continue
            text = self._read(path)
            metadata = self._metadata(text)
            identifier = metadata.get("Publication identifier", path.stem).strip("`")
            publications.append(Record(identifier, "publications", path, metadata, set(ID_RE.findall(text)), text))
        return publications

    def _validate_required_lineage(self, records: dict[str, Record]) -> None:
        for record in records.values():
            for prefix, upstream in UPSTREAM_PREFIX.items():
                if not record.identifier.startswith(prefix):
                    continue
                upstream_refs = sorted(ref for ref in record.references if ref.startswith(upstream))
                if not upstream_refs:
                    raise RuntimeError(f"Invalid required lineage in {record.path}: {record.identifier} has no {upstream} reference.")
                unresolved = [ref for ref in upstream_refs if ref not in records]
                if unresolved:
                    raise RuntimeError(f"Invalid required lineage in {record.path}: unresolved references {', '.join(unresolved)}.")

    def _funnel(self, stage_records: dict[str, list[Record]], publications: int) -> list[dict[str, Any]]:
        items = [("Knowledge Sources", "knowledge_sources", len(stage_records["knowledge_sources"])), ("Engineering Observations", "engineering_observations", len(stage_records["engineering_observations"])), ("Knowledge Candidates", "knowledge_candidates", len(stage_records["knowledge_candidates"])), ("Knowledge Concepts", "knowledge_concepts", len(stage_records["knowledge_concepts"])), ("Generalized Knowledge", "generalized_knowledge", len(stage_records["generalized_knowledge"])), ("Certified Knowledge", "certified_knowledge", len(stage_records["certified_knowledge"])), ("Publications", "publications", publications)]
        observations = len(stage_records["engineering_observations"])
        result = []
        previous = None
        for label, key, count in items:
            records = stage_records.get(key, [])
            statuses = self._lifecycle_counts(records) if records else {"active": None, "deprecated": None, "superseded": None, "retired": None}
            result.append({"stage": key, "label": label, "total": count, **statuses, "percentage_of_previous_stage": self._percentage(count, previous), "percentage_of_observations": self._percentage(count, observations)})
            previous = count
        return result

    def _domains(self, stage_records: dict[str, list[Record]]) -> list[dict[str, Any]]:
        counts: dict[str, Counter[str]] = defaultdict(Counter)
        for stage, records in stage_records.items():
            if stage == "knowledge_sources":
                continue
            for record in records:
                for domain in self._values(record.metadata.get("Engineering domains") or record.metadata.get("Engineering domain")):
                    counts[domain][stage] += 1
        return [{"domain": domain, **{stage: counts[domain].get(stage, 0) for stage, _, _ in STAGES if stage != "knowledge_sources"}} for domain in sorted(counts)]

    def _classifications(self, stage_records: dict[str, list[Record]], publications: list[Record]) -> dict[str, Any]:
        records = [record for values in stage_records.values() for record in values if record.stage != "knowledge_sources"]
        fields = {"knowledge_category": ("Knowledge category",), "abstraction_level": ("Abstraction level",), "lifecycle_state": ("Lifecycle state",), "certification_state": ("Certification status",), "confidence": ("Confidence",), "evidence_type": ("Evidence type", "Observation type"), "knowledge_source": ("Knowledge Source", "Knowledge sources"), "repository": ("Source repository",)}
        result: dict[str, Any] = {}
        for name, keys in fields.items():
            counter = Counter()
            for record in records:
                value = next((record.metadata[key] for key in keys if record.metadata.get(key)), None)
                counter.update(self._values(value))
            result[name] = dict(sorted(counter.items())) if counter else None
        publication_types = Counter(record.metadata.get("Publication type", "Unknown") for record in publications)
        result["publication_type"] = dict(sorted(publication_types.items())) if publications else None
        return result

    def _traceability(self, records: dict[str, Record], publications: list[Record]) -> dict[str, Any]:
        lifecycle = [record for record in records.values() if record.stage != "knowledge_sources"]
        complete = [record for record in lifecycle if self._has_full_lineage(record, records, set())]
        missing_sources = [record.identifier for record in lifecycle if not self._source_refs(record, records, set())]
        missing_evidence = [record.identifier for record in lifecycle if record.identifier.startswith("EO-") and not self._has_evidence(record)]
        orphaned = [record.identifier for record in lifecycle if record.identifier.startswith(tuple(UPSTREAM_PREFIX)) and not any(ref.startswith(UPSTREAM_PREFIX[next(prefix for prefix in UPSTREAM_PREFIX if record.identifier.startswith(prefix))]) for ref in record.references)]
        missing_targets = sorted({target for record in records.values() for target in record.references if target.startswith(("KS-", "EO-", "KC-", "KCN-", "GK-", "CK-")) and target not in records})
        certified = [record for record in lifecycle if record.identifier.startswith("CK-")]
        publication_without_sources = [record.identifier for record in publications if not any(ref.startswith("CK-") for ref in record.references)]
        return {"knowledge_objects_with_complete_lineage": len(complete), "knowledge_objects_with_incomplete_lineage": len(lifecycle) - len(complete), "orphaned_records": sorted(orphaned), "records_with_missing_source_references": sorted(missing_sources), "records_with_missing_evidence_references": sorted(missing_evidence), "relationships_pointing_to_missing_targets": missing_targets, "certified_knowledge_without_full_upstream_lineage": sorted(record.identifier for record in certified if record not in complete), "publications_without_certified_knowledge_sources": sorted(publication_without_sources)}

    def _relationships(self, records: dict[str, Record]) -> dict[str, Any]:
        edges = []
        for record in records.values():
            for row in self._table(record.text, "Relationships"):
                target = row.get("Target", "").strip("`")
                relation = row.get("Relationship", "")
                if target and relation:
                    edges.append((record.identifier, target, relation))
        degrees = Counter()
        by_type = Counter()
        cross_domain = same_domain = 0
        for source, target, relation in edges:
            degrees[source] += 1
            degrees[target] += 1
            by_type[relation] += 1
            if target in records:
                source_domains = set(self._values(records[source].metadata.get("Engineering domains") or records[source].metadata.get("Engineering domain")))
                target_domains = set(self._values(records[target].metadata.get("Engineering domains") or records[target].metadata.get("Engineering domain")))
                if source_domains and target_domains:
                    if source_domains & target_domains:
                        same_domain += 1
                    else:
                        cross_domain += 1
        return {"total": len(edges), "by_type": dict(sorted(by_type.items())), "inbound_relationship_count": len(edges), "outbound_relationship_count": len(edges), "isolated_knowledge_objects": sorted(identifier for identifier, record in records.items() if record.stage != "knowledge_sources" and not degrees[identifier]), "most_connected_knowledge_objects": [{"identifier": identifier, "relationship_count": count} for identifier, count in sorted(degrees.items(), key=lambda item: (-item[1], item[0]))[:10]], "cross_domain_relationships": cross_domain, "same_domain_relationships": same_domain}

    def _certification(self, stage_records: dict[str, list[Record]]) -> dict[str, Any]:
        cycles = sorted((self.repository_root / "certification" / "cycles").glob("*.md")) if (self.repository_root / "certification" / "cycles").exists() else []
        decisions = Counter()
        for path in cycles:
            for row in self._table(self._read(path), "Certification Decisions"):
                if row.get("Decision"):
                    decisions[row["Decision"]] += 1
        generalized = len(stage_records["generalized_knowledge"])
        certified = len(stage_records["certified_knowledge"])
        by_domain = Counter(domain for record in stage_records["certified_knowledge"] for domain in self._values(record.metadata.get("Engineering domains") or record.metadata.get("Engineering domain")))
        by_category = Counter(record.metadata.get("Knowledge category", "Unknown") for record in stage_records["certified_knowledge"])
        return {"total_certification_records": len(cycles), "certified_knowledge": certified, "decisions": dict(sorted(decisions.items())) if decisions else None, "certification_coverage_over_generalized_knowledge": self._percentage(certified, generalized), "certified_knowledge_by_domain": dict(sorted(by_domain.items())), "certified_knowledge_by_category": dict(sorted(by_category.items()))}

    def _sources(self, stage_records: dict[str, list[Record]]) -> list[dict[str, Any]]:
        sources = stage_records["knowledge_sources"]
        lifecycle = [record for stage, records in stage_records.items() if stage != "knowledge_sources" for record in records]
        result = []
        for source in sorted(sources, key=lambda item: item.identifier):
            related = [record for record in lifecycle if source.identifier in record.references or source.identifier in self._values(record.metadata.get("Knowledge Source") or record.metadata.get("Knowledge sources"))]
            repositories = sorted({repo for record in related for repo in self._values(record.metadata.get("Source repository"))})
            profile_repositories = [row.get("Repository", "").strip("`") for row in self._table(source.text, "Repository Inventory") if row.get("Repository")]
            if profile_repositories:
                repositories = sorted(set(repositories) | set(profile_repositories))
            dates = sorted(value for record in related for value in (record.metadata.get("Observation date"), record.metadata.get("Extraction date"), record.metadata.get("Revision date")) if value)
            counts = Counter(record.stage for record in related)
            result.append({"identifier": source.identifier, "repository_count": len(repositories), "repositories": repositories, **{stage: counts.get(stage, 0) for stage, _, _ in STAGES if stage != "knowledge_sources"}, "evidence_count": sum(1 for record in related if self._has_evidence(record)), "last_known_ingestion_or_update": dates[-1] if dates else None, "lifecycle_status": source.metadata.get("Lifecycle status") or source.metadata.get("Onboarding status") or source.metadata.get("Repository lifecycle") or None})
        return result

    def _publication_stats(self, publications: list[Record]) -> dict[str, Any]:
        by_type = Counter(record.metadata.get("Publication type", "Unknown") for record in publications)
        by_status = Counter(record.metadata.get("Publication status", "Unknown") for record in publications)
        complete = [record for record in publications if any(ref.startswith("CK-") for ref in record.references)]
        stale = [record.identifier for record in publications if record.metadata.get("Publication status", "").lower() in {"stale", "superseded", "retired"}]
        return {"count": len(publications), "by_type": dict(sorted(by_type.items())) if publications else None, "by_status": dict(sorted(by_status.items())) if publications else None, "publication_source_coverage": self._percentage(len(complete), len(publications)), "publications_with_complete_traceability": len(complete), "stale_or_superseded_publications": sorted(stale)}

    def _runtime_inventory(self) -> dict[str, Any]:
        generators_root = self.repository_root / "generators"
        templates_root = self.repository_root / "templates"
        return {"generators": len(list(generators_root.glob("*/README.md"))) if generators_root.exists() else None, "templates": len([path for path in templates_root.glob("**/*") if path.is_file()]) if templates_root.exists() else None, "implemented_cli_commands": len(IMPLEMENTED_COMMANDS), "architecture_only_cli_commands": len(ARCHITECTURE_ONLY_COMMANDS), "registered_capabilities": {"supported": False, "count": None}, "registered_agents": {"supported": False, "count": None}, "engineering_programs": {"supported": False, "count": None}, "evolution_reports": {"supported": False, "count": None}, "validation_reports": {"supported": False, "count": None}}

    def _warnings(self, stage_records: dict[str, list[Record]], publications: list[Record]) -> list[str]:
        warnings = []
        if not publications:
            warnings.append("No publication records are present.")
        if not stage_records["knowledge_sources"]:
            warnings.append("No registered Knowledge Source records are present.")
        return warnings

    def _has_full_lineage(self, record: Record, records: dict[str, Record], visited: set[str]) -> bool:
        if record.identifier in visited:
            return False
        if record.identifier.startswith("EO-"):
            return bool(self._source_refs(record, records, set()) and self._has_evidence(record))
        upstream = next((prefix for prefix in UPSTREAM_PREFIX if record.identifier.startswith(prefix)), None)
        if not upstream:
            return True
        dependencies = [records[ref] for ref in record.references if ref.startswith(UPSTREAM_PREFIX[upstream]) and ref in records]
        return bool(dependencies) and all(self._has_full_lineage(dependency, records, visited | {record.identifier}) for dependency in dependencies)

    def _source_refs(self, record: Record, records: dict[str, Record], visited: set[str]) -> set[str]:
        if record.identifier in visited:
            return set()
        direct = {ref for ref in record.references if ref.startswith("KS-") and ref in records}
        for ref in record.references:
            if ref in records and not ref.startswith("KS-"):
                direct |= self._source_refs(records[ref], records, visited | {record.identifier})
        return direct

    @staticmethod
    def _has_evidence(record: Record) -> bool:
        return bool(record.metadata.get("Evidence type") or record.metadata.get("Observation type") or "Evidence" in record.text)

    @staticmethod
    def _lifecycle_counts(records: list[Record]) -> dict[str, int | None]:
        states = [record.metadata.get("Lifecycle state", "") for record in records]
        if not states:
            return {"active": None, "deprecated": None, "superseded": None, "retired": None}
        return {"active": sum(not any(state.lower().startswith(value) for value in ("deprecated", "superseded", "retired")) for state in states), "deprecated": sum(state.lower().startswith("deprecated") for state in states), "superseded": sum(state.lower().startswith("superseded") for state in states), "retired": sum(state.lower().startswith("retired") for state in states)}

    @staticmethod
    def _percentage(value: int, total: int | None) -> float | None:
        return None if total in (None, 0) else round(value * 100 / total, 2)

    @staticmethod
    def _values(value: str | None) -> list[str]:
        if not value:
            return []
        return [item.strip().strip("`") for item in value.split(",") if item.strip()]

    @staticmethod
    def _metadata(text: str) -> dict[str, str]:
        result = {}
        in_metadata = False
        for line in text.splitlines():
            if line == "## Metadata":
                in_metadata = True
                continue
            if in_metadata and line.startswith("## "):
                break
            if in_metadata and line.startswith("| "):
                parts = [part.strip() for part in line.strip().strip("|").split("|")]
                if len(parts) == 2 and parts[0] != "---":
                    result[parts[0]] = parts[1]
        return result

    @staticmethod
    def _all_table_metadata(text: str) -> dict[str, str]:
        result = {}
        for line in text.splitlines():
            if not line.startswith("| "):
                continue
            parts = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(parts) == 2 and parts[0] != "---":
                result[parts[0]] = parts[1]
        return result

    @staticmethod
    def _table(text: str, heading: str) -> list[dict[str, str]]:
        lines = text.splitlines()
        try:
            start = lines.index(f"## {heading}") + 1
        except ValueError:
            return []
        table = []
        for line in lines[start:]:
            if line.startswith("## "):
                break
            if line.startswith("| "):
                table.append([part.strip() for part in line.strip().strip("|").split("|")])
        if len(table) < 3:
            return []
        headers = table[0]
        return [dict(zip(headers, row)) for row in table[2:] if len(row) == len(headers)]

    @staticmethod
    def _id_from_text(text: str, prefix: str) -> str:
        match = re.search(rf"\b{re.escape(prefix)}[A-Z0-9-]+\b", text)
        return match.group(0) if match else ""

    @staticmethod
    def _read(path: Path) -> str:
        try:
            return path.read_text(encoding="utf-8")
        except OSError as error:
            raise RuntimeError(f"Unable to read required canonical record {path}: {error}") from error

    @staticmethod
    def render_json(data: dict[str, Any]) -> str:
        return json.dumps(data, indent=2, sort_keys=True) + "\n"

    @staticmethod
    def render_markdown(data: dict[str, Any]) -> str:
        summary = "\n".join(f"| {key.replace('_', ' ').title()} | {value} |" for key, value in data["summary"].items())
        funnel = "\n".join(f"| {item['label']} | {item['total']} | {item['active'] if item['active'] is not None else 'Unknown'} | {item['percentage_of_previous_stage'] if item['percentage_of_previous_stage'] is not None else 'Unknown'}% | {item['percentage_of_observations'] if item['percentage_of_observations'] is not None else 'Unknown'}% |" for item in data["lifecycle_funnel"])
        domains = "\n".join(f"| {item['domain']} | {item['engineering_observations']} | {item['knowledge_candidates']} | {item['knowledge_concepts']} | {item['generalized_knowledge']} | {item['certified_knowledge']} |" for item in data["domains"]) or "| No domains discovered | 0 | 0 | 0 | 0 | 0 |"
        sources = "\n".join(f"| `{item['identifier']}` | {item['repository_count']} | {item['engineering_observations']} | {item['knowledge_candidates']} | {item['knowledge_concepts']} | {item['generalized_knowledge']} | {item['certified_knowledge']} | {item['evidence_count']} | {item['last_known_ingestion_or_update'] or 'Unknown'} | {item['lifecycle_status'] or 'Unknown'} |" for item in data["sources"]) or "| No registered sources | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Unknown | Unknown |"
        classifications = "\n".join(f"| {key.replace('_', ' ').title()} | {json.dumps(value, sort_keys=True) if value is not None else 'Unsupported'} |" for key, value in data["classifications"].items())
        runtime = "\n".join(f"| {key.replace('_', ' ').title()} | {json.dumps(value, sort_keys=True) if isinstance(value, dict) else value} |" for key, value in data["runtime_inventory"].items())
        traceability = "\n".join(f"| {key.replace('_', ' ').title()} | {json.dumps(value, sort_keys=True) if isinstance(value, list) else value} |" for key, value in data["traceability"].items())
        relationships = "\n".join(f"| {key.replace('_', ' ').title()} | {json.dumps(value, sort_keys=True) if isinstance(value, (dict, list)) else value} |" for key, value in data["relationships"].items())
        certification = "\n".join(f"| {key.replace('_', ' ').title()} | {json.dumps(value, sort_keys=True) if isinstance(value, dict) else value} |" for key, value in data["certification"].items())
        publications = "\n".join(f"| {key.replace('_', ' ').title()} | {json.dumps(value, sort_keys=True) if isinstance(value, (dict, list)) else value} |" for key, value in data["publications"].items())
        warnings = "\n".join(f"- {warning}" for warning in data["warnings"]) or "- None."
        return f"""# AI Platform Engineering Knowledge Base Statistics

## Report Metadata

| Field | Value |
| --- | --- |
| Generated at | `{data['generated_at']}` |
| Repository root | `{data['repository_root']}` |
| Canonical | No; this is a derived, read-only report. |

## Executive Summary

| Metric | Count |
| --- | ---: |
{summary}

## Knowledge Lifecycle Funnel

Promotion ratios are descriptive counts, not quality thresholds.

| Stage | Total | Active | % Previous Stage | % Engineering Observations |
| --- | ---: | ---: | ---: | ---: |
{funnel}

## Engineering Domains

| Domain | Observations | Candidates | Concepts | Generalized | Certified |
| --- | ---: | ---: | ---: | ---: |
{domains}

## Classification Distribution

| Dimension | Distribution |
| --- | --- |
{classifications}

## Traceability

| Metric | Value |
| --- | --- |
{traceability}

## Relationships

| Metric | Value |
| --- | --- |
{relationships}

## Certification

| Metric | Value |
| --- | --- |
{certification}

## Knowledge Sources

| Source | Repositories | Observations | Candidates | Concepts | Generalized | Certified | Evidence | Last update | Lifecycle status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
{sources}

## Publications

| Metric | Value |
| --- | --- |
{publications}

## CLI and Runtime Inventory

| Inventory | Value |
| --- | --- |
{runtime}

## Warnings

{warnings}

This command does not modify the Knowledge Base or registered Knowledge Sources. An output file is written only when explicitly requested.
"""
