# CK-DJCONNECT-004: Backend-Owned Context Adoption In Clients

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `CK-DJCONNECT-004` |
| Lifecycle state | Certified Knowledge |
| Certification status | Certified |
| Certification date | 2026-07-12 |
| Originating Generalized Knowledge | `GK-DJCONNECT-004` |
| Knowledge category | Practice |
| Engineering domains | Client Engineering, Architecture, Embedded Systems |
| Abstraction level | Canonical |
| Confidence | High |
| Publication eligibility | Eligible |
| Certification record | [2026-07-12 First Knowledge Certification Cycle](../../certification/cycles/2026-07-12-first-certification-cycle.md) |

## Certified Statement

Clients may adopt backend-owned context by carrying request context, decoding response metadata, and handling structured errors while preserving backend ownership of resolution, persistence, privacy policy, and routing.

Client-specific UI and privacy boundaries may shape how context is rendered, but they must not transfer ownership of backend-resolved state into the client.

## Engineering Rationale

Centralizing context resolution in the backend reduces divergent client behavior. Clients can still send context signals, render resolved metadata, and present repair or setup states through structured errors without inventing local resolution logic.

## Applicability

This knowledge applies to systems where multiple clients consume a shared backend-owned context, identity, profile, tenant, session, or routing model.

## Constraints

- Clients may have different UI and privacy constraints.
- Backend-owned state must not become client-owned cache or local authority.
- Explicit client context fields must remain compatible with backend resolution rules.
- Personal, tenant, session, or private-context behavior requires careful persistence boundaries.

## Traceability

```text
CK-DJCONNECT-004
->
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
evidence files and commits listed below
```

## Source Evidence

| Observation | Repository | Evidence | Commit |
| --- | --- | --- | --- |
| `EO-DJCONNECT-007` | `pcvantol/djconnect-app` | `APPLE_PROFILE_ADOPTION_REPORT.md` | `a743e3e2fbde5dd4cb82d6d56df521a99cc8a6c6` |
| `EO-DJCONNECT-008` | `pcvantol/djconnect-pi` | `PI_PROFILE_ADOPTION_REPORT.md` | `35585114ef0f745044e17eea1fcce57ab45e60ff` |
| `EO-DJCONNECT-008` | `pcvantol/djconnect-windows` | `WINDOWS_PROFILE_ADOPTION_REPORT.md` | `37710090d05fbebe5cfb37f6f275ef7af528f569` |

## Relationships

| Relationship | Target | Direction | Rationale |
| --- | --- | --- | --- |
| related to | `CK-DJCONNECT-001` | this knowledge -> target | Client context adoption may require verification support across client runtimes. |

## Certification Rationale

Certified because the originating Generalized Knowledge is supported by multiple client repositories, preserves backend ownership constraints, and avoids client-specific implementation prescription.

## Revision History

| Date | Change |
| --- | --- |
| 2026-07-12 | Initial certification from `GK-DJCONNECT-004`. |
