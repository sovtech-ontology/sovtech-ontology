"""Reads bond prospectus PDFs into structured form: pdfplumber extracts
plain text by default; marker (the optional extra) produces higher-fidelity
markdown when enabled."""

import importlib
from functools import lru_cache
from pathlib import Path
from typing import Protocol

import pdfplumber

from ontology_evals_pipeline.prospectus import BondProspectus


def read_prospectus(path: Path, *, use_marker: bool = False) -> BondProspectus:
    text = _marker_text(path) if use_marker else _pdfplumber_text(path)
    return BondProspectus(identifier=path.stem, path=path, text=text)


def read_prospectuses(
    directory: Path, *, use_marker: bool = False
) -> list[BondProspectus]:
    return [
        read_prospectus(path, use_marker=use_marker)
        for path in sorted(directory.glob("*.pdf"))
    ]


def _pdfplumber_text(path: Path) -> str:
    with pdfplumber.open(path) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)


class _Converter(Protocol):
    def __call__(self, path: str) -> object: ...


@lru_cache(maxsize=1)
def _marker_converter() -> _Converter:
    """Marker's model weights load once and are reused across PDFs. The
    import is resolved at runtime because marker is an optional extra."""
    try:
        converters = importlib.import_module("marker.converters.pdf")
        models = importlib.import_module("marker.models")
    except ImportError as error:
        raise RuntimeError(
            "marker is not installed; install the extra: uv sync --extra marker"
        ) from error
    converter: _Converter = converters.PdfConverter(
        artifact_dict=models.create_model_dict()
    )
    return converter


def _marker_text(path: Path) -> str:
    output = importlib.import_module("marker.output")
    text, _, _ = output.text_from_rendered(_marker_converter()(str(path)))
    return str(text)
