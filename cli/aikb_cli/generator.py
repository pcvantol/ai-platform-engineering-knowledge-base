from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Generic, TypeVar


ConfigT = TypeVar("ConfigT")
ResultT = TypeVar("ResultT")


@dataclass(frozen=True)
class GeneratorDescriptor:
    identifier: str
    version: str
    supported_project_types: tuple[str, ...]


class Generator(ABC, Generic[ConfigT, ResultT]):
    descriptor: GeneratorDescriptor

    @abstractmethod
    def generate(self, config: ConfigT) -> ResultT:
        """Generate derived output from Certified Knowledge and passive templates."""


class GeneratorRegistry:
    def __init__(self) -> None:
        self._project_generators: dict[str, type[Generator]] = {}

    def register_project_generator(
        self,
        project_types: tuple[str, ...],
        generator_type: type[Generator],
    ) -> None:
        for project_type in project_types:
            self._project_generators[project_type] = generator_type

    def project_types(self) -> tuple[str, ...]:
        return tuple(sorted(self._project_generators))

    def create_for_project_type(
        self,
        project_type: str,
        repository_root: Path,
    ) -> Generator:
        try:
            generator_type = self._project_generators[project_type]
        except KeyError as exc:
            supported = ", ".join(self.project_types())
            raise RuntimeError(
                f"Unsupported project type: {project_type}. Supported project types: {supported}"
            ) from exc
        return generator_type(repository_root)
