# Statistics Report Examples

`aikb stats` produces a derived, non-canonical snapshot of the Knowledge Base. It does not modify canonical Knowledge Objects, governance state, Git state, or registered Knowledge Sources.

Markdown output to the terminal:

```text
bin/aikb stats
```

JSON output for a dashboard or trend-analysis consumer:

```text
bin/aikb stats --format json
```

An explicitly requested derived report:

```text
bin/aikb stats --format markdown --output reports/aikb-stats.md
```

Lifecycle percentages in the report describe the current population funnel. They are not promotion targets or quality thresholds.
