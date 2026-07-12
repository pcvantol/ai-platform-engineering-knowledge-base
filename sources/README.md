# Knowledge Source Integration Framework

This area defines the canonical framework that allows external software projects and engineering repositories to become Knowledge Sources for the Knowledge Base.

Projects remain independent. Projects never become canonical. The Knowledge Base remains the canonical destination.

This framework does not connect repositories, extract knowledge, implement connectors, or define automation.

The canonical Knowledge Source Onboarding Framework is defined in [../source-onboarding/README.md](../source-onboarding/README.md). A repository becomes a Knowledge Source only after successful onboarding and approval.

The canonical Multi-Project Knowledge Integration Framework is defined in [../multi-project-integration/README.md](../multi-project-integration/README.md). It governs how multiple registered Knowledge Sources may contribute to shared concepts, generalized knowledge, Certified Knowledge, and publications without making any source canonical.

## Core Principle

Projects produce engineering work.

The Knowledge Base consumes engineering knowledge.

Knowledge flows in one direction only:

```text
Repository
->
Engineering Observation
->
Knowledge Candidate
->
Knowledge Base
```

Repositories provide evidence. They do not become authoritative knowledge sources.

## Read-Only Knowledge Source Contract

A registered Knowledge Source is an autonomous, externally owned and authoritative provider of engineering evidence. It is read-only for every Knowledge Base operation.

The Knowledge Base must never, during onboarding, extraction, classification, review, generalization, certification, retrieval, validation, improvement, or status reporting:

- modify source files or documentation;
- change branches, versions, releases, or repository configuration;
- rewrite history, create commits, push, or create pull requests; or
- require a source repository to adopt Knowledge Base structure, tooling, or workflows.

Repository changes are outside the Knowledge Source contract. They require a separately invoked engineering action and explicit engineer intent. The Knowledge Base records resulting repository changes as future evidence; it does not make them implicitly.

## Knowledge Source Model

A Knowledge Source is a registered external project, repository, or engineering source that may provide evidence for the Knowledge Base.

Knowledge Sources may include:

- software repositories
- architecture repositories
- verification repositories
- research repositories
- operational repositories
- documentation repositories
- release repositories
- incident repositories
- experiment repositories

Future repository types may be added without redesign when they provide observable engineering work and traceable evidence.

## Registered Knowledge Sources

Current registered Knowledge Sources:

| Identifier | Name | Source type | Status |
| --- | --- | --- | --- |
| `KS-DJCONNECT-001` | [DJConnect](./djconnect/README.md) | Multi-repository software platform source | Approved |
| `KS-GITHUB-DJCONNECT-001` | [djconnect](./local-github-djconnect/README.md) | Software repository | Registered |
| `KS-PCVANTOL-DJCONNECT-WINDOWS-001` | [djconnect-windows](./github-com-pcvantol-djconnect-windows/README.md) | Software repository | Registered |

## Source Registration

Registration describes a source so it can be evaluated and used for traceable extraction.

Registration must document:

- repository identity
- repository ownership
- repository purpose
- repository type
- technology stack
- engineering domains
- extraction policy
- traceability information
- supported evidence types
- access and visibility constraints
- lifecycle status
- maintainers or source contacts

Registration must not require repository modification.

The Knowledge Base adapts extraction to the source. The source does not adapt to the Knowledge Base.

## Source Independence

Knowledge Sources remain autonomous.

Rules:

- The Knowledge Base must not require sources to adopt specific implementation patterns.
- The Knowledge Base must not require source repository restructuring.
- The Knowledge Base must not write canonical knowledge back into sources.
- The Knowledge Base must not modify source repositories during knowledge operations.
- Extraction must preserve source context without making source context canonical.
- Source ownership remains outside the Knowledge Base.
- Source history must not be changed by integration.

## Source Metadata Model

Canonical source metadata:

| Metadata | Purpose |
| --- | --- |
| Identifier | Stable Knowledge Source identity inside the Knowledge Base. |
| Name | Human-readable source name. |
| Description | Summary of the source and its engineering relevance. |
| Repository URL | Location or reference for the repository or source. |
| Repository type | Source type, such as software, architecture, verification, research, operations, or documentation. |
| Technology stack | Technologies used by the source, treated as source context. |
| Primary engineering domains | Engineering domains represented by the source. |
| Maintainers | Source owners or contacts. |
| Lifecycle status | Current source status, such as active, archived, deprecated, or retired. |
| Extraction configuration | Conceptual extraction constraints and policies. |
| Supported evidence | Evidence types available from the source. |
| Knowledge maturity | Expected maturity of evidence from this source. |
| Traceability anchors | Commit, version, release, document, or event identifiers available for traceability. |

Metadata describes the source. It does not certify knowledge extracted from the source.

## Supported Evidence Model

Supported evidence types include:

- source code
- architecture documents
- verification evidence
- coverage reports
- qualification reports
- release notes
- engineering decisions
- management summaries
- issue discussions
- commit history
- design discussions
- test results
- production incidents
- operational metrics
- experiment results
- postmortems

Future evidence types may be added when they can be traced and reviewed.

Evidence remains evidence. It does not become canonical knowledge until it progresses through extraction, generalization, and certification.

## Extraction Boundaries

The Knowledge Base may consume:

- Engineering Observations
- architecture rationale
- verification evidence
- engineering decisions
- lessons learned
- implementation experience
- operational evidence
- release evidence
- failure analysis
- design trade-offs

The Knowledge Base must never automatically consume:

- secrets
- credentials
- temporary build artifacts
- personal information
- unverified assumptions
- private communications without authorization
- generated build outputs
- raw telemetry without governance
- source content outside the extraction policy

Extraction boundaries protect source autonomy, privacy, security, and knowledge quality.

## Multi-Repository Knowledge

Reusable knowledge may originate from multiple Knowledge Sources.

Examples of source families may include:

- DJConnect
- Verification Runtime
- future AI platforms
- general engineering repositories
- future software systems

The same Knowledge Concept may reference observations from multiple repositories. Multiple independent observations may strengthen evidence without making any source canonical.

Multi-repository rules:

- Preserve each source identity.
- Preserve each observation lineage.
- Merge candidates only when they express the same reusable implication.
- Merge concepts only when they describe the same engineering pattern.
- Preserve conflicting evidence for review.
- Treat source diversity as evidence strength, not authority.

Cross-repository consolidation, conflict representation, shared certification expectations, and stewardship responsibilities are governed by the Multi-Project Knowledge Integration Framework.

## Traceability Model

Complete traceability must be preserved.

Canonical source traceability:

```text
Knowledge
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

Traceability requirements:

- Every observation must identify its Knowledge Source.
- Every Knowledge Source must preserve source identity and traceability anchors.
- Every candidate must link back to observations.
- Every certified item must reconstruct the full chain back to source evidence.
- No generalization step may remove lineage.
- Source evidence must remain distinguishable from Knowledge Base interpretation.

## AI-Assisted Source Integration

AI may assist with:

- repository scanning
- observation discovery
- candidate suggestion
- duplicate detection
- relationship suggestion
- cross-repository analysis
- evidence summarization
- source metadata suggestions

AI must never:

- modify repositories
- change source history
- invent source evidence
- invent repository ownership
- invent traceability
- bypass extraction boundaries
- certify knowledge
- register sources without governed review

AI source analysis produces proposals only. Human-governed review remains authoritative.

## Scalability Principles

The framework must support:

- dozens of repositories
- hundreds of repositories
- thousands of Knowledge Objects
- multiple organizations
- future repository technologies
- future evidence types

Scalability rules:

- Source identity must be stable.
- Source metadata must be extensible.
- Evidence types must be extensible.
- Extraction policies must be source-specific.
- Knowledge Objects must remain independent from source repository structure.
- Multi-source traceability must remain reconstructable.

## Integration With Existing Frameworks

Knowledge Source integration must conform to:

- [Knowledge Lifecycle](../lifecycle/README.md)
- [Knowledge Model](../model/README.md)
- [Knowledge Classification System](../classification/README.md)
- [Knowledge Source Onboarding Framework](../source-onboarding/README.md)
- [Knowledge Extraction Framework](../extraction/README.md)
- [Knowledge Certification Framework](../certification/README.md)
- [Publication Framework](../publications/README.md)
- [AI Knowledge Operations Framework](../ai-operations/README.md)

Knowledge Source integration provides governed source context for extraction. It does not replace extraction, certification, or publication governance.

The canonical ingestion pipeline for transforming registered Knowledge Sources into Knowledge Candidate proposals is defined in [../ingestion/README.md](../ingestion/README.md).
