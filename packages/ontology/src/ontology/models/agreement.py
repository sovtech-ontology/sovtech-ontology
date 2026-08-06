from typing import Annotated, Literal, override

from pydantic import AnyUrl, ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.cbox import AgreementType, GoverningLaw
from ontology.models.iri import Iri
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta
from ontology.models.thing import Thing
from ontology.models.timestamp import Timestamp


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="Agreement",
        description=(
            "A legal instrument creating or administering debt: a trust "
            "indenture, fiscal agency agreement, trust deed, loan agreement, "
            "or guarantee. The attachment point for governing law, "
            "jurisdiction, provisions, defined terms, and party roles. "
            "Memorialized by digital documents via about."
        ),
        named_individuals=named_individuals,
    )


class Agreement(BaseResource):
    """A legal instrument creating or administering debt: a trust indenture,
    fiscal agency agreement, trust deed, loan agreement, or guarantee. The
    attachment point for governing law, jurisdiction, provisions, defined
    terms, and party roles. Memorialized by digital documents via about."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["Agreement"] = Field(alias="@type")
    agreement_type: Annotated[
        AnyUrl,
        named_individual_iri_enum("AgreementType"),
        PropertyMeta(
            description=(
                "The kind of legal instrument (trust indenture vs fiscal "
                "agency agreement)."
            ),
            range_=AgreementType,
            title="Agreement Type",
        ).generate_meta(),
    ] = Field(alias="agreementType")
    description: Annotated[str | None, Thing.Fields.DESCRIPTION] = None
    effective_date: Annotated[
        Timestamp | None,
        PropertyMeta(
            description="When the agreement takes effect.",
            title="Effective Date",
        ).generate_meta(),
    ] = Field(default=None, alias="effectiveDate")
    execution_date: Annotated[
        Timestamp | None,
        PropertyMeta(
            description="When the agreement was signed.",
            title="Execution Date",
        ).generate_meta(),
    ] = Field(default=None, alias="executionDate")
    governing_law: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("GoverningLaw"),
        PropertyMeta(
            description=("The body of law governing interpretation and enforcement."),
            range_=GoverningLaw,
            title="Governing Law",
        ).generate_meta(),
    ] = Field(default=None, alias="governingLaw")
    jurisdiction: Annotated[
        tuple[Iri, ...] | None,
        PropertyMeta(
            description=("The venue(s) whose courts have jurisdiction over disputes."),
            range_="Place",
            title="Jurisdiction",
        ).generate_meta(),
    ] = None
    name: Annotated[str | None, Thing.Fields.NAME] = None

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
