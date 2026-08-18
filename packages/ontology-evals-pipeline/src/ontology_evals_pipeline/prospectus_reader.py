"""Reads bond prospectus PDFs into structured form: pdfplumber extracts
plain text by default; marker (the optional extra) produces higher-fidelity
markdown when enabled."""

import importlib
from pathlib import Path

import pdfplumber

from ontology_evals_pipeline.prospectus import BondProspectus


def read_prospectus(path: Path, *, use_marker: bool = False) -> BondProspectus:
    with pdfplumber.open(path) as pdf:
        page_count = len(pdf.pages)
        text = (
            ""
            if use_marker
            else "\n".join(page.extract_text() or "" for page in pdf.pages)
        )
    if use_marker:
        text = _marker_text(path)
    return BondProspectus(
        identifier=path.stem, path=path, page_count=page_count, text=text
    )


def read_prospectuses(
    directory: Path, *, use_marker: bool = False
) -> list[BondProspectus]:
    return [
        read_prospectus(path, use_marker=use_marker)
        for path in sorted(directory.glob("*.pdf"))
    ]


def _marker_text(path: Path) -> str:
    # marker is an optional extra, so it is resolved at runtime only.
    try:
        converters = importlib.import_module("marker.converters.pdf")
        models = importlib.import_module("marker.models")
        output = importlib.import_module("marker.output")
    except ImportError as error:
        raise RuntimeError(
            "marker is not installed; install the extra: uv sync --extra marker"
        ) from error
    converter = converters.PdfConverter(artifact_dict=models.create_model_dict())
    text, _, _ = output.text_from_rendered(converter(str(path)))
    return str(text)
