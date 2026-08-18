from ontology.models import Resource
from ontology_evals_pipeline.evaluator import evaluate
from ontology_evals_pipeline.hashing import HashedResource, hash_resource


def _hashed(resources: list[Resource]) -> list[HashedResource]:
    return [hash_resource(resource, num_perm=128) for resource in resources]


def test_identical_sets_fully_match(sample_resources: list[Resource]) -> None:
    report = evaluate(
        _hashed(sample_resources),
        _hashed(sample_resources),
        threshold=0.8,
        num_perm=128,
    )
    assert report.passed is True
    assert len(report.matches) == 3
    assert not report.unmatched_extracted
    assert not report.unmatched_ground_truth


def test_labels_use_the_ontology_type(sample_resources: list[Resource]) -> None:
    report = evaluate(
        _hashed(sample_resources[:1]),
        _hashed(sample_resources[:1]),
        threshold=0.8,
        num_perm=128,
    )
    assert report.matches[0][0].startswith("Organization ")


def test_no_ground_truth_means_no_verdict(
    sample_resources: list[Resource],
) -> None:
    report = evaluate(_hashed(sample_resources), [], threshold=0.8, num_perm=128)
    assert report.passed is None
    assert len(report.unmatched_extracted) == 3


def test_disjoint_sets_do_not_match(sample_resources: list[Resource]) -> None:
    report = evaluate(
        _hashed(sample_resources[:1]),
        _hashed(sample_resources[1:]),
        threshold=0.8,
        num_perm=128,
    )
    assert report.passed is False
    assert not report.matches
    assert len(report.unmatched_extracted) == 1
    assert len(report.unmatched_ground_truth) == 2
