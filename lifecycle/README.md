# Knowledge Lifecycle

This area defines the canonical lifecycle used to move engineering evidence toward certified reusable knowledge and derived publications.

The lifecycle is deterministic. Knowledge always matures through controlled refinement, never skips lifecycle stages, and always remains traceable.

## Canonical Lifecycle

```text
Software Repository
->
Repository Observation
->
Knowledge Candidate
->
Knowledge Concept
->
Generalized Knowledge
->
Certified Knowledge
->
Publication
```

Software repositories and engineering systems provide evidence. The Knowledge Base converts evidence into reusable knowledge through governed lifecycle stages.

Every lifecycle item is represented by the canonical Knowledge Object model defined in [../model/README.md](../model/README.md).

The canonical process for extracting Engineering Observations from sources is defined in [../extraction/README.md](../extraction/README.md).

## Lifecycle Stages

### Repository Observation

Purpose: capture evidence from software repositories and engineering systems without treating that evidence as reusable knowledge.

Entry criteria:

- Evidence originates from a software project, engineering system, operational event, design discussion, experiment, failure, verification activity, architecture decision, or successful engineering practice.
- The origin and context can be identified.

Exit criteria:

- The observation is assessed as potentially reusable.
- The reusable aspect is clear enough to create a knowledge candidate.

Ownership: knowledge stewards capture observations; subject matter reviewers may validate source context.

Expected artifacts:

- observation record
- source reference
- context summary
- evidence classification

Traceability requirements:

- Preserve source repository or system reference.
- Preserve date or version context when available.
- Preserve links to supporting evidence when available.

### Knowledge Candidate

Purpose: record an immature knowledge item that appears reusable but has not yet been normalized or generalized.

Entry criteria:

- A repository observation has a reusable engineering implication.
- The candidate can be traced to at least one repository observation.

Exit criteria:

- The candidate is refined into a concept or rejected as not reusable.
- Duplicate or related candidates are identified.

Ownership: knowledge stewards manage candidates; engineering reviewers assess reuse potential.

Expected artifacts:

- candidate record
- originating observation references
- reuse hypothesis
- initial classification

Traceability requirements:

- Link each candidate to its originating observations.
- Preserve rejected candidates with rationale instead of deleting them.

### Knowledge Concept

Purpose: normalize related candidates, eliminate duplication, and identify common engineering patterns.

Entry criteria:

- One or more candidates describe a related engineering concern.
- Candidate overlap, duplication, or common pattern potential is identifiable.

Exit criteria:

- The concept is stable enough to generalize.
- Boundaries, assumptions, terminology, and related candidates are explicit.

Ownership: concept owners refine concepts; reviewers validate coherence and duplication handling.

Expected artifacts:

- concept record
- related candidate references
- normalized terminology
- assumptions and boundaries
- pattern description

Traceability requirements:

- Link each concept to all contributing candidates.
- Preserve merge and split history when concepts evolve.

### Generalized Knowledge

Purpose: remove project-specific details and express knowledge in a project-independent, technology-independent form whenever practical.

Entry criteria:

- A concept is coherent and reusable beyond its source project.
- Project-specific assumptions can be separated from the reusable engineering knowledge.

Exit criteria:

- The knowledge is expressed independently of any specific product.
- Residual technology constraints are explicit.
- The item is ready for certification review.

Ownership: knowledge stewards generalize concepts; subject matter reviewers validate independence and correctness.

Expected artifacts:

- generalized knowledge record
- source concept references
- applicability statement
- constraints and exclusions
- evidence summary

Traceability requirements:

- Link each generalized item to contributing concepts.
- Preserve known source projects as evidence, not as authority.

### Certified Knowledge

Purpose: establish accepted engineering knowledge as canonical within the Knowledge Base.

Entry criteria:

- Generalized knowledge is reviewed for correctness, clarity, independence, and traceability.
- Evidence is sufficient for certification.

Exit criteria:

- The item is certified, rejected, returned for refinement, deprecated, superseded, or retired.
- Certification state and review decision are recorded.

Ownership: designated certifiers approve certification through the Knowledge Certification Framework; knowledge stewards maintain certified records.

Expected artifacts:

- certified knowledge record
- certification decision
- review history
- traceability chain
- revision state

Traceability requirements:

- Link certified knowledge to generalized knowledge.
- Preserve the full chain back to repository observations.
- Preserve certification decisions and revision history.

Certification governance is defined in [../certification/README.md](../certification/README.md).

### Publication

Purpose: produce derived artifacts for a specific audience or use without making the publication canonical.

Entry criteria:

- Source certified knowledge exists.
- The publication purpose, audience, and scope are defined.

Exit criteria:

- The publication identifies its certified knowledge sources.
- The publication can be updated when certified knowledge changes.

Ownership: publication owners produce publications; knowledge stewards verify source alignment.

Expected artifacts:

- publication artifact
- source certified knowledge references
- publication scope
- audience statement

Traceability requirements:

- Link each publication section or artifact to source certified knowledge where practical.
- Preserve the chain from publication to certified knowledge and back to originating observations.

Publication governance is defined in [../publications/README.md](../publications/README.md).

## Traceability Model

Traceability follows the lifecycle chain:

```text
Observation
->
Candidate
->
Concept
->
Generalized Knowledge
->
Certified Knowledge
->
Publication
```

Each lifecycle item must record its immediate predecessors. Certified knowledge and publications must be able to reconstruct the full chain back to originating observations.

Traceability is preserved through references, review history, revision history, and retirement history. Generalization may remove project-specific details from the knowledge statement, but it must not remove evidence lineage.

## Promotion Rules

- Knowledge must not skip lifecycle stages.
- Promotion requires meeting the exit criteria of the current stage and the entry criteria of the next stage.
- Promotion must preserve traceability to predecessor items.
- Promotion must record reviewer or owner decisions appropriate to the stage.
- Rejected items must preserve rationale.
- Publications may only be derived from certified knowledge.

The canonical review and promotion governance is defined in [../review-promotion/README.md](../review-promotion/README.md).

## Knowledge Evolution

Knowledge evolves without losing history.

Candidates evolve by refinement, rejection, or promotion to concepts. Concepts may merge when multiple concepts describe the same reusable pattern. Concepts may split when one concept contains multiple independent patterns. Generalized knowledge may be revised when new evidence changes applicability, constraints, or wording. Certified knowledge may be updated through certification review. Obsolete certified knowledge must be retired rather than deleted.

History must remain preserved across all of these changes. Superseded, merged, split, rejected, and retired items remain part of the knowledge record.

## Governance Expectations

Governance applies to every lifecycle transition.

- Promotion reviews verify criteria, traceability, and terminology.
- Certification reviews verify correctness, project independence, evidence sufficiency, and publication readiness.
- Publication reviews verify that derived artifacts remain aligned with certified knowledge.
- Retirement reviews preserve historical context and identify superseding knowledge when applicable.

The lifecycle supports continuous knowledge growth over many years by separating evidence, candidate knowledge, normalized concepts, generalized knowledge, certified knowledge, and publications.

Lifecycle state is independent from knowledge category, engineering domain, abstraction level, applicability, technology scope, evidence classification, and certification status. Those model and classification concepts are defined in [../model/README.md](../model/README.md) and [../classification/README.md](../classification/README.md).
