# EO-DJCONNECT-004: DJConnect established Coverage Baseline 1 for Home Assistant, Apple and Raspberry Pi

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `EO-DJCONNECT-004` |
| Lifecycle state | Repository Observation |
| Knowledge Source | `KS-DJCONNECT-001` |
| Source repository | `pcvantol/djconnect` |
| Repository location | `https://github.com/pcvantol/djconnect` |
| Engineering domain | Verification, Software Assurance |
| Observation type | Coverage milestone |
| Observation date | 2026-07-12 |
| Extraction date | 2026-07-12 |
| Confidence | High |
| Candidate status | Not created |

## Summary

The `pcvantol/djconnect` repository recorded `CROSS_PLATFORM_COVERAGE_BASELINE_ESTABLISHED` for Home Assistant, Apple and Raspberry Pi using Verification Runtime `1.1.0`.

## Observed Evidence

The evidence file `CODE_COVERAGE_BASELINE_1.md` records Coverage Baseline 1 as the first cross-platform native code coverage measurement ingested by Verification Runtime `1.1.0`.

The evidence records coverage entries for:

- Home Assistant repository `pcvantol/djconnect` at commit `9bedd037f87ac4c359da5dee5f63bddacf37cd74`
- Apple repository `pcvantol/djconnect-app` at commit `6062ddd8e1367bf52c1666b3e2c95514d189a9cf`
- Raspberry Pi repository `pcvantol/djconnect-pi` at commit `ef9300e6b3a1d3c23311b52beaff0872d023a32b`

The file records runtime image `pcvantol/djconnect-verification-platform:1.1.0`, immutable digest `sha256:3f0b8d3ba5f07afa5c8f05cd305dd92c43806e0fed24395be96d832e7ef72619`, and coverage qualifications `COVERAGE_VALID` for all three entries.

## Traceability References

- Knowledge Source: `KS-DJCONNECT-001`
- Repository: `pcvantol/djconnect`
- Evidence file: `CODE_COVERAGE_BASELINE_1.md`
- Evidence commit: `0e90b1b3a853a4bfa8db415f98000b953d4eaba8`
- Commit date: 2026-07-12
- Commit subject: `docs(coverage): establish Pi baseline after native coverage fix`
- Engineering activity: Coverage Baseline 1 documentation and runtime ingestion record

## Related Repositories

- `pcvantol/djconnect-app`
- `pcvantol/djconnect-pi`

## Observation Boundary

This observation records repository-specific coverage evidence only. It does not create a Knowledge Candidate or define coverage policy.
