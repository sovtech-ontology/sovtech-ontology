"""Reads an RDF serialization into ontology models (the interchange
format), reverse-mapping predicate IRIs to JSON-LD context terms."""

import json
from pathlib import Path

from pyoxigraph import Literal, NamedNode, RdfFormat, parse

from ontology.models import Resource, ResourceAdapter

_RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
_PREFIXES = ("schema", "skos", "svto", "svto-cbox")


def load_context(path: Path) -> dict[str, object]:
    context: dict[str, object] = json.loads(path.read_text(encoding="utf-8"))[
        "@context"
    ]
    return context


def reverse_maps(
    context: dict[str, object],
) -> tuple[dict[str, str], dict[str, str], frozenset[str]]:
    """(property IRI -> term, class IRI -> "@type" name, @set terms)."""
    prefixes = {key: str(context[key]) for key in _PREFIXES}

    def expand(curie: str) -> str:
        prefix, _, reference = curie.partition(":")
        return prefixes[prefix] + reference if prefix in prefixes else curie

    properties: dict[str, str] = {}
    classes: dict[str, str] = {}
    set_terms: set[str] = set()
    for term, value in context.items():
        if term in prefixes:
            continue
        if isinstance(value, str):
            (classes if term[0].isupper() else properties)[expand(value)] = term
        elif isinstance(value, dict):
            properties[expand(str(value["@id"]))] = term
            if value.get("@container") == "@set":
                set_terms.add(term)
    return properties, classes, frozenset(set_terms)


def read_resources(path: Path, context: dict[str, object]) -> list[Resource]:
    properties, classes, set_terms = reverse_maps(context)
    nodes: dict[str, dict[str, object]] = {}
    rdf_format = RdfFormat.from_extension(path.suffix.lstrip(".")) or RdfFormat.TURTLE
    for quad in parse(path=str(path), format=rdf_format):
        subject, obj = quad.subject.value, quad.object
        node = nodes.setdefault(subject, {"@id": subject})
        value = obj.value if isinstance(obj, NamedNode | Literal) else str(obj)
        if quad.predicate.value == _RDF_TYPE and value in classes:
            node["@type"] = classes[value]
            continue
        term = properties.get(quad.predicate.value)
        if term is None:
            continue
        if term in set_terms:
            existing = node.setdefault(term, [])
            if isinstance(existing, list):
                existing.append(value)
        else:
            node.setdefault(term, value)
    return [
        ResourceAdapter.validate_python(node)
        for node in nodes.values()
        if "@type" in node
    ]


def read_ground_truth(directory: Path, context: dict[str, object]) -> list[Resource]:
    """The ground truth resources; an absent directory simply means none."""
    if not directory.is_dir():
        return []
    return [
        resource
        for path in sorted(directory.glob("*.ttl"))
        for resource in read_resources(path, context)
    ]
