# Engineering Handbook

## Metadata

| Field | Value |
| --- | --- |
| Publication identifier | `PUB-AIPE-HANDBOOK-001` |
| Publication type | Engineering Handbook |
| Publication status | Published |
| Revision | 1.0.0 |
| Revision date | 2026-07-12 |
| Target audience | Engineers, reviewers, operators |
| Publication owner | AI Platform Engineering Knowledge Base maintainers |
| Source knowledge snapshot | Certified Knowledge snapshot from 2026-07-12 |

## Purpose

This handbook adapts Certified Knowledge into practical engineering review guidance.

The handbook is derived from Certified Knowledge and does not define new canonical knowledge.

## Scope

This handbook covers operational use of the first Certified Knowledge set for engineering review and implementation assessment.

It does not define project source code, implementation artifacts, coverage thresholds, tooling mandates, or release policy.

## Source Certified Knowledge

| Certified Knowledge | Handbook Use |
| --- | --- |
| [CK-DJCONNECT-001](../../certified/djconnect/CK-DJCONNECT-001.md) | Review verification adapter responsibility boundaries. |
| [CK-DJCONNECT-002](../../certified/djconnect/CK-DJCONNECT-002.md) | Review coverage evidence provenance and baseline history. |
| [CK-DJCONNECT-003](../../certified/djconnect/CK-DJCONNECT-003.md) | Review the separation between behavioural verification and assurance governance. |
| [CK-DJCONNECT-004](../../certified/djconnect/CK-DJCONNECT-004.md) | Review client adoption of backend-owned context. |

## Engineering Review Guidance

### Verification Adapters

When reviewing a verification adapter, confirm that runtime-specific execution support is separate from product behavior assertions.

Review whether live-target absence, destructive operations, and target-specific execution behavior remain explicit and traceable. These checks are derived from `CK-DJCONNECT-001`.

### Coverage Evidence

When reviewing coverage evidence, confirm that the record preserves repository identity, source revision, runtime or tool context, native report location, qualification status, and baseline history.

Review whether post-baseline evidence is distinguishable from the original baseline unless governance has explicitly revised that baseline. These checks are derived from `CK-DJCONNECT-002`.

### Software Assurance Governance

When reviewing assurance practice, confirm that behavioural verification and software assurance governance are separated but connected through evidence.

Review whether governance evaluates the engineering system's ability to build, verify, release, and evolve safely rather than replacing behavioural scenarios or product architecture. These checks are derived from `CK-DJCONNECT-003`.

### Client Context Adoption

When reviewing client context adoption, confirm that clients carry context, decode response metadata, and handle structured errors without becoming authoritative for backend-owned resolution, persistence, privacy policy, or routing.

Review whether client-specific UI and privacy boundaries shape presentation without transferring ownership of backend-resolved state. These checks are derived from `CK-DJCONNECT-004`.

## Review Checklist

| Review Area | Derived Check | Source |
| --- | --- | --- |
| Verification adapter | Runtime primitives and product behavior assertions are separate. | `CK-DJCONNECT-001` |
| Verification adapter | Live-target absence and destructive operations are explicit and traceable. | `CK-DJCONNECT-001` |
| Coverage evidence | Repository, source revision, tool context, report location, qualification status, and baseline history are visible. | `CK-DJCONNECT-002` |
| Coverage evidence | Post-baseline evidence does not mutate historical baseline without governance revision. | `CK-DJCONNECT-002` |
| Assurance governance | Behavioural verification and assurance governance are separated but evidence-connected. | `CK-DJCONNECT-003` |
| Assurance governance | CI systems, runners, and tools are treated as execution surfaces rather than governance owners. | `CK-DJCONNECT-003` |
| Client context | Clients do not become authoritative for backend-owned resolution, persistence, privacy policy, or routing. | `CK-DJCONNECT-004` |
| Client context | Client-specific UI and privacy constraints preserve backend ownership of resolved state. | `CK-DJCONNECT-004` |

## Traceability

```text
PUB-AIPE-HANDBOOK-001
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

This handbook is approved for publication as an operational adaptation of Certified Knowledge.

Revisions must regenerate guidance from Certified Knowledge, preserve this publication identity, and update the source knowledge snapshot. Superseding or retirement affects only this publication.

## Revision History

| Date | Revision | Change |
| --- | --- | --- |
| 2026-07-12 | 1.0.0 | Initial engineering handbook generated from the first Certified Knowledge set. |
