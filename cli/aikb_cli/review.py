from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class ReviewConfig:
    source: str | None = None
    force: bool = False


@dataclass(frozen=True)
class ReviewResult:
    source_identifier: str
    concept_set_path: Path
    created_count: int
    skipped_count: int


@dataclass(frozen=True)
class Candidate:
    identifier: str
    title: str
    knowledge_source: str
    category: str
    domains: str
    confidence: str
    source_repository: str
    observation: str
    evidence: str
    commit: str
    path: Path
    set_slug: str


class KnowledgeConceptFormer:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root
        self.candidates_root = repository_root / "candidates"
        self.concepts_root = repository_root / "concepts"

    def review(self, config: ReviewConfig) -> list[ReviewResult]:
        candidates = self._load_candidates()
        selected = self._select_candidates(candidates, config.source)
        if not selected:
            raise RuntimeError("No Knowledge Candidates found for concept formation.")
        grouped_by_source: dict[str, list[Candidate]] = {}
        for candidate in selected:
            grouped_by_source.setdefault(candidate.knowledge_source, []).append(candidate)
        return [
            self._review_source(source, source_candidates, config.force)
            for source, source_candidates in sorted(grouped_by_source.items())
        ]

    def _load_candidates(self) -> list[Candidate]:
        candidates: list[Candidate] = []
        for path in sorted(self.candidates_root.glob("*/KC-*.md")):
            text = path.read_text(encoding="utf-8")
            metadata = self._metadata(text)
            identifier = metadata.get("Identifier", path.stem).strip("`")
            knowledge_source = metadata.get("Knowledge Source", "").strip("`")
            if not knowledge_source:
                continue
            evidence_row = self._evidence_row(text)
            candidates.append(
                Candidate(
                    identifier=identifier,
                    title=self._heading_title(text),
                    knowledge_source=knowledge_source,
                    category=metadata.get("Knowledge category", "Practice"),
                    domains=metadata.get("Engineering domains", ""),
                    confidence=metadata.get("Confidence", "Medium"),
                    source_repository=metadata.get("Source repositories", "").strip("`"),
                    observation=self._first_match(text, r"`(EO-[A-Z0-9-]+)`"),
                    evidence=evidence_row.get("evidence", ""),
                    commit=evidence_row.get("commit", ""),
                    path=path,
                    set_slug=path.parent.name,
                )
            )
        return candidates

    def _select_candidates(
        self,
        candidates: list[Candidate],
        requested: str | None,
    ) -> list[Candidate]:
        if not requested:
            return candidates
        normalized = requested.lower()
        return [
            candidate
            for candidate in candidates
            if normalized in candidate.knowledge_source.lower()
            or normalized in candidate.set_slug.lower()
        ]

    def _review_source(
        self,
        source_identifier: str,
        candidates: list[Candidate],
        force: bool,
    ) -> ReviewResult:
        source_slug = candidates[0].set_slug
        concept_dir = self.concepts_root / source_slug
        concept_dir.mkdir(parents=True, exist_ok=True)
        existing_candidates = self._existing_supporting_candidates(concept_dir)
        existing_ids = {path.stem for path in concept_dir.glob("KCN-*.md")}

        created: list[tuple[str, str, list[Candidate]]] = []
        skipped_count = 0
        for group_key, group_candidates in self._groups(candidates).items():
            group_candidate_ids = {candidate.identifier for candidate in group_candidates}
            if group_candidate_ids.issubset(existing_candidates) and not force:
                skipped_count += len(group_candidates)
                continue
            identifier = self._next_identifier(source_identifier, existing_ids)
            existing_ids.add(identifier)
            title = self._concept_title(group_key, group_candidates)
            self._write_concept(concept_dir / f"{identifier}.md", identifier, title, group_candidates)
            created.append((identifier, title, group_candidates))

        self._write_index(concept_dir, source_identifier, source_slug)
        self._update_concept_root(source_identifier, source_slug)
        return ReviewResult(
            source_identifier=source_identifier,
            concept_set_path=concept_dir / "README.md",
            created_count=len(created),
            skipped_count=skipped_count,
        )

    def _groups(self, candidates: list[Candidate]) -> dict[str, list[Candidate]]:
        groups: dict[str, list[Candidate]] = {}
        for candidate in candidates:
            groups.setdefault(self._group_key(candidate), []).append(candidate)
        return groups

    def _group_key(self, candidate: Candidate) -> str:
        title = candidate.title.lower()
        if "architecture" in title or candidate.category == "Architecture":
            return "architecture documentation model"
        if "release" in title or "changelog" in title or candidate.category == "Workflow":
            return "release documentation workflow"
        if "requirements" in title or "status" in title or candidate.category == "Reference":
            return "repository quality reference"
        if "readme" in title or "repository documentation" in title:
            return "repository overview practice"
        return f"{candidate.category.lower()} candidate group"

    def _concept_title(self, group_key: str, candidates: list[Candidate]) -> str:
        source = candidates[0].source_repository
        return f"{source} {group_key.title()}"

    def _write_concept(
        self,
        path: Path,
        identifier: str,
        title: str,
        candidates: list[Candidate],
    ) -> None:
        category = self._dominant("category", candidates)
        domains = self._join_unique(candidate.domains for candidate in candidates)
        repositories = self._join_unique(candidate.source_repository for candidate in candidates)
        source = candidates[0].knowledge_source
        supporting_candidates = "\n".join(
            f"- [{candidate.identifier}](../../candidates/{candidate.set_slug}/{candidate.identifier}.md)"
            for candidate in candidates
        )
        supporting_observations = "\n".join(
            f"- [{candidate.observation}](../../observations/{candidate.set_slug}/{candidate.observation}.md)"
            for candidate in candidates
            if candidate.observation
        )
        evidence_rows = "\n".join(
            f"| `{candidate.identifier}` | `{candidate.observation}` | `{candidate.source_repository}` | `{candidate.evidence}` | `{candidate.commit}` |"
            for candidate in candidates
        )
        candidate_ids = ", ".join(candidate.identifier for candidate in candidates)
        observation_ids = ", ".join(candidate.observation for candidate in candidates if candidate.observation)
        content = f"""# {identifier}: {title}

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `{identifier}` |
| Lifecycle state | Knowledge Concept |
| Knowledge Source | `{source}` |
| Review status | Awaiting Review |
| Certification status | Candidate |
| Knowledge category | {category} |
| Engineering domains | {domains} |
| Abstraction level | Reusable |
| Confidence | Medium |
| Source repositories | {repositories} |

## Concept Summary

{title} is a normalized project-aware concept formed from related Knowledge Candidates.

This concept normalizes terminology across its supporting candidates, but it is not Generalized Knowledge and is not Certified Knowledge.

## Supporting Candidates

{supporting_candidates}

## Supporting Observations

{supporting_observations}

## Source Evidence

| Candidate | Observation | Repository | Evidence | Commit |
| --- | --- | --- | --- | --- |
{evidence_rows}

## Relationships

| Relationship | Target | Direction | Rationale |
| --- | --- | --- | --- |
| originates from | `{candidate_ids}` | this concept -> candidates | Concept formed directly from supporting Knowledge Candidates. |

## Traceability

```text
{identifier}
->
{candidate_ids}
->
{observation_ids}
->
{source}
->
{repositories}
->
evidence files and commits listed above
```

## Review History

| Event | Status |
| --- | --- |
| Concept formation | Awaiting Review |

## Concept Boundary

This concept remains project aware. It does not generalize knowledge beyond the supporting candidates, certify knowledge, or create publications.
"""
        path.write_text(content, encoding="utf-8")

    def _write_index(self, concept_dir: Path, source_identifier: str, source_slug: str) -> None:
        rows = []
        for concept_file in sorted(concept_dir.glob("KCN-*.md")):
            text = concept_file.read_text(encoding="utf-8")
            metadata = self._metadata(text)
            candidates = "`, `".join(self._unique(re.findall(r"`(KC-[A-Z0-9-]+)`", text)))
            rows.append(
                "| [{identifier}](./{file}) | {title} | `{candidates}` | {category} | {status} |".format(
                    identifier=metadata.get("Identifier", concept_file.stem).strip("`"),
                    file=concept_file.name,
                    title=self._heading_title(text),
                    candidates=candidates,
                    category=metadata.get("Knowledge category", ""),
                    status=metadata.get("Review status", ""),
                )
            )
        content = f"""# {source_slug} Knowledge Concepts

This area contains Knowledge Concepts normalized from Knowledge Candidates for `{source_identifier}`.

These records are concepts only. They do not create Generalized Knowledge, Certified Knowledge, or Publications.

## Concept Index

| Identifier | Title | Supporting candidates | Knowledge category | Review status |
| --- | --- | --- | --- | --- |
{chr(10).join(rows)}

## Concept Boundary

Concepts in this folder normalize candidates into coherent engineering ideas. They are not yet generalized, certified, or publishable.
"""
        (concept_dir / "README.md").write_text(content, encoding="utf-8")

    def _update_concept_root(self, source_identifier: str, source_slug: str) -> None:
        index_path = self.concepts_root / "README.md"
        text = index_path.read_text(encoding="utf-8")
        row = f"| `{source_identifier}` | [{source_slug} Knowledge Concepts](./{source_slug}/README.md) | Concepts recorded; generalized knowledge not created |\n"
        if f"`{source_identifier}`" in text:
            return
        marker = "| `KS-DJCONNECT-001` | [DJConnect Knowledge Concepts](./djconnect/README.md) | Concepts recorded; generalized knowledge not created |\n"
        if marker in text:
            text = text.replace(marker, marker + row)
        else:
            text = text.rstrip() + "\n" + row
        index_path.write_text(text, encoding="utf-8")

    def _existing_supporting_candidates(self, concept_dir: Path) -> set[str]:
        candidates: set[str] = set()
        for concept in concept_dir.glob("KCN-*.md"):
            candidates.update(re.findall(r"`(KC-[A-Z0-9-]+)`", concept.read_text(encoding="utf-8")))
        return candidates

    def _next_identifier(self, source_identifier: str, existing_ids: set[str]) -> str:
        base = re.sub(r"-\d{3}$", "", source_identifier.removeprefix("KS-"))
        index = 1
        while True:
            identifier = f"KCN-{base}-{index:03d}"
            if identifier not in existing_ids:
                return identifier
            index += 1

    def _dominant(self, field: str, candidates: list[Candidate]) -> str:
        values: dict[str, int] = {}
        for candidate in candidates:
            value = getattr(candidate, field)
            values[value] = values.get(value, 0) + 1
        return sorted(values.items(), key=lambda item: (-item[1], item[0]))[0][0]

    def _join_unique(self, values: object) -> str:
        unique: list[str] = []
        for value in values:
            for part in str(value).split(","):
                cleaned = part.strip().strip("`")
                if cleaned and cleaned not in unique:
                    unique.append(cleaned)
        return ", ".join(unique)

    def _unique(self, values: list[str]) -> list[str]:
        unique: list[str] = []
        for value in values:
            if value not in unique:
                unique.append(value)
        return unique

    def _evidence_row(self, text: str) -> dict[str, str]:
        for line in text.splitlines():
            if not line.startswith("| `"):
                continue
            parts = [part.strip().strip("`") for part in line.strip().strip("|").split("|")]
            if len(parts) == 3 and parts[2] != "---":
                return {"repository": parts[0], "evidence": parts[1], "commit": parts[2]}
        return {"repository": "", "evidence": "", "commit": ""}

    def _first_match(self, text: str, pattern: str) -> str:
        match = re.search(pattern, text)
        return match.group(1) if match else ""

    def _heading_title(self, text: str) -> str:
        for line in text.splitlines():
            if line.startswith("# "):
                return line.split(": ", 1)[-1]
        return ""

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
