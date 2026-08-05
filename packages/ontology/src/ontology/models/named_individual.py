"""The shape of one CBox named individual, as carried in a model's
json_schema_extra.

Functional TypedDict syntax is required because "@id" is not a valid Python
identifier.
"""

from typing import TypedDict

NamedIndividual = TypedDict(
    "NamedIndividual",
    {
        "@id": str,
        "description": str,
        "name": str,
    },
)
