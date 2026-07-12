from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
import re
import subprocess
import tempfile


SUPPORTED_EVIDENCE_NAMES = (
    "ARCHITECTURE",
    "ARCHITECTURE_DECISIONS",
    "TECHNICAL_DESIGN_DECISIONS",
    "REPORT",
    "BASELINE",
    "QUALIFICATION",
    "COVERAGE",
    "RELEASE",
    "CHANGELOG",
    "REPOSITORY_STATUS",
    "BUILD_RELEASE_HYGIENE",
    "NON_FUNCTIONAL_REQUIREMENTS",
)


@dataclass(frozen=True)
class ExtractConfig:
    source: str | None = None
    force: bool = False


@dataclass(frozen=True)
class ExtractResult:
    source_identifier: str
    observation_set_path: Path
    created_count: int
    skipped_count: int


@dataclass(frozen=True)
class KnowledgeSource:
    identifier: str
    name: str
    slug: str
    repository_url: str
    repository_owner: str
    engineering_domains: str


@dataclass(frozen=True)
class EvidenceDocument:
    path: str
    title: str
    evidence_type: str
    engineering_domain: str


class EngineeringObservationExtractor:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root
        self.sources_root = repository_root / "sources"
        self.observations_root = repository_root / "observations"

    def extract(self, config: ExtractConfig) -> list[ExtractResult]:
        sources = self._select_sources(self._load_sources(), config.source)
        if not sources:
            raise RuntimeError("No extractable Knowledge Sources found.")
        return [self._extract_source(source, config.force) for source in sources]

    def _load_sources(self) -> list[KnowledgeSource]:
        sources: list[KnowledgeSource] = []
        for profile in sorted(self.sources_root.glob("*/README.md")):
            metadata = self._metadata(profile.read_text(encoding="utf-8"))
            identifier = (
                metadata.get("Identifier")
                or metadata.get("Knowledge Source identifier")
                or ""
            ).strip("`")
            repository_url = metadata.get("Repository URL", "")
            if not identifier or not repository_url:
                continue
            sources.append(
                KnowledgeSource(
                    identifier=identifier,
                    name=metadata.get("Repository name", profile.parent.name).strip("`"),
                    slug=profile.parent.name,
                    repository_url=repository_url,
                    repository_owner=metadata.get("Repository owner", "unknown").strip("`"),
                    engineering_domains=metadata.get("Engineering domains", "Platform Engineering"),
                )
            )
        return sources

    def _select_sources(
        self,
        sources: list[KnowledgeSource],
        requested: str | None,
    ) -> list[KnowledgeSource]:
        if not requested:
            return sources
        normalized = requested.lower()
        return [
            source
            for source in sources
            if normalized in {
                source.identifier.lower(),
                source.name.lower(),
                source.slug.lower(),
            }
            or normalized in source.identifier.lower()
            or normalized in source.name.lower()
            or normalized in source.slug.lower()
        ]

    def _extract_source(self, source: KnowledgeSource, force: bool) -> ExtractResult:
        observation_dir = self.observations_root / source.slug
        observation_dir.mkdir(parents=True, exist_ok=True)
        existing_evidence = self._existing_evidence_paths()
        existing_ids = self._existing_observation_ids(observation_dir)

        with tempfile.TemporaryDirectory(prefix="aikb-extract-") as temp_dir:
            repo_dir = Path(temp_dir) / "repository"
            self._clone(source.repository_url, repo_dir)
            commit = self._git(repo_dir, ["rev-parse", "HEAD"])
            documents = self._discover_evidence(repo_dir, source)

        created: list[tuple[str, EvidenceDocument]] = []
        skipped_count = 0
        for document in documents:
            if document.path in existing_evidence and not force:
                skipped_count += 1
                continue
            identifier = self._next_identifier(source.identifier, existing_ids)
            existing_ids.add(identifier)
            self._write_observation(
                observation_dir / f"{identifier}.md",
                identifier,
                source,
                document,
                commit,
            )
            created.append((identifier, document))

        self._write_index(observation_dir, source, created)
        self._update_observation_root(source)
        return ExtractResult(
            source_identifier=source.identifier,
            observation_set_path=observation_dir / "README.md",
            created_count=len(created),
            skipped_count=skipped_count,
        )

    def _clone(self, repository_url: str, repo_dir: Path) -> None:
        subprocess.run(
            ["git", "clone", "--depth", "1", repository_url, str(repo_dir)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    def _git(self, repo_dir: Path, args: list[str]) -> str:
        return subprocess.check_output(["git", "-C", str(repo_dir), *args], text=True).strip()

    def _discover_evidence(
        self,
        repo_dir: Path,
        source: KnowledgeSource,
    ) -> list[EvidenceDocument]:
        documents: list[EvidenceDocument] = []
        for path in sorted(repo_dir.rglob("*.md")):
            if ".git" in path.parts:
                continue
            relative = path.relative_to(repo_dir).as_posix()
            name = path.name.upper()
            if not self._supported_evidence_name(name, relative):
                continue
            documents.append(
                EvidenceDocument(
                    path=relative,
                    title=self._title(path),
                    evidence_type=self._evidence_type(name, relative),
                    engineering_domain=self._domain(name, relative, source.engineering_domains),
                )
            )
        return documents

    def _supported_evidence_name(self, name: str, relative: str) -> bool:
        if relative == "README.md":
            return True
        return any(token in name for token in SUPPORTED_EVIDENCE_NAMES)

    def _title(self, path: Path) -> str:
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            stripped = line.strip()
            if stripped.startswith("# "):
                return stripped[2:].strip()
        return path.stem.replace("_", " ").replace("-", " ").title()

    def _evidence_type(self, name: str, relative: str) -> str:
        if "COVERAGE" in name or "BASELINE" in name:
            return "coverage report"
        if "REPORT" in name or "QUALIFICATION" in name:
            return "engineering report"
        if "ARCHITECTURE" in name or "DECISION" in name:
            return "architecture documentation"
        if "RELEASE" in name or "CHANGELOG" in name:
            return "release documentation"
        if relative == "README.md" or "STATUS" in name:
            return "repository documentation"
        return "engineering documentation"

    def _domain(self, name: str, relative: str, fallback: str) -> str:
        if "COVERAGE" in name or "REPORT" in name or "QUALIFICATION" in name:
            return "Verification, Software Assurance"
        if "ARCHITECTURE" in name or "DECISION" in name:
            return "Architecture"
        if "RELEASE" in name or "CHANGELOG" in name:
            return "Release Engineering"
        if "PROFILE" in name or "CLIENT" in name or "WINDOWS" in name:
            return "Client Engineering, Architecture"
        return fallback

    def _write_observation(
        self,
        path: Path,
        identifier: str,
        source: KnowledgeSource,
        document: EvidenceDocument,
        commit: str,
    ) -> None:
        today = date.today().isoformat()
        title = f"{source.name} contains {document.evidence_type}: {document.title}"
        content = f"""# {identifier}: {title}

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `{identifier}` |
| Lifecycle state | Engineering Observation |
| Title | {title} |
| Knowledge Source | `{source.identifier}` |
| Source repository | `{source.repository_owner}/{source.name}` |
| Repository URL | {source.repository_url} |
| Supporting evidence | `{document.path}` |
| Evidence type | {document.evidence_type} |
| Engineering domain | {document.engineering_domain} |
| Repository location | `{document.path}` |
| Observation date | {today} |
| Source commit | `{commit}` |
| Confidence | Medium |

## Summary

The repository `{source.repository_owner}/{source.name}` contains `{document.path}` with the title "{document.title}".

This observation records the existence of repository-specific engineering evidence only. It does not interpret, generalize, or recommend knowledge.

## Supporting Evidence

| Evidence | Repository | Commit |
| --- | --- | --- |
| `{document.path}` | `{source.repository_owner}/{source.name}` | `{commit}` |

## Relationships

| Relationship | Target | Rationale |
| --- | --- | --- |
| originates from | `{source.identifier}` | The observation was extracted from the registered Knowledge Source. |

## Traceability

```text
{identifier}
->
{source.identifier}
->
{source.repository_owner}/{source.name}
->
{document.path}
->
{commit}
```

## Boundary

This record is an Engineering Observation only. It does not create a Knowledge Candidate, Knowledge Concept, Generalized Knowledge, Certified Knowledge, or Publication.
"""
        path.write_text(content, encoding="utf-8")

    def _write_index(
        self,
        observation_dir: Path,
        source: KnowledgeSource,
        created: list[tuple[str, EvidenceDocument]],
    ) -> None:
        rows = []
        for observation_file in sorted(observation_dir.glob("EO-*.md")):
            metadata = self._metadata(observation_file.read_text(encoding="utf-8"))
            rows.append(
                "| [{identifier}](./{file}) | {title} | `{repository}` | {domain} | {confidence} |".format(
                    identifier=metadata.get("Identifier", observation_file.stem).strip("`"),
                    file=observation_file.name,
                    title=metadata.get("Title", observation_file.stem),
                    repository=metadata.get("Source repository", source.name).strip("`"),
                    domain=metadata.get("Engineering domain", ""),
                    confidence=metadata.get("Confidence", ""),
                )
            )
        index = "\n".join(rows)
        content = f"""# {source.name} Engineering Observations

This area contains Engineering Observations extracted from `{source.identifier}`.

These records are observations only. They are repository-specific evidence records and do not create Knowledge Candidates, Knowledge Concepts, Generalized Knowledge, Certified Knowledge, or Publications.

## Observation Index

| Identifier | Title | Source repository | Engineering domain | Confidence |
| --- | --- | --- | --- | --- |
{index}

## Extraction Summary

| Field | Value |
| --- | --- |
| Knowledge Source | `{source.identifier}` |
| Source repository | `{source.repository_owner}/{source.name}` |
| Last extraction date | {date.today().isoformat()} |
| New observations in last run | {len(created)} |

## Traceability Boundary

Every observation links back to:

```text
Engineering Observation
->
Knowledge Source
->
Repository
->
Evidence file
->
Commit
```
"""
        (observation_dir / "README.md").write_text(content, encoding="utf-8")

    def _update_observation_root(self, source: KnowledgeSource) -> None:
        index_path = self.observations_root / "README.md"
        text = index_path.read_text(encoding="utf-8")
        row = f"| `{source.identifier}` | [{source.name} Engineering Observations](./{source.slug}/README.md) | Observations recorded; candidates not created |\n"
        if f"`{source.identifier}`" in text:
            return
        marker = "| `KS-DJCONNECT-001` | [DJConnect Engineering Observations](./djconnect/README.md) | Observations recorded; candidates not created |\n"
        if marker in text:
            text = text.replace(marker, marker + row)
        else:
            text = text.rstrip() + "\n" + row
        index_path.write_text(text, encoding="utf-8")

    def _existing_evidence_paths(self) -> set[str]:
        paths: set[str] = set()
        for observation in self.observations_root.glob("**/EO-*.md"):
            text = observation.read_text(encoding="utf-8", errors="replace")
            paths.update(re.findall(r"`([^`]+\.md)`", text))
        return paths

    def _existing_observation_ids(self, observation_dir: Path) -> set[str]:
        return {path.stem for path in observation_dir.glob("EO-*.md")}

    def _next_identifier(self, source_identifier: str, existing_ids: set[str]) -> str:
        base = re.sub(r"-\d{3}$", "", source_identifier.removeprefix("KS-"))
        index = 1
        while True:
            identifier = f"EO-{base}-{index:03d}"
            if identifier not in existing_ids:
                return identifier
            index += 1

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
