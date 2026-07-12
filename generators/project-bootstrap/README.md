# Project Bootstrap Generator

This is the first implemented generator for the AI Platform Engineering Knowledge Base.

The generator is implemented by the thin CLI runtime in `cli/aikb_cli/project_bootstrap.py`.

## Identifier

`project-bootstrap`

## Version

`0.1.0`

## Purpose

Bootstrap a new engineering repository from Certified Knowledge, a passive template, and command configuration.

## Inputs

- Certified Knowledge from `certified/`
- template `templates/project-bootstrap/basic`
- project type
- project name
- output directory

## Outputs

- repository structure
- `.aikb/project-manifest.json`
- `.aikb/knowledge-source.md`
- `README.md`
- `GOVERNANCE.md`
- `ROADMAP.md`
- `BACKLOG.md`
- `docs/architecture.md`

## Governance Boundary

The generator does not certify knowledge, alter Certified Knowledge, onboard repositories, or create canonical knowledge.
