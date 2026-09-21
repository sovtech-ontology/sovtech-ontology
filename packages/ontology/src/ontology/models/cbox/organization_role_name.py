from typing import Annotated, Literal, override

from pydantic import ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.cbox.organization_role_category import OrganizationRoleCategory
from ontology.models.iri import Iri
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta
from ontology.models.thing import Thing


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="OrganizationRoleName",
        description=(
            "A classification of the role an organization plays on a debt "
            "instrument or agreement (issuer, trustee, fiscal agent)."
        ),
        named_individuals=named_individuals,
    )


class OrganizationRoleName(BaseResource):
    """A classification of the role an organization plays on a debt
    instrument or agreement (issuer, trustee, fiscal agent)."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    id: Annotated[Iri, named_individual_iri_enum("OrganizationRoleName")] = Field(
        alias="@id"
    )
    type_: Literal["OrganizationRoleName"] = Field(alias="@type")
    additional_type: Annotated[
        Iri | None,
        Thing.Fields.ADDITIONAL_TYPE,
        PropertyMeta(
            description="The broad category this role name falls under.",
            range_=OrganizationRoleCategory,
            title="Additional Type",
        ).generate_meta(),
    ] = Field(default=None, alias="additionalType")
    description: Annotated[str | None, Thing.Fields.DESCRIPTION] = None
    name: Annotated[str | None, Thing.Fields.NAME] = None

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
