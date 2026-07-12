# CK-DJCONNECT-002: Coverage Evidence Provenance

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `CK-DJCONNECT-002` |
| Lifecycle state | Certified Knowledge |
| Certification status | Certified |
| Certification date | 2026-07-12 |
| Originating Generalized Knowledge | `GK-DJCONNECT-002` |
| Knowledge category | Workflow |
| Engineering domains | Verification, Software Assurance, Client Engineering |
| Abstraction level | Canonical |
| Confidence | High |
| Publication eligibility | Eligible |
| Certification record | [2026-07-12 First Knowledge Certification Cycle](../../certification/cycles/2026-07-12-first-certification-cycle.md) |

## Certified Statement

Coverage evidence must preserve provenance for the measured repository, source revision, verification runtime or tool context, native report location, qualification status, and baseline history.

Coverage evidence produced after an established baseline must be recorded without mutating the historical baseline unless governance explicitly revises that baseline.

## Engineering Rationale

Coverage data is engineering evidence only when reviewers can reconstruct what was measured, which source revision produced the measurement, which tool or runtime produced the report, and how the result was qualified. Preserving baseline history avoids retroactive ambiguity.

## Applicability

This knowledge applies to coverage records, verification evidence baselines, release qualification inputs, and cross-platform evidence snapshots.

## Constraints

- Coverage metrics must remain tied to source revisions and native reports.
- Runtime or tool versions must remain visible where they affect interpretation.
- Post-baseline evidence must remain distinguishable from the original baseline.
- This knowledge does not define coverage thresholds.

## Traceability

```text
CK-DJCONNECT-002
->
GK-DJCONNECT-002
->
KCN-DJCONNECT-002
->
KC-DJCONNECT-004, KC-DJCONNECT-005
->
EO-DJCONNECT-004, EO-DJCONNECT-005
->
KS-DJCONNECT-001
->
repositories and evidence listed below
```

## Source Evidence

| Observation | Repository | Evidence | Commit |
| --- | --- | --- | --- |
| `EO-DJCONNECT-004` | `pcvantol/djconnect` | `CODE_COVERAGE_BASELINE_1.md` | `0e90b1b3a853a4bfa8db415f98000b953d4eaba8` |
| `EO-DJCONNECT-005` | `pcvantol/djconnect` | `CODE_COVERAGE_WINDOWS_BASELINE_1.md` | `08ebcaf7332f82f955dc7f6981842d1f1be486b1` |

Referenced source commits:

- `pcvantol/djconnect`: `9bedd037f87ac4c359da5dee5f63bddacf37cd74`
- `pcvantol/djconnect-app`: `6062ddd8e1367bf52c1666b3e2c95514d189a9cf`
- `pcvantol/djconnect-pi`: `ef9300e6b3a1d3c23311b52beaff0872d023a32b`
- `pcvantol/djconnect-windows`: `b205f087214eb5fe90c4129c2afa9dee7f836a82`

## Relationships

| Relationship | Target | Direction | Rationale |
| --- | --- | --- | --- |
| supported by | `CK-DJCONNECT-001` | this knowledge <- target | Verification adapter evidence can contribute to coverage qualification evidence. |
| supported by | `CK-DJCONNECT-003` | this knowledge <- target | Assurance governance explains why provenance and baseline history matter. |

## Certification Rationale

Certified because the originating Generalized Knowledge is traceable across multiple repository commits, preserves evidence provenance, avoids threshold claims, and is reusable for future coverage evidence records.

## Revision History

| Date | Change |
| --- | --- |
| 2026-07-12 | Initial certification from `GK-DJCONNECT-002`. |
