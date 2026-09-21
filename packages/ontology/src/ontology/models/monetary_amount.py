from typing import Annotated, Literal, override

from pydantic import ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="MonetaryAmount",
        description=(
            "An amount of money in a currency. A structured value with an "
            "IRI like every resource; its purpose is expressed by the "
            "property pointing at it, so it carries no name."
        ),
        named_individuals=named_individuals,
    )


class MonetaryAmount(BaseResource):
    """An amount of money in a currency. A structured value with an IRI like
    every resource; its purpose is expressed by the property pointing at it,
    so it carries no name."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["MonetaryAmount"] = Field(alias="@type")
    currency: Annotated[
        str,
        PropertyMeta(
            description='The ISO 4217 currency code ("USD").',
            title="Currency",
        ).generate_meta(),
    ]
    value: Annotated[
        float,
        PropertyMeta(
            description="The amount.",
            title="Value",
        ).generate_meta(),
    ]

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
