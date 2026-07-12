# KC-DJCONNECT-005: Windows coverage baseline is recorded as post-baseline evidence without mutating the original baseline

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `KC-DJCONNECT-005` |
| Lifecycle state | Knowledge Candidate |
| Knowledge Source | `KS-DJCONNECT-001` |
| Review status | Awaiting Review |
| Certification status | Candidate |
| Knowledge category | Decision |
| Engineering domains | Verification, Client Engineering |
| Abstraction level | Project Specific |
| Confidence | Medium |
| Source repositories | `pcvantol/djconnect`, `pcvantol/djconnect-windows` |

## Candidate Summary

DJConnect may have reusable engineering value in the decision to record Windows coverage as post-baseline evidence without modifying or retroactively extending the already established Coverage Baseline 1.

This is a candidate proposal only. It is not generalized and not certified.

## Supporting Observations

- [EO-DJCONNECT-005](../../observations/djconnect/EO-DJCONNECT-005.md)

## Supporting Evidence

| Repository | Evidence | Commit |
| --- | --- | --- |
| `pcvantol/djconnect` | `CODE_COVERAGE_WINDOWS_BASELINE_1.md` | `08ebcaf7332f82f955dc7f6981842d1f1be486b1` |

Referenced coverage commit inside the evidence:

- `pcvantol/djconnect-windows`: `b205f087214eb5fe90c4129c2afa9dee7f836a82`

## Traceability

```text
KC-DJCONNECT-005
->
EO-DJCONNECT-005
->
pcvantol/djconnect
->
CODE_COVERAGE_WINDOWS_BASELINE_1.md
->
08ebcaf7332f82f955dc7f6981842d1f1be486b1
```

## Related Candidates

- `KC-DJCONNECT-004`

## Candidate Boundary

This candidate preserves DJConnect baseline terminology. It does not generalize baseline immutability and does not certify a baseline revision policy.
