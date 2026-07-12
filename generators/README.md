# Generator Architecture

This area defines the canonical architecture for future generators orchestrated by the AI Platform Engineering CLI.

Generators consume Certified Knowledge, templates, and configuration. Generators remain replaceable. Generators do not contain canonical engineering intelligence.

This area contains generator architecture and registered generator documentation. Implemented generators include [project-bootstrap](./project-bootstrap/README.md) and [engineering-program](./engineering-program/README.md).

Future capabilities may declare supported generators through the [Capability Extension Framework](../capabilities/README.md). Capability registration does not make generator output canonical.

## Core Principle

```text
Certified Knowledge
->
Template
->
Generator
->
Derived Output
```

Generators instantiate. Certified Knowledge decides.

## Generator Responsibilities

Generators may produce:

- repository bootstrap outputs;
- onboarding packets;
- extraction proposals;
- classification packets;
- review packets;
- certification readiness packets;
- publication drafts;
- documentation drafts;
- health reports;
- backlogs;
- complete Engineering Programs.

Generators must not:

- duplicate Certified Knowledge;
- modify Certified Knowledge;
- certify knowledge;
- approve publications;
- change governance;
- treat generated output as canonical;
- hide source knowledge identifiers.

## Engineering Action Boundary

Current generators create derived outputs in explicitly selected output locations. They do not modify registered Knowledge Sources.

Any future generator or engineering action that can propose or apply repository changes must be separately invoked by an engineer, state that repository changes may occur, require an explicit target repository, and preserve traceability from Certified Knowledge to the resulting repository commit. No knowledge operation may invoke such an action implicitly.

## Generator Inputs

Canonical generator inputs:

- Certified Knowledge;
- Knowledge Object metadata;
- relationships;
- traceability references;
- templates;
- configuration;
- command context;
- target output type.

## Generator Outputs

Generated outputs are derived artifacts.

Every generator output should identify:

- source Certified Knowledge;
- source Knowledge Base version or snapshot;
- template used;
- generator used;
- configuration used;
- traceability references;
- governance status.

## Replaceability

Generators should remain replaceable.

Rules:

- generator interfaces should be stable;
- generator outputs should preserve traceability;
- generator behavior should be deterministic where practical;
- replacing a generator must not change Certified Knowledge;
- generator implementation details must not become canonical knowledge.

## AI-Assisted Generation

AI may assist generation by drafting, summarizing, adapting, and explaining.

AI-assisted generator outputs remain proposals or derived artifacts until governed review approves their use.
