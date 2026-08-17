from typing import Annotated, Literal, override

from pydantic import ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.iri import Iri
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.thing import Thing


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="PaymentFrequency",
        description=(
            "How often interest is paid (annual, semi-annual, quarterly, "
            "monthly, at maturity)."
        ),
        named_individuals=named_individuals,
    )


class PaymentFrequency(BaseResource):
    """How often interest is paid (annual, semi-annual, quarterly, monthly,
    at maturity)."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    id: Annotated[Iri, named_individual_iri_enum("PaymentFrequency")] = Field(
        alias="@id"
    )
    type_: Literal["PaymentFrequency"] = Field(alias="@type")
    name: Annotated[str | None, Thing.Fields.NAME] = None
    description: Annotated[str | None, Thing.Fields.DESCRIPTION] = None

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
