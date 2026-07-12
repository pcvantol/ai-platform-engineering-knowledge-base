# Multi-Agent Workflow Examples

This area documents example workflows for the future Multi-Agent Engineering Runtime.

Examples are non-canonical. They demonstrate orchestration shapes only and do not implement agents.

## Architecture Review Workflow

```text
Engineer Request
->
Architecture Agent
->
Software Assurance Agent
->
Runtime Aggregation
->
Traceable Review Result
->
Human Engineering Review
```

Expected traceability:

```text
Review Result
->
Agent
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

## Verification Strategy Workflow

```text
Engineer Request
->
Verification Agent
->
Certified Knowledge Retrieval
->
Evidence-Aware Strategy Draft
->
Human Review
```

## Knowledge Extraction Preparation Workflow

```text
Engineer Request
->
Repository Analysis Agent
->
Knowledge Extraction Agent
->
Knowledge Review Agent
->
Governed Lifecycle Command
```

## Conflict Reporting Workflow

```text
Parallel Agent Results
->
Runtime Conflict Detection
->
Supporting Knowledge Comparison
->
Evidence Review
->
Human Decision
```

## Boundary

The examples do not:

- implement agents;
- implement scheduling;
- modify Certified Knowledge;
- approve certification;
- approve publication;
- change governance;
- mutate repository history.
