# Validation Report Examples

This area documents example uses of `aikb validate`.

Validation Reports are evidence artifacts for governance review. They do not modify the Knowledge Base and do not approve remediation.

## Example Commands

```text
bin/aikb validate
```

```text
bin/aikb validate --knowledge
```

```text
bin/aikb validate --publications
```

```text
bin/aikb validate --sources
```

```text
bin/aikb validate --knowledge --output /tmp/aikb-validation-report.md
```

## Report Contents

Each validation report contains:

- validation metadata;
- qualification decisions;
- Knowledge Scorecard;
- validation findings;
- evidence for each finding;
- remediation recommendations;
- repository qualification boundary.

## Qualification Decisions

Supported decisions:

- `KNOWLEDGE_VALID`
- `TRACEABILITY_VALID`
- `RELATIONSHIPS_VALID`
- `CERTIFICATION_VALID`
- `PUBLICATION_VALID`
- `REPOSITORY_VALID`

## Read-Only Boundary

`aikb validate` does not:

- modify Certified Knowledge;
- repair findings automatically;
- change governance;
- approve qualification;
- rewrite publications;
- rewrite source records.
