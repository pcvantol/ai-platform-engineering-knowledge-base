# CK-DJCONNECT-009: Independent Software Assurance Governance

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `CK-DJCONNECT-009` |
| Lifecycle state | Certified Knowledge |
| Certification status | Certified |
| Certification date | 2026-07-12 |
| Originating Generalized Knowledge | `GK-DJCONNECT-009` |
| Knowledge category | Architecture |
| Engineering domains | Software Assurance Engineering |
| Abstraction level | Canonical |
| Confidence | High |
| Publication eligibility | Eligible |
| Certification record | [2026-07-12 Software Assurance Engineering Population Certification](../../certification/cycles/2026-07-12-generation-2-software-assurance-engineering-population.md) |

## Certified Statement

Software Assurance should be governed as a discipline separate from behavioral verification while consuming verification, release qualification and platform health evidence.

## Engineering Rationale

Separating assurance governance from behavioral verification prevents tests from becoming the only confidence mechanism and makes evidence, release readiness and platform health reviewable assurance inputs.

## Traceability

`CK-DJCONNECT-009` -> `GK-DJCONNECT-009` -> `KCN-DJCONNECT-009` -> `KC-DJCONNECT-017`, `KC-DJCONNECT-020` -> `EO-DJCONNECT-017`, `EO-DJCONNECT-020` -> `KS-DJCONNECT-001`.

## Source Evidence

| Observation | Repository | Evidence | Commit |
| --- | --- | --- | --- |
| `EO-DJCONNECT-017` | `pcvantol/djconnect` | `SOFTWARE_ASSURANCE_PLATFORM.md` | `07178bad48d3bb8ad977e6b9070abfdf444889b4` |
| `EO-DJCONNECT-020` | `pcvantol/djconnect` | `SOFTWARE_ASSURANCE_PLATFORM.md`, platform qualification reports | `07178bad48d3bb8ad977e6b9070abfdf444889b4` |
