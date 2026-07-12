# CK-DJCONNECT-003: Software Assurance Governance Separation

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `CK-DJCONNECT-003` |
| Lifecycle state | Certified Knowledge |
| Certification status | Certified |
| Certification date | 2026-07-12 |
| Originating Generalized Knowledge | `GK-DJCONNECT-003` |
| Knowledge category | Architecture |
| Engineering domains | Software Assurance, Governance |
| Abstraction level | Canonical |
| Confidence | High |
| Publication eligibility | Eligible |
| Certification record | [2026-07-12 First Knowledge Certification Cycle](../../certification/cycles/2026-07-12-first-certification-cycle.md) |

## Certified Statement

Software assurance governance must be separated from behavioural verification while remaining connected to verification evidence, release qualification, and platform health.

Behavioural verification determines whether a system behaves as expected. Software assurance governance evaluates whether the engineering system can build, verify, release, and evolve the system safely.

## Engineering Rationale

Behavioural tests alone do not establish engineering-system trust. Separating software assurance governance allows source quality, supply chain posture, runtime robustness, execution strategy, release assurance, evidence, reporting, and platform health to be governed deliberately.

## Applicability

This knowledge applies to engineering platforms where verification, quality evidence, release readiness, and long-term platform health must be governed as separate but related concerns.

## Constraints

- Verification and assurance remain connected through evidence.
- Assurance governance does not replace product architecture or behavioural scenarios.
- CI systems, runners, and tools are execution surfaces, not the owner of governance.

## Traceability

```text
CK-DJCONNECT-003
->
GK-DJCONNECT-003
->
KCN-DJCONNECT-003
->
KC-DJCONNECT-006
->
EO-DJCONNECT-006
->
KS-DJCONNECT-001
->
pcvantol/djconnect
->
SOFTWARE_ASSURANCE_PLATFORM.md
->
bdd49e640212f615df3993259aa83bd0ca5f078b
```

## Source Evidence

| Observation | Repository | Evidence | Commit |
| --- | --- | --- | --- |
| `EO-DJCONNECT-006` | `pcvantol/djconnect` | `SOFTWARE_ASSURANCE_PLATFORM.md` | `bdd49e640212f615df3993259aa83bd0ca5f078b` |

## Relationships

| Relationship | Target | Direction | Rationale |
| --- | --- | --- | --- |
| supports | `CK-DJCONNECT-002` | this knowledge -> target | Assurance governance provides context for evidence and baseline provenance. |
| related to | `CK-DJCONNECT-001` | this knowledge -> target | Verification adapter boundaries are part of the verification side of the assurance boundary. |

## Certification Rationale

Certified because the originating Generalized Knowledge is project independent, internally consistent, technology independent, and includes explicit constraints separating governance from execution tools and behavioural scenarios.

## Revision History

| Date | Change |
| --- | --- |
| 2026-07-12 | Initial certification from `GK-DJCONNECT-003`. |
