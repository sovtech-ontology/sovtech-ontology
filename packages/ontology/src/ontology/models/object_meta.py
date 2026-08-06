import re

from pydantic.config import JsonDict

from ontology.models.named_individual import NamedIndividual
from ontology.models.namespaces import SVTO_CBOX
from ontology.models.resource_type import ResourceType


def capital_case(value: str) -> str:
    """Space-separate a PascalCase identifier ("PersonRoleCategory" ->
    "Person Role Category")."""
    return " ".join(
        word.capitalize()
        for word in re.findall(r"[A-Z]+(?![a-z])|[A-Z][a-z0-9]*|[a-z0-9]+", value)
    )


class ObjectMeta:
    type_: ResourceType
    description: str
    title: str
    named_individuals: list[NamedIndividual] | None

    def __init__(
        self,
        *,
        type_: ResourceType,
        description: str,
        title: str | None = None,
        named_individuals: dict[str, dict[str, dict[str, str]]],
    ) -> None:
        self.type_ = type_
        self.description = description
        self.title = title if title is not None else capital_case(type_)

        self.named_individuals = None
        if type_ in named_individuals:
            self.named_individuals = [
                {
                    "@id": f"{SVTO_CBOX}{id_}{type_}",
                    "description": entry["description"],
                    "name": entry.get("name", capital_case(id_)),
                }
                for id_, entry in named_individuals[type_].items()
            ]

    def json_schema_extra(self) -> JsonDict:
        extra: JsonDict = {
            "@type": self.type_,
            "description": self.description,
            "title": self.title,
        }
        if self.named_individuals is not None:
            extra["namedIndividuals"] = [
                {
                    "@id": ni["@id"],
                    "description": ni["description"],
                    "name": ni["name"],
                }
                for ni in self.named_individuals
            ]
        return extra
