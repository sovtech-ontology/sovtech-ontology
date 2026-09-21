from collections.abc import Sequence
from typing import TYPE_CHECKING

from pydantic import Field
from pydantic.fields import FieldInfo

if TYPE_CHECKING:
    from pydantic.config import JsonDict

from ontology.models.base_resource import BaseResource
from ontology.models.resource_type import ResourceType

RangeTarget = type[BaseResource] | ResourceType


def _resolve_range(range_: RangeTarget) -> ResourceType:
    if isinstance(range_, str):
        return range_
    meta = range_.object_meta()
    if meta is None:
        raise ValueError("PropertyMeta range target must have a @type in its meta")
    return meta.type_


class PropertyMeta:
    # range_ follows the same trailing-underscore convention as
    # ObjectMeta.type_.
    description: str
    range_: ResourceType | tuple[ResourceType, ...] | None
    title: str

    def __init__(
        self,
        *,
        description: str,
        range_: RangeTarget | Sequence[RangeTarget] | None = None,
        title: str,
    ) -> None:
        self.description = description
        self.title = title

        self.range_ = None
        if isinstance(range_, Sequence) and not isinstance(range_, str):
            resolved: list[ResourceType] = [_resolve_range(r) for r in range_]
            self.range_ = tuple(resolved)
        elif range_ is not None:
            self.range_ = _resolve_range(range_)

    def generate_meta(self) -> FieldInfo:
        """The Annotated metadata for a property: a Field carrying this
        PropertyMeta's contributions, with the instance riding along in the
        Field's metadata for retrieval."""
        extra: JsonDict = {}
        if isinstance(self.range_, tuple):
            extra["range"] = list(self.range_)
        elif self.range_ is not None:
            extra["range"] = self.range_
        field_info: FieldInfo = Field(
            title=self.title,
            description=self.description,
            json_schema_extra=extra or None,
        )
        field_info.metadata.append(self)
        return field_info
