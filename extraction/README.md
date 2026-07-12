# Knowledge Extraction Framework

This area defines the canonical framework for extracting reusable engineering knowledge from software projects and other engineering sources into the Knowledge Base.

Software repositories and engineering artifacts are sources. The Knowledge Base is the destination. Knowledge is not authored directly without traceable engineering evidence. Knowledge always originates from observable engineering work.

This framework is conceptual. It does not define automation, extraction tooling, AI workflows, scripts, pipelines, or populated knowledge.

The first operational extraction interface is `aikb extract`, documented in [../cli/README.md](../cli/README.md). The command creates Engineering Observations only and must not create Knowledge Candidates.

The canonical framework for registering and describing Knowledge Sources is defined in [../sources/README.md](../sources/README.md).

The canonical ingestion pipeline that precedes candidate lifecycle review is defined in [../ingestion/README.md](../ingestion/README.md).

## Extraction Principles

- Extraction must be deterministic, repeatable, and traceable.
- Extraction starts from observable engineering work.
- An Engineering Observation is evidence, not knowledge.
- Knowledge Candidates must be traceable to Engineering Observations.
- Project-specific details may be removed only when traceability is preserved.
- Engineering intent, rationale, and value must be retained.
- Knowledge quality is more important than extraction volume.
- Certification remains governed and cannot be automated by extraction.

## Canonical Extraction Flow

```text
Engineering Source
->
Engineering Observation
->
Knowledge Candidate
->
Knowledge Concept
->
Generalized Knowledge
->
Certified Knowledge
->
Publication
```

This framework defines how Engineering Observations enter the existing lifecycle.

## Supported Sources

Supported source types include:

- software repositories
- architecture documents
- verification evidence
- coverage reports
- qualification reports
- design decisions
- management summaries
- release notes
- issue discussions
- experiments
- postmortems
- operational experience

Future source types may be added when they represent observable engineering work and can preserve traceability.

Source registration, source metadata, and source independence rules are defined in [../sources/README.md](../sources/README.md).

## Engineering Observation Model

An Engineering Observation is a traceable record of observable engineering work. In the canonical lifecycle, an Engineering Observation is represented as a Repository Observation.

Examples include:

- successful implementation
- architectural decision
- verification result
- production failure
- root cause analysis
- performance improvement
- design trade-off
- release strategy
- engineering workflow

An observation must capture:

- source type
- source reference
- source context
- observed engineering fact
- supporting evidence
- engineering rationale when available
- extraction date
- observer or extractor
- evidence classification

An observation must not claim general reusable knowledge by itself.

## Extraction Workflow

Extraction converts observations into Knowledge Candidates.

Operational ingestion stages for scan, detection, normalization, candidate proposal, registration, and human review are defined in [../ingestion/README.md](../ingestion/README.md).

Workflow:

```text
Select source
->
Capture evidence
->
Record Engineering Observation
->
Identify reusable implication
->
Check existing candidates and concepts
->
Create or link Knowledge Candidate
->
Preserve traceability
```

Extraction should:

- identify reusable knowledge
- preserve source evidence
- capture engineering rationale
- avoid duplicate candidates
- remain independent from implementation language
- avoid treating project-specific decisions as canonical knowledge

Extraction should not:

- certify knowledge
- create publications
- remove source lineage
- import product source code
- convert every source artifact into knowledge

## Generalization Workflow

Generalization converts concepts into reusable, project-independent knowledge.

Generalization removes or neutralizes:

- repository names
- product names
- temporary implementation details
- incidental technology-specific details
- project-specific organizational context

Generalization preserves:

- engineering intent
- engineering rationale
- engineering value
- applicability constraints
- evidence lineage
- known limitations

Generalization must not hide meaningful technology constraints. If a technology-specific detail is essential to the knowledge, it should be classified as technology scope rather than erased.

## Traceability Model

Every extracted knowledge item must remain traceable.

Canonical extraction traceability:

```text
Knowledge Object
->
Knowledge Candidate
->
Engineering Observation
->
Engineering Source
->
Source Version or Commit
->
Evidence
```

Traceability requirements:

- Each Knowledge Candidate must reference at least one Engineering Observation.
- Each Engineering Observation must reference its source.
- Source version, commit, document version, report version, or event date should be preserved when available.
- Evidence must remain distinguishable from interpretation.
- Generalization must preserve source lineage even when source names are removed from the knowledge statement.
- Certified Knowledge must reconstruct the full lineage back to originating observations.

## Evidence Model

Evidence supports observations and later knowledge.

Evidence may include:

- source code references
- commits
- pull requests
- architecture records
- verification results
- test results
- coverage data
- qualification evidence
- issue discussions
- incident reports
- experiment results
- release records
- operational metrics

Evidence rules:

- Evidence is not canonical knowledge.
- Evidence must be classified using the Knowledge Classification System where applicable.
- Evidence must remain linked to observations.
- Evidence strength may increase when equivalent observations recur across sources.
- Conflicting evidence must be preserved and surfaced for review.

## Duplicate Handling

Multiple sources may produce equivalent or overlapping observations.

Duplicate handling rules:

- Do not delete duplicate observations when they provide independent evidence.
- Link equivalent observations to a shared candidate when they support the same reusable implication.
- Merge candidates when they express the same reusable knowledge.
- Merge concepts when they normalize the same engineering pattern.
- Preserve source identities and merge rationale.
- Superseded knowledge must remain historically traceable.

Knowledge consolidation should reduce duplicated knowledge statements while preserving evidence diversity.

## AI-Assisted Extraction Principles

AI may assist extraction, but it does not govern knowledge.

AI may assist with:

- candidate identification
- concept suggestion
- classification suggestions
- relationship suggestions
- summarization
- generalization proposals
- duplicate detection suggestions

AI must not:

- automatically certify knowledge
- remove traceability
- decide governance outcomes
- treat generated summaries as evidence
- replace human or governed review where certification is required

AI outputs are proposals. Certification remains a governed process.

The canonical AI operations boundaries are defined in [../ai-operations/README.md](../ai-operations/README.md).

## Quality Principles

Extraction should maximize:

- accuracy
- traceability
- reusability
- determinism
- repeatability
- engineering value

Low-quality extraction creates long-term knowledge debt. The repository should prefer fewer well-evidenced candidates over many weak candidates.
