# Multi-Agent Engineering Runtime

This area defines the architecture for a future Multi-Agent Engineering Runtime.

The runtime orchestrates AI Engineering Agents. It does not make agents authoritative. Certified Knowledge remains the single engineering authority.

This framework does not implement agents, runtime scheduling, model execution, repository mutation, certification approval, publication approval, or governance automation.

## Core Principle

```text
Certified Knowledge
->
Engineering Agents
->
Engineering Work
```

Agents never own knowledge.

Agents consume knowledge.

## Runtime Mission

The Multi-Agent Engineering Runtime enables multiple AI Engineering Agents to collaborate on engineering tasks while preserving:

- Certified Knowledge authority;
- traceability;
- governance boundaries;
- replaceability;
- explainability;
- human approval.

## Runtime Flow

```text
Engineer Request
->
Task Analysis
->
Agent Selection
->
Knowledge Retrieval
->
Agent Execution
->
Engineering Result
->
Traceability
```

The runtime orchestrates. Certified Knowledge provides engineering intelligence.

The detailed Engineering Runtime Orchestrator architecture is defined in [orchestrator.md](./orchestrator.md). It covers planning, task graphs, dependency management, validation gates, result aggregation, human approval checkpoints and future `aikb run`-style CLI integration.

## Agent Model

An Engineering Agent is a replaceable runtime participant that performs a bounded engineering responsibility.

Every agent must declare:

| Field | Purpose |
| --- | --- |
| Agent identifier | Stable runtime identity. |
| Agent role | Engineering responsibility such as architecture, verification, assurance, release or publication. |
| Capabilities | Supported task types. |
| Required knowledge domains | Certified Knowledge domains required for execution. |
| Inputs | Accepted task inputs. |
| Outputs | Produced result types. |
| Permissions | Allowed and forbidden actions. |
| Traceability contract | Required lineage in every result. |
| Human approval boundary | Decisions that require human review. |

Agent declarations are runtime metadata. They are not Certified Knowledge.

## Canonical Agent Roles

Initial logical roles:

| Agent role | Primary responsibility | Authority boundary |
| --- | --- | --- |
| Architecture Agent | Analyze architecture decisions and propose architecture guidance. | May recommend; may not approve architecture governance. |
| Verification Agent | Propose verification strategies, evidence models and validation plans. | May recommend; may not certify verification adequacy. |
| Software Assurance Agent | Analyze assurance concerns and qualification relationships. | May recommend; may not approve assurance governance. |
| Release Engineering Agent | Propose release, versioning and documentation workflows. | May recommend; may not approve releases. |
| Knowledge Extraction Agent | Prepare observation and candidate proposals from registered sources. | May propose; may not create canonical knowledge without workflow execution. |
| Knowledge Review Agent | Prepare review packets and relationship analysis. | May prepare; may not promote or certify knowledge. |
| Publication Agent | Draft publication outputs from Certified Knowledge. | May draft; may not approve or publish. |
| Generator Agent | Prepare generator inputs and generated artifact proposals. | May generate derived outputs; may not make outputs canonical. |
| Repository Analysis Agent | Analyze repositories for evidence and health signals. | May analyze; may not mutate repository history. |

Future agents may be added without redesign when they follow the same registration, permission and traceability contracts.

## Task Orchestration Model

The runtime must support:

- single-agent execution;
- multi-agent collaboration;
- parallel execution;
- sequential execution;
- dependency management;
- handoff between agents;
- conflict reporting;
- result aggregation.

## Orchestration Modes

| Mode | Purpose | Example |
| --- | --- | --- |
| Single-agent | One agent handles the request. | Verification Agent answers a verification strategy question. |
| Sequential | Agents execute in a governed order. | Repository Analysis Agent -> Knowledge Extraction Agent -> Knowledge Review Agent. |
| Parallel | Multiple agents analyze independently. | Architecture Agent and Software Assurance Agent review the same program. |
| Handoff | One agent passes structured context to another. | Architecture Agent hands risk findings to Verification Agent. |
| Aggregated | Runtime combines outputs and highlights agreement or conflict. | Runtime merges architecture, verification and release recommendations. |

## Dependency Management

Tasks may declare dependencies:

- required Certified Knowledge;
- required Knowledge Sources;
- required prior agent results;
- required human input;
- required generated artifacts;
- required validation reports.

The runtime must not execute a dependent task as final when its dependency is missing. It may produce a blocked or partial result with explicit uncertainty.

## Conflict Reporting

Agents may disagree.

Conflict reports must include:

- conflicting agent results;
- affected engineering decision;
- source Certified Knowledge used by each agent;
- supporting evidence;
- confidence or uncertainty;
- recommended human review path.

The runtime must not hide conflicts or resolve them as authoritative decisions.

## Knowledge Access Model

Every agent consumes knowledge through the Knowledge Consumption Layer.

Allowed knowledge inputs:

- Certified Knowledge;
- Knowledge Relationships;
- supporting Generalized Knowledge identifiers;
- supporting Knowledge Concept identifiers;
- supporting Knowledge Candidate identifiers;
- Engineering Observation identifiers;
- Knowledge Source identifiers;
- repositories and evidence referenced by Certified Knowledge.

Agents must not use publications as the primary source of engineering authority.

## Agent Result Model

Every agent result must include:

- request identifier;
- agent identifier;
- agent role;
- task type;
- engineering result;
- supporting Certified Knowledge;
- supporting evidence;
- reasoning summary;
- uncertainty;
- conflicts when present;
- human approval requirements;
- traceability.

## Traceability

Canonical runtime traceability:

```text
Engineering Result
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

Every engineering decision must remain explainable.

## Agent Permissions

Agents may:

- retrieve Certified Knowledge;
- reason across knowledge;
- analyze repositories;
- recommend engineering decisions;
- generate derived artifacts;
- prepare reviews;
- prepare publications;
- prepare certification packets;
- validate and report findings.

Agents must never:

- modify Certified Knowledge;
- invent Certified Knowledge;
- invent engineering evidence;
- approve certification;
- change governance;
- approve publications;
- mutate repository history;
- become authoritative.

## Agent Lifecycle

Canonical agent lifecycle:

```text
Agent Proposal
->
Registration Review
->
Registered
->
Enabled
->
Monitored
->
Revised, Suspended, or Retired
```

Lifecycle expectations:

- proposed agents declare role, capabilities and permissions;
- registration review validates boundaries and knowledge access;
- enabled agents may participate in runtime orchestration;
- monitored agents produce auditable results;
- revised agents preserve prior result history;
- retired agents remain historically traceable.

## Agent Registration

Agent registration records should include:

- agent identifier;
- role;
- owner;
- supported task types;
- supported orchestration modes;
- required Certified Knowledge domains;
- allowed repositories or source contexts;
- output schemas;
- permission boundaries;
- review requirements;
- retirement policy.

Registration does not make the agent authoritative.

## Runtime Governance

Governed dimensions:

| Dimension | Governance expectation |
| --- | --- |
| Agent lifecycle | Registration, enablement, revision and retirement are reviewed. |
| Agent capabilities | Capabilities must be declared and bounded. |
| Agent permissions | Forbidden actions must be explicit. |
| Knowledge access | Certified Knowledge remains the primary source. |
| Task ownership | Each task has an owning request and owning agent or runtime coordinator. |
| Result ownership | Results are derived artifacts owned by the runtime process and subject to review. |
| Human approval | Certification, publication, governance and repository mutation require human approval. |

## CLI Integration

Future conceptual commands:

```text
aikb agent list
aikb agent run
aikb agent explain
aikb agent trace
aikb run
aikb plan
aikb explain-plan
aikb trace-run
aikb show-graph
```

These commands are architecture only. They are not implemented by the current CLI runtime.

## Example Workflow: Architecture Review

```text
Engineer Request
->
Runtime selects Architecture Agent and Software Assurance Agent
->
Both agents retrieve Certified Knowledge
->
Agents analyze the proposed architecture independently
->
Runtime aggregates findings
->
Runtime reports agreements, conflicts, evidence and approval boundaries
```

## Example Workflow: Verification Strategy

```text
Engineer Request
->
Runtime selects Verification Agent
->
Verification Agent retrieves Certified Knowledge about verification, evidence and assurance
->
Agent drafts verification strategy
->
Runtime attaches traceability to Certified Knowledge and source evidence
->
Human engineer reviews result
```

## Example Workflow: Knowledge Extraction Preparation

```text
Engineer Request
->
Repository Analysis Agent inspects registered source context
->
Knowledge Extraction Agent prepares observation proposals
->
Knowledge Review Agent checks candidate readiness
->
Runtime emits proposals with traceability and uncertainty
->
Governed lifecycle commands perform any approved changes
```

## Success Criteria

The Multi-Agent Engineering Runtime architecture is valid when:

- every agent consumes Certified Knowledge;
- every result remains traceable;
- agents remain replaceable;
- orchestration supports collaboration and conflict reporting;
- governance boundaries are explicit;
- no agent becomes authoritative;
- future runtime implementation can proceed without redesigning the Knowledge Base.
