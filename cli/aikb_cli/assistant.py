from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import textwrap


@dataclass(frozen=True)
class AskConfig:
    question: str
    limit: int = 4
    show_all_evidence: bool = False


@dataclass(frozen=True)
class CertifiedKnowledge:
    identifier: str
    title: str
    summary: str
    category: str
    domains: str
    confidence: str
    knowledge_source: str
    generalized: str
    concepts: list[str]
    candidates: list[str]
    observations: list[str]
    evidence_rows: list[dict[str, str]]
    relationships: list[dict[str, str]]
    path: Path


@dataclass(frozen=True)
class RetrievalMatch:
    knowledge: CertifiedKnowledge
    score: int
    reasons: list[str]


class EngineeringAssistant:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root
        self.certified_root = repository_root / "certified"

    def answer(self, config: AskConfig) -> str:
        knowledge = self._load_certified_knowledge()
        if not knowledge:
            return self._no_knowledge_answer(config.question)
        matches = self._retrieve(knowledge, config.question, config.limit)
        if not matches:
            return self._no_match_answer(config.question, knowledge)
        return self._render_answer(config, matches)

    def _load_certified_knowledge(self) -> list[CertifiedKnowledge]:
        items: list[CertifiedKnowledge] = []
        for path in sorted(self.certified_root.glob("*/CK-*.md")):
            text = path.read_text(encoding="utf-8")
            metadata = self._metadata(text)
            if metadata.get("Certification status") != "Certified":
                continue
            items.append(
                self._knowledge_from_text(path, text, metadata)
            )
        return items

    def _knowledge_from_text(
        self,
        path: Path,
        text: str,
        metadata: dict[str, str],
    ) -> CertifiedKnowledge:
        source = metadata.get("Knowledge sources", "").strip("`")
        if not source:
            source = self._first_match(text, r"\b(KS-[A-Z0-9-]+)\b")
        return CertifiedKnowledge(
            identifier=metadata.get("Identifier", path.stem).strip("`"),
            title=self._heading_title(text),
            summary=self._section(text, "Certified Statement"),
            category=metadata.get("Knowledge category", ""),
            domains=metadata.get("Engineering domains", ""),
            confidence=metadata.get("Confidence", "Medium"),
            knowledge_source=source,
            generalized=metadata.get("Originating Generalized Knowledge", "").strip("`"),
            concepts=self._unique(re.findall(r"\b(KCN-[A-Z0-9-]+)\b", text)),
            candidates=self._unique(re.findall(r"\b(KC-[A-Z0-9-]+)\b", text)),
            observations=self._unique(re.findall(r"\b(EO-[A-Z0-9-]+)\b", text)),
            evidence_rows=self._evidence_rows(text),
            relationships=self._relationship_rows(text),
            path=path,
        )

    def _retrieve(
        self,
        knowledge: list[CertifiedKnowledge],
        question: str,
        limit: int,
    ) -> list[RetrievalMatch]:
        query_terms = self._terms(question)
        matches: list[RetrievalMatch] = []
        for item in knowledge:
            score, reasons = self._score(item, query_terms, question)
            if score > 0:
                matches.append(RetrievalMatch(item, score, reasons))
        matches.sort(key=lambda match: (-match.score, match.knowledge.identifier))
        return matches[: max(1, limit)]

    def _score(
        self,
        item: CertifiedKnowledge,
        query_terms: set[str],
        question: str,
    ) -> tuple[int, list[str]]:
        searchable = " ".join(
            [
                item.identifier,
                item.title,
                item.summary,
                item.category,
                item.domains,
                item.knowledge_source,
                item.generalized,
                " ".join(item.concepts),
                " ".join(item.candidates),
                " ".join(item.observations),
                " ".join(row.get("evidence", "") for row in item.evidence_rows),
            ]
        )
        haystack_terms = self._terms(searchable)
        overlap = sorted(query_terms & haystack_terms)
        score = len(overlap)
        reasons: list[str] = []
        lower_question = question.lower()

        if item.identifier.lower() in lower_question:
            score += 30
            reasons.append("knowledge identifier matched")
        if self._phrase_matches(item.title, lower_question):
            score += 12
            reasons.append("title matched")
        if self._field_overlap(item.domains, query_terms):
            score += 8
            reasons.append("engineering domain matched")
        if self._field_overlap(item.category, query_terms):
            score += 6
            reasons.append("knowledge category matched")
        if self._field_overlap(item.summary, query_terms):
            score += 4
            reasons.append("certified statement matched")
        if any(self._field_overlap(row.get("evidence", ""), query_terms) for row in item.evidence_rows):
            score += 3
            reasons.append("supporting evidence matched")
        if overlap:
            reasons.append("term overlap: " + ", ".join(overlap[:8]))
        return score, reasons

    def _render_answer(self, config: AskConfig, matches: list[RetrievalMatch]) -> str:
        primary = matches[0].knowledge
        related = [match.knowledge for match in matches[1:]]
        lines = [
            "# Knowledge-Driven Engineering Answer",
            "",
            f"Question: {config.question}",
            "",
            "## Engineering Conclusion",
            "",
            self._conclusion(config.question, matches),
            "",
            "## Supporting Rationale",
            "",
            self._rationale(matches),
            "",
            "## Supporting Certified Knowledge",
            "",
            self._knowledge_table(matches),
            "",
            "## Supporting Evidence",
            "",
            self._evidence_table(matches, config.show_all_evidence),
            "",
            "## Related Knowledge",
            "",
            self._related_knowledge(primary, related),
            "",
            "## Knowledge Confidence",
            "",
            self._confidence(matches),
            "",
            "## Traceability References",
            "",
            self._traceability(matches),
            "",
            "## Uncertainty",
            "",
            self._uncertainty(matches),
        ]
        return "\n".join(lines).rstrip() + "\n"

    def _conclusion(self, question: str, matches: list[RetrievalMatch]) -> str:
        titles = [match.knowledge.title for match in matches]
        if len(titles) == 1:
            return (
                f"Use `{titles[0]}` as the primary canonical basis for this engineering decision. "
                "The answer is constrained to Certified Knowledge and its supporting evidence."
            )
        joined = ", ".join(f"`{title}`" for title in titles)
        return (
            f"Use the combined Certified Knowledge around {joined}. "
            "The decision should be grounded in the relationships and evidence recorded for these items, "
            "not in external documentation or unstated assumptions."
        )

    def _rationale(self, matches: list[RetrievalMatch]) -> str:
        bullets = []
        for match in matches:
            item = match.knowledge
            reason_text = "; ".join(match.reasons) if match.reasons else "selected by canonical metadata"
            bullets.append(
                f"- `{item.identifier}` supports the answer because {reason_text}. "
                f"It traces to `{item.generalized}` and {len(item.observations)} Engineering Observation(s)."
            )
        return "\n".join(bullets)

    def _knowledge_table(self, matches: list[RetrievalMatch]) -> str:
        rows = [
            "| Certified Knowledge | Title | Domain | Category | Source | Match rationale |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for match in matches:
            item = match.knowledge
            rows.append(
                "| `{identifier}` | {title} | {domain} | {category} | `{source}` | {reasons} |".format(
                    identifier=item.identifier,
                    title=item.title,
                    domain=item.domains,
                    category=item.category,
                    source=item.knowledge_source,
                    reasons="; ".join(match.reasons[:3]) or "canonical match",
                )
            )
        return "\n".join(rows)

    def _evidence_table(self, matches: list[RetrievalMatch], show_all: bool) -> str:
        rows = [
            "| Certified Knowledge | Observation | Repository | Evidence | Commit |",
            "| --- | --- | --- | --- | --- |",
        ]
        count = 0
        for match in matches:
            for evidence in match.knowledge.evidence_rows:
                rows.append(
                    "| `{ck}` | `{observation}` | `{repository}` | `{evidence}` | `{commit}` |".format(
                        ck=match.knowledge.identifier,
                        observation=evidence.get("observation", ""),
                        repository=evidence.get("repository", ""),
                        evidence=evidence.get("evidence", ""),
                        commit=evidence.get("commit", ""),
                    )
                )
                count += 1
                if not show_all and count >= 8:
                    rows.append("| More evidence available | Use `--all-evidence` |  |  |  |")
                    return "\n".join(rows)
        return "\n".join(rows)

    def _related_knowledge(
        self,
        primary: CertifiedKnowledge,
        related: list[CertifiedKnowledge],
    ) -> str:
        rows = [
            f"- Primary: `{primary.identifier}` -> `{primary.generalized}` -> "
            + ", ".join(f"`{concept}`" for concept in primary.concepts)
        ]
        for item in related:
            rows.append(f"- Related: `{item.identifier}` shares query relevance through {item.domains} / {item.category}.")
        return "\n".join(rows)

    def _confidence(self, matches: list[RetrievalMatch]) -> str:
        values = ", ".join(
            f"`{match.knowledge.identifier}`: {match.knowledge.confidence}" for match in matches
        )
        return (
            f"Knowledge confidence: {values}. "
            "The assistant confidence is bounded by the retrieved Certified Knowledge and recorded evidence."
        )

    def _traceability(self, matches: list[RetrievalMatch]) -> str:
        blocks = []
        for match in matches:
            item = match.knowledge
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
                "repositories, evidence files and commits listed above\n"
                "```"
            )
        return "\n\n".join(blocks)

    def _uncertainty(self, matches: list[RetrievalMatch]) -> str:
        if len(matches) == 1:
            return (
                "Only one Certified Knowledge item matched strongly. Treat this as a focused answer, "
                "not a complete architecture review."
            )
        return (
            "The answer is limited to existing Certified Knowledge. If the question requires areas not covered "
            "by the listed items, create or certify additional knowledge before treating the gap as settled."
        )

    def _no_knowledge_answer(self, question: str) -> str:
        return textwrap.dedent(
            f"""\
            # Knowledge-Driven Engineering Answer

            Question: {question}

            No Certified Knowledge is available. The assistant cannot answer canonically without Certified Knowledge.
            """
        )

    def _no_match_answer(self, question: str, knowledge: list[CertifiedKnowledge]) -> str:
        available = ", ".join(f"`{item.identifier}`" for item in knowledge)
        return textwrap.dedent(
            f"""\
            # Knowledge-Driven Engineering Answer

            Question: {question}

            No relevant Certified Knowledge matched deterministically.

            Available Certified Knowledge: {available}

            Uncertainty: the assistant did not search markdown documentation or external sources. Certify additional knowledge or ask using canonical terminology if this question should be answerable.
            """
        )

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

    def _section(self, text: str, heading: str) -> str:
        pattern = rf"^## {re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)"
        match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
        if not match:
            return ""
        return " ".join(line.strip() for line in match.group("body").splitlines() if line.strip())

    def _evidence_rows(self, text: str) -> list[dict[str, str]]:
        rows: list[dict[str, str]] = []
        for line in text.splitlines():
            if not line.startswith("| `EO-"):
                continue
            parts = [part.strip().strip("`") for part in line.strip().strip("|").split("|")]
            if len(parts) == 4:
                rows.append(
                    {
                        "observation": parts[0],
                        "repository": parts[1],
                        "evidence": parts[2],
                        "commit": parts[3],
                    }
                )
        return rows

    def _relationship_rows(self, text: str) -> list[dict[str, str]]:
        rows: list[dict[str, str]] = []
        in_table = False
        for line in text.splitlines():
            if line == "| Relationship | Target | Direction | Rationale |":
                in_table = True
                continue
            if in_table and not line.startswith("|"):
                break
            if not in_table or line.startswith("| ---"):
                continue
            parts = [part.strip().strip("`") for part in line.strip().strip("|").split("|")]
            if len(parts) == 4:
                rows.append(
                    {
                        "relationship": parts[0],
                        "target": parts[1],
                        "direction": parts[2],
                        "rationale": parts[3],
                    }
                )
        return rows

    def _heading_title(self, text: str) -> str:
        for line in text.splitlines():
            if line.startswith("# "):
                return line.split(": ", 1)[-1]
        return ""

    def _first_match(self, text: str, pattern: str) -> str:
        match = re.search(pattern, text)
        return match.group(1) if match else ""

    def _terms(self, value: str) -> set[str]:
        stop_words = {
            "a",
            "an",
            "and",
            "as",
            "be",
            "for",
            "from",
            "how",
            "i",
            "in",
            "is",
            "of",
            "or",
            "should",
            "the",
            "to",
            "use",
            "what",
            "with",
        }
        return {
            term
            for term in re.findall(r"[a-z0-9]+", value.lower())
            if len(term) > 2 and term not in stop_words
        }

    def _field_overlap(self, field: str, query_terms: set[str]) -> bool:
        return bool(self._terms(field) & query_terms)

    def _phrase_matches(self, title: str, lower_question: str) -> bool:
        title_terms = self._terms(title)
        if not title_terms:
            return False
        return len(title_terms & self._terms(lower_question)) >= max(1, min(2, len(title_terms)))

    def _unique(self, values: list[str]) -> list[str]:
        unique: list[str] = []
        for value in values:
            if value not in unique:
                unique.append(value)
        return unique
