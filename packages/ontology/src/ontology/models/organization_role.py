from typing import Annotated, Literal, override

from pydantic import AnyUrl, ConfigDict, Field

from ontology.models.cbox import OrganizationRoleName
from ontology.models.iri import Iri
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta
from ontology.models.role_base import RoleBase
from ontology.models.thing import Thing


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="OrganizationRole",
        description=(
            "A dated, named role an organization plays on a debt instrument, "
            "an agreement, or within another organization. The organization "
            "points to this role via memberOf; the role points onward to its "
            "target the same way."
        ),
        named_individuals=named_individuals,
    )


class OrganizationRole(RoleBase):
    """A dated, named role an organization plays on a debt instrument, an
    agreement, or within another organization. The organization points to
    this role via memberOf; the role points onward to its target the same
    way."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["OrganizationRole"] = Field(alias="@type")
    member_of: Annotated[
        Iri | None,
        Thing.Fields.MEMBER_OF,
        PropertyMeta(
            description="The thing this role is a membership of.",
            range_=("DebtInstrument", "Agreement", "Organization"),
            title="Member Of",
        ).generate_meta(),
    ] = Field(default=None, alias="memberOf")
    role_name: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("OrganizationRoleName"),
        Thing.Fields.ROLE_NAME,
        PropertyMeta(
            description="The role played (issuer, trustee, fiscal agent).",
            range_=OrganizationRoleName,
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
