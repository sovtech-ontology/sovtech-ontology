from typing import TypedDict

NamedIndividual = TypedDict(
    "NamedIndividual",
    {
        "@id": str,
        "description": str,
        "name": str,
    },
)
