# Evolution Report Examples

This area documents example uses of `aikb evolve`.

Evolution Reports are derived review artifacts. They are not Certified Knowledge and they do not approve program changes.

## Example Commands

```text
bin/aikb evolve --program /tmp/verification-platform-program
```

```text
bin/aikb evolve verification-platform --output /tmp/verification-platform-evolution
```

```text
bin/aikb evolve --program /tmp/ai-platform-program --output /tmp/ai-platform-evolution-report.md
```

## Report Contents

Each report contains:

- review metadata;
- knowledge drift classification;
- gap analysis;
- impact analysis;
- evolution recommendations;
- affected artifacts;
- affected Certified Knowledge;
- supporting traceability;
- manifest extension proposal;
- governance boundary.

## Read-Only Boundary

`aikb evolve` does not:

- modify an Engineering Program;
- modify an Engineering Program Manifest;
- modify Certified Knowledge;
- modify repositories;
- approve evolution;
- generate publications.
