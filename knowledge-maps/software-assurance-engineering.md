# Software Assurance Engineering Knowledge Map

## Scope

This map covers Software Assurance Engineering knowledge derived from `KS-DJCONNECT-001`.

It maps lifecycle lineage and relationships only. Certified Knowledge remains authoritative.

## Certified Knowledge Lineage

| Certified Knowledge | Generalized Knowledge | Concept | Candidates | Observations |
| --- | --- | --- | --- | --- |
| `CK-DJCONNECT-003` | `GK-DJCONNECT-003` | `KCN-DJCONNECT-003` | `KC-DJCONNECT-006` | `EO-DJCONNECT-006` |
| `CK-DJCONNECT-009` | `GK-DJCONNECT-009` | `KCN-DJCONNECT-009` | `KC-DJCONNECT-017`, `KC-DJCONNECT-020` | `EO-DJCONNECT-017`, `EO-DJCONNECT-020` |
| `CK-DJCONNECT-010` | `GK-DJCONNECT-010` | `KCN-DJCONNECT-010` | `KC-DJCONNECT-018`, `KC-DJCONNECT-022` | `EO-DJCONNECT-018`, `EO-DJCONNECT-022` |
| `CK-DJCONNECT-011` | `GK-DJCONNECT-011` | `KCN-DJCONNECT-011` | `KC-DJCONNECT-019`, `KC-DJCONNECT-023` | `EO-DJCONNECT-019`, `EO-DJCONNECT-023` |
| `CK-DJCONNECT-012` | `GK-DJCONNECT-012` | `KCN-DJCONNECT-012` | `KC-DJCONNECT-021`, `KC-DJCONNECT-024` | `EO-DJCONNECT-021`, `EO-DJCONNECT-024` |

## Relationship Map

```text
CK-DJCONNECT-009 Independent Software Assurance Governance
  parent of CK-DJCONNECT-010 Evidence-Based Assurance Confidence Model

CK-DJCONNECT-010 Evidence-Based Assurance Confidence Model
  supports CK-DJCONNECT-011 Baseline-Gated Assurance Readiness

CK-DJCONNECT-012 Assurance Review and Reporting Traceability
  supports CK-DJCONNECT-011 Baseline-Gated Assurance Readiness

CK-DJCONNECT-003 Software Assurance Governance Separation
  related to CK-DJCONNECT-009 Independent Software Assurance Governance
```

## Assurance Flow

```text
Software Assurance
->
Engineering Governance
->
Evidence
->
Traceability
->
Engineering Confidence
->
Quality Gates
->
Risk Management
->
Readiness
->
Certification
```
