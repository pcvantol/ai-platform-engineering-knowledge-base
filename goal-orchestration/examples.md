# Example Engineering Goals

This document provides example Goal-driven orchestration plans.

Examples are non-executable. They do not implement `aikb goal`, execute agents, modify repositories, or create deliverables.

## Goal: Create a Verification Platform

| Field | Value |
| --- | --- |
| Goal identity | `GOAL-VERIFICATION-PLATFORM` |
| Goal description | Create a verification platform. |
| Engineering intent | Generate an engineering program for verification runtime, evidence and assurance. |
| Desired deliverables | Architecture, roadmap, backlog, verification strategy, assurance plan, validation checklist. |
| Engineering domains | Verification, Architecture, Software Assurance, Release Engineering |
| Priority | High |
| Success criteria | Program plan is traceable to Certified Knowledge and ready for human review. |

Capability Graph:

```text
Verification Engineering
->
Architecture Engineering
->
Software Assurance
->
Release Engineering
->
Engineering Program
```

Execution Plan:

```text
TASK-001: Retrieve Certified Knowledge
TASK-002: Compose capability graph
TASK-003: Prepare architecture plan
TASK-004: Prepare verification plan
TASK-005: Prepare assurance plan
TASK-006: Prepare release and documentation plan
TASK-007: Validate traceability
TASK-008: Human review checkpoint
```

## Goal: Bootstrap an Embedded AI Client

| Field | Value |
| --- | --- |
| Goal identity | `GOAL-EMBEDDED-AI-CLIENT` |
| Goal description | Bootstrap an embedded AI client. |
| Engineering intent | Prepare repository and engineering program plan for an embedded AI client. |
| Desired deliverables | Repository bootstrap plan, architecture plan, verification plan, release plan. |
| Engineering domains | Embedded Systems, Client Engineering, Architecture, Verification |
| Priority | Medium |
| Success criteria | Bootstrap plan identifies constraints, required capabilities and validation gates. |

Capability Graph:

```text
Architecture Engineering
->
Platform Engineering
->
Verification Engineering
->
Release Engineering
->
Repository Bootstrap
```

Execution Plan:

```text
TASK-001: Interpret embedded constraints
TASK-002: Retrieve Certified Knowledge
TASK-003: Select architecture and verification capabilities
TASK-004: Prepare bootstrap plan
TASK-005: Prepare validation gates
TASK-006: Human review checkpoint
```

## Goal: Introduce Software Assurance

| Field | Value |
| --- | --- |
| Goal identity | `GOAL-SOFTWARE-ASSURANCE` |
| Goal description | Introduce Software Assurance. |
| Engineering intent | Establish assurance governance, evidence, validation and documentation plan. |
| Desired deliverables | Assurance plan, evidence model, governance checklist, review plan. |
| Engineering domains | Software Assurance, Verification, Governance, Documentation |
| Priority | High |
| Success criteria | Assurance plan is explainable, evidence-based and ready for review. |

Capability Graph:

```text
Software Assurance
->
Verification Engineering
->
Governance
->
Documentation Engineering
->
Assurance Program
```

Execution Plan:

```text
TASK-001: Retrieve assurance Certified Knowledge
TASK-002: Compose assurance capability graph
TASK-003: Plan evidence and qualification
TASK-004: Plan documentation and governance
TASK-005: Validate traceability
TASK-006: Human approval checkpoint
```

## Required Traceability

```text
Goal
->
Execution Plan
->
Capability Graph
->
Engineering Tasks
->
Certified Knowledge
->
Evidence
->
Knowledge Sources
->
Repositories
```
