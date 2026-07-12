# Architecture Reference Guide

## Metadata

| Field | Value |
| --- | --- |
| Publication identifier | `PUB-AIPE-ARCHREF-001` |
| Publication type | Architecture Guide |
| Publication status | Published |
| Revision | 1.0.0 |
| Revision date | 2026-07-12 |
| Target audience | Architects, engineers, technical leads |
| Publication owner | AI Platform Engineering Knowledge Base maintainers |
| Source knowledge snapshot | Certified Knowledge snapshot from 2026-07-12 |

## Purpose

This guide translates the first Certified Knowledge set into an architecture reference for engineering platform design review.

The guide is a derived publication. It does not replace or modify Certified Knowledge.

## Scope

This guide covers architecture concerns represented by the first Certified Knowledge set:

- verification execution boundaries
- evidence provenance boundaries
- assurance governance boundaries
- client context ownership boundaries

It does not introduce product-specific architecture, implementation artifacts, tooling requirements, or new certification criteria.

## Source Certified Knowledge

| Certified Knowledge | Architecture Concern |
| --- | --- |
| [CK-DJCONNECT-001](../../certified/djconnect/CK-DJCONNECT-001.md) | Verification adapter boundary |
| [CK-DJCONNECT-002](../../certified/djconnect/CK-DJCONNECT-002.md) | Coverage evidence provenance |
| [CK-DJCONNECT-003](../../certified/djconnect/CK-DJCONNECT-003.md) | Software assurance governance separation |
| [CK-DJCONNECT-004](../../certified/djconnect/CK-DJCONNECT-004.md) | Backend-owned context adoption in clients |

## Reference Architecture Concerns

### Verification Adapter Boundary

Architecture should distinguish runtime execution primitives from product behavior assertions.

Adapters may support target-specific collection, launch, stop, restart, routing, planning, and evidence capture. Product behavior expectations, destructive hardware mutation, live-target availability, and unavailable-target handling remain explicit, reviewable, and traceable outside adapter implementation.

Source: `CK-DJCONNECT-001`.

### Coverage Evidence Provenance

Architecture should preserve evidence provenance so reviewers can reconstruct what was measured and how the measurement was produced.

Coverage records should keep the measured repository, source revision, runtime or tool context, native report location, qualification status, and baseline history visible. Post-baseline evidence remains distinguishable from the original baseline unless governance revises that baseline.

Source: `CK-DJCONNECT-002`.

### Software Assurance Governance Separation

Architecture should separate behavioural verification from software assurance governance while connecting both through evidence.

Behavioural verification determines whether expected behavior is present. Assurance governance evaluates the engineering system's ability to build, verify, release, and evolve safely.

Source: `CK-DJCONNECT-003`.

### Backend-Owned Context Adoption In Clients

Architecture should allow clients to carry context signals, decode response metadata, and handle structured errors without making clients authoritative for backend-owned resolution, persistence, privacy policy, or routing.

Client-specific UI and privacy boundaries may shape presentation, but they do not transfer ownership of backend-resolved state.

Source: `CK-DJCONNECT-004`.

## Relationship Map

| Source | Relationship | Target | Architecture Meaning |
| --- | --- | --- | --- |
| `CK-DJCONNECT-001` | supports | `CK-DJCONNECT-002` | Adapter evidence can support coverage evidence provenance. |
| `CK-DJCONNECT-003` | supports | `CK-DJCONNECT-002` | Assurance governance explains why provenance and baseline history matter. |
| `CK-DJCONNECT-004` | related to | `CK-DJCONNECT-001` | Client context adoption may require verification support across client runtimes. |

## Traceability

```text
PUB-AIPE-ARCHREF-001
->
CK-DJCONNECT-001, CK-DJCONNECT-002, CK-DJCONNECT-003, CK-DJCONNECT-004
->
GK-DJCONNECT-001, GK-DJCONNECT-002, GK-DJCONNECT-003, GK-DJCONNECT-004
->
KCN-DJCONNECT-001, KCN-DJCONNECT-002, KCN-DJCONNECT-003, KCN-DJCONNECT-004
->
KC-DJCONNECT-001 through KC-DJCONNECT-008
->
EO-DJCONNECT-001 through EO-DJCONNECT-008
->
KS-DJCONNECT-001
->
registered DJConnect repositories
```

## Publication Governance

This guide is approved for publication as an audience-specific architecture reference derived from eligible Certified Knowledge.

Revisions must cite the Certified Knowledge snapshot used for regeneration. Superseding or retirement affects this publication only and does not alter Certified Knowledge.

## Revision History

| Date | Revision | Change |
| --- | --- | --- |
| 2026-07-12 | 1.0.0 | Initial architecture reference guide generated from the first Certified Knowledge set. |
