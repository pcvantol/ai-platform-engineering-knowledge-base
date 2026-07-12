from __future__ import annotations

from pathlib import Path
import string


class TemplateRenderer:
    def __init__(self, repository_root: Path, template_id: str) -> None:
        self.repository_root = repository_root
        self.template_id = template_id
        self.template_root = repository_root / "templates" / "project-bootstrap" / template_id
        if not self.template_root.exists():
            raise RuntimeError(f"Template not found: {template_id}")

    @property
    def version(self) -> str:
        version_file = self.template_root / "VERSION"
        return version_file.read_text(encoding="utf-8").strip()

    def render(self, template_name: str, values: dict[str, str]) -> str:
        path = self.template_root / template_name
        text = path.read_text(encoding="utf-8")
        return string.Template(text).safe_substitute(values)
