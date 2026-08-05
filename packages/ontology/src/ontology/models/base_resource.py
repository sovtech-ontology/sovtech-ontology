"""Abstract base for all resources.

Every resource has an "@id", typed with Iri, so compact IRIs (CURIEs) are
expanded ahead of AnyUrl validation. Subclasses narrow the id type where the
model requires it (e.g. to a named-individual enum) and serialize/validate
under the JSON-LD "@id" alias.
"""

import json
from abc import ABC, abstractmethod
from typing import cast

from pydantic import BaseModel, ConfigDict, Field
from pyld import jsonld

from ontology.models.config import Config
from ontology.models.iri import Iri
from ontology.models.object_meta import ObjectMeta


def default_context() -> dict:
    """The package's JSON-LD context, read from the file Config points at."""

    return cast(
        "dict",
        json.loads(Config().sovtech_jsonld_context.read_text(encoding="utf-8"))[
            "@context"
        ],
    )


class BaseResource(BaseModel, ABC):
    model_config = ConfigDict(populate_by_name=True)

    id: Iri = Field(alias="@id")

    @classmethod
    @abstractmethod
    def object_meta(cls) -> ObjectMeta | None:
        """The class-level metadata: concrete models return their module's
        _object_meta(), which lets PropertyMeta resolve a range model to its
        @type; abstract shared shapes (e.g. RoleBase) inherit the None."""
        return None

    @abstractmethod
    def to_rdf(self, jsonld_context: dict) -> str:
        """Serialize a JSON-LD node object to RDF (N-Quads), interpreting it
        against jsonld_context (typically default_context()).

        Abstract with a default implementation: concrete models must opt in
        explicitly, typically with `return super().to_rdf(jsonld_context)`.
        """

        # pyld is untyped; with a "format" option to_rdf always returns str.
        return cast(
            "str",
            jsonld.to_rdf(
                {
                    "@context": jsonld_context,
                    **(self.model_dump(mode="json", by_alias=True, exclude_none=True)),
                },
                {"format": "application/n-quads"},
            ),
        )
