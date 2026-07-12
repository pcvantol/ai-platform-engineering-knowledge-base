# Knowledge Review & Promotion Framework

This area defines the canonical governance framework for moving knowledge through the maturity pipeline.

Knowledge is promoted. Knowledge is never automatically upgraded. Every promotion requires supporting evidence and remains traceable.

This framework does not promote knowledge, ingest repositories, or implement automation.

## Promotion Pipeline

Canonical promotion pipeline:

```text
Knowledge Candidate
->
Knowledge Review
->
Knowledge Concept
->
Concept Review
->
Generalized Knowledge
->
Generalization Review
->
Certified Knowledge
->
Publication
```

Certification review is governed by the Knowledge Certification Framework. Publication review is governed by the Publication Framework.

## Review Stages

### Knowledge Candidate Review

Purpose: determine whether a Knowledge Candidate should become a Knowledge Concept.

Review determines:

- relevance
- uniqueness
- engineering value
- sufficient evidence
- traceability to Engineering Observations
- candidate classification quality

Promotion target: Knowledge Concept.

### Knowledge Concept Review

Purpose: determine whether a Knowledge Concept is normalized, coherent, and ready for generalization.

Review determines:

- normalization quality
- relationship quality
- duplicate elimination
- abstraction quality
- terminology consistency
- concept boundary clarity

Promotion target: Generalized Knowledge.

### Generalization Review

Purpose: determine whether knowledge has become reusable beyond its source context.

Review determines:

- project independence
- technology independence where practical
- reusability
- engineering correctness
- applicability constraints
- evidence sufficiency for generalization

Promotion target: Certified Knowledge review.

### Certification Review

Purpose: determine whether Generalized Knowledge is ready to become Certified Knowledge.

Review determines:

- canonical readiness
- consistency
- governance compliance
- publication readiness
- evidence strength
- traceability completeness

Certification review is detailed in [../certification/README.md](../certification/README.md).

## Promotion Criteria

Every promotion must define:

- entry criteria
- exit criteria
- mandatory evidence
- review expectations
- traceability requirements
- quality expectations

Promotion must not skip lifecycle stages. A Knowledge Object may remain in its current state until criteria are met.

## Transition Criteria

### Candidate to Concept

Entry criteria:

- Candidate is registered.
- Candidate has traceability to at least one Engineering Observation.
- Candidate has an engineering summary and initial classification.

Mandatory evidence:

- supporting observations
- source evidence references
- candidate rationale

Exit criteria:

- Reusable engineering concern is clear.
- Duplicate or related candidates are identified.
- Candidate is accepted, merged, split, revised, rejected, or retained.

Traceability requirements:

- Preserve candidate identity.
- Preserve originating observations and evidence.
- Preserve review decision and rationale.

### Concept to Generalized Knowledge

Entry criteria:

- Concept has contributing candidate references.
- Concept boundaries, terminology, and relationships are explicit.
- Duplicate handling has been reviewed.

Mandatory evidence:

- contributing candidates
- normalized concept rationale
- relationship evidence

Exit criteria:

- Concept expresses a reusable engineering pattern or concern.
- Project-specific details are identified.
- Concept is ready for generalization or requires revision.

Traceability requirements:

- Preserve contributing candidate lineage.
- Preserve merge and split history.
- Preserve relationship decisions.

### Generalized Knowledge to Certified Knowledge

Entry criteria:

- Generalized Knowledge is project independent.
- Technology constraints are explicit.
- Applicability and exclusions are documented.
- Traceability to concepts and candidates is preserved.

Mandatory evidence:

- source concepts
- evidence summary
- applicability rationale
- relationship review

Exit criteria:

- Knowledge is ready for certification review, returned for refinement, rejected, deprecated, superseded, or retired.

Traceability requirements:

- Preserve full lineage back to observations.
- Preserve review and certification decisions.
- Preserve revision history.

### Certified Knowledge to Publication

Entry criteria:

- Certified Knowledge exists.
- Publication purpose, audience, and scope are defined.

Mandatory evidence:

- source Certified Knowledge references
- publication scope
- audience statement

Exit criteria:

- Publication is approved, revised, superseded, or retired under publication governance.

Traceability requirements:

- Preserve links from publication to Certified Knowledge.
- Preserve publication version and source knowledge snapshot.

## Review Outcomes

Canonical review decisions:

| Decision | Meaning |
| --- | --- |
| Promote | Move knowledge to the next maturity stage. |
| Remain in Current State | Keep knowledge where it is without rejection. |
| Needs More Evidence | Require additional observations or evidence before promotion. |
| Revise | Require changes before another review. |
| Merge | Combine overlapping knowledge while preserving source identities. |
| Split | Separate knowledge into multiple Knowledge Objects. |
| Reject | Stop promotion because the item is not suitable. |
| Supersede | Replace with newer or more accurate knowledge. |
| Retire | Remove from active use while preserving history. |

Review decisions must preserve rationale.

## Knowledge Evolution Model

Knowledge may evolve through:

- revision
- merging
- splitting
- superseding
- deprecation
- retirement

The continuous evolution model for long-term revisions, drift, impact analysis, restoration, and publication impact is defined in the [Continuous Knowledge Evolution Framework](../continuous-evolution/README.md).

Evolution rules:

- History must remain intact.
- Merges must preserve all source identities.
- Splits must reference the source Knowledge Object.
- Superseded knowledge must identify successor knowledge.
- Deprecated knowledge remains historically traceable.
- Retired knowledge remains auditable.
- Revisions must identify what changed and why.

## Promotion Governance

Promotion governance ensures controlled maturity movement.

Governance expectations:

- Promotion requires evidence.
- Promotion requires traceability.
- Promotion requires review decision records.
- Promotion decisions must identify affected Knowledge Objects.
- Promotion must respect lifecycle, model, classification, extraction, ingestion, certification, and publication frameworks.
- AI may recommend promotion but must not perform promotion.

## Audit Model

Every promotion must be auditable.

Audit records should support:

- who reviewed
- what evidence was considered
- what changed
- why promotion occurred
- which Knowledge Objects were affected
- which relationships changed
- which classifications changed
- whether merge, split, supersession, deprecation, or retirement occurred
- whether additional evidence was requested

Auditability protects the Knowledge Base from premature certification, hidden knowledge loss, and untraceable authority.

## AI Support

AI may assist with:

- review preparation
- relationship analysis
- duplicate analysis
- consistency checking
- evidence summarization
- promotion recommendations
- impact analysis
- terminology checks

AI never performs promotion.

AI outputs are review inputs only. Promotion remains an engineering governance decision.

## Quality Expectations

Promotion should maximize:

- engineering quality
- reusability
- consistency
- traceability
- long-term maintainability
- review clarity

Promotion should minimize:

- duplication
- premature certification
- knowledge fragmentation
- repository drift
- unsupported promotion
- untraceable revisions

## Integration With Existing Frameworks

Review and promotion must conform to:

- [Knowledge Lifecycle](../lifecycle/README.md)
- [Knowledge Model](../model/README.md)
- [Knowledge Classification System](../classification/README.md)
- [Knowledge Ingestion Pipeline](../ingestion/README.md)
- [Knowledge Extraction Framework](../extraction/README.md)
- [Knowledge Certification Framework](../certification/README.md)
- [Publication Framework](../publications/README.md)
- [AI Knowledge Operations Framework](../ai-operations/README.md)

Review and promotion govern maturity movement. They do not replace certification, publication governance, or source integration.
