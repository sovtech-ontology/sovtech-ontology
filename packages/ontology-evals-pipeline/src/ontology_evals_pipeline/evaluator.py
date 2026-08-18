"""Compares extracted resources to ground truth by LSH similarity: ground
truth signatures go into a MinHashLSH index, each extracted resource is
matched greedily to its most similar unclaimed candidate."""

from datasketch import MinHashLSH
from pydantic import BaseModel

from ontology_evals_pipeline.hashing import HashedResource


class EvaluationReport(BaseModel):
    extracted_count: int
    ground_truth_count: int
    matches: tuple[tuple[str, str], ...]
    unmatched_extracted: tuple[str, ...]
    unmatched_ground_truth: tuple[str, ...]
    passed: bool | None


def evaluate(
    extracted: list[HashedResource],
    ground_truth: list[HashedResource],
    *,
    threshold: float,
    num_perm: int,
) -> EvaluationReport:
    lsh = MinHashLSH(threshold=threshold, num_perm=num_perm)
    for index, hashed in enumerate(ground_truth):
        lsh.insert(index, hashed["hash"])

    unclaimed = dict(enumerate(ground_truth))
    matches: list[tuple[str, str]] = []
    unmatched_extracted: list[str] = []
    for hashed in extracted:
        candidates = [
            key
            for key in lsh.query(hashed["hash"])
            if isinstance(key, int) and key in unclaimed
        ]
        if candidates:
            best = max(
                candidates,
                key=lambda index: hashed["hash"].jaccard(unclaimed[index]["hash"]),
            )
            matches.append((_label(hashed), _label(unclaimed.pop(best))))
        else:
            unmatched_extracted.append(_label(hashed))

    return EvaluationReport(
        extracted_count=len(extracted),
        ground_truth_count=len(ground_truth),
        matches=tuple(matches),
        unmatched_extracted=tuple(unmatched_extracted),
        unmatched_ground_truth=tuple(_label(hashed) for hashed in unclaimed.values()),
        passed=len(matches) == len(ground_truth) if ground_truth else None,
    )


def _label(hashed: HashedResource) -> str:
    model = hashed["model"]
    return f"{model.type_} {model.id}"
