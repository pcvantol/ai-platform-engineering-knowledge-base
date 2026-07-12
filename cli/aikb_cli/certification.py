from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
import re


@dataclass(frozen=True)
class CertifyConfig:
    source: str | None = None
    force: bool = False


@dataclass(frozen=True)
class CertifyResult:
    source_identifier: str
    certified_set_path: Path
    certification_record_path: Path
    certified_count: int
    skipped_count: int


@dataclass(frozen=True)
class GeneralizedKnowledge:
    identifier: str
    title: str
    knowledge_source: str
    category: str
    domains: str
    confidence: str
    concept: str
    candidates: list[str]
    observations: list[str]
    evidence_rows: list[dict[str, str]]
    path: Path
    set_slug: str


class KnowledgeCertifier:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root
        self.generalized_root = repository_root / "generalized"
        self.certified_root = repository_root / "certified"
        self.cycles_root = repository_root / "certification" / "cycles"

    def certify(self, config: CertifyConfig) -> list[CertifyResult]:
        items = self._load_generalized()
        selected = self._select_items(items, config.source)
        if not selected:
            raise RuntimeError("No Generalized Knowledge found for certification.")
        grouped: dict[str, list[GeneralizedKnowledge]] = {}
        for item in selected:
            grouped.setdefault(item.knowledge_source, []).append(item)
        return [
            self._certify_source(source, source_items, config.force)
            for source, source_items in sorted(grouped.items())
        ]

    def _load_generalized(self) -> list[GeneralizedKnowledge]:
        items: list[GeneralizedKnowledge] = []
        for path in sorted(self.generalized_root.glob("*/GK-*.md")):
            text = path.read_text(encoding="utf-8")
            metadata = self._metadata(text)
            source = metadata.get("Knowledge sources", "").strip("`")
            if not source:
                continue
            items.append(
                GeneralizedKnowledge(
                    identifier=metadata.get("Identifier", path.stem).strip("`"),
                    title=self._heading_title(text),
                    knowledge_source=source,
                    category=metadata.get("Knowledge category", ""),
                    domains=metadata.get("Engineering domains", ""),
                    confidence=metadata.get("Confidence", "Medium"),
                    concept=self._first_match(text, r"(?:`|\[)(KCN-[A-Z0-9-]+)(?:`|\])"),
                    candidates=self._unique(
                        re.findall(r"(?:`|\[)(KC-[A-Z0-9-]+)(?:`|\])", text)
                    ),
                    observations=self._unique(
                        re.findall(r"(?:`|\[)(EO-[A-Z0-9-]+)(?:`|\])", text)
                    ),
                    evidence_rows=self._evidence_rows(text),
                    path=path,
                    set_slug=path.parent.name,
                )
            )
        return items

    def _select_items(
        self,
        items: list[GeneralizedKnowledge],
        requested: str | None,
    ) -> list[GeneralizedKnowledge]:
        if not requested:
            return items
        normalized = requested.lower()
        return [
            item
            for item in items
            if normalized in item.knowledge_source.lower()
            or normalized in item.set_slug.lower()
        ]

    def _certify_source(
        self,
        source_identifier: str,
        items: list[GeneralizedKnowledge],
        force: bool,
    ) -> CertifyResult:
        source_slug = items[0].set_slug
        certified_dir = self.certified_root / source_slug
        certified_dir.mkdir(parents=True, exist_ok=True)
        existing_generalized = self._existing_originating_generalized(certified_dir)
        existing_ids = {path.stem for path in certified_dir.glob("CK-*.md")}

        certified: list[tuple[str, GeneralizedKnowledge]] = []
        skipped_count = 0
        for item in items:
            if item.identifier in existing_generalized and not force:
                skipped_count += 1
                continue
            if not self._ready(item):
                skipped_count += 1
                continue
            identifier = self._next_identifier(source_identifier, existing_ids)
            existing_ids.add(identifier)
            self._write_certified(certified_dir / f"{identifier}.md", identifier, item)
            certified.append((identifier, item))

        cycle_path = self._write_cycle(source_identifier, source_slug, certified, skipped_count)
        self._write_index(certified_dir, source_identifier, source_slug, cycle_path)
        self._update_certified_root(source_identifier, source_slug)
        return CertifyResult(
            source_identifier=source_identifier,
            certified_set_path=certified_dir / "README.md",
            certification_record_path=cycle_path,
            certified_count=len(certified),
            skipped_count=skipped_count,
        )

    def _ready(self, item: GeneralizedKnowledge) -> bool:
        return bool(item.concept and item.candidates and item.observations and item.evidence_rows)

    def _write_certified(self, path: Path, identifier: str, item: GeneralizedKnowledge) -> None:
        today = date.today().isoformat()
        evidence_rows = "\n".join(
            f"| `{row['observation']}` | `{row['repository']}` | `{row['evidence']}` | `{row['commit']}` |"
            for row in item.evidence_rows
        )
        candidate_links = "\n".join(
            f"- [{candidate}](../../candidates/{item.set_slug}/{candidate}.md)"
            for candidate in item.candidates
        )
        observation_links = "\n".join(
            f"- [{observation}](../../observations/{item.set_slug}/{observation}.md)"
            for observation in item.observations
        )
        content = f"""# {identifier}: {item.title}

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `{identifier}` |
| Lifecycle state | Certified Knowledge |
| Certification status | Certified |
| Certification date | {today} |
| Originating Generalized Knowledge | `{item.identifier}` |
| Knowledge category | {item.category} |
| Engineering domains | {item.domains} |
| Abstraction level | Canonical |
| Confidence | High |
| Publication eligibility | Eligible |
| Knowledge sources | `{item.knowledge_source}` |

## Certified Statement

{item.title} is accepted as reusable engineering knowledge within the AI Platform Engineering Knowledge Base.

The knowledge is certified from `{item.identifier}` and remains authoritative only within the scope, constraints, and traceability recorded here.

## Engineering Rationale

Certification is based on reviewed Generalized Knowledge with complete lineage to supporting concept, candidate, observation, source repository, evidence file, and commit references.

## Applicability

This knowledge applies where the same engineering concern appears outside the originating repository context and where the preserved constraints remain valid.

## Constraints

- Certification does not make the originating repository canonical.
- Source evidence remains evidence, not authority.
- Material changes require governed re-certification.
- Publications may use this record as source, but publications do not revise this record.

## Supporting Generalized Knowledge

- [{item.identifier}](../../generalized/{item.set_slug}/{item.identifier}.md)

## Supporting Concepts

- [{item.concept}](../../concepts/{item.set_slug}/{item.concept}.md)

## Supporting Candidates

{candidate_links}

## Supporting Observations

{observation_links}

## Traceability

```text
{identifier}
->
{item.identifier}
->
{item.concept}
->
{", ".join(item.candidates)}
->
{", ".join(item.observations)}
->
{item.knowledge_source}
->
source repositories and evidence listed below
```

## Source Evidence

| Observation | Repository | Evidence | Commit |
| --- | --- | --- | --- |
{evidence_rows}

## Relationships

| Relationship | Target | Direction | Rationale |
| --- | --- | --- | --- |
| originates from | `{item.identifier}` | this knowledge -> generalized knowledge | Certified directly from reviewed Generalized Knowledge. |

## Certification Rationale

Certified because the originating Generalized Knowledge preserves complete traceability, has supporting source evidence, is reusable beyond the source repository wording, and satisfies conservative certification readiness checks.

## Review History

| Date | Review activity | Outcome |
| --- | --- | --- |
| {today} | Certification readiness review for `{item.identifier}`. | Passed certification criteria. |

## Certification History

| Date | Event |
| --- | --- |
| {today} | Initial certification from `{item.identifier}`. |
"""
        path.write_text(content, encoding="utf-8")

    def _write_cycle(
        self,
        source_identifier: str,
        source_slug: str,
        certified: list[tuple[str, GeneralizedKnowledge]],
        skipped_count: int,
    ) -> Path:
        today = date.today().isoformat()
        cycle_path = self.cycles_root / f"{today}-{source_slug}-certification-cycle.md"
        decision_rows = "\n".join(
            f"| `{item.identifier}` | Certified | `{identifier}` | Traceability, evidence, reuse and governance checks passed. |"
            for identifier, item in certified
        )
        if not decision_rows:
            decision_rows = "| None | No new certification | None | All selected items were skipped or already certified. |"
        content = f"""# {today} Certification Cycle for {source_identifier}

## Purpose

This record documents a governed certification cycle executed by `aikb certify`.

Certification promotes eligible Generalized Knowledge into Certified Knowledge. Certification does not create publications.

## Scope

Originating Knowledge Source:

- `{source_identifier}`

Source generalized knowledge set:

- [generalized/{source_slug}](../../generalized/{source_slug}/README.md)

## Review Criteria

Each Generalized Knowledge item was reviewed for:

- engineering correctness
- supporting evidence
- traceability completeness
- relationship consistency
- reusability
- maturity
- governance readiness
- publication readiness

## Certification Decisions

| Generalized Knowledge | Decision | Certified Knowledge | Rationale |
| --- | --- | --- | --- |
{decision_rows}

Skipped items: {skipped_count}

## Traceability

```text
Certified Knowledge
->
Generalized Knowledge
->
Knowledge Concept
->
Knowledge Candidate
->
Engineering Observation
->
Knowledge Source
->
Repository
->
Evidence
```

## Publication Boundary

The certified items are publication eligible.

This certification cycle does not create publications.

## Certification History

| Date | Event |
| --- | --- |
| {today} | Certification cycle completed for `{source_identifier}`. |
"""
        self.cycles_root.mkdir(parents=True, exist_ok=True)
        cycle_path.write_text(content, encoding="utf-8")
        return cycle_path

    def _write_index(
        self,
        certified_dir: Path,
        source_identifier: str,
        source_slug: str,
        cycle_path: Path,
    ) -> None:
        rows = []
        for ck_file in sorted(certified_dir.glob("CK-*.md")):
            text = ck_file.read_text(encoding="utf-8")
            metadata = self._metadata(text)
            gk = metadata.get("Originating Generalized Knowledge", "").strip("`")
            rows.append(
                "| [{identifier}](./{file}) | {title} | `{gk}` | {category} | {status} |".format(
                    identifier=metadata.get("Identifier", ck_file.stem).strip("`"),
                    file=ck_file.name,
                    title=self._heading_title(text),
                    gk=gk,
                    category=metadata.get("Knowledge category", ""),
                    status=metadata.get("Certification status", ""),
                )
            )
        relative_cycle = Path("../../") / cycle_path.relative_to(self.repository_root)
        content = f"""# Certified Knowledge Derived From {source_slug}

This area contains Certified Knowledge promoted from Generalized Knowledge for `{source_identifier}`.

These records are canonical Certified Knowledge inside the Knowledge Base. They are publication eligible, but this folder does not create publications.

## Certified Knowledge Index

| Identifier | Title | Originating generalized knowledge | Knowledge category | Certification status |
| --- | --- | --- | --- | --- |
{chr(10).join(rows)}

## Certification Record

Certification decision record:

- [{cycle_path.stem}]({relative_cycle.as_posix()})

## Publication Boundary

Certified Knowledge in this folder is eligible for future publication generation. No publication is created by this certification cycle.
"""
        (certified_dir / "README.md").write_text(content, encoding="utf-8")

    def _update_certified_root(self, source_identifier: str, source_slug: str) -> None:
        index_path = self.certified_root / "README.md"
        text = index_path.read_text(encoding="utf-8")
        row = f"| `{source_identifier}` | [Certified Knowledge Derived From {source_slug}](./{source_slug}/README.md) | Certified |\n"
        if f"`{source_identifier}`" in text:
            return
        marker = "| `KS-DJCONNECT-001` | [Certified Knowledge Derived From DJConnect](./djconnect/README.md) | Certified |\n"
        if marker in text:
            text = text.replace(marker, marker + row)
        else:
            text = text.rstrip() + "\n" + row
        index_path.write_text(text, encoding="utf-8")

    def _existing_originating_generalized(self, certified_dir: Path) -> set[str]:
        values: set[str] = set()
        for item in certified_dir.glob("CK-*.md"):
            metadata = self._metadata(item.read_text(encoding="utf-8"))
            value = metadata.get("Originating Generalized Knowledge", "").strip("`")
            if value:
                values.add(value)
        return values

    def _next_identifier(self, source_identifier: str, existing_ids: set[str]) -> str:
        base = re.sub(r"-\d{3}$", "", source_identifier.removeprefix("KS-"))
        index = 1
        while True:
            identifier = f"CK-{base}-{index:03d}"
            if identifier not in existing_ids:
                return identifier
            index += 1

    def _evidence_rows(self, text: str) -> list[dict[str, str]]:
        rows: list[dict[str, str]] = []
        for line in text.splitlines():
            if not line.startswith("| `EO-"):
                continue
            parts = [part.strip().strip("`") for part in line.strip().strip("|").split("|")]
            if len(parts) == 5:
                rows.append(
                    {
                        "observation": parts[0],
                        "knowledge_source": parts[1],
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
