"""Reusable field metadata. Each property maps to its schema.org counterpart
in the JSON-LD context (data/input/context.json), so the field descriptions
are copied from schema.org.
"""

from pydantic import Field


class Thing:  # Just a namespace
    class Fields:  # Just a namespace
        NAME = Field(min_length=1, title="Name", description="The name of the item.")
        DESCRIPTION = Field(
            min_length=1,
            title="Description",
            description="A description of the item.",
        )
        ABOUT = Field(
            description="The subject matter of the content.",
        )
        ADDITIONAL_TYPE = Field(
            description=(
                "An additional type for the item, typically used for adding "
                "more specific types from external vocabularies in microdata "
                "syntax."
            )
        )
        HAS_PART = Field(
            description=(
                "Indicates an item or CreativeWork that is part of this "
                "item, or CreativeWork (in some sense)."
            )
        )
        IDENTIFIER = Field(
            description=(
                "The identifier property represents any kind of identifier "
                "for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc."
            )
        )
        IS_PART_OF = Field(
            description=(
                "Indicates an item or CreativeWork that this item, or "
                "CreativeWork (in some sense), is part of."
            )
        )
        LOCATION = Field(
            description=(
                "The location of, for example, where an event is happening, "
                "where an organization is located, or where an action takes "
                "place."
            )
        )
        MEMBER_OF = Field(
            description=(
                "An Organization (or ProgramMembership) to which this Person "
                "or Organization belongs."
            )
        )
        ROLE_NAME = Field(
            description=(
                "A role played, performed or filled by a person or organization."
            )
        )
        START_DATE = Field(
            description="The start date and time of the item (in ISO 8601 date format)."
        )
        END_DATE = Field(
            description="The end date and time of the item (in ISO 8601 date format)."
        )
