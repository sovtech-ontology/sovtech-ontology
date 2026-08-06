from typing import Annotated, Literal, override

from pydantic import AnyUrl, ConfigDict, Field

from ontology.models.cbox.document_class import DocumentClass
from ontology.models.creative_work import CreativeWork
from ontology.models.iri import Iri
from ontology.models.media_object import MediaObject
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta
from ontology.models.text_object import TextObject
from ontology.models.thing import Thing


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="DigitalDocument",
        description=(
            "A document in the sovereign prospectus corpus: a prospectus, "
            "base prospectus, supplement, final terms, indenture, notice, or "
            "loan agreement."
        ),
        named_individuals=named_individuals,
    )


class DigitalDocument(CreativeWork):
    """A document in the sovereign prospectus corpus: a prospectus, base
    prospectus, supplement, final terms, indenture, notice, or loan
    agreement."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["DigitalDocument"] = Field(alias="@type")
    amends: Annotated[
        tuple[Iri, ...] | None,
        PropertyMeta(
            description=(
                "The document(s) this document supplements or amends (a "
                "supplement amends a prospectus)."
            ),
            range_="DigitalDocument",
            title="Amends",
        ).generate_meta(),
    ] = None
    associated_media: Annotated[
        tuple[Iri, ...] | None,
        PropertyMeta(
            description="The stored file(s) encoding this document (the PDF).",
            range_=MediaObject,
            title="Associated Media",
        ).generate_meta(),
    ] = Field(default=None, alias="associatedMedia")
    completes: Annotated[
        Iri | None,
        PropertyMeta(
            description=(
                "The base prospectus this document completes for one tranche "
                "(final terms complete a base prospectus)."
            ),
            range_="DigitalDocument",
            title="Completes",
        ).generate_meta(),
    ] = None
    document_class: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("DocumentClass"),
        PropertyMeta(
            description=(
                "The corpus document class. Optional by design: unclassified "
                "documents sit in the review queue, never forced."
            ),
            range_=DocumentClass,
            title="Document Class",
        ).generate_meta(),
    ] = Field(default=None, alias="documentClass")
    has_part: Annotated[
        tuple[Iri, ...] | None,
        Thing.Fields.HAS_PART,
        PropertyMeta(
            description="The text parts extracted from this document.",
            range_=TextObject,
            title="Has Part",
        ).generate_meta(),
    ] = Field(default=None, alias="hasPart")
    identifier: Annotated[
        str | None,
        Thing.Fields.IDENTIFIER,
        PropertyMeta(
            description="The corpus storage key.",
            title="Identifier",
        ).generate_meta(),
    ] = None
    incorporates_by_reference: Annotated[
        tuple[Iri, ...] | None,
        PropertyMeta(
            description="The documents incorporated by reference.",
            range_="DigitalDocument",
            title="Incorporates By Reference",
        ).generate_meta(),
    ] = Field(default=None, alias="incorporatesByReference")
    source: Annotated[
        str | None,
        PropertyMeta(
            description="The corpus source system.",
            title="Source",
        ).generate_meta(),
    ] = None
    url: Annotated[
        str | None,
        PropertyMeta(
            description="The canonical source URL, where one exists.",
            title="URL",
        ).generate_meta(),
    ] = None

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
