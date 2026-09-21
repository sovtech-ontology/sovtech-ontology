from typing import Annotated, Literal, override

from pydantic import ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.debt_instrument import DebtInstrument
from ontology.models.iri import Iri
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.organization import Organization
from ontology.models.property_meta import PropertyMeta
from ontology.models.thing import Thing
from ontology.models.timestamp import Timestamp


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="CreditRating",
        description=(
            "A credit rating assigned by an agency to an organization or "
            "debt instrument, on the agency's own scale. An unrated thing "
            "has no rating node."
        ),
        named_individuals=named_individuals,
    )


class CreditRating(BaseResource):
    """A credit rating assigned by an agency to an organization or debt
    instrument, on the agency's own scale. An unrated thing has no rating
    node."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["CreditRating"] = Field(alias="@type")
    about: Annotated[
        Iri | None,
        Thing.Fields.ABOUT,
        PropertyMeta(
            description="The organization or instrument this rating rates.",
            range_=(Organization, DebtInstrument),
            title="About",
        ).generate_meta(),
    ] = None
    author: Annotated[
        Iri | None,
        PropertyMeta(
            description="The rating agency.",
            range_=Organization,
            title="Author",
        ).generate_meta(),
    ] = None
    date_published: Annotated[
        Timestamp | None,
        PropertyMeta(
            description="When the rating was assigned or last affirmed.",
            title="Date Published",
        ).generate_meta(),
    ] = Field(default=None, alias="datePublished")
    rating_value: Annotated[
        str,
        PropertyMeta(
            description='The rating on the agency\'s own scale ("B2", "AA-").',
            title="Rating Value",
        ).generate_meta(),
    ] = Field(alias="ratingValue")

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
