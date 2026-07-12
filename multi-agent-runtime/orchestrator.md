# Engineering Runtime Orchestrator

This document defines the Engineering Runtime Orchestrator.

The orchestrator plans and coordinates engineering work. Agents execute engineering work. Certified Knowledge remains the engineering authority.

This document does not implement runtime scheduling, agents, repository mutation, Certified Knowledge modification, governance approval, or model execution.

The Autonomous Engineering Mission Runtime uses this orchestrator as the mission execution coordinator. Mission state transitions, checkpoints, reports and feedback are defined in [../mission-runtime/README.md](../mission-runtime/README.md); task graph planning and agent coordination remain governed by this orchestrator model.

## Core Principle

```text
Engineer Goal
->
Engineering Runtime
->
Planning
->
Task Graph
->
Agent Execution
->
Knowledge Validation
->
Engineering Deliverables
```

The Runtime coordinates.

Certified Knowledge decides.

## Orchestrator Responsibilities

The orchestrator is responsible for:

- receiving an engineering objective;
- receiving interpreted goals from the Goal-Driven Engineering Orchestration framework;
- identifying required capabilities;
- selecting registered capabilities when capability metadata matches the objective;
- retrieving Certified Knowledge context;
- creating an execution plan;
- building a dependency graph;
- assigning tasks to registered agent roles;
- coordinating execution order;
- collecting agent results;
- aggregating results;
- validating outputs;
- preserving traceability;
- inserting human approval checkpoints.

The orchestrator must not perform engineering work itself. It plans, routes, validates and aggregates.

## Planning Model

An execution plan describes how an engineering goal should become deliverables.

Every plan should include:

| Field | Purpose |
| --- | --- |
| Plan identifier | Stable identifier for the orchestration plan. |
| Engineering goal | Human-readable objective. |
| Goal type | Program generation, repository bootstrap, architecture review, assurance plan, publication, or future type. |
| Required capabilities | Agent capabilities required to satisfy the goal. |
| Certified Knowledge context | Source Certified Knowledge used for planning. |
| Task graph | Directed graph of tasks and dependencies. |
| Validation gates | Required validation before acceptance. |
| Human approval checkpoints | Decisions requiring human review. |
| Expected deliverables | Derived outputs produced by agents or generators. |
| Traceability contract | Required lineage for the final result. |

## Task Graph Model

Engineering work is represented as a directed graph.

Each task node must include:

| Field | Purpose |
| --- | --- |
| Task identifier | Stable identity inside the plan. |
| Task type | Planning, analysis, generation, validation, review, publication, or approval. |
| Assigned agent role | Agent role expected to execute the task. |
| Required knowledge | Certified Knowledge identifiers or domains required before execution. |
| Inputs | Inputs consumed by the task. |
| Outputs | Outputs produced by the task. |
| Dependencies | Prior tasks or human approvals required before execution. |
| Execution mode | Sequential, parallel, conditional, optional, validation, or human review. |
| Validation criteria | Checks required before accepting output. |
| Traceability requirements | Knowledge and evidence lineage required in the task result. |

Supported task node types:

- planning task;
- agent execution task;
- parallel task group;
- sequential task;
- conditional task;
- optional task;
- human review task;
- knowledge validation task;
- artifact validation task;
- publication task;
- aggregation task.

## Task Graph Example

```text
GOAL-001
|
+--> TASK-001: Retrieve Certified Knowledge
|
+--> TASK-002: Architecture analysis
|       depends on TASK-001
|
+--> TASK-003: Verification analysis
|       depends on TASK-001
|
+--> TASK-004: Software assurance analysis
|       depends on TASK-001
|
+--> TASK-005: Aggregate engineering result
|       depends on TASK-002, TASK-003, TASK-004
|
+--> TASK-006: Validate traceability
|       depends on TASK-005
|
+--> TASK-007: Human approval checkpoint
        depends on TASK-006
```

## Agent Coordination Model

The orchestrator may coordinate:

- Architecture Agent;
- Verification Agent;
- Software Assurance Agent;
- Knowledge Agent;
- Publication Agent;
- Generator Agent;
- Review Agent;
- future registered agents.

Agent assignment is capability-based. The orchestrator selects roles by matching task requirements to registered agent capabilities and required knowledge domains.

The orchestrator must support:

- single-agent execution;
- multi-agent collaboration;
- parallel execution;
- sequential execution;
- dependency management;
- handoff between agents;
- conflict reporting;
- result aggregation.

## Execution Model

Every task execution should produce:

- result;
- traceability;
- supporting Certified Knowledge;
- supporting evidence;
- dependencies used;
- execution metadata;
- validation status;
- uncertainty;
- conflicts when present;
- human approval requirements.

Execution metadata should include:

- plan identifier;
- task identifier;
- agent identifier or role;
- execution mode;
- input references;
- output references;
- validation outcome;
- timestamp or runtime event marker;
- governance boundary.

## Knowledge Access Model

Every execution begins with:

```text
Certified Knowledge
->
Knowledge Relationships
->
Engineering Rationale
->
Task Planning
->
Agent Execution
```

No task should execute without knowledge context.

Allowed planning inputs:

- Certified Knowledge;
- Knowledge Relationships;
- supporting evidence;
- Knowledge Source identifiers;
- validation reports;
- engineering program manifests;
- generated artifacts when treated as derived inputs.

Forbidden primary authorities:

- publications as canonical source;
- prior agent outputs without Certified Knowledge traceability;
- generated artifacts without manifest traceability;
- unstated assumptions.

## Validation Model

Every completed task should be validated before acceptance.

Supported validation gates:

| Validation gate | Purpose |
| --- | --- |
| Knowledge validation | Confirms referenced Certified Knowledge exists and is certified. |
| Relationship validation | Confirms relationship targets resolve. |
| Traceability validation | Confirms result lineage reaches evidence. |
| Artifact validation | Confirms generated artifact exists and records source knowledge. |
| Engineering consistency | Confirms result does not contradict selected Certified Knowledge. |
| Human approval | Captures decisions requiring human engineering review. |

Validation outcomes:

- accepted;
- accepted with warnings;
- blocked;
- requires human review;
- rejected by validation.

The orchestrator may report validation status. It must not approve governance decisions.

## Result Aggregation Model

The orchestrator aggregates agent outputs into an Engineering Result.

Aggregation must preserve:

- individual agent results;
- supporting Certified Knowledge;
- supporting evidence;
- agreements;
- conflicts;
- unresolved questions;
- validation outcomes;
- human approval requirements.

The final result must distinguish generated content, retrieved knowledge, agent reasoning, and human decisions.

## Human Approval Checkpoints

Human approval is required for:

- certification;
- publication approval;
- governance changes;
- repository mutation;
- accepting conflicting agent results;
- final engineering decisions that affect project execution;
- changes to canonical frameworks.

The orchestrator may pause at a checkpoint and prepare review material. It must not bypass the checkpoint.

## Traceability

Canonical orchestrator traceability:

```text
Engineering Goal
->
Execution Plan
->
Task Graph
->
Agent
->
Certified Knowledge
->
Evidence
->
Engineering Deliverables
```

When full knowledge lineage is required:

```text
Engineering Deliverable
->
Task
->
Agent
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
->
Knowledge Sources
->
Repositories
->
Evidence
```

## Deliverable Orchestration

The orchestrator may coordinate delivery of:

- repositories;
- roadmaps;
- backlogs;
- verification programs;
- software assurance plans;
- documentation;
- publications;
- engineering reports;
- future engineering artifacts.

All deliverables are derived unless they enter the governed Knowledge Lifecycle.

## Conceptual CLI Integration

Future conceptual commands:

```text
aikb run
aikb plan
aikb explain-plan
aikb trace-run
aikb show-graph
```

These commands are architecture only. They are not implemented by the current CLI runtime.

## Example Plan: Verification Platform

| Task | Type | Agent role | Dependencies | Validation |
| --- | --- | --- | --- | --- |
| `TASK-001` | Knowledge retrieval | Runtime | none | Certified Knowledge exists |
| `TASK-002` | Architecture planning | Architecture Agent | `TASK-001` | Traceability validation |
| `TASK-003` | Verification planning | Verification Agent | `TASK-001` | Evidence validation |
| `TASK-004` | Assurance planning | Software Assurance Agent | `TASK-001` | Relationship validation |
| `TASK-005` | Program generation | Generator Agent | `TASK-002`, `TASK-003`, `TASK-004` | Artifact validation |
| `TASK-006` | Review preparation | Review Agent | `TASK-005` | Human review required |

## Example Plan: Architecture Review

| Task | Type | Agent role | Dependencies | Validation |
| --- | --- | --- | --- | --- |
| `TASK-001` | Goal analysis | Runtime | none | Objective recorded |
| `TASK-002` | Knowledge retrieval | Runtime | `TASK-001` | Certified Knowledge exists |
| `TASK-003` | Architecture review | Architecture Agent | `TASK-002` | Engineering consistency |
| `TASK-004` | Assurance review | Software Assurance Agent | `TASK-002` | Traceability validation |
| `TASK-005` | Conflict analysis | Runtime | `TASK-003`, `TASK-004` | Conflict report complete |
| `TASK-006` | Human approval checkpoint | Human reviewer | `TASK-005` | Human decision required |

## Governance Boundary

The Engineering Runtime Orchestrator is thin and replaceable.

It must not:

- implement agents;
- implement runtime scheduling in this repository foundation;
- modify Certified Knowledge;
- approve governance;
- mutate repository history;
- remove traceability;
- treat generated results as canonical.

Certified Knowledge remains the single engineering authority.

Capabilities used by the orchestrator are defined by the [Capability Extension Framework](../capabilities/README.md). Capability selection must not require Runtime architecture changes.

Goal interpretation and Capability Graph composition are defined in the [Goal-Driven Engineering Orchestration Framework](../goal-orchestration/README.md).
