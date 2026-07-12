# DJConnect Knowledge Candidates

This area contains Knowledge Candidates derived from DJConnect Engineering Observations.

Knowledge Source:

- `KS-DJCONNECT-001`
- [DJConnect Knowledge Source](../../sources/djconnect/README.md)

These records are candidates only. They are immature proposals awaiting review and do not create Knowledge Concepts, Generalized Knowledge, Certified Knowledge, or Publications.

## Candidate Index

| Identifier | Title | Supporting observation | Knowledge category | Review status |
| --- | --- | --- | --- | --- |
| [KC-DJCONNECT-001](./KC-DJCONNECT-001.md) | ESP32 verification adapter uses explicit gates for live hardware and destructive operations | `EO-DJCONNECT-001` | Practice | Awaiting Review |
| [KC-DJCONNECT-002](./KC-DJCONNECT-002.md) | Windows verification adapter records runtime primitives separately from product behavior assertions | `EO-DJCONNECT-002` | Practice | Awaiting Review |
| [KC-DJCONNECT-003](./KC-DJCONNECT-003.md) | Raspberry Pi verification adapter records live target absence without treating it as adapter failure | `EO-DJCONNECT-003` | Practice | Awaiting Review |
| [KC-DJCONNECT-004](./KC-DJCONNECT-004.md) | Cross-platform coverage baseline records repository commits, runtime version and native report provenance | `EO-DJCONNECT-004` | Workflow | Awaiting Review |
| [KC-DJCONNECT-005](./KC-DJCONNECT-005.md) | Windows coverage baseline is recorded as post-baseline evidence without mutating the original baseline | `EO-DJCONNECT-005` | Decision | Awaiting Review |
| [KC-DJCONNECT-006](./KC-DJCONNECT-006.md) | Software Assurance Platform separates behavioural verification from engineering quality governance | `EO-DJCONNECT-006` | Architecture | Awaiting Review |
| [KC-DJCONNECT-007](./KC-DJCONNECT-007.md) | Apple Profile Platform adoption places profile context in the shared client contract layer | `EO-DJCONNECT-007` | Practice | Awaiting Review |
| [KC-DJCONNECT-008](./KC-DJCONNECT-008.md) | Pi and Windows Profile Platform adoption preserves backend-owned profile resolution with client-specific boundaries | `EO-DJCONNECT-008` | Practice | Awaiting Review |
| [KC-DJCONNECT-009](./KC-DJCONNECT-009.md) | Verification runtime should be versioned separately from source-specific scenarios | `EO-DJCONNECT-009` | Architecture | Promoted to Concept |
| [KC-DJCONNECT-010](./KC-DJCONNECT-010.md) | Verification adapters should remain thin execution and evidence boundaries | `EO-DJCONNECT-010` | Architecture | Promoted to Concept |
| [KC-DJCONNECT-011](./KC-DJCONNECT-011.md) | Coverage baselines should preserve provenance and qualification state | `EO-DJCONNECT-011` | Workflow | Promoted to Concept |
| [KC-DJCONNECT-012](./KC-DJCONNECT-012.md) | Qualification decisions should be separated from validation evidence | `EO-DJCONNECT-012` | Governance | Promoted to Concept |
| [KC-DJCONNECT-013](./KC-DJCONNECT-013.md) | Verification capability metadata should describe runtime compatibility | `EO-DJCONNECT-013` | Architecture | Promoted to Concept |
| [KC-DJCONNECT-014](./KC-DJCONNECT-014.md) | Scenario execution should preserve planning, routing and evidence metadata | `EO-DJCONNECT-014` | Workflow | Promoted to Concept |
| [KC-DJCONNECT-015](./KC-DJCONNECT-015.md) | Verification status should distinguish unavailable targets from failed verification | `EO-DJCONNECT-015` | Practice | Promoted to Concept |
| [KC-DJCONNECT-016](./KC-DJCONNECT-016.md) | Verification reporting should expose scorecards and health signals | `EO-DJCONNECT-016` | Workflow | Promoted to Concept |
| [KC-DJCONNECT-017](./KC-DJCONNECT-017.md) | Software Assurance should be governed separately from behavioral verification | `EO-DJCONNECT-017` | Architecture | Promoted to Concept |
| [KC-DJCONNECT-018](./KC-DJCONNECT-018.md) | Assurance confidence should be based on multiple quality themes | `EO-DJCONNECT-018` | Principle | Promoted to Concept |
| [KC-DJCONNECT-019](./KC-DJCONNECT-019.md) | Assurance implementation should be gated by baseline readiness | `EO-DJCONNECT-019` | Governance | Promoted to Concept |
| [KC-DJCONNECT-020](./KC-DJCONNECT-020.md) | Assurance governance should connect evidence, release qualification and platform health | `EO-DJCONNECT-020` | Governance | Promoted to Concept |
| [KC-DJCONNECT-021](./KC-DJCONNECT-021.md) | Engineering acceptance should require durable traceable evidence | `EO-DJCONNECT-021` | Workflow | Promoted to Concept |
| [KC-DJCONNECT-022](./KC-DJCONNECT-022.md) | Assurance evidence should preserve provenance for auditability | `EO-DJCONNECT-022` | Workflow | Promoted to Concept |
| [KC-DJCONNECT-023](./KC-DJCONNECT-023.md) | Assurance readiness should distinguish architecture readiness from residual implementation risk | `EO-DJCONNECT-023` | Governance | Promoted to Concept |
| [KC-DJCONNECT-024](./KC-DJCONNECT-024.md) | Assurance reporting should expose readiness, decisions and pending gates | `EO-DJCONNECT-024` | Workflow | Promoted to Concept |
| [KC-DJCONNECT-025](./KC-DJCONNECT-025.md) | Runtime releases should expose version and distribution identity | `EO-DJCONNECT-025` | Architecture | Promoted to Concept |
| [KC-DJCONNECT-026](./KC-DJCONNECT-026.md) | Release baselines should preserve historical comparison points | `EO-DJCONNECT-026` | Governance | Promoted to Concept |
| [KC-DJCONNECT-027](./KC-DJCONNECT-027.md) | Release lifecycle should separate architecture freeze, qualification and baseline certification | `EO-DJCONNECT-027` | Governance | Promoted to Concept |
| [KC-DJCONNECT-028](./KC-DJCONNECT-028.md) | Release roadmaps should sequence increments, dependencies and gates | `EO-DJCONNECT-028` | Workflow | Promoted to Concept |
| [KC-DJCONNECT-029](./KC-DJCONNECT-029.md) | Repository release documentation should preserve delivery hygiene | `EO-DJCONNECT-029` | Practice | Promoted to Concept |
| [KC-DJCONNECT-030](./KC-DJCONNECT-030.md) | Qualification milestones should produce release readiness evidence | `EO-DJCONNECT-030` | Workflow | Promoted to Concept |
| [KC-DJCONNECT-031](./KC-DJCONNECT-031.md) | Release artifacts should preserve traceability to commits, reports and runtime identity | `EO-DJCONNECT-031` | Workflow | Promoted to Concept |
| [KC-DJCONNECT-032](./KC-DJCONNECT-032.md) | Release closure should record completion evidence and next-action state | `EO-DJCONNECT-032` | Workflow | Promoted to Concept |

## Candidate Boundary

Every candidate in this folder follows:

```text
Engineering Observation
->
Knowledge Candidate
```

Candidates remain repository-specific proposals. They must not be treated as concepts, generalized knowledge, certified knowledge, or publication sources.
