from typing import Annotated, Literal, override

from pydantic import AnyUrl, ConfigDict, Field

from ontology.models.cbox import PersonRoleName
from ontology.models.iri import Iri
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta
from ontology.models.role_base import RoleBase
from ontology.models.thing import Thing


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="PersonRole",
        description=(
            "A dated, named role a person plays within an organization or on "
            "an agreement. The person points to this role via memberOf; the "
            "role points onward to its target the same way."
        ),
        named_individuals=named_individuals,
    )


class PersonRole(RoleBase):
    """A dated, named role a person plays within an organization or on an
    agreement. The person points to this role via memberOf; the role points
    onward to its target the same way."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["PersonRole"] = Field(alias="@type")
    member_of: Annotated[
        Iri,
        Thing.Fields.MEMBER_OF,
        PropertyMeta(
            description="The thing this role is a membership of.",
            range_=("Organization", "Agreement"),
            title="Member Of",
        ).generate_meta(),
    ] = Field(alias="memberOf")
    role_name: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("PersonRoleName"),
        Thing.Fields.ROLE_NAME,
        PropertyMeta(
            description=("The role played (signatory, authorized representative)."),
            range_=PersonRoleName,
            title="Role Name",
        ).generate_meta(),
    ] = Field(default=None, alias="roleName")

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
