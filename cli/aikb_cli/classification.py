from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class ClassifyConfig:
    source: str | None = None
    force: bool = False


@dataclass(frozen=True)
class ClassifyResult:
    source_identifier: str
    candidate_set_path: Path
    created_count: int
    skipped_count: int


@dataclass(frozen=True)
class Observation:
    identifier: str
    title: str
    knowledge_source: str
    source_repository: str
    supporting_evidence: str
    engineering_domain: str
    source_commit: str
    confidence: str
    path: Path
    set_slug: str


class KnowledgeCandidateGenerator:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root
        self.observations_root = repository_root / "observations"
        self.candidates_root = repository_root / "candidates"

    def classify(self, config: ClassifyConfig) -> list[ClassifyResult]:
        observations = self._load_observations()
        selected = self._select_observations(observations, config.source)
        if not selected:
            raise RuntimeError("No Engineering Observations found for classification.")
        grouped: dict[str, list[Observation]] = {}
        for observation in selected:
            grouped.setdefault(observation.knowledge_source, []).append(observation)
        return [
            self._classify_source(source_identifier, source_observations, config.force)
            for source_identifier, source_observations in sorted(grouped.items())
        ]

    def _load_observations(self) -> list[Observation]:
        observations: list[Observation] = []
        for path in sorted(self.observations_root.glob("*/EO-*.md")):
            metadata = self._metadata(path.read_text(encoding="utf-8"))
            identifier = metadata.get("Identifier", path.stem).strip("`")
            knowledge_source = metadata.get("Knowledge Source", "").strip("`")
            if not knowledge_source:
                continue
            observations.append(
                Observation(
                    identifier=identifier,
                    title=metadata.get("Title", path.stem),
                    knowledge_source=knowledge_source,
                    source_repository=metadata.get("Source repository", "").strip("`"),
                    supporting_evidence=metadata.get("Supporting evidence", "").strip("`"),
                    engineering_domain=metadata.get("Engineering domain", ""),
                    source_commit=metadata.get("Source commit", "").strip("`"),
                    confidence=metadata.get("Confidence", "Medium"),
                    path=path,
                    set_slug=path.parent.name,
                )
            )
        return observations

    def _select_observations(
        self,
        observations: list[Observation],
        requested: str | None,
    ) -> list[Observation]:
        if not requested:
            return observations
        normalized = requested.lower()
        return [
            observation
            for observation in observations
            if normalized in observation.knowledge_source.lower()
            or normalized in observation.source_repository.lower()
            or normalized in observation.set_slug.lower()
        ]

    def _classify_source(
        self,
        source_identifier: str,
        observations: list[Observation],
        force: bool,
    ) -> ClassifyResult:
        source_slug = observations[0].set_slug
        candidate_dir = self.candidates_root / source_slug
        candidate_dir.mkdir(parents=True, exist_ok=True)
        existing_observations = self._existing_supporting_observations(candidate_dir)
        existing_ids = {path.stem for path in candidate_dir.glob("KC-*.md")}

        created: list[tuple[str, Observation]] = []
        skipped_count = 0
        for observation in observations:
            if observation.identifier in existing_observations and not force:
                skipped_count += 1
                continue
            identifier = self._next_identifier(source_identifier, existing_ids)
            existing_ids.add(identifier)
            self._write_candidate(candidate_dir / f"{identifier}.md", identifier, observation)
            created.append((identifier, observation))

        self._write_index(candidate_dir, source_identifier, source_slug)
        self._update_candidate_root(source_identifier, source_slug)
        return ClassifyResult(
            source_identifier=source_identifier,
            candidate_set_path=candidate_dir / "README.md",
            created_count=len(created),
            skipped_count=skipped_count,
        )

    def _write_candidate(self, path: Path, identifier: str, observation: Observation) -> None:
        category = self._category(observation)
        title = self._candidate_title(observation)
        content = f"""# {identifier}: {title}

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `{identifier}` |
| Lifecycle state | Knowledge Candidate |
| Knowledge Source | `{observation.knowledge_source}` |
| Review status | Awaiting Review |
| Certification status | Candidate |
| Knowledge category | {category} |
| Engineering domains | {observation.engineering_domain} |
| Abstraction level | Project Specific |
| Confidence | {observation.confidence} |
| Source repositories | `{observation.source_repository}` |

## Candidate Summary

The observation `{observation.identifier}` may contain reusable engineering value related to `{observation.title}`.

This is a Knowledge Candidate proposal only. It is repository specific, not normalized into a Knowledge Concept, not generalized, and not certified.

## Supporting Observations

- [{observation.identifier}](../../observations/{observation.set_slug}/{observation.identifier}.md)

## Supporting Evidence

| Repository | Evidence | Commit |
| --- | --- | --- |
| `{observation.source_repository}` | `{observation.supporting_evidence}` | `{observation.source_commit}` |

## Relationships

| Relationship | Target | Rationale |
| --- | --- | --- |
| originates from | `{observation.identifier}` | Candidate generated directly from the supporting Engineering Observation. |

## Traceability

```text
{identifier}
->
{observation.identifier}
->
{observation.knowledge_source}
->
{observation.source_repository}
->
{observation.supporting_evidence}
->
{observation.source_commit}
```

## Candidate Boundary

This candidate preserves repository terminology and source lineage. It does not normalize concepts, generalize knowledge, certify knowledge, or create publications.
"""
        path.write_text(content, encoding="utf-8")

    def _write_index(
        self,
        candidate_dir: Path,
        source_identifier: str,
        source_slug: str,
    ) -> None:
        rows = []
        for candidate_file in sorted(candidate_dir.glob("KC-*.md")):
            metadata = self._metadata(candidate_file.read_text(encoding="utf-8"))
            supporting = self._first_supporting_observation(candidate_file)
            rows.append(
                "| [{identifier}](./{file}) | {title} | `{supporting}` | {category} | {status} |".format(
                    identifier=metadata.get("Identifier", candidate_file.stem).strip("`"),
                    file=candidate_file.name,
                    title=self._heading_title(candidate_file),
                    supporting=supporting,
                    category=metadata.get("Knowledge category", ""),
                    status=metadata.get("Review status", ""),
                )
            )
        index = "\n".join(rows)
        content = f"""# {source_slug} Knowledge Candidates

This area contains Knowledge Candidates derived from Engineering Observations for `{source_identifier}`.

These records are candidates only. They are immature proposals awaiting review and do not create Knowledge Concepts, Generalized Knowledge, Certified Knowledge, or Publications.

## Candidate Index

| Identifier | Title | Supporting observation | Knowledge category | Review status |
| --- | --- | --- | --- | --- |
{index}

## Classification Summary

| Field | Value |
| --- | --- |
| Knowledge Source | `{source_identifier}` |
| Total candidate count | {len(rows)} |

## Candidate Boundary

Every candidate in this folder follows:

```text
Engineering Observation
->
Knowledge Candidate
```

Candidates remain repository-specific proposals. They must not be treated as concepts, generalized knowledge, certified knowledge, or publication sources.
"""
        (candidate_dir / "README.md").write_text(content, encoding="utf-8")

    def _update_candidate_root(self, source_identifier: str, source_slug: str) -> None:
        index_path = self.candidates_root / "README.md"
        text = index_path.read_text(encoding="utf-8")
        row = f"| `{source_identifier}` | [{source_slug} Knowledge Candidates](./{source_slug}/README.md) | Candidates recorded; concepts not created |\n"
        if f"`{source_identifier}`" in text:
            return
        marker = "| `KS-DJCONNECT-001` | [DJConnect Knowledge Candidates](./djconnect/README.md) | Candidates recorded; concepts not created |\n"
        if marker in text:
            text = text.replace(marker, marker + row)
        else:
            text = text.rstrip() + "\n" + row
        index_path.write_text(text, encoding="utf-8")

    def _category(self, observation: Observation) -> str:
        title = observation.title.lower()
        if "architecture" in title or "decision" in title:
            return "Architecture"
        if "release" in title or "changelog" in title:
            return "Workflow"
        if "coverage" in title or "verification" in title:
            return "Practice"
        if "requirements" in title or "status" in title:
            return "Reference"
        return "Practice"

    def _candidate_title(self, observation: Observation) -> str:
        evidence = observation.supporting_evidence or observation.title
        topic = Path(evidence).stem.replace("_", " ").replace("-", " ").title()
        return f"{observation.source_repository} may provide reusable knowledge from {topic}"

    def _existing_supporting_observations(self, candidate_dir: Path) -> set[str]:
        observations: set[str] = set()
        for candidate in candidate_dir.glob("KC-*.md"):
            observations.update(re.findall(r"`(EO-[A-Z0-9-]+)`", candidate.read_text(encoding="utf-8")))
        return observations

    def _next_identifier(self, source_identifier: str, existing_ids: set[str]) -> str:
        base = re.sub(r"-\d{3}$", "", source_identifier.removeprefix("KS-"))
        index = 1
        while True:
            identifier = f"KC-{base}-{index:03d}"
            if identifier not in existing_ids:
                return identifier
            index += 1

    def _first_supporting_observation(self, candidate_file: Path) -> str:
        match = re.search(r"`(EO-[A-Z0-9-]+)`", candidate_file.read_text(encoding="utf-8"))
        return match.group(1) if match else ""

    def _heading_title(self, candidate_file: Path) -> str:
        for line in candidate_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line.split(": ", 1)[-1]
        return candidate_file.stem

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
