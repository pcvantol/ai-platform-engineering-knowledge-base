# Knowledge Classification System

This area defines the canonical classification system for Knowledge Objects in the Knowledge Base.

Classification describes what knowledge is. Lifecycle describes how knowledge evolves. These concepts must remain independent.

The classification system supports engineering navigation, knowledge discovery, AI retrieval, publication generation, traceability, certification, and long-term scalability. It is project independent, technology independent, deterministic, and extensible.

## Classification Principles

- Classification is multidimensional.
- Classification must not duplicate Knowledge Objects.
- Classification must not encode lifecycle progression.
- Lifecycle state and certification state may be used as reference dimensions, but they are not classifications of what knowledge is.
- Technology tags must never become the primary classification.
- A Knowledge Object may have multiple domains, technology tags, evidence classes, or applicability scopes when justified.
- New classification values may be added through governance without changing repository architecture.

## Classification Dimensions

Canonical classification uses the following dimensions:

| Dimension | Purpose | Required |
| --- | --- | --- |
| Engineering domain | Groups knowledge by engineering area. | Yes |
| Knowledge category | Describes the nature of the knowledge. | Yes |
| Abstraction level | Describes project and technology independence. | Yes |
| Applicability | Describes where the knowledge applies. | Yes |
| Technology scope | Describes relevant technology context without becoming primary classification. | Optional |
| Evidence classification | Describes the type of evidence supporting the knowledge. | Yes when evidence exists |
| Lifecycle state | References maturity stage from the lifecycle. | Reference only |
| Certification state | References certification maturity. | Reference only |

These dimensions are designed to classify all future Knowledge Objects without requiring repository redesign.

## Classification Diagram

```text
Knowledge Object
|- Engineering Domain
|- Knowledge Category
|- Abstraction Level
|- Applicability
|- Technology Scope
|- Evidence Classification
|- Lifecycle State (reference only)
`- Certification State (reference only)
```

## Engineering Domains

Engineering domains classify the area of engineering concern.

Canonical domains:

- Architecture
- Platform Engineering
- Verification
- Testing
- Software Assurance
- AI Engineering
- Release Engineering
- Operations
- Security
- Governance
- Observability
- Developer Experience
- Documentation

Domain rules:

- Domains are project independent.
- Domains may be combined when knowledge crosses engineering boundaries.
- Domains must not name specific products, repositories, or implementations.
- New domains may be added when existing domains cannot classify knowledge accurately.

## Knowledge Categories

Knowledge categories classify the nature of the knowledge. Categories are independent from lifecycle state.

Canonical categories:

- Principle
- Pattern
- Architecture
- Practice
- Guideline
- Decision
- Workflow
- Process
- Lifecycle
- Policy
- Reference
- Model
- Capability
- Constraint
- Anti-pattern
- Lesson Learned

Category rules:

- Category describes what the knowledge is, not whether it is mature.
- A Knowledge Object should have one primary category.
- Secondary categories may be used when they improve discovery without obscuring the primary category.
- New categories may be added when existing categories cannot classify knowledge without distortion.

## Abstraction Levels

Abstraction level describes how independent a Knowledge Object is from a specific project, product, or technology.

Canonical abstraction levels:

| Level | Meaning |
| --- | --- |
| Project Specific | Tied to one source project, implementation, or operating context. |
| Reusable | Usable across more than one project but may retain contextual or technology constraints. |
| Technology Independent | Expressed independently of a specific technology whenever practical. |
| Canonical | Certified as authoritative within the Knowledge Base. |

Abstraction relates to knowledge maturity but does not replace lifecycle state.

Typical evolution:

```text
Repository Observation: Project Specific
Knowledge Candidate: Project Specific or Reusable
Knowledge Concept: Reusable
Generalized Knowledge: Reusable or Technology Independent
Certified Knowledge: Canonical
Publication: Derived from Canonical
```

## Applicability Model

Applicability describes where knowledge applies.

Canonical applicability scopes:

| Scope | Meaning |
| --- | --- |
| Single Project | Applies to one known project or system. |
| Multiple Projects | Applies to more than one project or system. |
| AI Platform Engineering Program | Applies across the AI Platform Engineering program. |
| General Engineering | Applies beyond the AI Platform Engineering program. |
| Conditional | Applies only when explicit conditions are met. |

Applicability rules:

- Applicability must identify known scope and known constraints.
- Applicability may expand as evidence accumulates.
- Applicability may narrow when new evidence reveals constraints.
- Applicability must not imply certification.

## Technology Scope

Technology scope describes technology context. It must never become the primary classification.

Canonical technology scopes:

- Generic Engineering
- Programming Language
- Cloud Platform
- Embedded System
- AI System
- Verification System
- Data Platform
- Runtime Platform
- Developer Tooling
- Operational Platform

Technology scope rules:

- Use technology scope to improve discovery and retrieval.
- Avoid product-specific tags unless they are necessary evidence context.
- Preserve product and repository names as evidence references, not primary classification.
- Prefer technology-independent classification whenever practical.

## Evidence Classification

Evidence classification describes the type of evidence that supports a Knowledge Object.

Canonical evidence classes:

- Implementation
- Architecture
- Verification
- Testing
- Experiment
- Operational Experience
- Production Incident
- Design Discussion
- Failure Analysis
- Successful Practice
- Review Finding
- External Reference

Evidence rules:

- Evidence classification supports traceability and certification.
- A Knowledge Object may have multiple evidence classes.
- Evidence strength should improve as knowledge matures.
- Evidence classification does not make evidence canonical; it describes support for knowledge.

## Evidence Strength

Evidence strength describes the confidence contribution of available evidence.

Canonical evidence strength levels:

| Level | Meaning |
| --- | --- |
| Anecdotal | Based on limited observation or discussion. |
| Observed | Supported by one or more repository observations. |
| Repeated | Supported by recurring evidence across contexts. |
| Validated | Reviewed and supported by sufficient evidence for generalization or certification. |
| Contradicted | Evidence conflicts with the current knowledge statement. |

Evidence strength informs review and certification, but it is not the same as certification state.

## Reference Dimensions

Lifecycle state and certification state are reference dimensions.

Lifecycle state answers: how far has this knowledge progressed through the lifecycle?

Certification state answers: what is the current certification maturity?

Classification answers: what is this knowledge?

These dimensions may be used together for navigation and review, but they must not be merged.

## Navigation Principles

The classification system supports browsing and searching without duplicating knowledge.

Users should be able to navigate by:

- engineering domain
- knowledge category
- abstraction level
- applicability
- technology scope
- evidence class
- lifecycle state
- certification state

Navigation views must reference Knowledge Objects rather than copy them. A single Knowledge Object may appear in multiple navigation paths while remaining one canonical object.

## AI Retrieval Principles

The classification system prepares the repository for future AI-assisted retrieval without implementing retrieval infrastructure.

The canonical query and retrieval framework is defined in [../query-retrieval/README.md](../query-retrieval/README.md).

Principles:

- Semantic retrieval should use classification metadata as context, not as a replacement for knowledge content.
- Concept discovery should use domains, categories, relationships, and evidence classes to identify related knowledge.
- Related knowledge discovery should respect directional relationships defined in the Knowledge Model.
- Cross-domain retrieval should preserve domain boundaries while surfacing connections.
- AI retrieval should distinguish canonical knowledge from candidates, observations, and publications.
- Retrieval systems must preserve traceability from results back to Knowledge Objects and originating observations.

This repository does not yet introduce vector databases, embeddings, indexing pipelines, extraction tooling, or AI workflows.

AI-assisted extraction principles are defined in [../extraction/README.md](../extraction/README.md). Classification may support AI assistance, but AI must not certify knowledge.

The canonical AI operations boundaries are defined in [../ai-operations/README.md](../ai-operations/README.md).

## Publication Support

Classification supports publication generation by allowing certified Knowledge Objects to be selected by domain, category, abstraction, applicability, technology scope, and certification state.

Publication generation must reference certified Knowledge Objects. Publications do not become classification authorities.
