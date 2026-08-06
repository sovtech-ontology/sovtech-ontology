from typing import Annotated, Literal, override

from pydantic import AnyUrl, ConfigDict, Field

from ontology.models.cbox import DocumentSectionType
from ontology.models.creative_work import CreativeWork
from ontology.models.iri import Iri
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta
from ontology.models.thing import Thing


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="TextObject",
        description=(
            "A text part of a document: an extracted section, clause span, "
            "or page range. The provenance anchor for provisions, defined "
            "terms, and events."
        ),
        named_individuals=named_individuals,
    )


class TextObject(CreativeWork):
    """A text part of a document: an extracted section, clause span, or page
    range. The provenance anchor for provisions, defined terms, and
    events."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["TextObject"] = Field(alias="@type")
    is_part_of: Annotated[
        Iri,
        Thing.Fields.IS_PART_OF,
        PropertyMeta(
            description="The document this text part belongs to.",
            range_="DigitalDocument",
            title="Is Part Of",
        ).generate_meta(),
    ] = Field(alias="isPartOf")
    page_end: Annotated[
        int | None,
        PropertyMeta(
            description="The last page of the span in the source document.",
            title="Page End",
        ).generate_meta(),
    ] = Field(default=None, alias="pageEnd")
    page_start: Annotated[
        int | None,
        PropertyMeta(
            description="The first page of the span in the source document.",
            title="Page Start",
        ).generate_meta(),
    ] = Field(default=None, alias="pageStart")
    section_type: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("DocumentSectionType"),
        PropertyMeta(
            description=(
                "The disclosure section this text belongs to (risk factors, "
                "definitions)."
            ),
            range_=DocumentSectionType,
            title="Section Type",
        ).generate_meta(),
    ] = Field(default=None, alias="sectionType")
    text: Annotated[
        str | None,
        PropertyMeta(
            description="The extracted text content.",
            title="Text",
        ).generate_meta(),
    ] = None

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
