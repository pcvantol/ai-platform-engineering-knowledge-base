# KCN-DJCONNECT-002: Coverage Baseline Provenance

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `KCN-DJCONNECT-002` |
| Lifecycle state | Knowledge Concept |
| Knowledge Source | `KS-DJCONNECT-001` |
| Review status | Awaiting Review |
| Certification status | Candidate |
| Knowledge category | Workflow |
| Engineering domains | Verification, Software Assurance, Client Engineering |
| Abstraction level | Reusable |
| Confidence | Medium |
| Source repositories | `pcvantol/djconnect`, `pcvantol/djconnect-app`, `pcvantol/djconnect-pi`, `pcvantol/djconnect-windows` |

## Concept Summary

Coverage Baseline Provenance is the normalized DJConnect concept that coverage baselines and post-baseline records preserve source repository commits, runtime version, report provenance, qualification status and baseline history.

This concept is not generalized and not certified.

## Supporting Candidates

- [KC-DJCONNECT-004](../../candidates/djconnect/KC-DJCONNECT-004.md)
- [KC-DJCONNECT-005](../../candidates/djconnect/KC-DJCONNECT-005.md)

## Supporting Observations

- [EO-DJCONNECT-004](../../observations/djconnect/EO-DJCONNECT-004.md)
- [EO-DJCONNECT-005](../../observations/djconnect/EO-DJCONNECT-005.md)

## Source Evidence

| Candidate | Observation | Repository | Evidence | Commit |
| --- | --- | --- | --- | --- |
| `KC-DJCONNECT-004` | `EO-DJCONNECT-004` | `pcvantol/djconnect` | `CODE_COVERAGE_BASELINE_1.md` | `0e90b1b3a853a4bfa8db415f98000b953d4eaba8` |
| `KC-DJCONNECT-005` | `EO-DJCONNECT-005` | `pcvantol/djconnect` | `CODE_COVERAGE_WINDOWS_BASELINE_1.md` | `08ebcaf7332f82f955dc7f6981842d1f1be486b1` |

Referenced coverage commits:

- `pcvantol/djconnect`: `9bedd037f87ac4c359da5dee5f63bddacf37cd74`
- `pcvantol/djconnect-app`: `6062ddd8e1367bf52c1666b3e2c95514d189a9cf`
- `pcvantol/djconnect-pi`: `ef9300e6b3a1d3c23311b52beaff0872d023a32b`
- `pcvantol/djconnect-windows`: `b205f087214eb5fe90c4129c2afa9dee7f836a82`

## Relationships

| Relationship | Target | Direction | Rationale |
| --- | --- | --- | --- |
| supported by | `KCN-DJCONNECT-001` | this concept <- target | Verification adapter qualification can provide evidence context for coverage qualification. |
| supported by | `KCN-DJCONNECT-003` | this concept <- target | Software Assurance governance defines why baseline evidence is relevant to platform health. |

## Traceability

```text
KCN-DJCONNECT-002
->
KC-DJCONNECT-004, KC-DJCONNECT-005
->
EO-DJCONNECT-004, EO-DJCONNECT-005
->
KS-DJCONNECT-001
->
pcvantol/djconnect and referenced DJConnect repositories
->
evidence files and commits listed above
```

## Concept Boundary

This concept preserves DJConnect coverage baseline terminology. It does not generalize a coverage model, does not define thresholds, and does not certify baseline policy.
