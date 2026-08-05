from typing import Annotated

from pydantic import Field

from ontology.models.base_resource import BaseResource
from ontology.models.iri import Iri
from ontology.models.property_meta import PropertyMeta
from ontology.models.thing import Thing
from ontology.models.timestamp import Timestamp


class CreativeWork(BaseResource):
    """The shared shape that documents and media extend: a work of
    authorship with subjects, authors, and publication metadata. Like
    RoleBase it has no "@type" of its own and no ObjectMeta; it stays
    abstract, so only concrete subclasses can be instantiated."""

    about: Annotated[
        tuple[Iri, ...] | None,
        Thing.Fields.ABOUT,
        PropertyMeta(
            description="The subjects this work is about.",
            range_=("DebtInstrument", "Agreement", "Organization"),
            title="About",
        ).generate_meta(),
    ] = None
    author: Annotated[
        tuple[Iri, ...] | None,
        PropertyMeta(
            description="The author(s) of the work.",
            range_=("Organization", "Person"),
            title="Author",
        ).generate_meta(),
    ] = None
    date_published: Annotated[
        Timestamp | None,
        PropertyMeta(
            description="The publication or filing date.",
            title="Date Published",
        ).generate_meta(),
    ] = Field(default=None, alias="datePublished")
    description: Annotated[str | None, Thing.Fields.DESCRIPTION] = None
    in_language: Annotated[
        str | None,
        PropertyMeta(
            description="The BCP 47 language tag of the content.",
            title="Language",
        ).generate_meta(),
    ] = Field(default=None, alias="inLanguage")
    name: Annotated[str | None, Thing.Fields.NAME] = None
    publisher: Annotated[
        Iri | None,
        PropertyMeta(
            description="The publishing or filing entity.",
            range_="Organization",
            title="Publisher",
        ).generate_meta(),
    ] = None
