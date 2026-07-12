# EO-DJCONNECT-026: DJConnect coverage baselines preserve release evidence without mutating prior baselines

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `EO-DJCONNECT-026` |
| Lifecycle state | Repository Observation |
| Observation status | Accepted |
| Source repository | `pcvantol/djconnect` |
| Knowledge Source | `KS-DJCONNECT-001` |
| Engineering domain | Release Engineering |
| Observation type | Baseline evidence |
| Confidence | High |
| Candidate status | Created as `KC-DJCONNECT-026` |

## Summary

DJConnect records coverage baselines and later Windows coverage records as release evidence while preserving earlier baselines as historical references.

## Supporting Evidence

| Evidence | Repository | Commit |
| --- | --- | --- |
| `CODE_COVERAGE_BASELINE_1.md` | `pcvantol/djconnect` | `07178bad48d3bb8ad977e6b9070abfdf444889b4` |
| Windows coverage baseline record | `pcvantol/djconnect` | `07178bad48d3bb8ad977e6b9070abfdf444889b4` |

## Traceability

`EO-DJCONNECT-026` -> `KS-DJCONNECT-001` -> `pcvantol/djconnect` -> baseline release evidence.

## Boundary

This observation records baseline preservation. It does not certify release quality by itself.
