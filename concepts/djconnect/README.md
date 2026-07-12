# DJConnect Knowledge Concepts

This area contains Knowledge Concepts normalized from DJConnect Knowledge Candidates.

Knowledge Source:

- `KS-DJCONNECT-001`
- [DJConnect Knowledge Source](../../sources/djconnect/README.md)

These records are concepts only. They do not create Generalized Knowledge, Certified Knowledge, or Publications.

## Concept Index

| Identifier | Title | Supporting candidates | Knowledge category | Review status |
| --- | --- | --- | --- | --- |
| [KCN-DJCONNECT-001](./KCN-DJCONNECT-001.md) | Thin Verification Adapter Boundary | `KC-DJCONNECT-001`, `KC-DJCONNECT-002`, `KC-DJCONNECT-003` | Architecture | Awaiting Review |
| [KCN-DJCONNECT-002](./KCN-DJCONNECT-002.md) | Coverage Baseline Provenance | `KC-DJCONNECT-004`, `KC-DJCONNECT-005` | Workflow | Awaiting Review |
| [KCN-DJCONNECT-003](./KCN-DJCONNECT-003.md) | Software Assurance Governance Boundary | `KC-DJCONNECT-006` | Architecture | Awaiting Review |
| [KCN-DJCONNECT-004](./KCN-DJCONNECT-004.md) | Profile Platform Client Contract Adoption | `KC-DJCONNECT-007`, `KC-DJCONNECT-008` | Practice | Awaiting Review |
| [KCN-DJCONNECT-005](./KCN-DJCONNECT-005.md) | Versioned Verification Runtime Boundary | `KC-DJCONNECT-009`, `KC-DJCONNECT-013` | Architecture | Generalized |
| [KCN-DJCONNECT-006](./KCN-DJCONNECT-006.md) | Thin Verification Adapter Execution Boundary | `KC-DJCONNECT-010`, `KC-DJCONNECT-015` | Architecture | Generalized |
| [KCN-DJCONNECT-007](./KCN-DJCONNECT-007.md) | Traceable Coverage Qualification Baseline | `KC-DJCONNECT-011`, `KC-DJCONNECT-012` | Workflow | Generalized |
| [KCN-DJCONNECT-008](./KCN-DJCONNECT-008.md) | Scenario Evidence and Verification Reporting Model | `KC-DJCONNECT-014`, `KC-DJCONNECT-016` | Workflow | Generalized |
| [KCN-DJCONNECT-009](./KCN-DJCONNECT-009.md) | Independent Software Assurance Governance | `KC-DJCONNECT-017`, `KC-DJCONNECT-020` | Architecture | Generalized |
| [KCN-DJCONNECT-010](./KCN-DJCONNECT-010.md) | Evidence-Based Assurance Confidence Model | `KC-DJCONNECT-018`, `KC-DJCONNECT-022` | Principle | Generalized |
| [KCN-DJCONNECT-011](./KCN-DJCONNECT-011.md) | Baseline-Gated Assurance Readiness | `KC-DJCONNECT-019`, `KC-DJCONNECT-023` | Governance | Generalized |
| [KCN-DJCONNECT-012](./KCN-DJCONNECT-012.md) | Assurance Review and Reporting Traceability | `KC-DJCONNECT-021`, `KC-DJCONNECT-024` | Workflow | Generalized |
| [KCN-DJCONNECT-013](./KCN-DJCONNECT-013.md) | Versioned Runtime Release Identity | `KC-DJCONNECT-025`, `KC-DJCONNECT-031` | Architecture | Generalized |
| [KCN-DJCONNECT-014](./KCN-DJCONNECT-014.md) | Immutable Release Baseline | `KC-DJCONNECT-026`, `KC-DJCONNECT-027` | Governance | Generalized |
| [KCN-DJCONNECT-015](./KCN-DJCONNECT-015.md) | Governed Release Roadmap and Readiness Workflow | `KC-DJCONNECT-028`, `KC-DJCONNECT-030` | Workflow | Generalized |
| [KCN-DJCONNECT-016](./KCN-DJCONNECT-016.md) | Repository Release Hygiene and Closure | `KC-DJCONNECT-029`, `KC-DJCONNECT-032` | Practice | Generalized |

## Concept Map

```text
KCN-DJCONNECT-003 Software Assurance Governance Boundary
- supports ->
KCN-DJCONNECT-002 Coverage Baseline Provenance

KCN-DJCONNECT-001 Thin Verification Adapter Boundary
- supports ->
KCN-DJCONNECT-002 Coverage Baseline Provenance

KCN-DJCONNECT-004 Profile Platform Client Contract Adoption
- related to ->
KCN-DJCONNECT-001 Thin Verification Adapter Boundary

KCN-DJCONNECT-005 Versioned Verification Runtime Boundary
- parent of ->
KCN-DJCONNECT-006 Thin Verification Adapter Execution Boundary

KCN-DJCONNECT-005 Versioned Verification Runtime Boundary
- parent of ->
KCN-DJCONNECT-008 Scenario Evidence and Verification Reporting Model

KCN-DJCONNECT-007 Traceable Coverage Qualification Baseline
- supports ->
KCN-DJCONNECT-008 Scenario Evidence and Verification Reporting Model

KCN-DJCONNECT-009 Independent Software Assurance Governance
- parent of ->
KCN-DJCONNECT-010 Evidence-Based Assurance Confidence Model

KCN-DJCONNECT-010 Evidence-Based Assurance Confidence Model
- supports ->
KCN-DJCONNECT-011 Baseline-Gated Assurance Readiness

KCN-DJCONNECT-012 Assurance Review and Reporting Traceability
- supports ->
KCN-DJCONNECT-011 Baseline-Gated Assurance Readiness

KCN-DJCONNECT-013 Versioned Runtime Release Identity
- supports ->
KCN-DJCONNECT-015 Governed Release Roadmap and Readiness Workflow

KCN-DJCONNECT-014 Immutable Release Baseline
- supports ->
KCN-DJCONNECT-015 Governed Release Roadmap and Readiness Workflow

KCN-DJCONNECT-016 Repository Release Hygiene and Closure
- supports ->
KCN-DJCONNECT-015 Governed Release Roadmap and Readiness Workflow
```

## Concept Boundary

Concepts in this folder normalize candidates into coherent engineering ideas. They are not yet generalized, certified, or publishable.
