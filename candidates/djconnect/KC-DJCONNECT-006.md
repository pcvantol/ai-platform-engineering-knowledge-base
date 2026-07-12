# KC-DJCONNECT-006: Software Assurance Platform separates behavioural verification from engineering quality governance

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `KC-DJCONNECT-006` |
| Lifecycle state | Knowledge Candidate |
| Knowledge Source | `KS-DJCONNECT-001` |
| Review status | Awaiting Review |
| Certification status | Candidate |
| Knowledge category | Architecture |
| Engineering domains | Software Assurance, Governance |
| Abstraction level | Project Specific |
| Confidence | Medium |
| Source repositories | `pcvantol/djconnect` |

## Candidate Summary

DJConnect may have reusable engineering value in the architecture decision to separate behavioural verification from software assurance governance over source quality, supply chain posture, runtime robustness, execution strategy, release assurance, evidence, reporting and platform health.

This is a candidate proposal only. It is not generalized and not certified.

## Supporting Observations

- [EO-DJCONNECT-006](../../observations/djconnect/EO-DJCONNECT-006.md)

## Supporting Evidence

| Repository | Evidence | Commit |
| --- | --- | --- |
| `pcvantol/djconnect` | `SOFTWARE_ASSURANCE_PLATFORM.md` | `bdd49e640212f615df3993259aa83bd0ca5f078b` |

## Traceability

```text
KC-DJCONNECT-006
->
EO-DJCONNECT-006
->
pcvantol/djconnect
->
SOFTWARE_ASSURANCE_PLATFORM.md
->
bdd49e640212f615df3993259aa83bd0ca5f078b
```

## Related Candidates

- `KC-DJCONNECT-004`
- `KC-DJCONNECT-005`

## Candidate Boundary

This candidate preserves DJConnect Software Assurance terminology. It does not define a generalized assurance architecture and does not certify the separation as canonical knowledge.
