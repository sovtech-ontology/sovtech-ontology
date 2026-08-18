from ontology_evals_pipeline.config import INPUT_DATA_DIRECTORY_PATH
from ontology_evals_pipeline.prospectus_reader import (
    read_prospectus,
    read_prospectuses,
)

_PROSPECTUSES = INPUT_DATA_DIRECTORY_PATH / "prospectuses"


def test_read_prospectus_extracts_text() -> None:
    prospectus = read_prospectus(_PROSPECTUSES / "JAM1.pdf")
    assert prospectus.identifier == "JAM1"
    assert len(prospectus.text) > 1000


def test_read_prospectuses_is_sorted() -> None:
    identifiers = [p.identifier for p in read_prospectuses(_PROSPECTUSES)]
    assert identifiers == sorted(identifiers)
    assert "JAM1" in identifiers
