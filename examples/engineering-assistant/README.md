# Knowledge-Driven Engineering Assistant Examples

This area contains examples for `aikb ask`.

Examples are derived usage demonstrations. They are not canonical knowledge and must not be treated as Certified Knowledge.

## Example Questions

```text
bin/aikb ask "How should I architect a verification runtime?"
```

```text
bin/aikb ask "What verification strategy should a new AI platform use?"
```

```text
bin/aikb ask "How should software assurance integrate with platform qualification?"
```

```text
bin/aikb ask "How should release documentation support platform governance?"
```

## Example Answer Shape

Every answer is rendered with the same structure:

- engineering conclusion
- supporting rationale
- supporting Certified Knowledge
- supporting evidence
- related knowledge
- knowledge confidence
- traceability references
- uncertainty statement

## Example Traceability

```text
Answer
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

## Governance Boundary

The assistant is read-only.

It does not:

- modify repositories
- extract observations
- generate candidates
- form concepts
- generalize knowledge
- certify knowledge
- generate publications
- invent Certified Knowledge
- invent engineering evidence
