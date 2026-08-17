from typing import Annotated, Literal, override

from pydantic import ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.iri import Iri
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta
from ontology.models.text_object import TextObject


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="DefinedTerm",
        description=(
            "A term defined in an agreement or disclosure document, as a "
            "SKOS concept in that agreement's lexicon. Defined terms are the "
            "wiring of the contract: negative pledge, pari passu, and "
            "cross-default all incorporate them."
        ),
        named_individuals=named_individuals,
    )


class DefinedTerm(BaseResource):
    """A term defined in an agreement or disclosure document, as a SKOS
    concept in that agreement's lexicon. Defined terms are the wiring of the
    contract: negative pledge, pari passu, and cross-default all incorporate
    them."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["DefinedTerm"] = Field(alias="@type")
    alt_label: Annotated[
        tuple[str, ...] | None,
        PropertyMeta(
            description="Variant forms and abbreviations of the term.",
            title="Alt Label",
        ).generate_meta(),
    ] = Field(default=None, alias="altLabel")
    broader: Annotated[
        tuple[Iri, ...] | None,
        PropertyMeta(
            description=(
                "Terms this term specializes, within the same agreement's lexicon."
            ),
            range_="DefinedTerm",
            title="Broader",
        ).generate_meta(),
    ] = None
    close_match: Annotated[
        tuple[Iri, ...] | None,
        PropertyMeta(
            description=("Substantially similar terms in other agreements' lexicons."),
            range_="DefinedTerm",
            title="Close Match",
        ).generate_meta(),
    ] = Field(default=None, alias="closeMatch")
    defined_in: Annotated[
        Iri,
        PropertyMeta(
            description="Where this term is defined.",
            range_=("Agreement", "DigitalDocument"),
            title="Defined In",
        ).generate_meta(),
    ] = Field(alias="definedIn")
    definition: Annotated[
        str | None,
        PropertyMeta(
            description="The definition text (or a summary of it).",
            title="Definition",
        ).generate_meta(),
    ] = None
    exact_match: Annotated[
        tuple[Iri, ...] | None,
        PropertyMeta(
            description=(
                "Terms in other agreements' lexicons whose definitions are "
                "interchangeable."
            ),
            range_="DefinedTerm",
            title="Exact Match",
        ).generate_meta(),
    ] = Field(default=None, alias="exactMatch")
    pref_label: Annotated[
        str,
        PropertyMeta(
            description=("The defined term itself, as it appears in the agreement."),
            title="Preferred Label",
        ).generate_meta(),
    ] = Field(alias="prefLabel")
    related: Annotated[
        tuple[Iri, ...] | None,
        PropertyMeta(
            description=("Associated terms that are neither broader nor narrower."),
            range_="DefinedTerm",
            title="Related",
        ).generate_meta(),
    ] = None
    recorded_in: Annotated[
        Iri | None,
        PropertyMeta(
            description="The definitions text this term was read from.",
            range_=TextObject,
            title="Recorded In",
        ).generate_meta(),
    ] = Field(default=None, alias="recordedIn")

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
