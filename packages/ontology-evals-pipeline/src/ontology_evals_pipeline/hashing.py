"""Locality-sensitive hashing of ontology resources.

A resource is reduced to its set of data tokens (field/value pairs), then
MinHash-signed, so nearly identical nodes hash alike even when their minted
IRIs differ. Minted IRIs are excluded from the tokens for exactly that
reason; CBox IRIs are stable vocabulary, so they count as data."""

from typing import TypedDict

from datasketch import MinHash

from ontology.models import Resource
from ontology.models.namespaces import SVTO_CBOX


class HashedResource(TypedDict):
    model: Resource
    hash: MinHash


def resource_tokens(resource: Resource) -> frozenset[str]:
    """The data tokens of a resource: every field/value pair except its own
    @id and references to other minted resources."""
    data = resource.model_dump(mode="json", by_alias=True, exclude_none=True)
    tokens: set[str] = set()
    for field, value in data.items():
        if field == "@id":
            continue
        values = value if isinstance(value, list) else [value]
        for item in values:
            if _is_minted_iri(item):
                continue
            tokens.add(f"{field}={item}")
    return frozenset(tokens)


def hash_resource(resource: Resource, *, num_perm: int) -> HashedResource:
    minhash = MinHash(num_perm=num_perm)
    for token in sorted(resource_tokens(resource)):
        minhash.update(token.encode("utf-8"))
    return HashedResource(model=resource, hash=minhash)


def _is_minted_iri(value: object) -> bool:
    return (
        isinstance(value, str)
        and value.startswith(("http://", "https://"))
        and not value.startswith(SVTO_CBOX)
    )
