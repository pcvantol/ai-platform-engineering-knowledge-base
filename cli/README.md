# AI Platform Engineering CLI Architecture

This area defines the canonical architecture for the AI Platform Engineering CLI.

The CLI is the primary engineering interface for consuming the Knowledge Base. It is intentionally thin. Engineering intelligence belongs inside Certified Knowledge, not inside CLI command implementations.

This area contains the initial thin CLI runtime. `aikb init`, `aikb onboard`, `aikb extract`, `aikb classify`, `aikb review`, `aikb generalize`, `aikb certify`, `aikb ask`, `aikb generate`, `aikb evolve`, `aikb validate`, `aikb improve`, and `aikb status` are implemented. Future commands remain architectural until explicitly implemented.

## Core Principle

```text
Knowledge
->
Templates
->
Generators
->
CLI
->
Engineer
```

The CLI orchestrates. The Knowledge Base decides.

## CLI Responsibilities

The CLI may orchestrate:

- Certified Knowledge consumption
- template instantiation
- generator execution
- repository bootstrapping
- Knowledge Source onboarding assistance
- publication generation
- Knowledge workflow execution
- engineering question answering
- repository and knowledge health checks

The CLI must not:

- duplicate Certified Knowledge
- embed engineering intelligence in command logic
- modify Certified Knowledge directly
- certify knowledge
- approve publications
- replace governance
- treat publications as canonical source knowledge

## Command Model

Canonical command namespace:

```text
aikb <command> [arguments] [options]
```

Initial command architecture:

| Command | Purpose | Implementation status |
| --- | --- | --- |
| `aikb init` | Initialize a project or repository from Certified Knowledge, templates, and generators. | Implemented |
| `aikb onboard` | Assist Knowledge Source onboarding for a repository. | Implemented |
| `aikb extract` | Extract Engineering Observations from registered Knowledge Sources. | Implemented |
| `aikb classify` | Generate Knowledge Candidates from Engineering Observations. | Implemented |
| `aikb review` | Form Knowledge Concepts from related Knowledge Candidates. | Implemented |
| `aikb generalize` | Create Generalized Knowledge from Knowledge Concepts. | Implemented |
| `aikb certify` | Certify eligible Generalized Knowledge. | Implemented |
| `aikb ask` | Answer engineering questions from Certified Knowledge, relationships, evidence, and rationale. | Implemented |
| `aikb generate` | Generate a complete engineering program from Certified Knowledge. | Implemented |
| `aikb evolve` | Compare Engineering Programs against current Certified Knowledge and propose governed evolution. | Implemented |
| `aikb validate` | Validate Knowledge Base consistency, traceability, health and qualification. | Implemented |
| `aikb improve` | Analyze repository metrics and propose governed Knowledge Operating System improvements. | Implemented |
| `aikb status` | Report implemented, architectural and placeholder CLI commands. | Implemented |
| `aikb agent` | Future namespace for Multi-Agent Engineering Runtime operations. | Architecture only |
| `aikb run` | Future Engineering Runtime Orchestrator entrypoint for planning task graphs and coordinating agents. | Architecture only |
| `aikb plan` | Future command for rendering execution plans without running agents. | Architecture only |
| `aikb explain-plan` | Future command for explaining plan rationale and Certified Knowledge basis. | Architecture only |
| `aikb trace-run` | Future command for rendering execution traceability. | Architecture only |
| `aikb show-graph` | Future command for visualizing task graphs. | Architecture only |
| `aikb capability` | Future namespace for capability discovery, registration, validation and activation. | Architecture only |
| `aikb goal` | Future namespace for goal interpretation, capability graph planning and goal traceability. | Architecture only |
| `aikb mission` | Future namespace for autonomous mission planning, status, explanation, traceability, validation and reporting. | Architecture only |
| `aikb qualify` | Future namespace for Engineering Operating System qualification, evidence, traceability, explanations and scorecards. | Architecture only |
| `aikb publish` | Generate or refresh publications from Certified Knowledge. | Architecture only |
| `aikb doctor` | Report repository, quality, traceability, and health findings. | Architecture only |

Only `aikb init`, `aikb onboard`, `aikb extract`, `aikb classify`, `aikb review`, `aikb generalize`, `aikb certify`, `aikb ask`, `aikb generate`, `aikb evolve`, `aikb validate`, `aikb improve`, and `aikb status` are implemented by the current runtime.

## Mission Command Architecture

The future `aikb mission` namespace will coordinate complete engineering missions through the Autonomous Engineering Mission Runtime.

Conceptual commands:

| Command | Purpose | Status |
| --- | --- | --- |
| `aikb mission` | Create or plan a mission from an engineering objective. | Architecture only |
| `aikb mission status` | Show Mission State, checkpoints, blockers and current progress. | Architecture only |
| `aikb mission explain` | Explain mission planning rationale, selected capabilities and Certified Knowledge basis. | Architecture only |
| `aikb mission trace` | Render mission traceability from outputs back to Certified Knowledge and evidence. | Architecture only |
| `aikb mission validate` | Validate mission state transitions, outputs, checkpoints and traceability. | Architecture only |
| `aikb mission report` | Produce a derived Mission Report. | Architecture only |

Conceptual flow:

```text
Engineering Mission
->
Goal Interpretation
->
Capability Graph
->
Task Graph
->
Engineering Runtime Orchestrator
->
Validation
->
Mission Report and Knowledge Feedback
```

These commands are not implemented by the current CLI runtime. Mission feedback must enter the Knowledge Lifecycle through governed extraction, review and certification.

## Qualification Command Architecture

The future `aikb qualify` namespace will qualify the Engineering Operating System itself.

Conceptual commands:

| Command | Purpose | Status |
| --- | --- | --- |
| `aikb qualify` | Run or plan Engineering Operating System qualification. | Architecture only |
| `aikb qualify runtime` | Qualify runtime, orchestrator, agent and mission architecture. | Architecture only |
| `aikb qualify knowledge` | Qualify Knowledge Base integrity, lineage and certification state. | Architecture only |
| `aikb qualify missions` | Qualify Mission Runtime state, checkpoints and evidence. | Architecture only |
| `aikb qualify report` | Produce a Qualification Report. | Architecture only |
| `aikb qualify trace` | Render qualification decision traceability. | Architecture only |
| `aikb qualify explain` | Explain findings, decisions and evidence basis. | Architecture only |
| `aikb qualify scorecard` | Produce knowledge, runtime, mission, repository and publication scorecards. | Architecture only |

Conceptual flow:

```text
Engineering Platform
->
Validation
->
Qualification
->
Evidence
->
Management Summary
```

These commands are not implemented by the current CLI runtime. The existing `aikb validate` command produces validation evidence that future qualification workflows may consume.

## Running the CLI

From the repository root:

```text
bin/aikb init verification-platform --name my-verification-platform --output /tmp/my-verification-platform
```

The command writes a generated repository containing a manifest, prepared Knowledge Source metadata, backlog, roadmap, governance, documentation, and traceability to source Certified Knowledge.

Repository onboarding:

```text
bin/aikb onboard github.com/pcvantol/djconnect-windows
```

The command writes a Knowledge Source profile and Extraction Profile under `sources/`, and updates the registered sources index. It does not extract observations or modify the source repository.

Observation extraction:

```text
bin/aikb extract --source djconnect-windows
```

The command inspects registered source evidence, writes Engineering Observations under `observations/`, and updates the observation index. It does not create Knowledge Candidates, generalize knowledge, certify knowledge, or modify source repositories.

Knowledge Candidate generation:

```text
bin/aikb classify --source djconnect-windows
```

The command reads Engineering Observations, writes Knowledge Candidates under `candidates/`, and preserves observation-to-evidence traceability. It does not create Knowledge Concepts, Generalized Knowledge, Certified Knowledge, or Publications.

Knowledge Concept formation:

```text
bin/aikb review --source djconnect-windows
```

The command reads Knowledge Candidates, groups related candidates into project-aware Knowledge Concepts, and preserves candidate-to-observation-to-evidence traceability. It does not create Generalized Knowledge, Certified Knowledge, or Publications.

Knowledge Generalization:

```text
bin/aikb generalize --source djconnect-windows
```

The command reads Knowledge Concepts and creates Generalized Knowledge records under `generalized/`. It preserves concept-to-candidate-to-observation-to-evidence traceability. It does not certify knowledge or generate publications.

Knowledge Certification:

```text
bin/aikb certify --source djconnect-windows
```

The command reads Generalized Knowledge, validates readiness, writes Certified Knowledge under `certified/`, and records a certification cycle under `certification/cycles/`. It does not generate publications.

Knowledge-driven engineering questions:

```text
bin/aikb ask "How should I architect a verification runtime?"
```

The command reads Certified Knowledge, follows recorded relationships and evidence, and renders an explainable answer with traceability. It does not modify repositories, extract knowledge, certify knowledge, generate publications, or search external documentation.

Engineering program generation:

```text
bin/aikb generate verification-platform --output /tmp/verification-platform-program
```

The command reads Certified Knowledge, selects a deterministic program generator, and writes a complete Engineering Program with architecture, governance, roadmap, backlog, strategies, guidance, checklists, prompts, and a manifest. It does not onboard repositories, extract observations, certify knowledge, modify canonical knowledge, or generate publications.

Engineering program evolution:

```text
bin/aikb evolve --program /tmp/verification-platform-program --output /tmp/verification-platform-evolution
```

The command reads an Engineering Program Manifest, compares it with current Certified Knowledge, detects knowledge drift, and writes or prints an Evolution Report. It does not modify the program, Certified Knowledge, repositories, or publications.

Knowledge Base validation:

```text
bin/aikb validate
```

```text
bin/aikb validate --knowledge --output /tmp/aikb-validation-report.md
```

The command validates Knowledge Sources, Knowledge Objects, relationships, traceability, certification, publications and repository health. It renders findings, evidence, a scorecard and qualification decisions. It does not repair findings or modify Certified Knowledge.

Continuous Knowledge System improvement:

```text
bin/aikb improve
```

```text
bin/aikb improve generators --output /tmp/aikb-improvement-report.md
```

The command collects repository, knowledge, generator and publication metrics, consumes validation evidence, and produces governed improvement recommendations. It does not modify repositories, Certified Knowledge, publications, templates or governance.

CLI command status:

```text
bin/aikb status
```

```text
bin/aikb status --output /tmp/aikb-cli-status-report.md
```

The command reports which commands are implemented and executable, which remain architecture-only, and which are non-executable placeholders. It does not modify the Knowledge Base unless an external report output is requested.

## Command Architecture

Every command should follow the same conceptual flow:

```text
Command Request
->
Knowledge Consumption Layer
->
Certified Knowledge and Metadata
->
Templates or Generators when needed
->
Governance and Traceability Checks
->
Command Output
```

Command outputs may include reports, proposed files, generated publication drafts, onboarding packets, backlogs, or review packets. Outputs remain derived artifacts unless explicitly promoted through the Knowledge Lifecycle.

## Init Command Architecture

Example:

```text
aikb init verification-platform
```

Conceptual flow:

```text
Load Certified Knowledge
->
Select Template
->
Execute Generators
->
Produce Repository
->
Produce Backlog
->
Produce Governance
->
Produce Documentation
```

`aikb init` should bootstrap from Certified Knowledge and selected templates. Templates provide structure. Generators instantiate structure. Certified Knowledge supplies engineering rationale and constraints.

## Init Implementation

The first implementation lives in:

- `bin/aikb`
- `cli/aikb_cli/certification.py`
- `cli/aikb_cli/evolution.py`
- `cli/aikb_cli/assistant.py`
- `cli/aikb_cli/main.py`
- `cli/aikb_cli/classification.py`
- `cli/aikb_cli/extraction.py`
- `cli/aikb_cli/generator.py`
- `cli/aikb_cli/generalization.py`
- `cli/aikb_cli/improvement.py`
- `cli/aikb_cli/onboarding.py`
- `cli/aikb_cli/program_generation.py`
- `cli/aikb_cli/project_bootstrap.py`
- `cli/aikb_cli/review.py`
- `cli/aikb_cli/validation.py`
- `cli/aikb_cli/knowledge.py`
- `cli/aikb_cli/templates.py`

The implementation uses only the Python standard library. It loads Certified Knowledge from `certified/`, renders the passive `templates/project-bootstrap/basic` template, and writes a generated repository with `.aikb/project-manifest.json`.

## Onboard Command Architecture

Example:

```text
aikb onboard <repository>
```

Conceptual flow:

```text
Repository Assessment
->
Knowledge Source Registration
->
Extraction Profile
->
Repository Ready
```

`aikb onboard` may prepare onboarding records, evidence summaries, extraction profile drafts, and validation checklists. Approval remains governed by the Knowledge Source Onboarding Framework.

## Extract Command Architecture

Example:

```text
aikb extract
```

Conceptual flow:

```text
Knowledge Source
->
Engineering Observations
->
Knowledge Candidates
```

`aikb extract` may discover observations and propose candidates. It must preserve source evidence and must not generalize, certify, or publish knowledge.

## Certify Command Architecture

Example:

```text
aikb certify
```

Conceptual flow:

```text
Knowledge Candidates
->
Knowledge Concepts
->
Generalized Knowledge
->
Certified Knowledge
```

`aikb certify` may prepare certification review packets and readiness checks. Certification authority remains outside the CLI.

## Publish Command Architecture

Example:

```text
aikb publish
```

Conceptual flow:

```text
Certified Knowledge
->
Blueprint
->
Engineering Handbook
->
Architecture Guide
```

`aikb publish` may generate publication drafts or refresh candidates from Certified Knowledge. It must not use publications as source knowledge.

## Ask Command Architecture

Example:

```text
aikb ask "How should I architect a verification runtime?"
```

Conceptual answer flow:

```text
Certified Knowledge
->
Relationships
->
Evidence
->
Engineering Rationale
->
Answer
```

`aikb ask` must search Certified Knowledge first, then relationships, evidence, and rationale. Publications may help audience formatting, but they must not be the primary source.

## Ask Implementation

The implemented assistant lives in `cli/aikb_cli/assistant.py`.

The command accepts a question as arguments or from stdin:

```text
bin/aikb ask "What verification strategy should a new AI platform use?"
```

```text
printf "How should software assurance integrate with platform qualification?\\n" | bin/aikb ask
```

Deterministic retrieval uses:

- Certified Knowledge identifier
- engineering domain
- knowledge category
- title and certified statement
- supporting relationships
- evidence references

Every answer contains:

- engineering conclusion
- supporting rationale
- supporting Certified Knowledge
- supporting evidence
- related knowledge
- knowledge confidence
- traceability references
- uncertainty statement

The assistant does not search markdown documentation as the primary source. It loads `certified/*/CK-*.md` records first and derives its answer from their metadata, relationships, and evidence.

## Generate Command Architecture

Example:

```text
aikb generate verification-platform
```

Conceptual generation flow:

```text
Certified Knowledge
->
Knowledge Retrieval
->
Knowledge Relationships
->
Engineering Reasoning
->
Program Generator
->
Generated Engineering Program
```

`aikb generate` supports:

- `verification-platform`
- `ai-platform`
- `embedded-platform`
- `software-assurance`

The generated program contains:

- repository architecture;
- project structure guidance;
- roadmap;
- backlog;
- engineering phases;
- verification strategy;
- software assurance strategy;
- release strategy;
- governance;
- Knowledge Source registration guidance;
- documentation;
- engineering prompts;
- engineering checklists;
- engineering principles;
- `.aikb/engineering-program-manifest.json`.

The Engineering Program Manifest records the program identifier, generation timestamp, Knowledge Base version, generator version, Certified Knowledge version, input Knowledge Sources, generated artifacts and traceability references.

## Evolve Command Architecture

Example:

```text
aikb evolve --program /tmp/verification-platform-program
```

Conceptual evolution flow:

```text
Existing Engineering Program
->
Knowledge Comparison
->
Gap Detection
->
Impact Analysis
->
Evolution Recommendations
->
Engineering Review
->
Approved Evolution
```

`aikb evolve` loads `.aikb/engineering-program-manifest.json`, compares the program traceability references with current Certified Knowledge, classifies knowledge drift and renders recommendations.

Supported drift classes:

- no drift
- minor drift
- moderate drift
- major drift
- critical drift

Supported recommendation categories include architecture improvements, verification improvements, software assurance improvements, roadmap evolution, backlog evolution, governance evolution, documentation evolution, knowledge integration and publication refresh.

The command is read-only. It prepares proposals for human review and does not update the program manifest automatically.

## Validate Command Architecture

Example:

```text
aikb validate --knowledge
```

Conceptual validation flow:

```text
Knowledge Base
->
Structural Validation
->
Relationship Validation
->
Traceability Validation
->
Consistency Validation
->
Certification Validation
->
Publication Validation
->
Repository Qualification
```

Supported scopes:

- `--knowledge`
- `--publications`
- `--sources`

When no scope is provided, `aikb validate` validates the repository, sources, knowledge and publications together.

Qualification decisions include:

- `KNOWLEDGE_VALID`
- `TRACEABILITY_VALID`
- `RELATIONSHIPS_VALID`
- `CERTIFICATION_VALID`
- `PUBLICATION_VALID`
- `REPOSITORY_VALID`

Validation is read-only. Findings are governance inputs and do not approve or perform remediation.

## Improve Command Architecture

Example:

```text
aikb improve knowledge
```

Conceptual improvement flow:

```text
Knowledge Base
->
Repository Metrics
->
Improvement Analysis
->
Improvement Opportunities
->
Engineering Review
->
Approved Improvements
```

Supported areas:

- `knowledge`
- `generators`
- `publications`
- `repository`
- `cli`

When no area is provided, `aikb improve` analyzes all supported areas.

Every recommendation includes objective metrics, supporting evidence, engineering rationale, estimated effort, engineering value and a governance path.

The command is read-only. Recommendations are proposals and do not approve or implement improvements.

## Agent Command Architecture

The future Multi-Agent Engineering Runtime may expose an `aikb agent` namespace.

Conceptual commands:

```text
aikb agent list
aikb agent run
aikb agent explain
aikb agent trace
```

These commands are architecture only and are not implemented by the current CLI runtime.

Conceptual runtime flow:

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

Agent commands must consume Certified Knowledge through the Knowledge Consumption Layer. Agents must not modify Certified Knowledge, approve certification, change governance, or treat publications as the primary source.

The canonical Multi-Agent Engineering Runtime architecture is defined in [../multi-agent-runtime/README.md](../multi-agent-runtime/README.md).

## Runtime Orchestrator Command Architecture

The future Engineering Runtime Orchestrator may expose direct orchestration commands.

Conceptual commands:

```text
aikb run
aikb plan
aikb explain-plan
aikb trace-run
aikb show-graph
```

These commands are architecture only and are not implemented by the current CLI runtime.

Conceptual orchestration flow:

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

The orchestrator plans work, builds dependency graphs, assigns agent roles, validates outputs and prepares human approval checkpoints. It does not perform engineering work itself, implement agents, schedule runtime execution, approve governance, or modify Certified Knowledge.

The detailed orchestrator architecture is defined in [../multi-agent-runtime/orchestrator.md](../multi-agent-runtime/orchestrator.md).

## Capability Command Architecture

The future Capability Extension Framework may expose an `aikb capability` namespace.

Conceptual commands:

```text
aikb capability list
aikb capability info
aikb capability enable
aikb capability disable
aikb capability validate
```

These commands are architecture only and are not implemented by the current CLI runtime.

Conceptual capability flow:

```text
Engineer Goal
->
Capability Selection
->
Knowledge Retrieval
->
Execution Plan
->
Agent Orchestration
->
Engineering Deliverables
```

The Runtime remains generic. Capabilities provide engineering behavior, consume Certified Knowledge and preserve traceability. The canonical Capability Extension Framework is defined in [../capabilities/README.md](../capabilities/README.md).

## Goal Command Architecture

The future Goal-Driven Engineering Orchestration framework may expose goal planning commands.

Conceptual commands:

```text
aikb goal
aikb explain-goal
aikb show-plan
aikb trace-goal
aikb simulate-goal
```

These commands are architecture only and are not implemented by the current CLI runtime.

Conceptual goal flow:

```text
Engineer Goal
->
Knowledge Interpretation
->
Capability Discovery
->
Capability Composition
->
Execution Plan
->
Engineering Runtime
->
Engineering Deliverables
```

The engineer specifies WHAT. The platform determines HOW by composing capabilities, retrieving Certified Knowledge, preparing execution plans and surfacing human review checkpoints.

The canonical Goal-Driven Engineering Orchestration Framework is defined in [../goal-orchestration/README.md](../goal-orchestration/README.md).

## AI Support

The CLI may prepare for future AI assistance.

AI may assist commands by:

- summarizing knowledge
- recommending templates
- explaining rationale
- drafting repository outputs
- preparing onboarding packets
- suggesting relationships
- preparing publication drafts

AI must never:

- modify Certified Knowledge directly
- certify knowledge
- approve governance decisions
- change repository history
- become authoritative

## Versioning

The CLI ships together with the Knowledge Base.

Rules:

- one repository
- one release
- one version
- CLI consumes the matching Knowledge Base version
- generated outputs should record the Knowledge Base version or source snapshot used

## Framework Relationships

| Framework | Relationship |
| --- | --- |
| [Knowledge Consumption Layer](../knowledge-consumption/README.md) | Defines how CLI commands read canonical knowledge. |
| [Templates](../templates/README.md) | Defines non-intelligent structure consumed by generators. |
| [Generators](../generators/README.md) | Defines replaceable generation units orchestrated by the CLI. |
| [Prompts](../prompts/README.md) | Defines prompt assets for future AI-assisted command behavior. |
| [Operating Model](../operating-model/README.md) | Defines roles, rhythms, and governance boundaries for CLI use. |
| [Certified Knowledge](../certified/README.md) | Provides canonical engineering source knowledge. |

## Success Criteria

The CLI architecture is valid when:

- the CLI remains thin;
- Certified Knowledge remains the engineering brain;
- commands consume knowledge instead of duplicating it;
- generators and templates remain replaceable;
- AI support remains non-authoritative;
- future implementation can proceed without redesigning the Knowledge Base.
