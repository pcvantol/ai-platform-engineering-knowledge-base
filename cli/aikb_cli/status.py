from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass(frozen=True)
class CommandStatus:
    command: str
    purpose: str
    status: str
    implementation: str
    execution: str


@dataclass(frozen=True)
class StatusConfig:
    output: Path | None = None


@dataclass(frozen=True)
class StatusResult:
    report: str
    report_path: Path | None
    implemented_count: int
    architecture_only_count: int


IMPLEMENTED_COMMANDS = (
    CommandStatus("aikb init", "Bootstrap a knowledge-driven engineering project.", "Implemented", "project_bootstrap.py", "Executable; writes a generated project to the selected output directory."),
    CommandStatus("aikb onboard", "Register a repository as a Knowledge Source.", "Implemented", "onboarding.py", "Executable; writes Knowledge Source onboarding records."),
    CommandStatus("aikb extract", "Extract Engineering Observations from registered Knowledge Sources.", "Implemented", "extraction.py", "Executable; writes Engineering Observation records."),
    CommandStatus("aikb classify", "Generate Knowledge Candidates from Engineering Observations.", "Implemented", "classification.py", "Executable; writes Knowledge Candidate records."),
    CommandStatus("aikb review", "Form Knowledge Concepts from related Knowledge Candidates.", "Implemented", "review.py", "Executable; writes Knowledge Concept records."),
    CommandStatus("aikb generalize", "Create Generalized Knowledge from Knowledge Concepts.", "Implemented", "generalization.py", "Executable; writes Generalized Knowledge records."),
    CommandStatus("aikb certify", "Certify eligible Generalized Knowledge.", "Implemented", "certification.py", "Executable; writes Certified Knowledge and a certification record."),
    CommandStatus("aikb ask", "Answer engineering questions from Certified Knowledge.", "Implemented", "assistant.py", "Executable; read-only."),
    CommandStatus("aikb generate", "Generate a complete engineering program from Certified Knowledge.", "Implemented", "program_generation.py", "Executable; writes a generated Engineering Program."),
    CommandStatus("aikb evolve", "Compare Engineering Programs against current Certified Knowledge.", "Implemented", "evolution.py", "Executable; read-only unless an external report output is requested."),
    CommandStatus("aikb validate", "Validate Knowledge Base consistency, traceability and qualification.", "Implemented", "validation.py", "Executable; read-only unless an external report output is requested."),
    CommandStatus("aikb improve", "Analyze Knowledge Operating System metrics and propose improvements.", "Implemented", "improvement.py", "Executable; read-only unless an external report output is requested."),
    CommandStatus("aikb status", "Report the implemented, architectural and placeholder CLI surface.", "Implemented", "status.py", "Executable; read-only unless an external report output is requested."),
    CommandStatus("aikb stats", "Report derived Knowledge Base statistics.", "Implemented", "stats.py", "Executable; read-only unless an external report output is requested."),
)


ARCHITECTURE_ONLY_COMMANDS = (
    CommandStatus("aikb agent", "Multi-Agent Engineering Runtime namespace.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb agent list", "List available engineering agents.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb agent run", "Run an engineering agent.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb agent explain", "Explain an agent decision and knowledge basis.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb agent trace", "Render agent execution traceability.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb run", "Coordinate a task graph through the Engineering Runtime Orchestrator.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb plan", "Render an execution plan without running agents.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb explain-plan", "Explain execution-plan rationale and Certified Knowledge basis.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb trace-run", "Render execution traceability for a runtime run.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb show-graph", "Visualize a runtime task graph.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb capability", "Capability Extension Framework namespace.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb capability list", "List available engineering capabilities.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb capability info", "Show capability metadata and dependencies.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb capability enable", "Activate a capability for an engineering context.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb capability disable", "Deactivate a capability for an engineering context.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb capability validate", "Validate a capability and its integration contract.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb goal", "Interpret an engineering goal and plan capabilities.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb explain-goal", "Explain goal interpretation and the selected knowledge basis.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb show-plan", "Show a goal-derived execution plan.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb trace-goal", "Render goal-to-deliverable traceability.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb simulate-goal", "Simulate a goal-driven engineering plan.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb mission", "Autonomous Engineering Mission Runtime namespace.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb mission status", "Show mission state, checkpoints, blockers and progress.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb mission explain", "Explain mission rationale, capabilities and knowledge basis.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb mission trace", "Render mission traceability to Certified Knowledge and evidence.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb mission validate", "Validate mission state, outputs, checkpoints and traceability.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb mission report", "Produce a derived Mission Report.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb qualify", "Engineering Operating System qualification namespace.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb qualify runtime", "Qualify runtime, orchestrator, agent and mission architecture.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb qualify knowledge", "Qualify Knowledge Base integrity, lineage and certification state.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb qualify missions", "Qualify mission state, checkpoints and evidence.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb qualify report", "Produce a Qualification Report.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb qualify trace", "Render qualification-decision traceability.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb qualify explain", "Explain qualification findings, decisions and evidence.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb qualify scorecard", "Produce knowledge, runtime, mission, repository and publication scorecards.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb publish", "Generate or refresh publications from Certified Knowledge.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
    CommandStatus("aikb doctor", "Report repository, quality, traceability and health findings.", "Architecture only", "None", "Placeholder; not registered by the CLI parser."),
)


class CliStatusReporter:
    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root

    def report(self, config: StatusConfig) -> StatusResult:
        report = self._render_report()
        report_path = None
        if config.output:
            report_path = config.output.resolve()
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(report, encoding="utf-8")
        return StatusResult(
            report=report,
            report_path=report_path,
            implemented_count=len(IMPLEMENTED_COMMANDS),
            architecture_only_count=len(ARCHITECTURE_ONLY_COMMANDS),
        )

    def _render_report(self) -> str:
        timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        implemented = self._render_rows(IMPLEMENTED_COMMANDS)
        architecture_only = self._render_rows(ARCHITECTURE_ONLY_COMMANDS)
        return f"""# AI Platform Engineering CLI Status Report

## Report Metadata

| Field | Value |
| --- | --- |
| Generated at | `{timestamp}` |
| CLI entrypoint | `bin/aikb` |
| Repository root | `{self.repository_root}` |
| Report type | Derived runtime status; non-canonical |

## Status Summary

| Status | Count | Meaning |
| --- | ---: | --- |
| Implemented and executable | {len(IMPLEMENTED_COMMANDS)} | Registered by the current CLI parser and backed by a runtime implementation. |
| Architecture only | {len(ARCHITECTURE_ONLY_COMMANDS)} | Described in the CLI architecture but not registered by the current CLI parser. |
| Placeholders | {len(ARCHITECTURE_ONLY_COMMANDS)} | Architecture-only commands are placeholders and cannot be executed. |

## Implemented and Executable Commands

| Command | Purpose | Implementation | Execution |
| --- | --- | --- | --- |
{implemented}

## Architecture-Only Commands and Placeholders

| Command | Purpose | Implementation | Execution |
| --- | --- | --- | --- |
{architecture_only}

## Interpretation Rules

- **Implemented and executable** means the command is registered in `bin/aikb --help` and has a runtime implementation in `cli/aikb_cli/`.
- **Architecture only** means the command is intentionally documented as a future interface. It has no current parser registration or runtime implementation.
- **Placeholder** is not a separate implementation state in this repository: every architecture-only command is a non-executable placeholder until governed implementation work adds it to the runtime.
- This report describes command availability. It does not grant governance authority or change the canonical status of Certified Knowledge.
"""

    @staticmethod
    def _render_rows(commands: tuple[CommandStatus, ...]) -> str:
        return "\n".join(
            f"| `{item.command}` | {item.purpose} | `{item.implementation}` | {item.execution} |"
            for item in commands
        )
