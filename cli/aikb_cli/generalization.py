from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class GeneralizeConfig:
    source: str | None = None
    force: bool = False


@dataclass(frozen=True)
class GeneralizeResult:
    source_identifier: str
    generalized_set_path: Path
    created_count: int
    skipped_count: int


@dataclass(frozen=True)
class Concept:
    identifier: str
    title: str
    knowledge_source: str
    category: str
    domains: str
    confidence: str
    source_repositories: str
    candidates: list[str]
    observations: list[str]
    evidence_rows: list[dict[str, str]]
    path: Path
    set_slug: str


class KnowledgeGeneralizer:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root
        self.concepts_root = repository_root / "concepts"
        self.generalized_root = repository_root / "generalized"

    def generalize(self, config: GeneralizeConfig) -> list[GeneralizeResult]:
        concepts = self._load_concepts()
        selected = self._select_concepts(concepts, config.source)
        if not selected:
            raise RuntimeError("No Knowledge Concepts found for generalization.")
        grouped: dict[str, list[Concept]] = {}
        for concept in selected:
            grouped.setdefault(concept.knowledge_source, []).append(concept)
        return [
            self._generalize_source(source, source_concepts, config.force)
            for source, source_concepts in sorted(grouped.items())
        ]

    def _load_concepts(self) -> list[Concept]:
        concepts: list[Concept] = []
        for path in sorted(self.concepts_root.glob("*/KCN-*.md")):
            text = path.read_text(encoding="utf-8")
            metadata = self._metadata(text)
            source = metadata.get("Knowledge Source", "").strip("`")
            if not source:
                continue
            concepts.append(
                Concept(
                    identifier=metadata.get("Identifier", path.stem).strip("`"),
                    title=self._heading_title(text),
                    knowledge_source=source,
                    category=metadata.get("Knowledge category", "Practice"),
                    domains=metadata.get("Engineering domains", ""),
                    confidence=metadata.get("Confidence", "Medium"),
                    source_repositories=metadata.get("Source repositories", "").strip("`"),
                    candidates=self._unique(re.findall(r"`(KC-[A-Z0-9-]+)`", text)),
                    observations=self._unique(re.findall(r"`(EO-[A-Z0-9-]+)`", text)),
                    evidence_rows=self._evidence_rows(text),
                    path=path,
                    set_slug=path.parent.name,
                )
            )
        return concepts

    def _select_concepts(self, concepts: list[Concept], requested: str | None) -> list[Concept]:
        if not requested:
            return concepts
        normalized = requested.lower()
        return [
            concept
            for concept in concepts
            if normalized in concept.knowledge_source.lower()
            or normalized in concept.set_slug.lower()
        ]

    def _generalize_source(
        self,
        source_identifier: str,
        concepts: list[Concept],
        force: bool,
    ) -> GeneralizeResult:
        source_slug = concepts[0].set_slug
        generalized_dir = self.generalized_root / source_slug
        generalized_dir.mkdir(parents=True, exist_ok=True)
        existing_concepts = self._existing_supporting_concepts(generalized_dir)
        existing_ids = {path.stem for path in generalized_dir.glob("GK-*.md")}

        created: list[tuple[str, Concept]] = []
        skipped_count = 0
        for concept in concepts:
            if concept.identifier in existing_concepts and not force:
                skipped_count += 1
                continue
            identifier = self._next_identifier(source_identifier, existing_ids)
            existing_ids.add(identifier)
            self._write_generalized(generalized_dir / f"{identifier}.md", identifier, concept)
            created.append((identifier, concept))

        self._write_index(generalized_dir, source_identifier, source_slug)
        self._update_generalized_root(source_identifier, source_slug)
        return GeneralizeResult(
            source_identifier=source_identifier,
            generalized_set_path=generalized_dir / "README.md",
            created_count=len(created),
            skipped_count=skipped_count,
        )

    def _write_generalized(self, path: Path, identifier: str, concept: Concept) -> None:
        title = self._generalized_title(concept)
        candidate_links = "\n".join(
            f"- [{candidate}](../../candidates/{concept.set_slug}/{candidate}.md)"
            for candidate in concept.candidates
        )
        observation_links = "\n".join(
            f"- [{observation}](../../observations/{concept.set_slug}/{observation}.md)"
            for observation in concept.observations
        )
        evidence_rows = "\n".join(
            f"| `{row['observation']}` | `{concept.knowledge_source}` | `{row['repository']}` | `{row['evidence']}` | `{row['commit']}` |"
            for row in concept.evidence_rows
        )
        content = f"""# {identifier}: {title}

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `{identifier}` |
| Lifecycle state | Generalized Knowledge |
| Review status | Awaiting Certification Review |
| Certification status | Candidate |
| Knowledge category | {concept.category} |
| Engineering domains | {concept.domains} |
| Abstraction level | Technology Independent |
| Confidence | {concept.confidence} |
| Knowledge sources | `{concept.knowledge_source}` |

## Summary

{self._summary(title, concept)}

This item is Generalized Knowledge. It is reusable engineering knowledge, but it is not Certified Knowledge and is not publication-eligible.

## Engineering Rationale

The supporting concept indicates that related project evidence may express a reusable engineering concern. This generalized item preserves the engineering intent while removing unnecessary repository-specific wording from the knowledge title and summary.

## Preserved Constraints

- Applicability must be reviewed against the source evidence before certification.
- Repository-specific evidence remains authoritative only as evidence, not as canonical knowledge.
- Future certification must verify correctness, independence, and evidence sufficiency.

## Supporting Concepts

- [{concept.identifier}](../../concepts/{concept.set_slug}/{concept.identifier}.md)

## Supporting Candidates

{candidate_links}

## Supporting Observations

{observation_links}

## Source Evidence

| Observation | Knowledge Source | Repository | Evidence | Commit |
| --- | --- | --- | --- | --- |
{evidence_rows}

## Relationships

| Relationship | Target | Direction | Rationale |
| --- | --- | --- | --- |
| originates from | `{concept.identifier}` | this knowledge -> concept | Generalized Knowledge generated directly from the supporting Knowledge Concept. |

## Traceability

```text
{identifier}
->
{concept.identifier}
->
{", ".join(concept.candidates)}
->
{", ".join(concept.observations)}
->
{concept.knowledge_source}
->
{concept.source_repositories}
->
evidence files and commits listed above
```

## Generalization Notes

Removed direct repository naming from the knowledge title and summary where practical. Preserved source concept, candidate, observation, repository, evidence and commit lineage.

## Certification Boundary

This item is ready for certification review, but it is not certified. Certification must be performed by governed certification workflow.
"""
        path.write_text(content, encoding="utf-8")

    def _write_index(self, generalized_dir: Path, source_identifier: str, source_slug: str) -> None:
        rows = []
        for gk_file in sorted(generalized_dir.glob("GK-*.md")):
            text = gk_file.read_text(encoding="utf-8")
            metadata = self._metadata(text)
            concept = self._first_match(text, r"`(KCN-[A-Z0-9-]+)`")
            rows.append(
                "| [{identifier}](./{file}) | {title} | `{concept}` | {category} | {status} |".format(
                    identifier=metadata.get("Identifier", gk_file.stem).strip("`"),
                    file=gk_file.name,
                    title=self._heading_title(text),
                    concept=concept,
                    category=metadata.get("Knowledge category", ""),
                    status=metadata.get("Review status", ""),
                )
            )
        content = f"""# Generalized Knowledge Derived From {source_slug}

This area contains Generalized Knowledge derived from Knowledge Concepts for `{source_identifier}`.

These records are Generalized Knowledge only. They are not Certified Knowledge and are not publication-eligible.

## Generalized Knowledge Index

| Identifier | Title | Supporting concept | Knowledge category | Review status |
| --- | --- | --- | --- | --- |
{chr(10).join(rows)}

## Generalization Boundary

Generalized Knowledge in this folder removes unnecessary source-specific wording while preserving evidence lineage. Certification has not been performed.
"""
        (generalized_dir / "README.md").write_text(content, encoding="utf-8")

    def _update_generalized_root(self, source_identifier: str, source_slug: str) -> None:
        index_path = self.generalized_root / "README.md"
        text = index_path.read_text(encoding="utf-8")
        row = f"| `{source_identifier}` | [Generalized Knowledge Derived From {source_slug}](./{source_slug}/README.md) | Generalized knowledge recorded; certification not performed |\n"
        if f"`{source_identifier}`" in text:
            return
        marker = "| `KS-DJCONNECT-001` | [Generalized Knowledge Derived From DJConnect](./djconnect/README.md) | Generalized knowledge recorded; certification not performed |\n"
        if marker in text:
            text = text.replace(marker, marker + row)
        else:
            text = text.rstrip() + "\n" + row
        index_path.write_text(text, encoding="utf-8")

    def _generalized_title(self, concept: Concept) -> str:
        title = concept.title
        title = re.sub(r"\bpcvantol/djconnect-windows\b", "", title, flags=re.IGNORECASE)
        title = re.sub(r"\bdjconnect-windows\b", "", title, flags=re.IGNORECASE)
        title = re.sub(r"\s+", " ", title).strip()
        return title or concept.title

    def _summary(self, title: str, concept: Concept) -> str:
        return (
            f"{title} describes a reusable engineering concern derived from the normalized "
            f"concept `{concept.identifier}`. The knowledge remains grounded in the source "
            "lineage but is expressed without relying on the originating repository as authority."
        )

    def _existing_supporting_concepts(self, generalized_dir: Path) -> set[str]:
        concepts: set[str] = set()
        for item in generalized_dir.glob("GK-*.md"):
            concepts.update(re.findall(r"`(KCN-[A-Z0-9-]+)`", item.read_text(encoding="utf-8")))
        return concepts

    def _next_identifier(self, source_identifier: str, existing_ids: set[str]) -> str:
        base = re.sub(r"-\d{3}$", "", source_identifier.removeprefix("KS-"))
        index = 1
        while True:
            identifier = f"GK-{base}-{index:03d}"
            if identifier not in existing_ids:
                return identifier
            index += 1

    def _evidence_rows(self, text: str) -> list[dict[str, str]]:
        rows: list[dict[str, str]] = []
        for line in text.splitlines():
            if not line.startswith("| `KC-"):
                continue
            parts = [part.strip().strip("`") for part in line.strip().strip("|").split("|")]
            if len(parts) == 5:
                rows.append(
                    {
                        "candidate": parts[0],
                        "observation": parts[1],
                        "repository": parts[2],
                        "evidence": parts[3],
                        "commit": parts[4],
                    }
                )
        return rows

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

    def _heading_title(self, text: str) -> str:
        for line in text.splitlines():
            if line.startswith("# "):
                return line.split(": ", 1)[-1]
        return ""

    def _first_match(self, text: str, pattern: str) -> str:
        match = re.search(pattern, text)
        return match.group(1) if match else ""

    def _unique(self, values: list[str]) -> list[str]:
        unique: list[str] = []
        for value in values:
            if value not in unique:
                unique.append(value)
        return unique
