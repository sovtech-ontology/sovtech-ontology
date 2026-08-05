from typing import Annotated, Literal, override

from pydantic import AnyUrl, ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.iri import Iri
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.person_role_category import PersonRoleCategory
from ontology.models.property_meta import PropertyMeta
from ontology.models.thing import Thing


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="PersonRoleName",
        description=(
            "A classification of the role a person plays within an "
            "organization or on an agreement (signatory, authorized "
            "representative)."
        ),
        named_individuals=named_individuals,
    )


class PersonRoleName(BaseResource):
    """A classification of the role a person plays within an organization or
    on an agreement (signatory, authorized representative)."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    id: Annotated[AnyUrl, named_individual_iri_enum("PersonRoleName")] = Field(
        alias="@id"
    )
    type_: Literal["PersonRoleName"] = Field(alias="@type")
    additional_type: Annotated[
        Iri,
        Thing.Fields.ADDITIONAL_TYPE,
        PropertyMeta(
            description="The broad category this role name falls under.",
            range_=PersonRoleCategory,
            title="Additional Type",
        ).generate_meta(),
    ] = Field(alias="additionalType")
    description: Annotated[str | None, Thing.Fields.DESCRIPTION] = None
    name: Annotated[str | None, Thing.Fields.NAME] = None

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
