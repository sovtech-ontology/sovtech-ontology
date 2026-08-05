from typing import Annotated, Literal, override

from pydantic import AnyUrl, ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.event_type import EventType
from ontology.models.iri import Iri
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta
from ontology.models.text_object import TextObject
from ontology.models.thing import Thing
from ontology.models.timestamp import Timestamp


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="Event",
        description=(
            "A dated or triggered occurrence in the life of an instrument or "
            "agreement: issuance, settlement, an actual default, an "
            "acceleration. Contract language describing default triggers is "
            "a ContractProvision; the thing that happens is an Event."
        ),
        named_individuals=named_individuals,
    )


class Event(BaseResource):
    """A dated or triggered occurrence in the life of an instrument or
    agreement: issuance, settlement, an actual default, an acceleration.
    Contract language describing default triggers is a ContractProvision;
    the thing that happens is an Event."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["Event"] = Field(alias="@type")
    about: Annotated[
        tuple[Iri, ...] | None,
        Thing.Fields.ABOUT,
        PropertyMeta(
            description=("The instrument(s) or agreement(s) this event concerns."),
            range_=("DebtInstrument", "Agreement"),
            title="About",
        ).generate_meta(),
    ] = None
    description: Annotated[str | None, Thing.Fields.DESCRIPTION] = None
    end_date: Annotated[
        Timestamp | None,
        Thing.Fields.END_DATE,
        PropertyMeta(
            description=(
                "When the event ended, for events with duration (a grace period)."
            ),
            title="End Date",
        ).generate_meta(),
    ] = Field(default=None, alias="endDate")
    event_type: Annotated[
        AnyUrl,
        named_individual_iri_enum("EventType"),
        PropertyMeta(
            description="The kind of occurrence.",
            range_=EventType,
            title="Event Type",
        ).generate_meta(),
    ] = Field(alias="eventType")
    location: Annotated[
        Iri | None,
        Thing.Fields.LOCATION,
        PropertyMeta(
            description="Where the event occurred, when meaningful.",
            range_="Place",
            title="Location",
        ).generate_meta(),
    ] = None
    name: Annotated[str | None, Thing.Fields.NAME] = None
    source_text: Annotated[
        Iri | None,
        PropertyMeta(
            description="The text this event was reconstructed from.",
            range_=TextObject,
            title="Source Text",
        ).generate_meta(),
    ] = Field(default=None, alias="sourceText")
    start_date: Annotated[
        Timestamp | None,
        Thing.Fields.START_DATE,
        PropertyMeta(
            description="When the event occurred or began.",
            title="Start Date",
        ).generate_meta(),
    ] = Field(default=None, alias="startDate")
    under_provision: Annotated[
        Iri | None,
        PropertyMeta(
            description=(
                "The provision this event arises under (a default under the "
                "events-of-default clause)."
            ),
            range_="ContractProvision",
            title="Under Provision",
        ).generate_meta(),
    ] = Field(default=None, alias="underProvision")

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
