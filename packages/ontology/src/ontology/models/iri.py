from typing import Annotated

from pydantic import AnyUrl, BeforeValidator, Field

from ontology.models.utils import expand_iri

Iri = Annotated[
    AnyUrl,
    BeforeValidator(expand_iri),
    Field(
        title="IRI",
        description=(
            "An Internationalized Resource Identifier (IRI). May be a full IRI "
            "or a compact IRI (CURIE) resolved by the JSON-LD context."
        ),
    ),
]
