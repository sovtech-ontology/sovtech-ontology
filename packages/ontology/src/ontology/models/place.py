from typing import Annotated, Literal, override

from pydantic import ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.iri import Iri
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta
from ontology.models.thing import Thing


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="Place",
        description=(
            "A general place or venue that is neither a country nor an "
            "administrative area (the Borough of Manhattan)."
        ),
        named_individuals=named_individuals,
    )


class Place(BaseResource):
    """A general place or venue that is neither a country nor an
    administrative area (the Borough of Manhattan)."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["Place"] = Field(alias="@type")
    contained_in_place: Annotated[
        tuple[Iri, ...] | None,
        PropertyMeta(
            description="Places that contain this place.",
            range_="Place",
            title="Contained In Place",
        ).generate_meta(),
    ] = Field(default=None, alias="containedInPlace")
    name: Annotated[str | None, Thing.Fields.NAME] = None

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
