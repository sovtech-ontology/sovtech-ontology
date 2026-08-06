from typing import Annotated, Literal, override

from pydantic import AnyUrl, ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.cbox.issuer_type import IssuerType
from ontology.models.iri import Iri
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.organization_role import OrganizationRole
from ontology.models.property_meta import PropertyMeta
from ontology.models.thing import Thing


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="Organization",
        description=(
            "Any institutional actor: a sovereign state, ministry, central "
            "bank, sub-sovereign, SPV, state-owned enterprise, "
            "supranational, commercial bank, trustee, or law firm."
        ),
        named_individuals=named_individuals,
    )


class Organization(BaseResource):
    """Any institutional actor: a sovereign state, ministry, central bank,
    sub-sovereign, SPV, state-owned enterprise, supranational, commercial
    bank, trustee, or law firm."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["Organization"] = Field(alias="@type")
    description: Annotated[str | None, Thing.Fields.DESCRIPTION] = None
    issuer_type: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("IssuerType"),
        Thing.Fields.ADDITIONAL_TYPE,
        PropertyMeta(
            description=(
                "The public-sector classification, for organizations that "
                "issue. Absent for non-issuers."
            ),
            range_=IssuerType,
            title="Issuer Type",
        ).generate_meta(),
    ] = Field(default=None, alias="issuerType")
    lei_code: Annotated[
        str | None,
        PropertyMeta(
            description="The Legal Entity Identifier. Never guessed.",
            title="LEI",
        ).generate_meta(),
    ] = Field(default=None, alias="leiCode")
    location: Annotated[
        Iri | None,
        Thing.Fields.LOCATION,
        PropertyMeta(
            description=("The home country or seat (a Country for sovereigns)."),
            range_="Place",
            title="Location",
        ).generate_meta(),
    ] = None
    member_of: Annotated[
        tuple[Iri, ...],
        Thing.Fields.MEMBER_OF,
        PropertyMeta(
            description="The organization roles this organization fills.",
            range_=OrganizationRole,
            title="Member Of",
        ).generate_meta(),
    ] = Field(alias="memberOf")
    name: Annotated[str | None, Thing.Fields.NAME] = None
    parent_organization: Annotated[
        Iri | None,
        PropertyMeta(
            description=(
                "The organization this one belongs to (an SOE or central "
                "bank pointing to its state)."
            ),
            range_="Organization",
            title="Parent Organization",
        ).generate_meta(),
    ] = Field(default=None, alias="parentOrganization")

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
