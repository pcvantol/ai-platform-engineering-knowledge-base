# Knowledge Model

This area defines the canonical conceptual model for engineering knowledge in the Knowledge Base.

The model is conceptual. It does not define implementation formats, file formats, schemas, extraction tooling, or AI workflows. Future implementation formats must conform to this model.

The canonical classification dimensions used by Knowledge Objects are defined in [../classification/README.md](../classification/README.md).

## Model Principles

- Every knowledge item is represented as a Knowledge Object.
- Knowledge identity remains stable across revisions.
- Lifecycle state and knowledge category are separate concepts.
- Relationships are directional and traceable.
- Publications reference Knowledge Objects; Knowledge Objects do not depend on publications.
- The model must remain project independent, technology independent, deterministic, traceable, and extensible.

## Knowledge Object

A Knowledge Object is the canonical conceptual representation of a knowledge item stored in this repository.

Every Knowledge Object must support:

- unique identifier
- title
- description
- lifecycle state
- knowledge category
- engineering domain
- abstraction level
- originating observations
- related concepts
- dependencies
- references
- certification state
- publication relationships
- revision history

The same Knowledge Object model applies across lifecycle stages. The expected completeness of the object increases as knowledge matures.

## Knowledge Identity

Knowledge identity is stable and independent from revision state.

A Knowledge Object has one persistent identifier that remains the same when the object is revised, clarified, reclassified, promoted through lifecycle stages, or certified.

Identity rules:

- The identifier represents the knowledge item, not a file, document, publication, or implementation artifact.
- Revisions must preserve the identifier.
- Certification updates must preserve the identifier.
- Publication references must point to Knowledge Object identity, not copied publication text.
- If knowledge is split, each new Knowledge Object receives a new identifier and references the source object.
- If knowledge is merged, the resulting Knowledge Object receives either a new identifier or a designated surviving identifier, and all merged source identities remain preserved in history.

## Metadata Model

Metadata describes the state, classification, governance, and traceability of a Knowledge Object.

Mandatory metadata:

| Metadata | Purpose |
| --- | --- |
| Identifier | Stable identity of the Knowledge Object. |
| Title | Human-readable name. |
| Description | Concise statement of the knowledge item. |
| Owner | Accountable steward or ownership group. |
| Lifecycle state | Current lifecycle stage. |
| Knowledge category | Nature of the knowledge, independent from lifecycle state. |
| Engineering domain | Domain or domains where the knowledge applies. |
| Abstraction level | Degree of project and technology independence. |
| Creation date | Date the object was first created. |
| Revision date | Date of most recent revision. |
| Revision history | Record of material changes. |
| Traceability references | Links to predecessor lifecycle items or originating observations. |
| Certification status | Certification maturity of the object. |
| Review status | Current review state. |

Optional metadata:

| Metadata | Purpose |
| --- | --- |
| Confidence | Stated confidence in the knowledge before or after certification. |
| Source repositories | Repositories that provided evidence. |
| Source evidence | Specific evidence supporting the object. |
| Applicable technologies | Technologies where the knowledge is known to apply. |
| Excluded technologies | Technologies or contexts where the knowledge is known not to apply. |
| Dependencies | Other Knowledge Objects required to understand or apply this object. |
| Conflicts | Knowledge Objects that conflict or require reconciliation. |
| Supersession | Knowledge Objects superseded by or superseding this object. |
| Publication eligibility | Whether the object may be used as a publication source. |
| Publication references | Publications that reference the object. |

Optional metadata may become mandatory for a specific lifecycle state through governance rules, but the conceptual model does not define implementation formats.

## Relationship Model

Knowledge relationships are directional and traceable.

Core lifecycle relationships:

```text
Repository Observation
->
Knowledge Candidate
->
Knowledge Concept
->
Generalized Knowledge
->
Certified Knowledge
```

Supported relationships:

| Relationship | Direction | Purpose |
| --- | --- | --- |
| originates from | later object -> earlier evidence or object | Preserves source lineage. |
| promotes to | earlier object -> later lifecycle object | Records lifecycle progression. |
| supports | supporting object -> supported object | Shows supporting knowledge. |
| conflicts with | object -> object | Identifies competing or inconsistent knowledge. |
| supersedes | newer object -> older object | Identifies replacement knowledge. |
| superseded by | older object -> newer object | Identifies successor knowledge. |
| parent of | broader object -> narrower object | Represents hierarchy. |
| child of | narrower object -> broader object | Represents hierarchy. |
| depends on | dependent object -> required object | Records required knowledge dependency. |
| example of | implementation example -> Knowledge Object | Links non-canonical examples to knowledge. |
| referenced by publication | Knowledge Object -> publication | Records derived publication usage. |
| publication source | publication -> certified Knowledge Object | Links publications back to canonical sources. |
| overlaps with | object -> object | Identifies related knowledge that may converge through review. |
| duplicates | object -> object | Identifies apparent duplication requiring governed review. |
| complements | object -> object | Identifies related knowledge that works together without merging. |
| alternative to | object -> object | Identifies different valid approaches under different constraints. |
| constrained by | object -> object | Identifies applicability constraints introduced by another object or source context. |

Relationships must preserve enough context to reconstruct why the relationship exists.

Cross-repository relationship governance is defined in the [Multi-Project Knowledge Integration Framework](../multi-project-integration/README.md).

## Knowledge Domains

Engineering domains group knowledge by area of applicability.

Initial domains are defined canonically by the Knowledge Classification System. The current domain set includes:

- Architecture
- Verification
- Testing
- Platform Engineering
- AI Engineering
- Software Assurance
- Release Engineering
- Operations
- Security
- Governance
- Observability
- Developer Experience
- Documentation

Domains are extensible. New domains may be added without redesigning the model when a knowledge area cannot be accurately classified by existing domains.

Knowledge Objects may belong to multiple domains when the knowledge genuinely crosses domain boundaries.

## Knowledge Categories

Knowledge categories describe the nature of knowledge. Categories are independent from lifecycle state.

Initial categories are defined canonically by the Knowledge Classification System. The current category set includes:

- Principle
- Pattern
- Architecture
- Guideline
- Practice
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

Categories are extensible. A new category may be added when existing categories cannot describe the nature of the knowledge without distortion.

## Abstraction Model

Abstraction level describes how independent a Knowledge Object is from a specific project, product, or technology.

Canonical abstraction levels are defined by the Knowledge Classification System:

| Level | Meaning |
| --- | --- |
| Project Specific | Tied to a source project or implementation context. |
| Reusable | Usable beyond the original source project but may retain technology or context constraints. |
| Technology Independent | Expressed independently of a specific technology whenever practical. |
| Canonical | Certified as authoritative within the Knowledge Base. |

Abstraction evolves through the lifecycle:

- Repository observations are usually project-specific.
- Knowledge candidates identify potential reuse.
- Knowledge concepts normalize reusable patterns.
- Generalized knowledge removes project-specific details and reduces technology dependency.
- Certified knowledge becomes canonical.
- Publications derive from certified knowledge but do not change abstraction level or authority.

## Certification Model

Certification represents the maturity and authority of knowledge, not implementation quality.

Certification status describes whether a Knowledge Object is ready to serve as canonical knowledge.

The canonical certification governance process is defined in [../certification/README.md](../certification/README.md).

Canonical certification statuses:

- Candidate
- Under Review
- Certified
- Rejected
- Returned for Refinement
- Deprecated
- Superseded
- Retired

Only certified Knowledge Objects in the Certified Knowledge lifecycle stage are canonical.

Publication eligibility depends on certification. Only certified knowledge may serve as the source for publications.

## Versioning Model

Knowledge evolves through revisions while preserving identity and traceability.

Supported evolution patterns:

- Revision: a Knowledge Object changes while retaining identity.
- Supersession: newer knowledge replaces older knowledge while preserving the older object.
- Merge: multiple Knowledge Objects combine into one object or one designated surviving object.
- Split: one Knowledge Object separates into multiple new objects.
- Retirement: obsolete knowledge is removed from active use without deleting history.

Versioning rules:

- Revisions preserve Knowledge Object identity.
- Material changes must be recorded in revision history.
- Superseded knowledge must remain traceable.
- Merged source objects must remain traceable from the resulting object.
- Split successor objects must reference the source object.
- Retired knowledge remains part of the historical knowledge record.

## Publications

Publications reference Knowledge Objects. Knowledge Objects never depend on publications.

Multiple publications may reference identical certified knowledge. A publication may organize, explain, or adapt certified knowledge for an audience, but it does not become canonical.

When certified knowledge changes, publications that reference it may require review or update. The certified Knowledge Object remains authoritative.

The canonical Publication Framework is defined in [../publications/README.md](../publications/README.md).

The canonical query and retrieval framework is defined in [../query-retrieval/README.md](../query-retrieval/README.md).

The canonical Knowledge Synthesis Framework is defined in [../synthesis/README.md](../synthesis/README.md). Synthesized artifacts reference Knowledge Objects but do not become Knowledge Objects.
