"""Reads an RDF serialization into ontology models (the interchange format)
by inverting BaseResource.to_rdf with the same library: N-Quads -> JSON-LD ->
compaction against the shared context -> Resource validation."""

from pathlib import Path
from typing import Any, cast

from pyld import jsonld
from pyoxigraph import RdfFormat, parse, serialize

from ontology.models import Resource, ResourceAdapter, schemas_by_name


def read_resources(path: Path, context: dict[str, object]) -> list[Resource]:
    # serialize returns bytes when no output argument is given.
    nquads = serialize(parse(path=str(path)), format=RdfFormat.N_QUADS) or b""
    # pyld is untyped; compacting a node collection always yields a dict.
    compacted = cast(
        "dict[str, Any]",
        jsonld.compact(jsonld.from_rdf(nquads.decode("utf-8")), context),
    )
    compacted.pop("@context", None)
    nodes = compacted.get("@graph", [compacted] if compacted else [])
    return [
        ResourceAdapter.validate_python(node)
        for node in nodes
        if node.get("@type") in schemas_by_name
    ]


def read_ground_truth(directory: Path, context: dict[str, object]) -> list[Resource]:
    """The ground truth resources; an absent directory simply means none."""
    if not directory.is_dir():
        return []
    return [
        resource
        for path in sorted(directory.iterdir())
        if path.is_file() and RdfFormat.from_extension(path.suffix[1:]) is not None
        for resource in read_resources(path, context)
    ]
