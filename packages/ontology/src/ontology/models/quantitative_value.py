from typing import Annotated, Literal, override

from pydantic import ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="QuantitativeValue",
        description="A number with a unit, possibly bounded.",
        named_individuals=named_individuals,
    )


class QuantitativeValue(BaseResource):
    """A number with a unit, possibly bounded."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["QuantitativeValue"] = Field(alias="@type")
    max_value: Annotated[
        float | None,
        PropertyMeta(
            description="The upper bound, where the value is a range or cap.",
            title="Max Value",
        ).generate_meta(),
    ] = Field(default=None, alias="maxValue")
    min_value: Annotated[
        float | None,
        PropertyMeta(
            description=(
                'The lower bound — used for "more than X percent" voting thresholds.'
            ),
            title="Min Value",
        ).generate_meta(),
    ] = Field(default=None, alias="minValue")
    unit_code: Annotated[
        str | None,
        PropertyMeta(
            description=(
                "The UN/CEFACT unit code, where one applies (P1 percent, DAY days)."
            ),
            title="Unit Code",
        ).generate_meta(),
    ] = Field(default=None, alias="unitCode")
    unit_text: Annotated[
        str | None,
        PropertyMeta(
            description=(
                'A human-readable unit ("percent of aggregate principal '
                'outstanding", "days").'
            ),
            title="Unit Text",
        ).generate_meta(),
    ] = Field(default=None, alias="unitText")
    value: Annotated[
        float | None,
        PropertyMeta(
            description="The scalar value, where a single number applies.",
            title="Value",
        ).generate_meta(),
    ] = None

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
