# Knowledge Consumption Layer

This area defines the canonical Knowledge Consumption Layer used by future runtime interfaces such as the AI Platform Engineering CLI.

The Knowledge Consumption Layer reads the Knowledge Base. It does not become the Knowledge Base.

This layer defines the consumption contract used by CLI implementations. The current runtime consumes Certified Knowledge and repository metadata for `aikb init`, `aikb ask`, `aikb generate`, `aikb evolve`, `aikb validate`, and `aikb improve`.

## Core Principle

Certified Knowledge remains authoritative.

Consumption layers provide access, selection, traceability, and orchestration support.

```text
Certified Knowledge
->
Knowledge Relationships
->
Evidence and Rationale
->
Consumption Layer
->
CLI or Other Interface
```

## Responsibilities

The Knowledge Consumption Layer defines how consumers should:

- locate Certified Knowledge;
- resolve Knowledge Object metadata;
- follow relationships;
- preserve lineage;
- identify source evidence;
- identify publication eligibility;
- select templates;
- provide generators with canonical inputs;
- answer questions from Certified Knowledge first;
- report traceability in outputs.

The layer must not:

- change Certified Knowledge;
- certify knowledge;
- treat publications as canonical source;
- hide uncertainty;
- remove lineage;
- embed engineering intelligence outside Certified Knowledge.

## Consumption Order

Canonical consumption order for engineering answers:

```text
Certified Knowledge
->
Relationships
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
```

Publications may be consulted for audience adaptation, but they must not override Certified Knowledge.

## Consumption Outputs

Consumption outputs may include:

- command responses
- repository bootstrap plans
- onboarding packets
- extraction proposals
- classification suggestions
- review packets
- certification readiness reports
- publication drafts
- health reports
- engineering answers

All outputs are derived artifacts unless entered into the Knowledge Lifecycle through governed review.

## Traceability

Every consumed answer or generated output should preserve traceability:

```text
Output
->
Certified Knowledge
->
Knowledge Object Lineage
->
Evidence
->
Knowledge Source
->
Repository
```

When an output uses AI assistance, the output should distinguish sourced knowledge, inference, and uncertainty.

## Versioning

The Knowledge Consumption Layer consumes the matching Knowledge Base version.

Generated outputs should record:

- Knowledge Base version or source snapshot;
- source Certified Knowledge identifiers;
- template identifier when applicable;
- generator identifier when applicable;
- command or workflow context when applicable.

## Relationship to CLI

The CLI should call the Knowledge Consumption Layer before selecting templates, executing generators, publishing content, answering questions, or reporting health.

The CLI orchestrates. The Knowledge Consumption Layer resolves canonical knowledge inputs.

## Engineering Assistant Consumption

`aikb ask` consumes Certified Knowledge first.

It may use:

- Certified Knowledge metadata;
- relationship references;
- supporting Generalized Knowledge identifiers;
- supporting Knowledge Concept identifiers;
- supporting Knowledge Candidate identifiers;
- supporting Engineering Observation identifiers;
- evidence files and commits.

It must not use markdown documentation as the primary authority. It must not modify Certified Knowledge or create new lifecycle objects.

## Engineering Program Consumption

`aikb generate` consumes Certified Knowledge to produce complete Engineering Programs.

Generated Engineering Programs may include:

- architecture;
- governance;
- roadmap;
- backlog;
- engineering phases;
- verification strategy;
- software assurance strategy;
- release strategy;
- engineering guidance;
- prompts;
- checklists;
- an Engineering Program Manifest.

The generated program remains derived. It must preserve traceability to Certified Knowledge, supporting evidence and Knowledge Sources.

## Engineering Program Evolution Consumption

`aikb evolve` consumes:

- an existing Engineering Program Manifest;
- current Certified Knowledge;
- recorded traceability references;
- generated artifact lists;
- evidence references.

It produces Evolution Reports and proposals. It must not update the program, accept recommendations, reject recommendations, or modify canonical knowledge.

## Validation Consumption

`aikb validate` consumes:

- Knowledge Source records;
- lifecycle Knowledge Objects;
- relationship references;
- traceability references;
- Certified Knowledge metadata;
- publication references;
- repository structure.

It produces Validation Reports, Knowledge Scorecards and qualification decisions. It must not repair findings, modify knowledge, rewrite publications or approve remediation.

Future Engineering Operating System qualification workflows may consume validation outputs as evidence. Qualification remains governed separately by the [Engineering Operating System Qualification Framework](../qualification/README.md).

## Improvement Consumption

`aikb improve` consumes:

- repository metrics;
- validation evidence;
- knowledge object counts;
- publication references;
- generator and template inventory;
- CLI capability inventory.

It produces Improvement Reports and recommendations. It must not modify repositories, Certified Knowledge, publications, templates, governance or engineering history.

## Mission Runtime Consumption

Future `aikb mission` workflows consume Certified Knowledge through this layer before planning or executing mission work.

Mission Runtime consumption may use:

- Certified Knowledge;
- Knowledge Object relationships;
- evidence lineage;
- capability metadata;
- validation reports;
- generated artifact manifests;
- prior Mission Reports when treated as derived evidence.

Mission Runtime consumption must preserve traceability from mission outputs back to Certified Knowledge, supporting lifecycle objects, evidence, Knowledge Sources and repositories. Mission feedback must not modify Certified Knowledge directly.

## Multi-Agent Runtime Consumption

Future Engineering Agents consume knowledge through this layer.

Agents may consume:

- Certified Knowledge;
- Knowledge Relationships;
- supporting evidence;
- Knowledge Source identifiers;
- repository and commit references preserved by Certified Knowledge.

Agents must not use publications as primary authority, modify Certified Knowledge, approve governance decisions, or hide traceability.

## Engineering Runtime Orchestrator Consumption

The Engineering Runtime Orchestrator consumes Certified Knowledge before task planning.

It may consume:

- engineering goals;
- Certified Knowledge;
- Knowledge Relationships;
- engineering rationale;
- validation reports;
- generated program manifests;
- derived artifacts with manifest traceability.

It produces execution plans, task graphs, validation gates and traceability requirements. It must not execute agents as an authority, modify knowledge, approve governance, or treat derived artifacts as canonical.

## Goal-Orchestration Consumption

Goal-driven orchestration consumes Certified Knowledge to interpret engineering goals.

It may consume:

- goal descriptions;
- constraints and success criteria;
- Certified Knowledge;
- Knowledge Relationships;
- capability metadata;
- validation requirements;
- publication requirements.

It produces Capability Graphs, execution plans, review plans and traceability requirements. It must not execute runtime tasks, approve engineering work, modify Certified Knowledge or invent evidence.

## Capability Consumption

Capabilities consume Certified Knowledge through this layer.

Capabilities may request:

- Certified Knowledge by identifier, domain or category;
- Knowledge Relationships;
- Engineering Rationale;
- Evidence;
- Knowledge Source and repository references.

Capabilities must not duplicate Certified Knowledge as embedded logic, modify canonical knowledge, or treat publications as primary authority.
