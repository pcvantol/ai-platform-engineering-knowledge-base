from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
import json
import re

from .generator import Generator, GeneratorDescriptor
from .knowledge import CertifiedKnowledge, CertifiedKnowledgeStore
from .templates import TemplateRenderer


GENERATOR_ID = "project-bootstrap"
GENERATOR_VERSION = "0.1.0"
TEMPLATE_ID = "basic"
SUPPORTED_PROJECT_TYPES = (
    "verification-platform",
    "platform-runtime",
    "client-application",
    "embedded-client",
    "service",
    "library",
    "knowledge-base",
)


@dataclass(frozen=True)
class BootstrapConfig:
    project_type: str
    project_name: str
    output_dir: Path
    force: bool = False


@dataclass(frozen=True)
class BootstrapResult:
    project_name: str
    output_dir: Path
    manifest_path: Path
    certified_knowledge_ids: list[str]


class ProjectBootstrapGenerator(Generator[BootstrapConfig, BootstrapResult]):
    descriptor = GeneratorDescriptor(
        identifier=GENERATOR_ID,
        version=GENERATOR_VERSION,
        supported_project_types=SUPPORTED_PROJECT_TYPES,
    )

    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root
        self.knowledge_store = CertifiedKnowledgeStore(repository_root)
        self.template = TemplateRenderer(repository_root, TEMPLATE_ID)

    def generate(self, config: BootstrapConfig) -> BootstrapResult:
        output_dir = config.output_dir.resolve()
        self._validate_output_dir(output_dir, config.force)
        certified_knowledge = self.knowledge_store.load_all()
        output_dir.mkdir(parents=True, exist_ok=True)

        values = self._template_values(config, certified_knowledge)
        self._write(output_dir / "README.md", self.template.render("README.md.tpl", values))
        self._write(output_dir / "GOVERNANCE.md", self.template.render("GOVERNANCE.md.tpl", values))
        self._write(output_dir / "ROADMAP.md", self.template.render("ROADMAP.md.tpl", values))
        self._write(output_dir / "BACKLOG.md", self.template.render("BACKLOG.md.tpl", values))
        self._write(output_dir / "docs" / "architecture.md", self.template.render("architecture.md.tpl", values))
        self._write(output_dir / ".aikb" / "knowledge-source.md", self.template.render("knowledge-source.md.tpl", values))
        manifest_path = output_dir / ".aikb" / "project-manifest.json"
        self._write(manifest_path, json.dumps(self._manifest(config, certified_knowledge), indent=2) + "\n")

        return BootstrapResult(
            project_name=config.project_name,
            output_dir=output_dir,
            manifest_path=manifest_path,
            certified_knowledge_ids=[record.identifier for record in certified_knowledge],
        )

    def _validate_output_dir(self, output_dir: Path, force: bool) -> None:
        if output_dir.exists() and any(output_dir.iterdir()) and not force:
            raise RuntimeError(
                f"Output directory is not empty: {output_dir}. Use --force to allow writing."
            )

    def _template_values(
        self,
        config: BootstrapConfig,
        certified_knowledge: list[CertifiedKnowledge],
    ) -> dict[str, str]:
        knowledge_ids = ", ".join(record.identifier for record in certified_knowledge)
        knowledge_table = "\n".join(
            f"| `{record.identifier}` | {record.title} | {record.knowledge_category} | {record.engineering_domains} |"
            for record in certified_knowledge
        )
        knowledge_statements = "\n\n".join(
            f"### {record.identifier}: {record.title}\n\n{record.certified_statement}"
            for record in certified_knowledge
        )
        slug = self._slug(config.project_name)
        generated_on = date.today().isoformat()
        return {
            "project_name": config.project_name,
            "project_slug": slug,
            "project_type": config.project_type,
            "generated_on": generated_on,
            "generator_id": GENERATOR_ID,
            "generator_version": GENERATOR_VERSION,
            "template_id": TEMPLATE_ID,
            "template_version": self.template.version,
            "knowledge_ids": knowledge_ids,
            "knowledge_table": knowledge_table,
            "knowledge_statements": knowledge_statements,
        }

    def _manifest(
        self,
        config: BootstrapConfig,
        certified_knowledge: list[CertifiedKnowledge],
    ) -> dict[str, object]:
        generated_on = date.today().isoformat()
        return {
            "project": {
                "identity": config.project_name,
                "slug": self._slug(config.project_name),
                "type": config.project_type,
            },
            "knowledge_base": {
                "version": "repository-snapshot",
                "generated_on": generated_on,
                "source_certified_knowledge": [
                    {
                        "identifier": record.identifier,
                        "title": record.title,
                        "path": str(record.path),
                    }
                    for record in certified_knowledge
                ],
            },
            "generator": {
                "id": GENERATOR_ID,
                "version": GENERATOR_VERSION,
            },
            "template": {
                "id": TEMPLATE_ID,
                "version": self.template.version,
            },
            "knowledge_source_registration": {
                "status": "prepared-not-onboarded",
                "repository_identity": self._slug(config.project_name),
                "traceability_identifier": f"KS-PREP-{self._slug(config.project_name).upper()}",
                "onboarding_required": True,
            },
        }

    def _write(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def _slug(self, value: str) -> str:
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
        return slug or "generated-project"
