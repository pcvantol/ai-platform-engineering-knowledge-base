# EO-DJCONNECT-007: Apple client adopted the canonical Profile Platform contract in the shared contract layer

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `EO-DJCONNECT-007` |
| Lifecycle state | Repository Observation |
| Knowledge Source | `KS-DJCONNECT-001` |
| Source repository | `pcvantol/djconnect-app` |
| Repository location | `https://github.com/pcvantol/djconnect-app` |
| Engineering domain | Client Engineering, Architecture |
| Observation type | Capability addition |
| Observation date | 2026-07-10 |
| Extraction date | 2026-07-12 |
| Confidence | High |
| Candidate status | Not created |

## Summary

The `pcvantol/djconnect-app` repository recorded Apple Profile Platform adoption in the shared Apple client contract layer.

## Observed Evidence

The evidence file `APPLE_PROFILE_ADOPTION_REPORT.md` records that Epic 3B Phase 2 adopted the canonical Home Assistant Profile Platform contract in the shared Apple client contract layer.

The evidence records that Apple remains the reference renderer and Home Assistant remains authoritative for Profile resolution, Music DNA, recommendations, Ask DJ history, mood persistence, household state, identity and music backend routing.

The evidence records implemented items including `DJConnectProfileContext`, profile-aware request wrapping, profile context support across Ask DJ, commands, Music DNA, Discover, Track Insight, HTTP Discover feed requests and raw voice upload headers, canonical response metadata decoding, structured Profile Platform failure classification, and canonical Profile context fixtures and tests.

## Traceability References

- Knowledge Source: `KS-DJCONNECT-001`
- Repository: `pcvantol/djconnect-app`
- Evidence file: `APPLE_PROFILE_ADOPTION_REPORT.md`
- Evidence commit: `a743e3e2fbde5dd4cb82d6d56df521a99cc8a6c6`
- Commit date: 2026-07-10
- Commit subject: `Adopt Apple profile context contract (#11)`
- Engineering activity: Apple Profile Platform contract adoption

## Related Repositories

- `pcvantol/djconnect`
- `pcvantol/djconnect-windows`
- `pcvantol/djconnect-pi`

## Observation Boundary

This observation records repository-specific Apple client evidence only. It does not create a Knowledge Candidate or generalize Profile Platform adoption.
