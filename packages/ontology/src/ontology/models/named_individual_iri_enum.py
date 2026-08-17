from ontology.models.iri_enum import IriEnum
from ontology.models.named_individuals import named_individuals
from ontology.models.namespaces import SVTO_CBOX


def named_individual_iri_enum(type_: str) -> IriEnum:
    """The "@id" constraint for a type's named individuals, for use in a
    metadata slot: Annotated[Iri, named_individual_iri_enum("X")]."""
    return IriEnum(
        tuple(f"{SVTO_CBOX}{key}{type_}" for key in named_individuals[type_])
    )
