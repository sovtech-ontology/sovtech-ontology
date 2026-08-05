from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any

from annotated_types import GroupedMetadata
from pydantic import AfterValidator, AnyUrl, BeforeValidator, Field

from ontology.models.utils import expand_iri


@dataclass(frozen=True)
class IriEnum(GroupedMetadata):
    """An AnyUrl restricted to a fixed set of IRIs, CURIE-expanded first."""

    allowed_iris: tuple[str, ...]

    def __iter__(self) -> Iterator[Any]:
        yield BeforeValidator(expand_iri)
        yield AfterValidator(self._check_membership)
        yield Field(json_schema_extra={"enum": list(self.allowed_iris)})

    def _check_membership(self, iri: AnyUrl) -> AnyUrl:
        if str(iri) not in self.allowed_iris:
            raise ValueError(f'"{iri}" is not one of {list(self.allowed_iris)}')
        return iri
