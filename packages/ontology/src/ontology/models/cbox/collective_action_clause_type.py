from typing import Annotated, Literal, override

from pydantic import AnyUrl, ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.thing import Thing


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="CollectiveActionClauseType",
        description=(
            "A classification of collective action clauses by generation, "
            "from none to the post-2014 enhanced ICMA model."
        ),
        named_individuals=named_individuals,
    )


class CollectiveActionClauseType(BaseResource):
    """A classification of collective action clauses by generation, from none
    to the post-2014 enhanced ICMA model."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    id: Annotated[AnyUrl, named_individual_iri_enum("CollectiveActionClauseType")] = (
        Field(alias="@id")
    )
    type_: Literal["CollectiveActionClauseType"] = Field(alias="@type")
    name: Annotated[str | None, Thing.Fields.NAME] = None
    description: Annotated[str | None, Thing.Fields.DESCRIPTION] = None

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
