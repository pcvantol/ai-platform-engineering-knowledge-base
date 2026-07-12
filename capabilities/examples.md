# Example Capabilities

This document provides example capability definitions.

Examples are non-active. They do not implement capabilities, activate runtime behavior, modify Certified Knowledge, or change governance.

## Verification Engineering Capability

| Field | Value |
| --- | --- |
| Capability identifier | `CAP-VERIFICATION-ENGINEERING` |
| Capability name | Verification Engineering |
| Purpose | Support verification strategy, evidence planning and validation workflows. |
| Engineering domain | Verification, Software Assurance |
| Supported commands | `aikb run verification-platform`, `aikb plan verification-platform` |
| Supported generators | Engineering Program Generator |
| Supported publications | Verification guide, engineering handbook sections |
| Required Certified Knowledge | Verification and evidence-related Certified Knowledge |
| Supported agent roles | Verification Agent, Review Agent, Generator Agent |
| Supported workflows | Verification strategy, evidence review, validation planning |
| Dependencies | Multi-Agent Runtime, Engineering Runtime Orchestrator, Knowledge Consumption Layer |
| Version | `0.1.0` |
| Status | Example only |

## Software Assurance Capability

| Field | Value |
| --- | --- |
| Capability identifier | `CAP-SOFTWARE-ASSURANCE` |
| Capability name | Software Assurance |
| Purpose | Support assurance governance, qualification planning and assurance evidence workflows. |
| Engineering domain | Software Assurance, Governance |
| Supported commands | `aikb run software-assurance`, `aikb plan software-assurance` |
| Supported generators | Engineering Program Generator |
| Supported publications | Assurance guide, executive summary sections |
| Required Certified Knowledge | Software Assurance Certified Knowledge |
| Supported agent roles | Software Assurance Agent, Review Agent |
| Supported workflows | Assurance plan, qualification review, governance analysis |
| Dependencies | Multi-Agent Runtime, Engineering Runtime Orchestrator, Validation |
| Version | `0.1.0` |
| Status | Example only |

## Architecture Engineering Capability

| Field | Value |
| --- | --- |
| Capability identifier | `CAP-ARCHITECTURE-ENGINEERING` |
| Capability name | Architecture Engineering |
| Purpose | Support architecture review, architecture program generation and design rationale workflows. |
| Engineering domain | Architecture, Platform Engineering |
| Supported commands | `aikb run architecture-review`, `aikb explain-plan architecture-review` |
| Supported generators | Engineering Program Generator |
| Supported publications | Architecture Reference Guide |
| Required Certified Knowledge | Architecture Certified Knowledge |
| Supported agent roles | Architecture Agent, Software Assurance Agent |
| Supported workflows | Architecture review, program architecture, conflict analysis |
| Dependencies | Multi-Agent Runtime, Engineering Runtime Orchestrator, Knowledge Query & Retrieval |
| Version | `0.1.0` |
| Status | Example only |

## Release Engineering Capability

| Field | Value |
| --- | --- |
| Capability identifier | `CAP-RELEASE-ENGINEERING` |
| Capability name | Release Engineering |
| Purpose | Support release workflows, documentation updates and publication refresh review. |
| Engineering domain | Release Engineering, Documentation Engineering |
| Supported commands | `aikb run release-review`, `aikb evolve` |
| Supported generators | Engineering Program Generator |
| Supported publications | Release guide, operations guide |
| Required Certified Knowledge | Release Engineering Certified Knowledge |
| Supported agent roles | Release Engineering Agent, Publication Agent, Review Agent |
| Supported workflows | Release strategy, publication refresh, documentation review |
| Dependencies | Publication Framework, Continuous Evolution, Validation |
| Version | `0.1.0` |
| Status | Example only |

## Traceability Requirement

Every capability output must preserve:

```text
Engineering Result
->
Capability
->
Certified Knowledge
->
Evidence
->
Knowledge Source
->
Repository
```
