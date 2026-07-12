# Knowledge Ingestion Pipeline

This area defines the canonical operational pipeline that transforms registered Knowledge Sources into Knowledge Candidate proposals.

Repositories are observed. Repositories are never imported. Knowledge is extracted. Repositories remain authoritative only for engineering evidence. The Knowledge Base remains authoritative for engineering knowledge.

This pipeline does not implement scanning, connect repositories, ingest knowledge, or create automation.

The canonical Knowledge Automation Framework is defined in [../automation/README.md](../automation/README.md). Automation may support ingestion activities, but candidate acceptance and lifecycle movement remain governed.

The canonical Knowledge Source Onboarding Framework is defined in [../source-onboarding/README.md](../source-onboarding/README.md). Ingestion may operate only on approved Knowledge Sources with documented extraction boundaries.

## Pipeline Principle

Knowledge enters the repository only through a governed pipeline.

Canonical ingestion flow:

```text
Knowledge Source
->
Source Scan
->
Engineering Observation Detection
->
Observation Normalization
->
Knowledge Candidate Proposal
->
Candidate Registration
->
Human Review
->
Knowledge Lifecycle
```

Ingestion ends with candidate registration and human review. Certification is outside ingestion and remains governed by the Knowledge Certification Framework.

## Pipeline Stages

### Knowledge Source

Purpose: identify a registered Knowledge Source eligible for ingestion.

Inputs:

- registered Knowledge Source
- source metadata
- extraction policy
- supported evidence types
- traceability anchors

Outputs:

- source selected for scan
- scan scope
- scan constraints

Rules:

- The source must be registered before ingestion.
- Source autonomy must be preserved.
- Source repositories must not be modified.

### Source Scan

Purpose: observe source evidence within the allowed extraction policy.

Scanning may discover:

- architecture evolution
- implementation changes
- verification evidence
- coverage changes
- engineering decisions
- release information
- design rationale
- operational experience
- future supported evidence

Outputs:

- scan findings
- source evidence references
- candidate observation signals

Rules:

- Scanning must never modify source repositories.
- Scanning must preserve source context and traceability anchors.
- Scanning must not treat findings as knowledge.
- Scanning must respect extraction boundaries.

### Engineering Observation Detection

Purpose: detect possible Engineering Observations from scan findings.

Observation examples:

- new capability
- bug fix
- architectural change
- verification milestone
- performance improvement
- quality improvement
- engineering lesson
- design trade-off
- release milestone

Outputs:

- proposed Engineering Observations
- supporting evidence references
- uncertainty or confidence notes

Rules:

- Observation detection produces observations only.
- Observations are evidence, not knowledge.
- False observations must be rejectable without deleting source evidence.

### Observation Normalization

Purpose: standardize proposed observations so they can be compared, reviewed, and linked.

Normalization should:

- remove duplicate observation records when they do not add independent evidence
- normalize terminology
- identify related observations
- standardize metadata
- preserve traceability
- preserve engineering meaning

Outputs:

- normalized Engineering Observations
- duplicate links
- related observation links
- normalized metadata

Rules:

- No engineering meaning may be lost.
- Source evidence and source context must remain traceable.
- Independent evidence must not be collapsed away.

### Knowledge Candidate Proposal

Purpose: identify reusable engineering implications from normalized observations.

Each Knowledge Candidate proposal should include:

- origin
- supporting observations
- supporting evidence
- engineering summary
- confidence
- relationships
- candidate classification
- known uncertainty
- duplicate or related candidates

Outputs:

- Knowledge Candidate proposal
- traceability chain
- classification suggestions
- relationship suggestions

Rules:

- Candidates remain proposals.
- Candidates are not certified.
- Candidate confidence is not certification.
- Candidate proposals must be explainable.

### Candidate Registration

Purpose: record accepted candidate proposals as Knowledge Candidates for lifecycle review.

Outputs:

- registered Knowledge Candidate
- candidate metadata
- traceability references
- review status

Rules:

- Candidate registration must preserve identity and lineage.
- Registered candidates remain non-canonical.
- Registration must not imply certification.
- Rejected proposals must preserve rejection rationale when useful for audit.

### Human Review

Purpose: evaluate candidate proposals before they proceed through the Knowledge Lifecycle.

Review may result in:

- accept candidate
- reject candidate
- merge candidate
- split candidate
- revise candidate
- request more evidence

Rules:

- Human review governs candidate acceptance.
- AI output may support review but does not approve candidates.
- Review decisions must remain auditable.

## Ingestion Governance

Ingestion governance covers:

- candidate review
- candidate rejection
- candidate merging
- candidate splitting
- candidate revision
- ingestion audit
- duplicate handling
- source boundary compliance

Governance expectations:

- Every candidate must be traceable to observations.
- Every observation must be traceable to a Knowledge Source.
- Rejections should preserve rationale when they inform future ingestion.
- Merges and splits must preserve source lineage.
- Ingestion audit must verify that sources were observed, not imported.

## Traceability Model

Canonical ingestion traceability:

```text
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

- Every candidate must remain explainable.
- Every candidate must reference supporting observations.
- Every observation must reference a Knowledge Source.
- Every Knowledge Source must preserve repository and evidence references.
- Source evidence must remain distinguishable from candidate interpretation.
- Normalization and candidate generation must not break lineage.

## AI-Assisted Ingestion

AI may assist with:

- source scanning
- observation identification
- candidate proposal
- relationship discovery
- duplicate detection
- summarization
- confidence estimation
- classification suggestions

AI must never:

- certify knowledge
- change repositories
- change engineering evidence
- invent observations
- invent source history
- bypass human review
- register candidates as certified knowledge

AI-assisted ingestion produces proposals only. Human review remains required.

## Quality Expectations

The ingestion pipeline should maximize:

- accuracy
- repeatability
- traceability
- consistency
- engineering value
- explainability

The ingestion pipeline should minimize:

- duplicate candidates
- hallucinations
- repository drift
- false observations
- unsupported candidate claims
- loss of source context

Quality is measured by useful, traceable candidates rather than ingestion volume.

## Scalability Principles

The pipeline must support:

- continuous ingestion
- incremental ingestion
- multiple repositories
- large repositories
- future repository technologies
- future evidence types

Scalability rules:

- Scan scope must be explicit.
- Incremental scans must preserve prior traceability.
- Multi-repository observations must preserve source identity.
- Candidate identity must remain stable after registration.
- Future evidence types must be addable without redesign.
- Pipeline stages must remain deterministic even when automated later.

## Integration With Existing Frameworks

Ingestion must conform to:

- [Knowledge Source Integration Framework](../sources/README.md)
- [Knowledge Extraction Framework](../extraction/README.md)
- [Knowledge Lifecycle](../lifecycle/README.md)
- [Knowledge Model](../model/README.md)
- [Knowledge Classification System](../classification/README.md)
- [AI Knowledge Operations Framework](../ai-operations/README.md)

Ingestion is the governed operational path from registered Knowledge Sources to Knowledge Candidates. It does not replace certification, generalization, or publication governance.
