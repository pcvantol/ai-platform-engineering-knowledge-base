from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from .assistant import AskConfig, EngineeringAssistant
from .classification import ClassifyConfig, KnowledgeCandidateGenerator
from .certification import CertifyConfig, KnowledgeCertifier
from .evolution import EvolveConfig, EngineeringProgramEvolution
from .extraction import EngineeringObservationExtractor, ExtractConfig
from .generator import GeneratorRegistry
from .generalization import GeneralizeConfig, KnowledgeGeneralizer
from .improvement import ImproveConfig, KnowledgeSystemImprover, SUPPORTED_IMPROVEMENT_AREAS
from .onboarding import OnboardConfig, RepositoryOnboarding
from .program_generation import (
    GenerateConfig,
    EngineeringProgramGenerator,
    SUPPORTED_PROGRAM_TYPES,
)
from .project_bootstrap import BootstrapConfig, ProjectBootstrapGenerator
from .review import KnowledgeConceptFormer, ReviewConfig
from .status import CliStatusReporter, StatusConfig
from .validation import KnowledgeBaseValidator, ValidateConfig


def build_registry() -> GeneratorRegistry:
    registry = GeneratorRegistry()
    registry.register_project_generator(
        ProjectBootstrapGenerator.descriptor.supported_project_types,
        ProjectBootstrapGenerator,
    )
    return registry


def build_parser(registry: GeneratorRegistry) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aikb",
        description="AI Platform Engineering Knowledge Base CLI.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser(
        "init",
        help="Bootstrap a knowledge-driven engineering project.",
    )
    init_parser.add_argument(
        "project_type",
        choices=registry.project_types(),
        help="Project type to bootstrap.",
    )
    init_parser.add_argument(
        "--name",
        help="Project identity. Defaults to the project type.",
    )
    init_parser.add_argument(
        "--output",
        type=Path,
        help="Output directory. Defaults to ./<name>.",
    )
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Allow writing into an existing directory.",
    )

    onboard_parser = subparsers.add_parser(
        "onboard",
        help="Register a repository as a Knowledge Source.",
    )
    onboard_parser.add_argument(
        "repository",
        help="Repository URL or host/path, such as github.com/owner/repository.",
    )
    onboard_parser.add_argument(
        "--identifier",
        help="Knowledge Source identifier. Defaults to a generated identifier.",
    )
    onboard_parser.add_argument(
        "--slug",
        help="Output folder under sources/. Defaults to a repository-derived slug.",
    )
    onboard_parser.add_argument(
        "--force",
        action="store_true",
        help="Allow overwriting generated onboarding files in an existing source folder.",
    )

    extract_parser = subparsers.add_parser(
        "extract",
        help="Extract Engineering Observations from registered Knowledge Sources.",
    )
    extract_parser.add_argument(
        "source_name",
        nargs="?",
        help="Optional Knowledge Source identifier, name, or slug.",
    )
    extract_parser.add_argument(
        "--source",
        dest="source_option",
        help="Optional Knowledge Source identifier, name, or slug.",
    )
    extract_parser.add_argument(
        "--force",
        action="store_true",
        help="Allow extracting evidence already referenced by existing observations.",
    )

    classify_parser = subparsers.add_parser(
        "classify",
        help="Generate Knowledge Candidates from Engineering Observations.",
    )
    classify_parser.add_argument(
        "source_name",
        nargs="?",
        help="Optional Knowledge Source identifier, repository name, or observation set slug.",
    )
    classify_parser.add_argument(
        "--source",
        dest="source_option",
        help="Optional Knowledge Source identifier, repository name, or observation set slug.",
    )
    classify_parser.add_argument(
        "--force",
        action="store_true",
        help="Allow generating candidates for observations already referenced by existing candidates.",
    )

    review_parser = subparsers.add_parser(
        "review",
        help="Form Knowledge Concepts from related Knowledge Candidates.",
    )
    review_parser.add_argument(
        "source_name",
        nargs="?",
        help="Optional Knowledge Source identifier, repository name, or candidate set slug.",
    )
    review_parser.add_argument(
        "--source",
        dest="source_option",
        help="Optional Knowledge Source identifier, repository name, or candidate set slug.",
    )
    review_parser.add_argument(
        "--force",
        action="store_true",
        help="Allow forming concepts from candidates already referenced by existing concepts.",
    )

    generalize_parser = subparsers.add_parser(
        "generalize",
        help="Create Generalized Knowledge from Knowledge Concepts.",
    )
    generalize_parser.add_argument(
        "source_name",
        nargs="?",
        help="Optional Knowledge Source identifier or concept set slug.",
    )
    generalize_parser.add_argument(
        "--source",
        dest="source_option",
        help="Optional Knowledge Source identifier or concept set slug.",
    )
    generalize_parser.add_argument(
        "--force",
        action="store_true",
        help="Allow generalizing concepts already referenced by existing generalized knowledge.",
    )

    certify_parser = subparsers.add_parser(
        "certify",
        help="Certify eligible Generalized Knowledge.",
    )
    certify_parser.add_argument(
        "source_name",
        nargs="?",
        help="Optional Knowledge Source identifier or generalized knowledge set slug.",
    )
    certify_parser.add_argument(
        "--source",
        dest="source_option",
        help="Optional Knowledge Source identifier or generalized knowledge set slug.",
    )
    certify_parser.add_argument(
        "--force",
        action="store_true",
        help="Allow certifying generalized knowledge already referenced by existing Certified Knowledge.",
    )

    ask_parser = subparsers.add_parser(
        "ask",
        help="Answer engineering questions from Certified Knowledge.",
    )
    ask_parser.add_argument(
        "question",
        nargs="*",
        help="Engineering question. If omitted, the question is read from stdin.",
    )
    ask_parser.add_argument(
        "--limit",
        type=int,
        default=4,
        help="Maximum number of Certified Knowledge items to use. Defaults to 4.",
    )
    ask_parser.add_argument(
        "--all-evidence",
        action="store_true",
        help="Render all supporting evidence instead of truncating long evidence lists.",
    )

    generate_parser = subparsers.add_parser(
        "generate",
        help="Generate a complete engineering program from Certified Knowledge.",
    )
    generate_parser.add_argument(
        "program_type",
        choices=SUPPORTED_PROGRAM_TYPES,
        help="Engineering program type to generate.",
    )
    generate_parser.add_argument(
        "--name",
        help="Program name. Defaults to a title derived from the program type.",
    )
    generate_parser.add_argument(
        "--output",
        type=Path,
        help="Output directory. Defaults to ./generated-programs/<program-type>.",
    )
    generate_parser.add_argument(
        "--force",
        action="store_true",
        help="Allow writing into an existing directory.",
    )

    evolve_parser = subparsers.add_parser(
        "evolve",
        help="Compare Engineering Programs against current Certified Knowledge.",
    )
    evolve_parser.add_argument(
        "target",
        nargs="?",
        help="Optional program type, program identifier, generated-programs slug, or program path.",
    )
    evolve_parser.add_argument(
        "--program",
        type=Path,
        help="Path to an Engineering Program directory or manifest.",
    )
    evolve_parser.add_argument(
        "--output",
        type=Path,
        help="Optional report file or directory. If omitted, reports are printed to stdout.",
    )

    validate_parser = subparsers.add_parser(
        "validate",
        help="Validate Knowledge Base consistency, traceability and qualification.",
    )
    validate_parser.add_argument(
        "--knowledge",
        action="store_true",
        help="Validate Knowledge Objects, relationships, traceability and certification.",
    )
    validate_parser.add_argument(
        "--publications",
        action="store_true",
        help="Validate publication consistency and Certified Knowledge references.",
    )
    validate_parser.add_argument(
        "--sources",
        action="store_true",
        help="Validate Knowledge Sources and source coverage.",
    )
    validate_parser.add_argument(
        "--output",
        type=Path,
        help="Optional validation report file. If omitted, the report is printed to stdout.",
    )

    improve_parser = subparsers.add_parser(
        "improve",
        help="Analyze Knowledge Operating System metrics and propose improvements.",
    )
    improve_parser.add_argument(
        "area",
        nargs="?",
        choices=SUPPORTED_IMPROVEMENT_AREAS,
        help="Optional improvement area. Defaults to all areas.",
    )
    improve_parser.add_argument(
        "--output",
        type=Path,
        help="Optional improvement report file. If omitted, the report is printed to stdout.",
    )

    status_parser = subparsers.add_parser(
        "status",
        help="Report implemented, architectural and placeholder CLI commands.",
    )
    status_parser.add_argument(
        "--output",
        type=Path,
        help="Optional status report file. If omitted, the report is printed to stdout.",
    )

    return parser


def main(
    argv: Sequence[str] | None = None,
    repository_root: Path | None = None,
) -> int:
    root = repository_root or Path.cwd()
    registry = build_registry()
    parser = build_parser(registry)
    args = parser.parse_args(argv)

    if args.command == "init":
        project_name = args.name or args.project_type
        output_dir = args.output or Path.cwd() / project_name
        config = BootstrapConfig(
            project_type=args.project_type,
            project_name=project_name,
            output_dir=output_dir,
            force=args.force,
        )
        generator = registry.create_for_project_type(args.project_type, root)
        result = generator.generate(config)
        print(f"Generated {result.project_name} at {result.output_dir}")
        print(f"Manifest: {result.manifest_path}")
        print(f"Certified Knowledge: {', '.join(result.certified_knowledge_ids)}")
        return 0

    if args.command == "onboard":
        result = RepositoryOnboarding(root).onboard(
            OnboardConfig(
                repository=args.repository,
                identifier=args.identifier,
                output_slug=args.slug,
                force=args.force,
            )
        )
        print(f"Registered Knowledge Source {result.identifier} for {result.name}")
        print(f"Profile: {result.profile_path}")
        print(f"Extraction Profile: {result.extraction_profile_path}")
        return 0

    if args.command == "extract":
        source = args.source_option or args.source_name
        results = EngineeringObservationExtractor(root).extract(
            ExtractConfig(source=source, force=args.force)
        )
        for result in results:
            print(
                f"Extracted {result.created_count} observations for {result.source_identifier} "
                f"({result.skipped_count} skipped)"
            )
            print(f"Observation set: {result.observation_set_path}")
        return 0

    if args.command == "classify":
        source = args.source_option or args.source_name
        results = KnowledgeCandidateGenerator(root).classify(
            ClassifyConfig(source=source, force=args.force)
        )
        for result in results:
            print(
                f"Generated {result.created_count} candidates for {result.source_identifier} "
                f"({result.skipped_count} skipped)"
            )
            print(f"Candidate set: {result.candidate_set_path}")
        return 0

    if args.command == "review":
        source = args.source_option or args.source_name
        results = KnowledgeConceptFormer(root).review(
            ReviewConfig(source=source, force=args.force)
        )
        for result in results:
            print(
                f"Formed {result.created_count} concepts for {result.source_identifier} "
                f"({result.skipped_count} candidates skipped)"
            )
            print(f"Concept set: {result.concept_set_path}")
        return 0

    if args.command == "generalize":
        source = args.source_option or args.source_name
        results = KnowledgeGeneralizer(root).generalize(
            GeneralizeConfig(source=source, force=args.force)
        )
        for result in results:
            print(
                f"Generated {result.created_count} generalized knowledge items for {result.source_identifier} "
                f"({result.skipped_count} skipped)"
            )
            print(f"Generalized knowledge set: {result.generalized_set_path}")
        return 0

    if args.command == "certify":
        source = args.source_option or args.source_name
        results = KnowledgeCertifier(root).certify(
            CertifyConfig(source=source, force=args.force)
        )
        for result in results:
            print(
                f"Certified {result.certified_count} knowledge items for {result.source_identifier} "
                f"({result.skipped_count} skipped)"
            )
            print(f"Certified knowledge set: {result.certified_set_path}")
            print(f"Certification record: {result.certification_record_path}")
        return 0

    if args.command == "ask":
        question = " ".join(args.question).strip()
        if not question:
            question = sys.stdin.read().strip()
        if not question:
            parser.error("aikb ask requires a question argument or stdin input.")
        answer = EngineeringAssistant(root).answer(
            AskConfig(
                question=question,
                limit=args.limit,
                show_all_evidence=args.all_evidence,
            )
        )
        print(answer, end="")
        return 0

    if args.command == "generate":
        output_dir = args.output or Path.cwd() / "generated-programs" / args.program_type
        result = EngineeringProgramGenerator(root).generate(
            GenerateConfig(
                program_type=args.program_type,
                name=args.name,
                output_dir=output_dir,
                force=args.force,
            )
        )
        print(f"Generated engineering program {result.program_identifier}")
        print(f"Output: {result.output_dir}")
        print(f"Manifest: {result.manifest_path}")
        print(f"Certified Knowledge: {', '.join(result.certified_knowledge_ids)}")
        return 0

    if args.command == "evolve":
        results = EngineeringProgramEvolution(root).evolve(
            EvolveConfig(
                target=args.target,
                program_path=args.program,
                output=args.output,
            )
        )
        for index, result in enumerate(results):
            if result.report_path:
                print(
                    f"Evolution report for {result.program_identifier}: "
                    f"{result.drift_level}, {result.recommendation_count} recommendations"
                )
                print(f"Report: {result.report_path}")
            else:
                if index:
                    print("\n---\n")
                print(result.report, end="")
        return 0

    if args.command == "validate":
        result = KnowledgeBaseValidator(root).validate(
            ValidateConfig(
                knowledge=args.knowledge,
                publications=args.publications,
                sources=args.sources,
                output=args.output,
            )
        )
        if result.report_path:
            print(f"Validation report: {result.report_path}")
            print(f"Findings: {result.finding_count}")
            print(
                "Qualification: "
                + ", ".join(f"{key}={value}" for key, value in result.qualification.items())
            )
        else:
            print(result.report, end="")
        return 0

    if args.command == "improve":
        result = KnowledgeSystemImprover(root).improve(
            ImproveConfig(area=args.area, output=args.output)
        )
        if result.report_path:
            print(f"Improvement report: {result.report_path}")
            print(f"Recommendations: {result.recommendation_count}")
        else:
            print(result.report, end="")
        return 0

    if args.command == "status":
        result = CliStatusReporter(root).report(StatusConfig(output=args.output))
        if result.report_path:
            print(f"CLI status report: {result.report_path}")
            print(f"Implemented and executable: {result.implemented_count}")
            print(f"Architecture only / placeholders: {result.architecture_only_count}")
        else:
            print(result.report, end="")
        return 0

    parser.error(f"Unsupported command: {args.command}")
    return 2
