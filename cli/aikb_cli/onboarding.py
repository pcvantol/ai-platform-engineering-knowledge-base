from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
import re
import subprocess
from urllib.parse import urlparse


@dataclass(frozen=True)
class OnboardConfig:
    repository: str
    identifier: str | None = None
    output_slug: str | None = None
    force: bool = False


@dataclass(frozen=True)
class OnboardResult:
    identifier: str
    name: str
    profile_path: Path
    extraction_profile_path: Path


@dataclass(frozen=True)
class RepositoryIdentity:
    original: str
    normalized_url: str
    host: str
    owner: str
    name: str
    slug: str


class RepositoryOnboarding:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root
        self.sources_root = repository_root / "sources"

    def onboard(self, config: OnboardConfig) -> OnboardResult:
        identity = self._parse_repository(config.repository)
        identifier = config.identifier or self._identifier(identity)
        output_slug = config.output_slug or identity.slug
        target_dir = self.sources_root / output_slug
        profile_path = target_dir / "README.md"
        extraction_profile_path = target_dir / "extraction-profile.md"

        if target_dir.exists() and any(target_dir.iterdir()) and not config.force:
            raise RuntimeError(
                f"Source profile already exists: {target_dir}. Use --force to overwrite generated onboarding files."
            )

        assessment = self._assess(identity)
        target_dir.mkdir(parents=True, exist_ok=True)
        profile_path.write_text(
            self._profile_markdown(identifier, identity, assessment),
            encoding="utf-8",
        )
        extraction_profile_path.write_text(
            self._extraction_profile_markdown(identifier, identity, assessment),
            encoding="utf-8",
        )
        self._update_sources_index(identifier, identity, output_slug)

        return OnboardResult(
            identifier=identifier,
            name=identity.name,
            profile_path=profile_path,
            extraction_profile_path=extraction_profile_path,
        )

    def _parse_repository(self, repository: str) -> RepositoryIdentity:
        value = repository.strip()
        parse_value = value if "://" in value else f"https://{value}"
        parsed = urlparse(parse_value)
        host = parsed.netloc or "local"
        path = parsed.path.strip("/")
        if path.endswith(".git"):
            path = path[:-4]
        parts = [part for part in path.split("/") if part]
        if len(parts) >= 2:
            owner = parts[-2]
            name = parts[-1]
        elif len(parts) == 1:
            owner = "unknown"
            name = parts[0]
        else:
            owner = "unknown"
            name = self._slug(value)
        normalized_url = f"https://{host}/{owner}/{name}" if host != "local" else value
        slug = self._slug(f"{host}-{owner}-{name}")
        return RepositoryIdentity(
            original=value,
            normalized_url=normalized_url,
            host=host,
            owner=owner,
            name=name,
            slug=slug,
        )

    def _assess(self, identity: RepositoryIdentity) -> dict[str, object]:
        name = identity.name.lower()
        domains = self._domains(name)
        stack = self._technology_stack(name)
        evidence = self._supported_evidence(name)
        accessibility = self._accessibility(identity.normalized_url)
        return {
            "repository_type": self._repository_type(name),
            "description": self._description(identity, domains),
            "engineering_domains": domains,
            "technology_stack": stack,
            "supported_evidence": evidence,
            "excluded_evidence": [
                "secrets",
                "credentials",
                "temporary build artifacts",
                "personal information",
                "private communications without authorization",
                "generated build outputs",
                "raw telemetry without governance",
            ],
            "repository_health": accessibility,
        }

    def _repository_type(self, name: str) -> str:
        if any(token in name for token in ("docs", "documentation", "handbook")):
            return "Documentation repository"
        if any(token in name for token in ("research", "paper", "experiment")):
            return "Research repository"
        if any(token in name for token in ("runtime", "verification", "platform")):
            return "Software engineering repository"
        return "Software repository"

    def _domains(self, name: str) -> list[str]:
        domains = {"Platform Engineering"}
        if any(token in name for token in ("verification", "runtime", "test")):
            domains.update({"Verification", "Testing", "Software Assurance"})
        if any(token in name for token in ("windows", "app", "client", "pi", "embedded")):
            domains.update({"Client Engineering", "Architecture"})
        if any(token in name for token in ("pi", "embedded", "esp")):
            domains.add("Embedded Systems")
        if "release" in name:
            domains.add("Release Engineering")
        return sorted(domains)

    def _technology_stack(self, name: str) -> list[str]:
        stack: set[str] = set()
        if "windows" in name:
            stack.add("Windows")
        if "pi" in name or "raspberry" in name:
            stack.add("Raspberry Pi")
        if "app" in name:
            stack.add("Client application")
        if "runtime" in name:
            stack.add("Runtime")
        return sorted(stack) or ["Unspecified until repository review"]

    def _supported_evidence(self, name: str) -> list[str]:
        evidence = {
            "source code",
            "commit history",
            "architecture documents",
            "engineering decisions",
            "release notes",
        }
        if any(token in name for token in ("verification", "runtime", "test")):
            evidence.update({"verification evidence", "test results", "coverage reports"})
        return sorted(evidence)

    def _description(self, identity: RepositoryIdentity, domains: list[str]) -> str:
        return (
            f"Repository `{identity.owner}/{identity.name}` registered for future knowledge extraction "
            f"across {', '.join(domains)}."
        )

    def _accessibility(self, normalized_url: str) -> str:
        try:
            result = subprocess.run(
                ["git", "ls-remote", "--heads", normalized_url],
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=10,
            )
        except (OSError, subprocess.TimeoutExpired):
            return "Repository accessibility not verified"
        return "Repository reachable by git ls-remote" if result.returncode == 0 else "Repository accessibility not verified"

    def _profile_markdown(
        self,
        identifier: str,
        identity: RepositoryIdentity,
        assessment: dict[str, object],
    ) -> str:
        today = date.today().isoformat()
        domains = ", ".join(assessment["engineering_domains"])
        stack = ", ".join(assessment["technology_stack"])
        evidence = "\n".join(f"- {item}" for item in assessment["supported_evidence"])
        return f"""# {identifier}: {identity.name}

This Knowledge Source profile was generated by `aikb onboard`.

The repository remains autonomous. The Knowledge Base consumes future evidence from the repository only through governed extraction.

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `{identifier}` |
| Repository name | `{identity.name}` |
| Repository owner | `{identity.owner}` |
| Repository URL | {identity.normalized_url} |
| Repository type | {assessment["repository_type"]} |
| Repository description | {assessment["description"]} |
| Engineering domains | {domains} |
| Technology stack | {stack} |
| Maintainers | Repository owner to confirm during governance review |
| Repository lifecycle | Active pending governance confirmation |
| Registration date | {today} |
| Onboarding status | Registered for future extraction |
| Repository health | {assessment["repository_health"]} |
| Extraction profile | [extraction-profile.md](./extraction-profile.md) |

## Supported Evidence

{evidence}

## Onboarding Pipeline

```text
Repository
->
Repository Assessment
->
Knowledge Source Profile
->
Engineering Domain Analysis
->
Evidence Registration
->
Extraction Profile
->
Repository Ready
```

## Traceability

```text
{identifier}
->
{identity.normalized_url}
->
future evidence references
```

No Engineering Observations, Knowledge Candidates, Generalized Knowledge, Certified Knowledge, or Publications are created by this onboarding record.

## Revision History

| Date | Change |
| --- | --- |
| {today} | Initial Knowledge Source profile generated by `aikb onboard`. |
"""

    def _extraction_profile_markdown(
        self,
        identifier: str,
        identity: RepositoryIdentity,
        assessment: dict[str, object],
    ) -> str:
        today = date.today().isoformat()
        supported = "\n".join(f"- {item}" for item in assessment["supported_evidence"])
        excluded = "\n".join(f"- {item}" for item in assessment["excluded_evidence"])
        return f"""# Extraction Profile for {identifier}

This Extraction Profile prepares `{identity.owner}/{identity.name}` for future knowledge extraction.

It does not extract knowledge.

## Included Evidence

{supported}

## Excluded Evidence

{excluded}

## Traceability Policy

Future extraction must preserve:

- Knowledge Source identifier `{identifier}`;
- repository URL `{identity.normalized_url}`;
- evidence location;
- commit, release, tag, document, or event reference when available;
- extraction date;
- extraction rationale.

## Normalization Policy

- Preserve repository terminology in Engineering Observations.
- Do not generalize during observation extraction.
- Do not merge observations during onboarding.
- Preserve repository-specific context until governed promotion.

## AI Assistance Policy

AI may assist with repository summarization, evidence identification, domain suggestions, and extraction preparation.

AI must not invent evidence, modify repositories, create observations without evidence, certify knowledge, or approve onboarding decisions.

## Future Ingestion Readiness

| Readiness Area | Status |
| --- | --- |
| Repository identity | Prepared |
| Knowledge Source identifier | Prepared |
| Supported evidence | Prepared |
| Excluded evidence | Prepared |
| Traceability policy | Prepared |
| Extraction execution | Not started |
| Engineering Observations | Not created |
| Knowledge Candidates | Not created |

## Revision History

| Date | Change |
| --- | --- |
| {today} | Initial Extraction Profile generated by `aikb onboard`. |
"""

    def _update_sources_index(
        self,
        identifier: str,
        identity: RepositoryIdentity,
        output_slug: str,
    ) -> None:
        index_path = self.sources_root / "README.md"
        text = index_path.read_text(encoding="utf-8")
        row = f"| `{identifier}` | [{identity.name}](./{output_slug}/README.md) | Software repository | Registered |\n"
        if f"`{identifier}`" in text:
            return
        marker = "| `KS-DJCONNECT-001` | [DJConnect](./djconnect/README.md) | Multi-repository software platform source | Approved |\n"
        if marker in text:
            text = text.replace(marker, marker + row)
        else:
            text = text.rstrip() + "\n" + row
        index_path.write_text(text, encoding="utf-8")

    def _identifier(self, identity: RepositoryIdentity) -> str:
        owner = self._slug(identity.owner).upper()
        name = self._slug(identity.name).upper()
        return f"KS-{owner}-{name}-001"

    def _slug(self, value: str) -> str:
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
        return slug or "repository"
