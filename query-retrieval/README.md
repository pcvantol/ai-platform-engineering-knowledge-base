# Knowledge Query & Retrieval Framework

This area defines the canonical framework for how humans and AI systems discover, retrieve, and navigate knowledge.

The Knowledge Base is the canonical source. Retrieval never changes knowledge. Retrieval only exposes existing knowledge and its traceability.

This framework does not implement search, indexing, databases, embeddings, vector databases, or generated knowledge.

## Core Principle

Knowledge is queried.

Knowledge is never duplicated for retrieval purposes.

Every retrieval result must remain traceable back to the originating Certified Knowledge when canonical knowledge is returned.

## Retrieval Objectives

The framework supports:

- semantic retrieval
- structured retrieval
- relationship navigation
- concept discovery
- publication generation
- AI-assisted retrieval
- human exploration

Retrieval is a read-only access pattern across Knowledge Objects, classifications, relationships, publications, evidence, and traceability chains.

The canonical Knowledge Synthesis Framework is defined in [../synthesis/README.md](../synthesis/README.md). Retrieval may provide inputs to synthesis, but retrieval does not create derived understanding by itself.

## Query Model

Canonical query dimensions:

| Query dimension | Purpose |
| --- | --- |
| Knowledge Identifier | Retrieve a specific Knowledge Object by stable identity. |
| Engineering Domain | Retrieve knowledge by domain. |
| Knowledge Category | Retrieve knowledge by category. |
| Lifecycle State | Retrieve knowledge by maturity stage. |
| Certification State | Retrieve knowledge by certification maturity. |
| Abstraction Level | Retrieve knowledge by project or technology independence. |
| Technology Scope | Retrieve knowledge by technology context. |
| Applicability | Retrieve knowledge by where it applies. |
| Relationships | Retrieve connected, dependent, parent, child, supporting, conflicting, or superseding knowledge. |
| Source Repository | Retrieve knowledge traceable to a source repository. |
| Evidence | Retrieve knowledge supported by specific evidence classes or evidence references. |
| Publication | Retrieve knowledge used by or represented in publications. |
| Audience | Retrieve publications or knowledge views suitable for an audience. |
| Review Status | Retrieve knowledge requiring review, revision, or follow-up. |

Query dimensions may be combined. Combined queries must preserve Knowledge Object identity rather than duplicating results.

## Retrieval Levels

Supported retrieval levels:

- Single Knowledge Object
- Knowledge Concept
- Knowledge Collection
- Engineering Domain
- Publication
- Related Knowledge
- Supporting Evidence
- Traceability Chain
- Source Context
- Review Context

Retrieval level determines the scope of results, not the authority of results.

## Retrieval Flow

```text
Query Intent
->
Query Dimensions
->
Knowledge Objects and Relationships
->
Traceability Chain
->
Result Explanation
```

The result explanation should identify why the retrieved knowledge matched the query and how it traces back to canonical sources.

## Navigation Principles

Users should be able to navigate through:

- knowledge relationships
- parent concepts
- child concepts
- supporting concepts
- related concepts
- dependencies
- conflicts
- supersession relationships
- evidence
- publications
- source repositories
- lifecycle stages
- certification states

Navigation must never duplicate knowledge. Navigation views reference Knowledge Objects and relationships.

## Relationship Navigation

Relationship navigation uses directional relationships from the Knowledge Model.

Supported navigation paths:

- from candidate to originating observations
- from concept to contributing candidates
- from generalized knowledge to concepts
- from certified knowledge to generalized knowledge
- from publication to Certified Knowledge
- from Knowledge Object to dependencies
- from Knowledge Object to supporting or conflicting knowledge
- from retired or superseded knowledge to successor knowledge
- from Knowledge Object to source evidence

Relationship navigation must preserve direction and context.

## Semantic Retrieval Principles

Semantic retrieval is conceptual and implementation independent.

It may support:

- concept similarity
- engineering similarity
- relationship discovery
- cross-domain discovery
- related concepts
- terminology-aware discovery
- evidence-aware discovery

Semantic retrieval must:

- use content and metadata together
- preserve traceability
- distinguish similarity from relationship
- distinguish suggestions from authoritative knowledge
- avoid creating duplicate knowledge
- avoid treating generated summaries as Knowledge Objects

This framework does not define embeddings, vector databases, indexes, ranking algorithms, or retrieval infrastructure.

## Implemented Engineering Assistant Retrieval

`aikb ask` implements the first deterministic retrieval path for engineering questions.

It retrieves only from Certified Knowledge records and ranks matches by:

- exact Certified Knowledge identifier match;
- title match;
- engineering domain match;
- knowledge category match;
- certified statement match;
- relationship identifiers;
- supporting evidence references.

This implementation is intentionally read-only. It does not create search indexes, embeddings, duplicate knowledge, or new Knowledge Objects.

## AI Retrieval Principles

AI may:

- search
- rank
- summarize
- recommend
- group
- explain
- compare
- suggest related knowledge
- prepare retrieval explanations

AI must not:

- create Certified Knowledge during retrieval
- modify Knowledge Objects
- invent traceability
- hide certification state
- present non-certified knowledge as certified
- create duplicate knowledge for retrieval convenience

AI-assisted retrieval must preserve the distinction between retrieval results, summaries, and AI-generated explanations.

## Traceability Model

Every retrieval result must preserve traceability.

Canonical retrieval traceability:

```text
Knowledge
->
Certified Knowledge
->
Generalized Knowledge
->
Knowledge Concept
->
Knowledge Candidate
->
Engineering Observation
->
Knowledge Source
->
Repository
```

Traceability requirements:

- Results must identify the Knowledge Object returned.
- Results must show lifecycle state and certification state where relevant.
- Certified results must trace back to originating observations and sources.
- Publication results must trace back to source Certified Knowledge.
- Evidence results must remain distinguishable from knowledge.
- AI summaries must point back to retrieved Knowledge Objects.

## Publication Retrieval Support

Publications consume retrieval. Retrieval does not consume publications as canonical sources.

Publication generation may retrieve Certified Knowledge by:

- domain
- category
- abstraction level
- applicability
- technology scope
- certification state
- audience
- relationship context

Publication retrieval rules:

- Certified Knowledge remains the canonical source.
- Publications may be retrieved as derived artifacts.
- Publications must not be treated as canonical knowledge.
- Publication generation must preserve traceability to Certified Knowledge.

## Quality Expectations

Retrieval should maximize:

- correctness
- relevance
- traceability
- explainability
- consistency
- engineering usefulness
- source clarity

Retrieval should minimize:

- duplication
- ambiguity
- hallucination
- knowledge fragmentation
- unsupported claims
- stale publication usage
- hidden uncertified results

## Scalability Principles

The framework must support:

- thousands of Knowledge Objects
- multiple organizations
- multiple engineering domains
- future AI systems
- future publication systems
- future query interfaces

Scalability rules:

- Retrieval must preserve stable Knowledge Object identity.
- Retrieval views must reference canonical objects rather than copy them.
- Query dimensions must remain extensible.
- Relationship traversal must remain directional.
- Results must remain explainable as the repository grows.

## Integration With Existing Frameworks

Query and retrieval must conform to:

- [Knowledge Model](../model/README.md)
- [Knowledge Classification System](../classification/README.md)
- [Knowledge Lifecycle](../lifecycle/README.md)
- [Knowledge Source Integration Framework](../sources/README.md)
- [Knowledge Certification Framework](../certification/README.md)
- [Publication Framework](../publications/README.md)
- [AI Knowledge Operations Framework](../ai-operations/README.md)

Query and retrieval expose knowledge. They do not replace lifecycle, certification, publication, ingestion, extraction, or review governance.
