from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


FIELD_RE = re.compile(r"^\| ([^|]+) \| ([^|]+) \|$")


@dataclass(frozen=True)
class CertifiedKnowledge:
    identifier: str
    title: str
    path: Path
    knowledge_category: str
    engineering_domains: str
    certified_statement: str


class CertifiedKnowledgeStore:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root
        self.certified_root = repository_root / "certified"

    def load_all(self) -> list[CertifiedKnowledge]:
        records = [
            self._load_record(path)
            for path in sorted(self.certified_root.glob("**/CK-*.md"))
        ]
        if not records:
            raise RuntimeError("No Certified Knowledge records found.")
        return records

    def _load_record(self, path: Path) -> CertifiedKnowledge:
        text = path.read_text(encoding="utf-8")
        title_line = next(
            (line for line in text.splitlines() if line.startswith("# ")),
            f"# {path.stem}",
        )
        title = title_line[2:].split(": ", 1)[-1].strip()
        metadata = self._metadata(text)
        statement = self._section_text(text, "Certified Statement")
        return CertifiedKnowledge(
            identifier=metadata.get("Identifier", path.stem).strip("`"),
            title=title,
            path=path.relative_to(self.repository_root),
            knowledge_category=metadata.get("Knowledge category", "Unclassified"),
            engineering_domains=metadata.get("Engineering domains", "Unclassified"),
            certified_statement=statement,
        )

    def _metadata(self, text: str) -> dict[str, str]:
        values: dict[str, str] = {}
        in_metadata = False
        for line in text.splitlines():
            if line == "## Metadata":
                in_metadata = True
                continue
            if in_metadata and line.startswith("## "):
                break
            if not in_metadata or not line.startswith("| "):
                continue
            match = FIELD_RE.match(line)
            if not match:
                continue
            key = match.group(1).strip()
            value = match.group(2).strip()
            if key != "---":
                values[key] = value
        return values

    def _section_text(self, text: str, heading: str) -> str:
        marker = f"## {heading}"
        lines = text.splitlines()
        try:
            start = lines.index(marker) + 1
        except ValueError:
            return ""
        collected: list[str] = []
        for line in lines[start:]:
            if line.startswith("## "):
                break
            if line.strip():
                collected.append(line.strip())
        return " ".join(collected)
