from typing import Annotated, Literal, override

from pydantic import AnyUrl, ConfigDict, Field

from ontology.models.agreement import Agreement
from ontology.models.base_resource import BaseResource
from ontology.models.cbox import (
    CollectiveActionClauseType,
    PariPassuType,
    ProvisionType,
    SovereignImmunityWaiverType,
    VotingAggregationMethod,
)
from ontology.models.iri import Iri
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta
from ontology.models.quantitative_value import QuantitativeValue
from ontology.models.text_object import TextObject
from ontology.models.thing import Thing


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="ContractProvision",
        description=(
            "A typed unit of contract content: a clause or clause family as "
            "it appears in an agreement. The provision type says what kind "
            "of clause it is; the optional facets carry the "
            "machine-readable economics of the clauses that have them. "
            "Provisions nest: a reserved-matter modification provision has "
            "one child per voting aggregation method."
        ),
        named_individuals=named_individuals,
    )


class ContractProvision(BaseResource):
    """A typed unit of contract content: a clause or clause family as it
    appears in an agreement. The provision type says what kind of clause it
    is; the optional facets carry the machine-readable economics of the
    clauses that have them. Provisions nest: a reserved-matter modification
    provision has one child per voting aggregation method."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["ContractProvision"] = Field(alias="@type")
    cac_type: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("CollectiveActionClauseType"),
        PropertyMeta(
            description=("For collective action clauses: the CAC generation."),
            range_=CollectiveActionClauseType,
            title="CAC Type",
        ).generate_meta(),
    ] = Field(default=None, alias="cacType")
    description: Annotated[str | None, Thing.Fields.DESCRIPTION] = None
    grace_period: Annotated[
        Iri | None,
        PropertyMeta(
            description=("For default-related provisions: the cure period."),
            range_=QuantitativeValue,
            title="Grace Period",
        ).generate_meta(),
    ] = Field(default=None, alias="gracePeriod")
    immunity_waiver_type: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("SovereignImmunityWaiverType"),
        PropertyMeta(
            description=("For sovereign immunity waivers: full, none, or selective."),
            range_=SovereignImmunityWaiverType,
            title="Immunity Waiver Type",
        ).generate_meta(),
    ] = Field(default=None, alias="immunityWaiverType")
    is_part_of: Annotated[
        Iri,
        Thing.Fields.IS_PART_OF,
        PropertyMeta(
            description=(
                "The agreement this provision belongs to, or the parent "
                "provision it is a sub-rule of."
            ),
            range_=(Agreement, "ContractProvision"),
            title="Is Part Of",
        ).generate_meta(),
    ] = Field(alias="isPartOf")
    name: Annotated[str | None, Thing.Fields.NAME] = None
    pari_passu_type: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("PariPassuType"),
        PropertyMeta(
            description=(
                "For pari passu clauses: old (payment-interpretation-"
                "exposed) vs enhanced (ranking-only)."
            ),
            range_=PariPassuType,
            title="Pari Passu Type",
        ).generate_meta(),
    ] = Field(default=None, alias="pariPassuType")
    per_series_voting_threshold: Annotated[
        Iri | None,
        PropertyMeta(
            description=(
                "For two-tier cross-series modification: the threshold each "
                "affected series must separately meet."
            ),
            range_=QuantitativeValue,
            title="Per-Series Voting Threshold",
        ).generate_meta(),
    ] = Field(default=None, alias="perSeriesVotingThreshold")
    provision_type: Annotated[
        AnyUrl,
        named_individual_iri_enum("ProvisionType"),
        PropertyMeta(
            description="The kind of clause.",
            range_=ProvisionType,
            title="Provision Type",
        ).generate_meta(),
    ] = Field(alias="provisionType")
    source_text: Annotated[
        Iri | None,
        PropertyMeta(
            description=("The document text this provision was extracted from."),
            range_=TextObject,
            title="Source Text",
        ).generate_meta(),
    ] = Field(default=None, alias="sourceText")
    uniformly_applicable_required: Annotated[
        bool | None,
        PropertyMeta(
            description=(
                "For single-aggregated cross-series voting: whether "
                "uniformly applicable treatment is a condition."
            ),
            title="Uniformly Applicable Required",
        ).generate_meta(),
    ] = Field(default=None, alias="uniformlyApplicableRequired")
    voting_aggregation_method: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("VotingAggregationMethod"),
        PropertyMeta(
            description=(
                "For modification provisions: how votes aggregate across series."
            ),
            range_=VotingAggregationMethod,
            title="Voting Aggregation Method",
        ).generate_meta(),
    ] = Field(default=None, alias="votingAggregationMethod")
    voting_threshold: Annotated[
        Iri | None,
        PropertyMeta(
            description=(
                "For modification provisions: the (aggregate) approval "
                "threshold, as a minimum percent of principal outstanding."
            ),
            range_=QuantitativeValue,
            title="Voting Threshold",
        ).generate_meta(),
    ] = Field(default=None, alias="votingThreshold")

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
