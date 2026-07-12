# GK-DJCONNECT-002: Coverage Evidence Provenance

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `GK-DJCONNECT-002` |
| Lifecycle state | Generalized Knowledge |
| Review status | Certification Completed |
| Certification status | Certified as `CK-DJCONNECT-002` |
| Knowledge category | Workflow |
| Engineering domains | Verification, Software Assurance, Client Engineering |
| Abstraction level | Technology Independent |
| Confidence | Medium |
| Knowledge sources | `KS-DJCONNECT-001` |

## Summary

Coverage evidence should preserve provenance for the measured repository, source revision, verification runtime or tool context, native report location, qualification status and baseline history.

When later coverage evidence is produced after an established baseline, it should be recorded without mutating the historical baseline unless governance explicitly revises that baseline.

This item remains the Generalized Knowledge source for certified item `CK-DJCONNECT-002`.

## Engineering Rationale

Coverage results are only useful as engineering evidence when they can be traced back to the exact source revision, producing toolchain, report artifact and qualification decision. Preserving baseline history avoids retroactive ambiguity in evidence records.

## Preserved Constraints

- Coverage metrics should remain tied to source revisions and native reports.
- Runtime or tool versions should remain visible where they affect interpretation.
- Post-baseline evidence should remain distinguishable from the original baseline.
- Thresholds are not implied by this knowledge item.

## Supporting Concepts

- [KCN-DJCONNECT-002](../../concepts/djconnect/KCN-DJCONNECT-002.md)

## Supporting Candidates

- [KC-DJCONNECT-004](../../candidates/djconnect/KC-DJCONNECT-004.md)
- [KC-DJCONNECT-005](../../candidates/djconnect/KC-DJCONNECT-005.md)

## Supporting Observations

- [EO-DJCONNECT-004](../../observations/djconnect/EO-DJCONNECT-004.md)
- [EO-DJCONNECT-005](../../observations/djconnect/EO-DJCONNECT-005.md)

## Source Evidence

| Observation | Knowledge Source | Repository | Evidence | Commit |
| --- | --- | --- | --- | --- |
| `EO-DJCONNECT-004` | `KS-DJCONNECT-001` | `pcvantol/djconnect` | `CODE_COVERAGE_BASELINE_1.md` | `0e90b1b3a853a4bfa8db415f98000b953d4eaba8` |
| `EO-DJCONNECT-005` | `KS-DJCONNECT-001` | `pcvantol/djconnect` | `CODE_COVERAGE_WINDOWS_BASELINE_1.md` | `08ebcaf7332f82f955dc7f6981842d1f1be486b1` |

Referenced source commits:

- `pcvantol/djconnect`: `9bedd037f87ac4c359da5dee5f63bddacf37cd74`
- `pcvantol/djconnect-app`: `6062ddd8e1367bf52c1666b3e2c95514d189a9cf`
- `pcvantol/djconnect-pi`: `ef9300e6b3a1d3c23311b52beaff0872d023a32b`
- `pcvantol/djconnect-windows`: `b205f087214eb5fe90c4129c2afa9dee7f836a82`

## Relationships

| Relationship | Target | Direction | Rationale |
| --- | --- | --- | --- |
| supported by | `GK-DJCONNECT-001` | this knowledge <- target | Verification adapter evidence can contribute to coverage qualification evidence. |
| supported by | `GK-DJCONNECT-003` | this knowledge <- target | Assurance governance explains why provenance and baseline history matter. |

## Traceability

```text
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
repositories and evidence listed above
```

## Generalization Notes

Removed DJConnect-specific baseline names from the main knowledge statement. Preserved baseline provenance, source revision, runtime/tool context, report references and historical baseline separation.

## Certification Boundary

This item was certified as `CK-DJCONNECT-002` on 2026-07-12. Future material changes require governed re-certification.
