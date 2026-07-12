# Template Architecture

This area defines the canonical architecture for templates consumed by future generators and CLI commands.

Templates remain data. Templates contain no engineering intelligence. Engineering intelligence remains inside Certified Knowledge.

This area contains template architecture and the first passive project bootstrap template. Template rendering is implemented by the CLI runtime.

## Core Principle

Templates provide structure.

Certified Knowledge provides engineering meaning.

Generators instantiate templates using Certified Knowledge and configuration.

## Template Responsibilities

Templates may define:

- file and folder structure;
- document skeletons;
- repository skeletons;
- publication layouts;
- onboarding packet layouts;
- review packet layouts;
- configuration placeholders;
- traceability placeholder locations.

Templates must not:

- encode engineering decisions;
- duplicate Certified Knowledge;
- become canonical knowledge;
- certify knowledge;
- hide source traceability;
- contain project-specific assumptions unless explicitly scoped as a template parameter.

## Template Inputs

Templates may consume:

- Certified Knowledge identifiers;
- Knowledge Object metadata;
- generator configuration;
- target repository name;
- target publication type;
- audience;
- governance requirements;
- traceability metadata.

## Template Selection

Template selection should be driven by:

- requested command;
- target output type;
- Certified Knowledge scope;
- engineering domain;
- audience;
- governance requirements;
- user-provided configuration.

AI may recommend templates, but template selection must remain explainable and reviewable.

## Versioning

Templates ship with the Knowledge Base and CLI.

Template outputs should record:

- template identifier;
- template version or source snapshot;
- Knowledge Base version;
- source Certified Knowledge identifiers;
- generator identifier when applicable.

## Implemented Templates

| Template | Purpose | Status |
| --- | --- | --- |
| [project-bootstrap/basic](./project-bootstrap/basic) | Passive structure for generated engineering repositories. | Implemented |
