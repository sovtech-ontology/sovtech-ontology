from typing import Annotated

from pydantic import Field

from ontology.models.base_resource import BaseResource
from ontology.models.property_meta import PropertyMeta
from ontology.models.thing import Thing
from ontology.models.timestamp import Timestamp


class RoleBase(BaseResource):
    description: Annotated[str | None, Thing.Fields.DESCRIPTION] = None
    end_date: Annotated[
        Timestamp | None,
        Thing.Fields.END_DATE,
        PropertyMeta(
            description="The date the role ended.", title="End Date"
        ).generate_meta(),
    ] = Field(default=None, alias="endDate")
    name: Annotated[str | None, Thing.Fields.NAME] = None
    start_date: Annotated[
        Timestamp | None,
        Thing.Fields.START_DATE,
        PropertyMeta(
            description="The date the role began.", title="Start Date"
        ).generate_meta(),
    ] = Field(default=None, alias="startDate")
