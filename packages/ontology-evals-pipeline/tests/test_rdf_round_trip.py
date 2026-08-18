from pathlib import Path

import pytest

from ontology.models import Resource
from ontology_evals_pipeline.hashing import hash_resource
from ontology_evals_pipeline.rdf_reader import read_ground_truth, read_resources
from ontology_evals_pipeline.rdf_store import store_resources


def test_store_then_read_round_trips(
    sample_resources: list[Resource], context: dict[str, object], tmp_path: Path
) -> None:
    destination = store_resources(sample_resources, context, tmp_path)
    assert destination.name == "resources.ttl"
    recovered = read_resources(destination, context)
    assert sorted(r.type_ for r in recovered) == sorted(
        r.type_ for r in sample_resources
    )
    original = {
        hash_resource(r, num_perm=128)["hash"].digest().tobytes()
        for r in sample_resources
    }
    returned = {
        hash_resource(r, num_perm=128)["hash"].digest().tobytes() for r in recovered
    }
    assert original == returned


def test_ground_truth_directory_may_be_absent(
    context: dict[str, object], tmp_path: Path
) -> None:
    assert read_ground_truth(tmp_path / "missing", context) == []


def test_ground_truth_reads_any_supported_extension(
    sample_resources: list[Resource], context: dict[str, object], tmp_path: Path
) -> None:
    store_resources(sample_resources, context, tmp_path, rdf_format="nq")
    assert len(read_ground_truth(tmp_path, context)) == 3


def test_unknown_format_extension_is_rejected(
    sample_resources: list[Resource], context: dict[str, object], tmp_path: Path
) -> None:
    with pytest.raises(ValueError, match="unknown RDF format"):
        store_resources(sample_resources, context, tmp_path, rdf_format="bogus")
