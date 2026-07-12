# Knowledge Certification Framework

This area defines the canonical governance framework through which engineering knowledge becomes Certified Knowledge.

Knowledge is not canonical because it exists. Knowledge becomes canonical only after it has been evaluated, validated, and accepted through a governed certification process.

Certification is deterministic, traceable, evidence based, repeatable, project independent, technology independent, and auditable.

This framework does not certify any knowledge, populate the repository, or define automation.

## Certification Scope

Knowledge progresses through:

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

Certification governs promotion from Generalized Knowledge into Certified Knowledge.

Certification state is separate from lifecycle state. Lifecycle state describes where knowledge is in the lifecycle. Certification state describes the governed certification decision or review maturity.

## Certification Objectives

Certification determines whether knowledge is:

- sufficiently generalized
- reusable
- technically correct
- internally consistent
- supported by evidence
- traceable
- publication worthy
- aligned with canonical terminology
- consistent with related Knowledge Objects
- suitable to become authoritative inside the Knowledge Base

## Certification Criteria

Canonical certification criteria:

| Criterion | Certification question |
| --- | --- |
| Engineering correctness | Is the knowledge technically sound? |
| Supporting evidence | Is the knowledge supported by sufficient evidence? |
| Traceability | Can the full lineage be reconstructed back to observations and sources? |
| Reusability | Is the knowledge useful beyond a single incidental context? |
| Project independence | Has project-specific detail been removed or isolated? |
| Technology independence | Is the knowledge technology independent where practical? |
| Internal consistency | Does the knowledge avoid contradictions inside its own statement? |
| Relationship consistency | Are dependencies, conflicts, supersession, parent, and child relationships valid? |
| Terminology consistency | Does the knowledge use canonical terminology? |
| Classification consistency | Are domain, category, abstraction, applicability, technology scope, and evidence classification correct? |
| Abstraction quality | Is the abstraction level justified by evidence and generalization? |
| Future-proof applicability | Are applicability constraints explicit enough for future systems? |
| Publication readiness | Can the knowledge serve as a source for publications without losing authority or traceability? |

Certification requires enough evidence and review confidence to accept the knowledge as canonical. It does not require universal applicability.

## Certification Evidence Model

Certification must reference evidence.

Evidence may include:

- verification reports
- architecture decisions
- engineering observations
- implementation experience
- multiple independent repositories
- production experience
- experiments
- test results
- operational evidence
- design discussions
- failure analysis
- external references

Evidence must be classified using the Knowledge Classification System where applicable.

Evidence strength should be documented using the evidence strength levels defined in [../classification/README.md](../classification/README.md). Certification reviewers must distinguish evidence from interpretation, summaries, and publication text.

## Decision Model

Canonical certification states:

| State | Meaning |
| --- | --- |
| Candidate | The item may be eligible for certification review but has not entered review. |
| Under Review | Certification review is active. |
| Certified | The item is accepted as canonical Certified Knowledge. |
| Rejected | The item is not accepted for certification. |
| Returned for Refinement | The item requires changes before certification can continue. |
| Deprecated | The item remains historically valid but is no longer recommended for active use. |
| Superseded | The item has been replaced by newer certified or certifiable knowledge. |
| Retired | The item is removed from active use while preserved historically. |

Decision rules:

- Certified is the only state that makes knowledge canonical.
- Rejected, Deprecated, Superseded, and Retired states must preserve rationale.
- Returned for Refinement must identify required remediation.
- Superseded knowledge must link to successor knowledge.
- Certification state must not be confused with lifecycle state.

## Certification Workflow

```text
Generalized Knowledge
->
Certification Request
->
Evidence Review
->
Technical Review
->
Knowledge Review
->
Consistency Review
->
Decision
->
Certified Knowledge or Non-certified Outcome
```

Workflow expectations:

- Certification starts from Generalized Knowledge.
- The request must identify the Knowledge Object and its traceability chain.
- Evidence review validates source support and evidence strength.
- Technical review validates engineering correctness.
- Knowledge review validates generalization, reusability, abstraction quality, and publication readiness.
- Consistency review validates terminology, classification, relationships, and internal consistency.
- Cross-domain review is required when knowledge spans multiple engineering domains or affects established certified knowledge.
- The decision and rationale must be recorded.

Pre-certification promotion governance is defined in [../review-promotion/README.md](../review-promotion/README.md).

## Review Types

Technical review evaluates engineering correctness, technology constraints, and known limitations.

Knowledge review evaluates project independence, reusable framing, abstraction level, and relationship to the canonical Knowledge Model.

Consistency review evaluates terminology, classification, relationship consistency, and alignment with lifecycle and extraction rules.

Cross-domain review evaluates knowledge that affects multiple domains or may conflict with certified knowledge in another domain.

Re-certification review evaluates certified knowledge after material revision, supersession, merge, split, deprecation, or changed evidence.

## Governance Roles

Canonical roles:

| Role | Responsibility |
| --- | --- |
| Knowledge Steward | Maintains Knowledge Objects, traceability, metadata, and lifecycle movement. |
| Technical Reviewer | Evaluates engineering correctness and evidence interpretation. |
| Knowledge Reviewer | Evaluates generalization, reusability, abstraction, and model consistency. |
| Domain Reviewer | Reviews domain-specific correctness and cross-domain implications. |
| Certifier | Makes or records the governed certification decision. |
| Publication Owner | Uses Certified Knowledge as a source for publications but does not certify knowledge. |
| Auditor | Reviews traceability, decision records, and governance compliance. |

One person may perform multiple roles only when governance permits it. Certification decisions must remain reviewable and auditable.

## Promotion Rules

- Only Generalized Knowledge may be promoted into Certified Knowledge.
- Promotion requires certification review.
- Promotion requires sufficient evidence and traceability.
- Promotion requires a recorded decision.
- Promotion must preserve Knowledge Object identity and revision history.
- Promotion must not be performed by publication generation.
- AI assistance cannot promote or certify knowledge.

## Revision Policy

Certified Knowledge may evolve.

Supported changes:

- revision
- superseding
- splitting
- merging
- deprecation
- retirement

Revision rules:

- Minor clarifications may preserve certification when meaning, applicability, evidence, and relationships do not materially change.
- Material revisions require re-certification.
- Splits create successor Knowledge Objects and preserve the source object history.
- Merges preserve all source object identities and merge rationale.
- Superseded knowledge remains traceable to successor knowledge.
- Deprecated and retired knowledge remains part of the historical record.

## Re-certification Policy

Re-certification is required when:

- technical meaning changes
- applicability expands or narrows materially
- evidence changes materially
- conflicting evidence appears
- relationships change in a way that affects correctness
- a certified item is split, merged, or superseded
- terminology or classification changes affect interpretation

Re-certification follows the same evidence based and traceable review expectations as initial certification.

## Certification Cycles

| Certification cycle | Scope | Decision |
| --- | --- | --- |
| [First Knowledge Certification Cycle](./cycles/2026-07-12-first-certification-cycle.md) | `GK-DJCONNECT-001` through `GK-DJCONNECT-004` | Certified |
| [Generation 2 Verification Engineering Population Certification](./cycles/2026-07-12-generation-2-verification-engineering-population.md) | `GK-DJCONNECT-005` through `GK-DJCONNECT-008` | Certified |
| [Generation 2 Software Assurance Engineering Population Certification](./cycles/2026-07-12-generation-2-software-assurance-engineering-population.md) | `GK-DJCONNECT-009` through `GK-DJCONNECT-012` | Certified |
| [Generation 2 Release Engineering Population Certification](./cycles/2026-07-12-generation-2-release-engineering-population.md) | `GK-DJCONNECT-013` through `GK-DJCONNECT-016` | Certified |
| [Windows Certification Cycle](./cycles/2026-07-12-github-com-pcvantol-djconnect-windows-certification-cycle.md) | Windows source-specific corpus | Certified |

## Deprecation and Retirement Policy

Deprecation indicates that knowledge should no longer be preferred for active use, while preserving historical value.

Retirement removes knowledge from active use, while preserving audit history and traceability.

Deprecation or retirement must record:

- reason
- effective date
- affected Knowledge Objects
- successor knowledge when available
- publication impact
- reviewer or decision authority

## Publication Rules

Only Certified Knowledge may serve as the source for publications.

Publications never certify knowledge. Certification always precedes publication.

If a publication conflicts with Certified Knowledge, Certified Knowledge is authoritative. Publication updates may be required when Certified Knowledge is revised, deprecated, superseded, or retired.

Publication governance is defined in [../publications/README.md](../publications/README.md).

## AI Support

AI may assist with:

- consistency checking
- relationship analysis
- duplicate detection
- evidence summarization
- review preparation
- terminology checks
- classification checks

AI must never autonomously certify knowledge.

AI outputs are review inputs, not certification decisions. Certification remains a governed engineering decision.

The canonical AI operations boundaries are defined in [../ai-operations/README.md](../ai-operations/README.md).

## Auditability

Certification must be auditable.

Audit records should allow reviewers to reconstruct:

- Knowledge Object identity
- certification state
- lifecycle state at review time
- evidence considered
- traceability chain
- reviewers and roles
- decision and rationale
- revision or re-certification history
- publication impact

Auditability protects the Knowledge Base from untraceable authority, project-specific drift, and undocumented certification decisions.

## Certification Cycles

| Date | Cycle | Status |
| --- | --- | --- |
| 2026-07-12 | [First Knowledge Certification Cycle](./cycles/2026-07-12-first-certification-cycle.md) | Completed |
