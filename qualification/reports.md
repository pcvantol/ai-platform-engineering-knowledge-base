# Qualification Reports

This document defines the canonical structure for Engineering Operating System Qualification Reports.

Qualification Reports are reproducible evidence artifacts. They are not Certified Knowledge and they do not approve themselves.

## Report Structure

Every Qualification Report should include:

| Section | Purpose |
| --- | --- |
| Executive summary | Management-level outcome, qualification status and high-level risks. |
| Qualification scope | Platform areas, repository snapshot, commands, configuration and exclusions. |
| Evidence package | Validation reports, scorecards, health reports and source references used. |
| Validation results | Findings by qualification area and severity. |
| Qualification decisions | Decision table with pass, fail, warning or exception outcomes. |
| Traceability | Decision-to-evidence-to-knowledge lineage. |
| Reproducibility | Inputs and steps required to reproduce the report. |
| Governance status | Required approvals, open decisions, exceptions and follow-up actions. |

## Qualification Status

Supported report-level statuses:

| Status | Meaning |
| --- | --- |
| `QUALIFIED` | All required decisions pass. |
| `QUALIFIED_WITH_EXCEPTIONS` | Required decisions pass with governed exceptions. |
| `NOT_QUALIFIED` | One or more required decisions fail. |
| `INCOMPLETE` | Required validation evidence is missing. |
| `REVIEW_REQUIRED` | Qualification cannot be concluded without governance review. |

## Evidence Package

An Evidence Package should include:

- validation report;
- knowledge scorecard;
- runtime scorecard;
- mission scorecard when mission scope is included;
- capability registry scorecard when capabilities are included;
- publication integrity report;
- repository health report;
- management summary.

Evidence must remain reproducible and traceable.

## Example Qualification Report

```text
Qualification Report: QR-EXAMPLE-OPERATING-SYSTEM-001
Scope: knowledge, runtime, missions, capabilities, generators, templates, publications, repository
Status: QUALIFIED

Decisions:
- KNOWLEDGE_PLATFORM_VALID: PASS
- TRACEABILITY_VALID: PASS
- ENGINEERING_RUNTIME_VALID: PASS
- MISSION_RUNTIME_VALID: PASS
- CAPABILITY_REGISTRY_VALID: PASS
- PUBLICATION_VALID: PASS
- OPERATING_SYSTEM_QUALIFIED: PASS

Evidence:
- Validation Report: current repository validation snapshot
- Knowledge Scorecard: lifecycle objects, Certified Knowledge, traceability and relationships
- Runtime Scorecard: orchestrator, capability, goal and mission architecture checks
- Repository Health Report: structure, indexes, scope boundaries and governance links

Traceability:
Qualification Decision
->
Validation Results
->
Knowledge Objects
->
Certified Knowledge
->
Evidence
->
Knowledge Sources
->
Repositories

Governance:
Qualification outcome requires human governance review before release or management acceptance.
```

The example demonstrates report shape only. It is not an actual qualification decision.
