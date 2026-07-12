# Knowledge Source Onboarding Framework

This area defines the canonical process through which a repository becomes an officially registered Knowledge Source.

Repositories remain autonomous. The Knowledge Base remains canonical. A repository is not assumed to be a Knowledge Source until onboarding is completed and approved.

This framework does not onboard repositories, connect repositories, extract knowledge, implement automation, or modify source repositories.

The first operational onboarding interface is `aikb onboard`, documented in [../cli/README.md](../cli/README.md). The command creates Knowledge Source profiles and Extraction Profiles inside this Knowledge Base, while leaving source repositories unchanged.

## Core Principle

A repository is never assumed to be a Knowledge Source.

A repository becomes a Knowledge Source only after successful onboarding.

Onboarding establishes:

- identity
- ownership
- scope
- extraction boundaries
- supported evidence
- engineering domains
- governance relationship

## Onboarding Objectives

The framework supports onboarding of:

- software repositories
- verification repositories
- architecture repositories
- documentation repositories
- research repositories
- operational repositories
- release repositories
- experiment repositories

Future repository types may be onboarded without architectural redesign when they can provide traceable engineering evidence.

## Onboarding Pipeline

Canonical onboarding workflow:

```text
Repository
->
Repository Discovery
->
Repository Assessment
->
Knowledge Source Registration
->
Evidence Registration
->
Extraction Profile Creation
->
Validation
->
Knowledge Source Approved
```

Every stage must preserve repository independence and prepare traceability for future ingestion.

## Onboarding Stages

### Repository

Purpose: identify a repository that may contain reusable engineering evidence.

Entry criteria:

- repository is known or proposed
- repository has an identifiable owner or contact
- repository may contain engineering evidence

Exit criteria:

- repository is ready for discovery
- initial repository reference is recorded

### Repository Discovery

Purpose: collect initial repository context without treating the repository as an approved Knowledge Source.

Discovery may identify:

- repository name
- repository location or reference
- repository purpose
- repository type
- owner or maintainer contacts
- visible evidence types
- initial engineering domains

Exit criteria:

- repository discovery summary exists
- repository can proceed to assessment or be rejected as out of scope

### Repository Assessment

Purpose: evaluate whether the repository is suitable to become a Knowledge Source.

Assessment covers:

- repository purpose
- repository maturity
- engineering domains
- technology stack
- repository structure
- supported evidence
- repository ownership
- maintenance status
- knowledge value
- traceability readiness
- access and visibility constraints
- privacy or security risks

Exit criteria:

- repository suitability is understood
- risks and limitations are documented
- onboarding may proceed, pause, or be rejected

### Knowledge Source Registration

Purpose: create the canonical Knowledge Source identity and profile.

Registration records:

- stable Knowledge Source identifier
- repository identity
- repository type
- repository owner
- maintainers
- engineering domains
- lifecycle status
- registration date

Registration does not start extraction by itself. It establishes the source as eligible for governed ingestion.

### Evidence Registration

Purpose: identify evidence types that may be used during extraction and ingestion.

Evidence registration records:

- supported evidence types
- evidence locations or references
- evidence traceability anchors
- evidence freshness expectations
- evidence exclusions
- evidence access constraints

Evidence remains evidence. Evidence registration does not create Knowledge Objects.

### Extraction Profile Creation

Purpose: define how future extraction may operate against the Knowledge Source.

The Extraction Profile records included evidence, excluded evidence, supported artifacts, traceability configuration, normalization policy, and AI assistance policy.

Extraction Profile approval does not extract knowledge. It defines the allowed boundaries for future extraction and ingestion.

### Validation

Purpose: confirm that the Knowledge Source Profile and Extraction Profile are complete, traceable, and governance-ready.

Validation checks:

- repository accessibility
- metadata completeness
- supported evidence
- traceability readiness
- repository health
- duplicate registration detection
- ownership clarity
- extraction boundary clarity
- governance readiness

Exit criteria:

- profile is approved, returned for revision, rejected, or deferred
- validation outcome is recorded

### Knowledge Source Approved

Purpose: mark the repository as an approved Knowledge Source.

Approval means:

- the source is registered
- the source profile is valid
- extraction boundaries are documented
- supported evidence is known
- future ingestion may reference this source

Approval does not certify any knowledge and does not approve any future candidate automatically.

## Repository Assessment Model

Repository assessment should evaluate:

| Assessment area | Purpose |
| --- | --- |
| Repository purpose | Understand why the repository exists and what engineering work it represents. |
| Repository maturity | Determine whether evidence is stable, experimental, historical, or actively evolving. |
| Engineering domains | Identify relevant domains for classification and future extraction. |
| Technology stack | Capture technology context without making the Knowledge Base technology dependent. |
| Repository structure | Understand where evidence may exist and how it is organized. |
| Supported evidence | Identify evidence that may support observations and candidates. |
| Repository ownership | Establish accountability and contact points. |
| Maintenance status | Determine whether the source is active, archived, deprecated, or retired. |
| Knowledge value | Assess whether the source may produce reusable engineering knowledge. |
| Traceability readiness | Confirm that future observations can link back to evidence. |

Assessment findings are not knowledge. They are onboarding evidence.

## Knowledge Source Profile

A Knowledge Source Profile is the canonical record describing an approved or proposed source.

Every Knowledge Source Profile should support:

- identifier
- repository name
- repository description
- repository reference or location
- repository type
- engineering domains
- technology stack
- supported evidence
- supported extraction scope
- repository owner
- maintainers
- lifecycle status
- registration date
- access or visibility constraints
- traceability anchors
- extraction profile reference
- governance owner
- revision history

The Knowledge Source Profile describes the source. It does not certify knowledge extracted from the source.

## Extraction Profile

An Extraction Profile defines allowed extraction boundaries for a Knowledge Source.

Every Extraction Profile should support:

- included evidence
- excluded evidence
- supported document types
- supported engineering artifacts
- traceability configuration
- normalization policy
- AI assistance policy
- privacy and security exclusions
- source freshness expectations
- review requirements
- profile owner
- revision history

Extraction Profile rules:

- Included evidence must be traceable.
- Excluded evidence must not be consumed.
- AI assistance must preserve source context and uncertainty.
- Normalization must not remove lineage.
- Profile revisions must preserve history.

## Validation Framework

Onboarding validation determines whether a repository can become an approved Knowledge Source.

Validation outcomes:

- Approved
- Approved with Constraints
- Returned for Revision
- Deferred
- Rejected
- Retired

Validation must confirm:

- repository accessibility is sufficient for intended extraction
- metadata is complete enough for traceability
- evidence types are supported and reviewable
- duplicate Knowledge Source registration does not exist
- repository owner or contact is known
- extraction boundaries are clear
- privacy, security, and access constraints are documented
- source lifecycle status is understood

Validation does not approve extracted knowledge. It approves the source profile and extraction boundaries.

## Governance Model

Source onboarding governance covers:

- registration
- review
- approval
- profile revision
- profile retirement
- repository ownership changes
- extraction boundary changes
- duplicate source handling

Governance expectations:

- No repository becomes a Knowledge Source without approval.
- Every Knowledge Source must have a stable identifier.
- Every Knowledge Source must have ownership or stewardship metadata.
- Extraction boundaries must be explicit before ingestion.
- Profile revisions must preserve history.
- Retired profiles must remain traceable.
- Ownership changes must be recorded before future ingestion depends on them.

## AI-Assisted Onboarding

AI may assist with:

- repository assessment
- metadata discovery
- engineering domain suggestion
- evidence discovery
- profile drafting
- risk identification
- duplicate registration detection
- extraction profile suggestions

AI must never:

- register repositories automatically
- change repository ownership
- change repository history
- approve onboarding
- invent repository metadata
- invent evidence
- bypass validation
- modify extraction boundaries without review

AI onboarding output is a proposal. Human-governed approval remains required.

## Traceability Model

Onboarding must preserve complete traceability.

Canonical source onboarding traceability:

```text
Knowledge Source
->
Knowledge Source Profile
->
Repository
->
Repository Owner
->
Evidence
```

Traceability requirements:

- Every Knowledge Source must reference its profile.
- Every Knowledge Source Profile must reference the repository.
- Repository ownership or stewardship must be recorded.
- Supported evidence must be identifiable and traceable.
- Future Knowledge Objects must reference a registered Knowledge Source.
- Profile revisions must preserve historical source identity.

## Quality Expectations

The onboarding process should maximize:

- repeatability
- traceability
- consistency
- repository independence
- engineering correctness
- governance clarity
- source coverage

The onboarding process should minimize:

- duplicate source registration
- unclear ownership
- ambiguous extraction boundaries
- unsupported evidence
- repository coupling
- untraceable future observations

## Scalability Principles

The framework must support:

- single repositories
- multiple repositories
- multiple organizations
- future repository technologies
- future engineering disciplines
- future evidence types

Onboarding must scale without requiring source repositories to change their structure, workflows, tools, or ownership model.

## Integration With Other Frameworks

Source onboarding precedes Knowledge Source integration. The Knowledge Source Integration Framework defines how approved sources provide evidence context after onboarding.

Source onboarding prepares the Knowledge Ingestion Pipeline by defining eligible sources, evidence boundaries, and traceability anchors.

Source onboarding prepares the Knowledge Automation Framework by identifying which sources may be monitored or scanned in future automation.

Source onboarding depends on governance for approval, revision, retirement, and ownership changes.

Source onboarding depends on the AI Knowledge Operations Framework when AI assists assessment, profile drafting, or risk identification.
