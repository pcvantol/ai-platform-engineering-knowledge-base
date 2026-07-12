# GK-DJCONNECT-004: Backend-Owned Context Adoption In Clients

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `GK-DJCONNECT-004` |
| Lifecycle state | Generalized Knowledge |
| Review status | Certification Completed |
| Certification status | Certified as `CK-DJCONNECT-004` |
| Knowledge category | Practice |
| Engineering domains | Client Engineering, Architecture, Embedded Systems |
| Abstraction level | Technology Independent |
| Confidence | Medium |
| Knowledge sources | `KS-DJCONNECT-001` |

## Summary

Clients can adopt backend-owned context by carrying request context, decoding response metadata and handling structured errors while preserving backend ownership of resolution, persistence, privacy policy and routing.

Client-specific UI and privacy boundaries may shape how the context is rendered, but they should not transfer ownership of backend-resolved state into the client.

This item remains the Generalized Knowledge source for certified item `CK-DJCONNECT-004`.

## Engineering Rationale

Centralizing context resolution in the backend reduces divergent client behavior while still allowing different client types to send context signals and render resolved metadata. Structured errors allow clients to present repair or setup states without inventing local resolution logic.

## Preserved Constraints

- Clients may have different UI and privacy constraints.
- Backend-owned state must not become client-owned cache or local authority.
- Explicit client context fields should remain compatible with backend resolution rules.
- Personal or private-session behavior requires careful persistence boundaries.

## Supporting Concepts

- [KCN-DJCONNECT-004](../../concepts/djconnect/KCN-DJCONNECT-004.md)

## Supporting Candidates

- [KC-DJCONNECT-007](../../candidates/djconnect/KC-DJCONNECT-007.md)
- [KC-DJCONNECT-008](../../candidates/djconnect/KC-DJCONNECT-008.md)

## Supporting Observations

- [EO-DJCONNECT-007](../../observations/djconnect/EO-DJCONNECT-007.md)
- [EO-DJCONNECT-008](../../observations/djconnect/EO-DJCONNECT-008.md)

## Source Evidence

| Observation | Knowledge Source | Repository | Evidence | Commit |
| --- | --- | --- | --- | --- |
| `EO-DJCONNECT-007` | `KS-DJCONNECT-001` | `pcvantol/djconnect-app` | `APPLE_PROFILE_ADOPTION_REPORT.md` | `a743e3e2fbde5dd4cb82d6d56df521a99cc8a6c6` |
| `EO-DJCONNECT-008` | `KS-DJCONNECT-001` | `pcvantol/djconnect-pi` | `PI_PROFILE_ADOPTION_REPORT.md` | `35585114ef0f745044e17eea1fcce57ab45e60ff` |
| `EO-DJCONNECT-008` | `KS-DJCONNECT-001` | `pcvantol/djconnect-windows` | `WINDOWS_PROFILE_ADOPTION_REPORT.md` | `37710090d05fbebe5cfb37f6f275ef7af528f569` |

## Relationships

| Relationship | Target | Direction | Rationale |
| --- | --- | --- | --- |
| related to | `GK-DJCONNECT-001` | this knowledge -> target | Client context adoption may require verification support across client runtimes. |

## Traceability

```text
GK-DJCONNECT-004
->
KCN-DJCONNECT-004
->
KC-DJCONNECT-007, KC-DJCONNECT-008
->
EO-DJCONNECT-007, EO-DJCONNECT-008
->
KS-DJCONNECT-001
->
pcvantol/djconnect-app, pcvantol/djconnect-pi, pcvantol/djconnect-windows
->
evidence files and commits listed above
```

## Generalization Notes

Removed DJConnect Profile Platform names from the main knowledge statement. Preserved backend-owned resolution, request context, response metadata, structured errors and client-specific privacy boundaries.

## Certification Boundary

This item was certified as `CK-DJCONNECT-004` on 2026-07-12. Future material changes require governed re-certification.
