from typing import Annotated, Literal, override

from pydantic import ConfigDict, Field

from ontology.models.creative_work import CreativeWork
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="MediaObject",
        description=(
            "A stored file that encodes a creative work — typically the PDF "
            "behind a digital document."
        ),
        named_individuals=named_individuals,
    )


class MediaObject(CreativeWork):
    """A stored file that encodes a creative work — typically the PDF behind
    a digital document."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["MediaObject"] = Field(alias="@type")
    content_size: Annotated[
        int | None,
        PropertyMeta(
            description="The file size in bytes.",
            title="Content Size",
        ).generate_meta(),
    ] = Field(default=None, alias="contentSize")
    content_url: Annotated[
        str | None,
        PropertyMeta(
            description="The location of the stored file.",
            title="Content URL",
        ).generate_meta(),
    ] = Field(default=None, alias="contentUrl")
    encoding_format: Annotated[
        str | None,
        PropertyMeta(
            description='The MIME type ("application/pdf").',
            title="Encoding Format",
        ).generate_meta(),
    ] = Field(default=None, alias="encodingFormat")
    sha256: Annotated[
        str | None,
        PropertyMeta(
            description=("The content hash, for integrity and deduplication."),
            title="SHA-256",
        ).generate_meta(),
    ] = None

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
