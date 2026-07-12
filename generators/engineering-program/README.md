# Engineering Program Generator

This generator creates complete Engineering Programs from Certified Knowledge.

Generated programs are derived artifacts. They are not canonical knowledge, publications, certification records or Knowledge Source registrations.

## Generator Identity

| Field | Value |
| --- | --- |
| Generator identifier | `engineering-program-generator` |
| Generator version | `0.1.0` |
| CLI command | `aikb generate` |
| Canonical input | Certified Knowledge |
| Output type | Engineering Program |

## Supported Program Types

- `verification-platform`
- `ai-platform`
- `embedded-platform`
- `software-assurance`

## Generation Flow

```text
Certified Knowledge
->
Knowledge Retrieval
->
Knowledge Relationships
->
Engineering Reasoning
->
Program Generator
->
Generated Engineering Program
```

## Generated Artifacts

Each generated program contains:

- `README.md`
- `ARCHITECTURE.md`
- `GOVERNANCE.md`
- `ROADMAP.md`
- `BACKLOG.md`
- `VERIFICATION_STRATEGY.md`
- `SOFTWARE_ASSURANCE_STRATEGY.md`
- `RELEASE_STRATEGY.md`
- `ENGINEERING_GUIDANCE.md`
- `CHECKLISTS.md`
- `PROMPTS.md`
- `.aikb/engineering-program-manifest.json`

## Manifest Requirements

The Engineering Program Manifest records:

- program identifier;
- generation timestamp;
- Knowledge Base version;
- generator version;
- Certified Knowledge version;
- input Knowledge Sources;
- generated artifacts;
- traceability references.

## Governance Boundary

The generator must not:

- modify Certified Knowledge;
- create Engineering Observations;
- create Knowledge Candidates;
- form Knowledge Concepts;
- create Generalized Knowledge;
- certify knowledge;
- onboard repositories;
- generate publications;
- invent evidence.

## Traceability

Every generated program preserves this lineage:

```text
Engineering Program
->
Certified Knowledge
->
Generalized Knowledge
->
Knowledge Concepts
->
Knowledge Candidates
->
Engineering Observations
->
Knowledge Sources
->
Repositories
->
Evidence
```
