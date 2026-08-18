"""Loads ontology resources into an RDF store and serializes the graph."""

from pathlib import Path

from pyoxigraph import DefaultGraph, RdfFormat, Store

from ontology.models import Resource


def store_resources(
    resources: list[Resource],
    context: dict[str, object],
    output_dir: Path,
    *,
    rdf_format: str = "ttl",
) -> Path:
    """rdf_format is a file extension resolved by pyoxigraph ("ttl", "nq",
    "rdf", ...)."""
    rdf = RdfFormat.from_extension(rdf_format)
    if rdf is None:
        raise ValueError(f"unknown RDF format extension: {rdf_format!r}")
    store = Store()
    nquads = "".join(resource.to_rdf(context) for resource in resources)
    store.load(nquads.encode("utf-8"), format=RdfFormat.N_QUADS)
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / f"resources.{rdf.file_extension}"
    store.dump(
        str(destination),
        format=rdf,
        from_graph=None if rdf.supports_datasets else DefaultGraph(),
    )
    return destination
