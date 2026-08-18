"""Loads ontology resources into an RDF store and serializes the graph."""

from pathlib import Path

from pyoxigraph import DefaultGraph, RdfFormat, Store

from ontology.models import Resource

_FORMATS = {
    "turtle": RdfFormat.TURTLE,
    "ntriples": RdfFormat.N_TRIPLES,
    "nquads": RdfFormat.N_QUADS,
    "rdfxml": RdfFormat.RDF_XML,
    "trig": RdfFormat.TRIG,
}


def store_resources(
    resources: list[Resource],
    context: dict[str, object],
    output_dir: Path,
    *,
    rdf_format: str = "turtle",
) -> Path:
    rdf = _FORMATS[rdf_format]
    store = Store()
    for resource in resources:
        store.load(resource.to_rdf(context).encode("utf-8"), format=RdfFormat.N_QUADS)
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / f"resources.{rdf.file_extension}"
    if rdf.supports_datasets:
        store.dump(str(destination), format=rdf)
    else:
        store.dump(str(destination), format=rdf, from_graph=DefaultGraph())
    return destination
