from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import json
import re

from .assistant import CertifiedKnowledge, EngineeringAssistant


GENERATOR_ID = "engineering-program-generator"
GENERATOR_VERSION = "0.1.0"
SUPPORTED_PROGRAM_TYPES = (
    "ai-platform",
    "embedded-platform",
    "software-assurance",
    "verification-platform",
)


@dataclass(frozen=True)
class GenerateConfig:
    program_type: str
    output_dir: Path
    name: str | None = None
    force: bool = False


@dataclass(frozen=True)
class GenerateResult:
    program_identifier: str
    output_dir: Path
    manifest_path: Path
    artifact_paths: list[Path]
    certified_knowledge_ids: list[str]


class EngineeringProgramGenerator:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root
        self.assistant = EngineeringAssistant(repository_root)

    def generate(self, config: GenerateConfig) -> GenerateResult:
        if config.program_type not in SUPPORTED_PROGRAM_TYPES:
            supported = ", ".join(SUPPORTED_PROGRAM_TYPES)
            raise RuntimeError(
                f"Unsupported program type: {config.program_type}. Supported program types: {supported}"
            )
        output_dir = config.output_dir.resolve()
        self._validate_output_dir(output_dir, config.force)
        knowledge = self._select_knowledge(config.program_type)
        if not knowledge:
            raise RuntimeError("No Certified Knowledge available for program generation.")

        program_name = config.name or self._title(config.program_type)
        program_identifier = self._program_identifier(config.program_type, program_name)
        generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        context = {
            "program_type": config.program_type,
            "program_name": program_name,
            "program_identifier": program_identifier,
            "generated_at": generated_at,
        }

        artifacts = {
            "README.md": self._readme(context, knowledge),
            "ARCHITECTURE.md": self._architecture(context, knowledge),
            "GOVERNANCE.md": self._governance(context, knowledge),
            "ROADMAP.md": self._roadmap(context, knowledge),
            "BACKLOG.md": self._backlog(context, knowledge),
            "VERIFICATION_STRATEGY.md": self._strategy(context, knowledge, "Verification"),
            "SOFTWARE_ASSURANCE_STRATEGY.md": self._strategy(context, knowledge, "Software Assurance"),
            "RELEASE_STRATEGY.md": self._strategy(context, knowledge, "Release"),
            "ENGINEERING_GUIDANCE.md": self._guidance(context, knowledge),
            "KNOWLEDGE_SOURCE_REGISTRATION.md": self._knowledge_source_registration(context, knowledge),
            "CHECKLISTS.md": self._checklists(context, knowledge),
            "PROMPTS.md": self._prompts(context, knowledge),
            ".aikb/engineering-program-manifest.json": json.dumps(
                self._manifest(context, knowledge, artifacts=[]),
                indent=2,
            )
            + "\n",
        }
        manifest = self._manifest(context, knowledge, artifacts=sorted(artifacts))
        artifacts[".aikb/engineering-program-manifest.json"] = json.dumps(manifest, indent=2) + "\n"

        written: list[Path] = []
        for relative_path, content in artifacts.items():
            path = output_dir / relative_path
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            written.append(path)

        return GenerateResult(
            program_identifier=program_identifier,
            output_dir=output_dir,
            manifest_path=output_dir / ".aikb" / "engineering-program-manifest.json",
            artifact_paths=written,
            certified_knowledge_ids=[item.identifier for item in knowledge],
        )

    def _validate_output_dir(self, output_dir: Path, force: bool) -> None:
        if output_dir.exists() and any(output_dir.iterdir()) and not force:
            raise RuntimeError(
                f"Output directory is not empty: {output_dir}. Use --force to allow writing."
            )

    def _select_knowledge(self, program_type: str) -> list[CertifiedKnowledge]:
        knowledge = self.assistant._load_certified_knowledge()
        profile_terms = set(self._program_terms(program_type))
        scored: list[tuple[int, CertifiedKnowledge]] = []
        for item in knowledge:
            text = " ".join(
                [
                    item.identifier,
                    item.title,
                    item.category,
                    item.domains,
                    item.summary,
                    " ".join(row.get("evidence", "") for row in item.evidence_rows),
                ]
            ).lower()
            terms = set(re.findall(r"[a-z0-9]+", text))
            score = len(profile_terms & terms)
            if score:
                scored.append((score, item))
        if not scored:
            return knowledge
        scored.sort(key=lambda pair: (-pair[0], pair[1].identifier))
        selected = [item for _, item in scored]
        return selected[: max(4, min(len(selected), 8))]

    def _program_terms(self, program_type: str) -> list[str]:
        common = ["architecture", "governance", "platform", "engineering"]
        profiles = {
            "verification-platform": ["verification", "runtime", "adapter", "coverage", "evidence"],
            "ai-platform": ["platform", "architecture", "verification", "assurance", "governance"],
            "embedded-platform": ["embedded", "client", "runtime", "adapter", "release"],
            "software-assurance": ["software", "assurance", "governance", "qualification", "evidence"],
        }
        return common + profiles[program_type]

    def _readme(self, context: dict[str, str], knowledge: list[CertifiedKnowledge]) -> str:
        return f"""# {context['program_name']}

This Engineering Program was generated from Certified Knowledge.

It is a derived artifact. The AI Platform Engineering Knowledge Base remains canonical.

## Program Identity

| Field | Value |
| --- | --- |
| Program identifier | `{context['program_identifier']}` |
| Program type | `{context['program_type']}` |
| Generated at | {context['generated_at']} |
| Generator | `{GENERATOR_ID}` |
| Generator version | {GENERATOR_VERSION} |

## Generated Artifacts

- `ARCHITECTURE.md`
- `GOVERNANCE.md`
- `ROADMAP.md`
- `BACKLOG.md`
- `VERIFICATION_STRATEGY.md`
- `SOFTWARE_ASSURANCE_STRATEGY.md`
- `RELEASE_STRATEGY.md`
- `ENGINEERING_GUIDANCE.md`
- `KNOWLEDGE_SOURCE_REGISTRATION.md`
- `CHECKLISTS.md`
- `PROMPTS.md`
- `.aikb/engineering-program-manifest.json`

## Source Certified Knowledge

{self._knowledge_table(knowledge)}

## Traceability

Every engineering decision in this program must be read as derived from the Certified Knowledge listed above and the evidence listed in the manifest.
"""

    def _architecture(self, context: dict[str, str], knowledge: list[CertifiedKnowledge]) -> str:
        return f"""# Architecture

## Architectural Basis

The architecture for `{context['program_identifier']}` is derived from Certified Knowledge.

## Repository Architecture

- keep source repositories as evidence sources, not canonical knowledge stores;
- keep engineering program outputs separate from Certified Knowledge;
- preserve explicit boundaries for runtime, verification, assurance, release and governance concerns;
- keep generated artifacts traceable through the program manifest.

## Engineering Rationale

{self._rationale_bullets(knowledge)}

## Traceability

{self._traceability_blocks(knowledge)}
"""

    def _governance(self, context: dict[str, str], knowledge: list[CertifiedKnowledge]) -> str:
        return f"""# Governance

## Governance Position

This program uses Certified Knowledge as authority and treats the generated program as a governed derived artifact.

## Governance Rules

- Certified Knowledge remains canonical.
- Program changes must preserve traceability to Certified Knowledge.
- New evidence must enter through Knowledge Source onboarding and lifecycle flow.
- Publications and program artifacts do not revise Certified Knowledge.

## Supporting Knowledge

{self._knowledge_table(knowledge)}
"""

    def _roadmap(self, context: dict[str, str], knowledge: list[CertifiedKnowledge]) -> str:
        return f"""# Roadmap

## Phase 1: Program Foundation

- establish repository structure;
- register planned Knowledge Sources;
- define governance and traceability expectations.

## Phase 2: Architecture and Verification

- define architecture boundaries from Certified Knowledge;
- establish verification and evidence capture strategy;
- connect assurance decisions to evidence provenance.

## Phase 3: Operationalization

- turn roadmap into backlog;
- execute engineering checklists;
- review gaps against Certified Knowledge.

## Phase 4: Knowledge Feedback

- onboard new repositories as Knowledge Sources;
- extract observations through the governed lifecycle;
- certify reusable knowledge before using it as canonical input.

## Source Rationale

{self._rationale_bullets(knowledge)}
"""

    def _backlog(self, context: dict[str, str], knowledge: list[CertifiedKnowledge]) -> str:
        rows = [
            "| Item | Work | Source Certified Knowledge |",
            "| --- | --- | --- |",
            "| EP-001 | Create initial repository architecture. | "
            + self._ids(knowledge)
            + " |",
            "| EP-002 | Define verification strategy and evidence model. | "
            + self._ids(self._filter(knowledge, "Verification"))
            + " |",
            "| EP-003 | Define software assurance governance. | "
            + self._ids(self._filter(knowledge, "Software Assurance"))
            + " |",
            "| EP-004 | Define release and documentation workflow. | "
            + self._ids(self._filter(knowledge, "Release"))
            + " |",
            "| EP-005 | Review traceability against the program manifest. | "
            + self._ids(knowledge)
            + " |",
        ]
        return "# Backlog\n\n" + "\n".join(rows) + "\n"

    def _strategy(
        self,
        context: dict[str, str],
        knowledge: list[CertifiedKnowledge],
        domain: str,
    ) -> str:
        selected = self._filter(knowledge, domain) or knowledge[:3]
        return f"""# {domain} Strategy

## Strategy Basis

This strategy is derived from Certified Knowledge related to {domain}.

## Engineering Guidance

{self._statement_bullets(selected)}

## Supporting Evidence

{self._evidence_table(selected)}

## Traceability

{self._traceability_blocks(selected)}
"""

    def _guidance(self, context: dict[str, str], knowledge: list[CertifiedKnowledge]) -> str:
        return f"""# Engineering Guidance

## Principles

- derive engineering decisions from Certified Knowledge;
- preserve evidence references for every major program decision;
- separate canonical knowledge from generated program artifacts;
- treat uncertainty as a governance input, not as an implementation detail.

## Certified Knowledge Guidance

{self._statement_bullets(knowledge)}
"""

    def _knowledge_source_registration(
        self,
        context: dict[str, str],
        knowledge: list[CertifiedKnowledge],
    ) -> str:
        sources = sorted({item.knowledge_source for item in knowledge if item.knowledge_source})
        rows = [
            "| Knowledge Source | Registration role |",
            "| --- | --- |",
            *[
                f"| `{source}` | Existing source evidence used by this generated program. |"
                for source in sources
            ],
            "| `future-program-repository` | Register only after a real repository exists and governance approves onboarding. |",
        ]
        return f"""# Knowledge Source Registration

This generated program does not register a repository as a Knowledge Source.

Knowledge Source registration must be performed through the governed onboarding workflow.

## Existing Input Sources

{chr(10).join(rows)}

## Registration Guidance

- create the implementation repository first;
- onboard the repository through `aikb onboard`;
- extract Engineering Observations only after evidence exists;
- do not treat this generated program as source evidence until it is implemented and governed.
"""

    def _checklists(self, context: dict[str, str], knowledge: list[CertifiedKnowledge]) -> str:
        return f"""# Engineering Checklists

## Program Readiness

- [ ] Program manifest exists.
- [ ] Source Certified Knowledge is listed.
- [ ] Generated artifacts reference traceability.
- [ ] Evidence references are preserved.
- [ ] Governance boundary is documented.

## Knowledge Traceability

- [ ] Certified Knowledge identifiers are present.
- [ ] Generalized Knowledge identifiers are present.
- [ ] Knowledge Concept identifiers are present.
- [ ] Knowledge Candidate identifiers are present.
- [ ] Engineering Observation identifiers are present.
- [ ] Source repositories, evidence files and commits are present.

## Source Knowledge

{self._knowledge_table(knowledge)}
"""

    def _prompts(self, context: dict[str, str], knowledge: list[CertifiedKnowledge]) -> str:
        return f"""# Engineering Prompts

These prompts are derived helpers. They are not canonical knowledge.

## Architecture Prompt

Use the Certified Knowledge in `{context['program_identifier']}` to review whether the proposed architecture preserves runtime, verification, assurance, release and governance boundaries.

## Verification Prompt

Use the Certified Knowledge traceability to verify that evidence capture, coverage provenance and runtime adapter decisions remain explicit and reviewable.

## Governance Prompt

Use the program manifest to verify that every generated decision remains traceable to Certified Knowledge and source evidence.

## Source Certified Knowledge

{self._knowledge_table(knowledge)}
"""

    def _manifest(
        self,
        context: dict[str, str],
        knowledge: list[CertifiedKnowledge],
        artifacts: list[str],
    ) -> dict[str, object]:
        return {
            "program": {
                "identifier": context["program_identifier"],
                "name": context["program_name"],
                "type": context["program_type"],
            },
            "generation": {
                "timestamp": context["generated_at"],
                "knowledge_base_version": "repository-snapshot",
                "generator_id": GENERATOR_ID,
                "generator_version": GENERATOR_VERSION,
                "certified_knowledge_version": "repository-snapshot",
            },
            "input_knowledge_sources": sorted(
                {item.knowledge_source for item in knowledge if item.knowledge_source}
            ),
            "generated_artifacts": artifacts,
            "evolution_tracking": {
                "current_knowledge_version": "repository-snapshot",
                "last_synchronization": context["generated_at"],
                "last_evolution_review": None,
                "accepted_recommendations": [],
                "rejected_recommendations": [],
                "pending_recommendations": [],
                "knowledge_drift": "no drift",
            },
            "traceability_references": [
                {
                    "certified_knowledge": item.identifier,
                    "title": item.title,
                    "generalized_knowledge": item.generalized,
                    "concepts": item.concepts,
                    "candidates": item.candidates,
                    "observations": item.observations,
                    "knowledge_source": item.knowledge_source,
                    "evidence": item.evidence_rows,
                    "path": str(item.path.relative_to(self.repository_root)),
                }
                for item in knowledge
            ],
        }

    def _filter(self, knowledge: list[CertifiedKnowledge], term: str) -> list[CertifiedKnowledge]:
        needle = term.lower()
        return [
            item
            for item in knowledge
            if needle in item.domains.lower()
            or needle in item.category.lower()
            or needle in item.title.lower()
            or needle in item.summary.lower()
        ]

    def _knowledge_table(self, knowledge: list[CertifiedKnowledge]) -> str:
        rows = [
            "| Certified Knowledge | Title | Domain | Category |",
            "| --- | --- | --- | --- |",
        ]
        for item in knowledge:
            rows.append(f"| `{item.identifier}` | {item.title} | {item.domains} | {item.category} |")
        return "\n".join(rows)

    def _statement_bullets(self, knowledge: list[CertifiedKnowledge]) -> str:
        return "\n".join(f"- `{item.identifier}`: {item.summary}" for item in knowledge)

    def _rationale_bullets(self, knowledge: list[CertifiedKnowledge]) -> str:
        return "\n".join(
            f"- `{item.identifier}` provides {item.category} guidance for {item.domains}."
            for item in knowledge
        )

    def _evidence_table(self, knowledge: list[CertifiedKnowledge]) -> str:
        rows = [
            "| Certified Knowledge | Observation | Repository | Evidence | Commit |",
            "| --- | --- | --- | --- | --- |",
        ]
        for item in knowledge:
            for evidence in item.evidence_rows:
                rows.append(
                    f"| `{item.identifier}` | `{evidence.get('observation', '')}` | "
                    f"`{evidence.get('repository', '')}` | `{evidence.get('evidence', '')}` | "
                    f"`{evidence.get('commit', '')}` |"
                )
        return "\n".join(rows)

    def _traceability_blocks(self, knowledge: list[CertifiedKnowledge]) -> str:
        blocks = []
        for item in knowledge:
            blocks.append(
                "```text\n"
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
                "repositories, evidence files and commits listed in the manifest\n"
                "```"
            )
        return "\n\n".join(blocks)

    def _ids(self, knowledge: list[CertifiedKnowledge]) -> str:
        if not knowledge:
            return "`review-required`"
        return ", ".join(f"`{item.identifier}`" for item in knowledge)

    def _title(self, value: str) -> str:
        return " ".join(part.capitalize() for part in value.split("-")) + " Engineering Program"

    def _program_identifier(self, program_type: str, name: str) -> str:
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.lower()).strip("-")
        program_slug = program_type.upper().replace("-", "-")
        name_slug = slug.upper().replace("-", "-")
        if slug in {program_type, f"{program_type}-engineering-program"}:
            return f"EP-{program_slug}"
        return f"EP-{program_slug}-{name_slug}"
