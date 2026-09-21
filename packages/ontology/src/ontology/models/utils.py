"""Shared helpers for the pydantic models."""

from ontology.models.expand_curie import expand_curie


def expand_iri(value: object) -> object:
    """Expand a compact IRI (CURIE) ahead of AnyUrl validation. Raising on
    failure is what surfaces expand_curie's None as a ValidationError."""
    if not isinstance(value, str):
        return value  # let AnyUrl validation report the type error
    expanded = expand_curie(value)
    if expanded is None:
        raise ValueError(f'cannot expand "{value}": unknown prefix or malformed IRI')
    return expanded
