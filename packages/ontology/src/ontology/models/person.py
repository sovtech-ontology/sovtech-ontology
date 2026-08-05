from typing import Annotated, Literal, override

from pydantic import ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.iri import Iri
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.person_role import PersonRole
from ontology.models.property_meta import PropertyMeta
from ontology.models.thing import Thing


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="Person",
        description=(
            "An individual person: a signatory, authorized representative, "
            "or named contact."
        ),
        named_individuals=named_individuals,
    )


class Person(BaseResource):
    """An individual person: a signatory, authorized representative, or
    named contact."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["Person"] = Field(alias="@type")
    description: Annotated[str | None, Thing.Fields.DESCRIPTION] = None
    member_of: Annotated[
        tuple[Iri, ...],
        Thing.Fields.MEMBER_OF,
        PropertyMeta(
            description="The person roles this person fills.",
            range_=PersonRole,
            title="Member Of",
        ).generate_meta(),
    ] = Field(alias="memberOf")
    name: Annotated[str | None, Thing.Fields.NAME] = None

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
