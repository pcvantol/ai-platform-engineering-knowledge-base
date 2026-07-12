# Engineering Program Examples

This area documents example uses of `aikb generate`.

Examples are non-canonical. Generated Engineering Programs are derived artifacts and must not be treated as Certified Knowledge.

## Example Commands

```text
bin/aikb generate verification-platform --output /tmp/verification-platform-program
```

```text
bin/aikb generate ai-platform --output /tmp/ai-platform-program
```

```text
bin/aikb generate embedded-platform --output /tmp/embedded-platform-program
```

```text
bin/aikb generate software-assurance --output /tmp/software-assurance-program
```

## Example Output Shape

Each generated program contains:

- architecture;
- governance;
- roadmap;
- backlog;
- verification strategy;
- software assurance strategy;
- release strategy;
- engineering guidance;
- engineering checklists;
- engineering prompts;
- an Engineering Program Manifest.

## Traceability Expectation

Every generated artifact must remain traceable to Certified Knowledge and supporting evidence through `.aikb/engineering-program-manifest.json`.
