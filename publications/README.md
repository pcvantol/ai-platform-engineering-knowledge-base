# Publication Framework

This area defines the canonical framework through which Certified Knowledge becomes human-consumable publications.

The Knowledge Base remains canonical. Publications are derived artifacts. Certified Knowledge remains authoritative.

This framework does not generate publications, import project knowledge, define storage formats, or implement automation.

## Core Principle

```text
Certified Knowledge
->
Publication
```

Never:

```text
Publication
->
Knowledge
```

Publications never become canonical. Knowledge remains canonical.

## Publication Objectives

The publication framework supports creating multiple publications from identical Certified Knowledge while preserving:

- correctness
- traceability
- consistency
- version awareness
- audience fit
- source authority

## Publication Types

Canonical publication types:

- Blueprint
- Architecture Guide
- Engineering Handbook
- Engineering Playbook
- Reference Manual
- Training Material
- Best Practices Guide
- Operational Guide
- Research Paper
- Executive Summary
- Tutorial
- Presentation
- Technical Brief
- Decision Summary
- Agent Reference
- Documentation Package

Publication types are extensible when a new type is needed for a distinct audience, purpose, or consumption model.

## Publication Sets

| Publication Set | Status | Source Certified Knowledge | Publications |
| --- | --- | --- | --- |
| [First Publication Generation Cycle](first-publication-cycle/README.md) | Published | `CK-DJCONNECT-001`, `CK-DJCONNECT-002`, `CK-DJCONNECT-003`, `CK-DJCONNECT-004` | Blueprint, Architecture Reference Guide, Engineering Handbook, Executive Summary |
| [Generation 2 DJConnect Publication Source Set](generation-2-djconnect-source-set/README.md) | Source Set Only | `CK-DJCONNECT-001` through `CK-DJCONNECT-016` | None |

## Publication Object

A Publication Object is the conceptual representation of a derived publication.

Every Publication Object must support:

- publication identity
- publication type
- title
- audience
- scope
- originating Certified Knowledge
- publication version
- publication status
- revision history
- dependencies
- publication owner
- approval state
- source knowledge snapshot

The Publication Object is not a Knowledge Object. It references Certified Knowledge but does not become canonical knowledge.

## Publication Identity

Publication identity is stable across publication revisions.

Identity rules:

- Publication identity identifies the publication, not the Certified Knowledge.
- Publication revisions preserve publication identity.
- A publication may be superseded by another publication while preserving its history.
- Publication identity must not replace Knowledge Object identity.
- Publication references to Certified Knowledge must remain explicit.

## Audiences

Publications may target different audiences.

Canonical audience groups:

- Engineers
- Architects
- Technical Leads
- Management
- Researchers
- Students
- AI Agents
- Documentation Systems
- Auditors
- Operators
- Product Stakeholders

The same Certified Knowledge may generate multiple audience-specific publications.

Audience adaptation may change structure, emphasis, examples, terminology level, and format. It must not change the meaning of the source Certified Knowledge.

## Publication Lifecycle

Canonical publication lifecycle:

```text
Publication Proposal
->
Draft
->
Review
->
Approved
->
Published
->
Revised, Superseded, or Retired
```

Lifecycle states:

| State | Meaning |
| --- | --- |
| Publication Proposal | A publication need has been identified. |
| Draft | Publication content is being prepared from Certified Knowledge. |
| Review | Publication is being checked for source alignment, audience fit, and consistency. |
| Approved | Publication has passed review but may not yet be released. |
| Published | Publication is available for its intended audience. |
| Revised | Publication has been updated while preserving identity. |
| Superseded | Publication has been replaced by a newer publication. |
| Retired | Publication is no longer active but history is preserved. |

Publication lifecycle is separate from Knowledge Certification.

## Publication Workflow

```text
Select Certified Knowledge
->
Define audience and scope
->
Create Publication Object
->
Draft publication
->
Validate source traceability
->
Review for consistency
->
Approve publication
->
Publish or retain as approved artifact
```

Publication workflow must reference Certified Knowledge. It must not create or certify knowledge.

Publication drafts may be prepared through knowledge synthesis when multiple Certified Knowledge Objects must be combined for an audience. The canonical Knowledge Synthesis Framework is defined in [../synthesis/README.md](../synthesis/README.md).

## Traceability

Every publication must reference its source Certified Knowledge and preserve the knowledge lineage.

Canonical publication traceability:

```text
Publication
->
Certified Knowledge
->
Generalized Knowledge
->
Knowledge Concepts
->
Knowledge Candidates
->
Engineering Observations
```

Traceability requirements:

- Each publication must identify its originating Certified Knowledge.
- Publication sections should reference source Certified Knowledge where practical.
- Publications must preserve source version awareness.
- Publications must not obscure the distinction between source knowledge and audience adaptation.
- If source Certified Knowledge is revised, deprecated, superseded, or retired, affected publications must be reviewable.

## Versioning

Publication versions are independent from Knowledge Object revisions.

Versioning rules:

- Publications reflect snapshots of Certified Knowledge.
- Publication version changes do not revise Certified Knowledge.
- Knowledge revisions may trigger publication review.
- Publication revisions must record source Certified Knowledge versions or revision states.
- Superseded publications remain historically traceable.
- Retired publications must preserve revision history and source references.

## Consistency Management

When Certified Knowledge changes, publication owners must determine whether publications:

- remain current
- require revision
- require regeneration
- should be superseded
- should be retired

Consistency review must check:

- source Certified Knowledge changes
- publication scope
- audience interpretation
- diagrams and examples
- terminology
- references
- publication dependencies

Certified Knowledge remains authoritative when conflict exists.

## Publication Relationships

Supported relationships:

| Relationship | Direction | Purpose |
| --- | --- | --- |
| derived from | publication -> Certified Knowledge | Identifies canonical source. |
| references | publication -> Knowledge Object | Identifies source or supporting knowledge. |
| adapts for audience | publication -> audience | Records audience-specific adaptation. |
| depends on | publication -> publication or Knowledge Object | Records required context. |
| supersedes | newer publication -> older publication | Identifies replacement publication. |
| superseded by | older publication -> newer publication | Identifies successor publication. |
| updates | revised publication -> prior publication version | Records publication revision. |

Publication relationships are not certification relationships.

## Publication Governance

Publication governance is separate from Knowledge Certification.

Publication governance covers:

- publication proposal
- publication approval
- publication review
- publication release
- publication revision
- publication superseding
- publication retirement

Publication approval verifies that the publication accurately derives from Certified Knowledge and is suitable for its intended audience. It does not certify knowledge.

## Review Expectations

Publication review should validate:

- source Certified Knowledge references
- traceability
- audience fit
- terminology consistency
- diagram and example consistency
- publication version awareness
- absence of unsupported claims
- distinction between Certified Knowledge and explanatory material

Reviewers may request changes to a publication. Changes to Certified Knowledge must follow the Knowledge Certification Framework.

## AI Support

AI may assist with:

- summarization
- format conversion
- diagram generation
- audience adaptation
- style adaptation
- publication drafting
- consistency checking
- source-reference checking

AI must never modify Certified Knowledge automatically.

AI generates or assists publications only. AI-generated publication content must remain traceable to Certified Knowledge and subject to publication review.

The canonical AI operations boundaries are defined in [../ai-operations/README.md](../ai-operations/README.md).

The canonical query and retrieval framework that supports publication generation is defined in [../query-retrieval/README.md](../query-retrieval/README.md).

The canonical synthesis framework that supports publication drafts derived from multiple Knowledge Objects is defined in [../synthesis/README.md](../synthesis/README.md).

## Publication Retirement

A publication may be retired when:

- its source Certified Knowledge is retired
- it is superseded by a newer publication
- it no longer serves its audience
- its scope is obsolete
- it cannot be updated without misleading readers

Retirement must preserve:

- publication identity
- publication version history
- source Certified Knowledge references
- retirement reason
- successor publication when available
