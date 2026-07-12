# GK-DJCONNECT-003: Software Assurance Governance Separation

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `GK-DJCONNECT-003` |
| Lifecycle state | Generalized Knowledge |
| Review status | Certification Completed |
| Certification status | Certified as `CK-DJCONNECT-003` |
| Knowledge category | Architecture |
| Engineering domains | Software Assurance, Governance |
| Abstraction level | Technology Independent |
| Confidence | Medium |
| Knowledge sources | `KS-DJCONNECT-001` |

## Summary

Software assurance governance should be separated from behavioural verification while remaining connected to verification evidence, release qualification and platform health.

Behavioural verification determines whether a system behaves as expected. Software assurance governance evaluates whether the engineering system can build, verify, release and evolve the system safely.

This item remains the Generalized Knowledge source for certified item `CK-DJCONNECT-003`.

## Engineering Rationale

Separating these responsibilities prevents behavioural test execution from becoming the only measure of trust. It allows quality themes such as source quality, supply chain posture, runtime robustness, execution strategy, release assurance, evidence, reporting and platform health to be governed deliberately.

## Preserved Constraints

- Verification and assurance remain connected through evidence.
- Assurance governance does not replace product architecture or behavioural scenarios.
- Execution tools and CI environments are execution surfaces, not the owner of governance.

## Supporting Concepts

- [KCN-DJCONNECT-003](../../concepts/djconnect/KCN-DJCONNECT-003.md)

## Supporting Candidates

- [KC-DJCONNECT-006](../../candidates/djconnect/KC-DJCONNECT-006.md)

## Supporting Observations

- [EO-DJCONNECT-006](../../observations/djconnect/EO-DJCONNECT-006.md)

## Source Evidence

| Observation | Knowledge Source | Repository | Evidence | Commit |
| --- | --- | --- | --- | --- |
| `EO-DJCONNECT-006` | `KS-DJCONNECT-001` | `pcvantol/djconnect` | `SOFTWARE_ASSURANCE_PLATFORM.md` | `bdd49e640212f615df3993259aa83bd0ca5f078b` |

## Relationships

| Relationship | Target | Direction | Rationale |
| --- | --- | --- | --- |
| supports | `GK-DJCONNECT-002` | this knowledge -> target | Assurance governance provides context for evidence and baseline provenance. |
| related to | `GK-DJCONNECT-001` | this knowledge -> target | Verification adapter boundaries are part of the verification side of the assurance boundary. |

## Traceability

```text
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

## Generalization Notes

Removed DJConnect platform names from the main knowledge statement. Preserved the distinction between behavioural correctness and engineering-system trust.

## Certification Boundary

This item was certified as `CK-DJCONNECT-003` on 2026-07-12. Future material changes require governed re-certification.
