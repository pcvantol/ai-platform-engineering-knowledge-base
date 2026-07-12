# CK-DJCONNECT-014: Immutable Release Baseline

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `CK-DJCONNECT-014` |
| Lifecycle state | Certified Knowledge |
| Certification status | Certified |
| Certification date | 2026-07-12 |
| Originating Generalized Knowledge | `GK-DJCONNECT-014` |
| Knowledge category | Governance |
| Engineering domains | Release Engineering |
| Abstraction level | Canonical |
| Confidence | High |
| Publication eligibility | Eligible |
| Certification record | [2026-07-12 Release Engineering Population Certification](../../certification/cycles/2026-07-12-generation-2-release-engineering-population.md) |

## Certified Statement

Release baselines should preserve historical comparison points while treating architecture freeze, qualification and baseline certification as distinct decisions.

## Engineering Rationale

Immutable baselines and separated release decisions prevent later work from rewriting prior evidence and help reviewers understand which decision was actually made.

## Traceability

`CK-DJCONNECT-014` -> `GK-DJCONNECT-014` -> `KCN-DJCONNECT-014` -> `KC-DJCONNECT-026`, `KC-DJCONNECT-027` -> `EO-DJCONNECT-026`, `EO-DJCONNECT-027` -> `KS-DJCONNECT-001`.

## Source Evidence

| Observation | Repository | Evidence | Commit |
| --- | --- | --- | --- |
| `EO-DJCONNECT-026` | `pcvantol/djconnect` | coverage baseline records | `07178bad48d3bb8ad977e6b9070abfdf444889b4` |
| `EO-DJCONNECT-027` | `pcvantol/djconnect` | `PLATFORM_STRATEGY.md`, `ARCHITECTURE_DECISION.md` | `07178bad48d3bb8ad977e6b9070abfdf444889b4` |
