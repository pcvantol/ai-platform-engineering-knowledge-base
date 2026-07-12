# KC-DJCONNECT-008: Pi and Windows Profile Platform adoption preserves backend-owned profile resolution with client-specific boundaries

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `KC-DJCONNECT-008` |
| Lifecycle state | Knowledge Candidate |
| Knowledge Source | `KS-DJCONNECT-001` |
| Review status | Awaiting Review |
| Certification status | Candidate |
| Knowledge category | Practice |
| Engineering domains | Client Engineering, Embedded Systems |
| Abstraction level | Project Specific |
| Confidence | Medium |
| Source repositories | `pcvantol/djconnect-pi`, `pcvantol/djconnect-windows` |

## Candidate Summary

DJConnect may have reusable engineering value in the practice of preserving backend-owned Profile resolution while allowing Pi and Windows clients to adopt Profile Platform context according to their client-specific UI and privacy boundaries.

This is a candidate proposal only. It is not generalized and not certified.

## Supporting Observations

- [EO-DJCONNECT-008](../../observations/djconnect/EO-DJCONNECT-008.md)

## Supporting Evidence

| Repository | Evidence | Commit |
| --- | --- | --- |
| `pcvantol/djconnect-pi` | `PI_PROFILE_ADOPTION_REPORT.md` | `35585114ef0f745044e17eea1fcce57ab45e60ff` |
| `pcvantol/djconnect-windows` | `WINDOWS_PROFILE_ADOPTION_REPORT.md` | `37710090d05fbebe5cfb37f6f275ef7af528f569` |

## Traceability

```text
KC-DJCONNECT-008
->
EO-DJCONNECT-008
->
pcvantol/djconnect-pi
->
PI_PROFILE_ADOPTION_REPORT.md
->
35585114ef0f745044e17eea1fcce57ab45e60ff
```

```text
KC-DJCONNECT-008
->
EO-DJCONNECT-008
->
pcvantol/djconnect-windows
->
WINDOWS_PROFILE_ADOPTION_REPORT.md
->
37710090d05fbebe5cfb37f6f275ef7af528f569
```

## Related Candidates

- `KC-DJCONNECT-007`

## Candidate Boundary

This candidate preserves DJConnect Pi and Windows client terminology. It does not generalize Profile Platform adoption and does not merge this candidate into a concept.
