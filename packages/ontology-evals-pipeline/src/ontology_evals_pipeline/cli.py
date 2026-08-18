"""Typer CLI: the only module that reads Config. Stages hand off through
files in the output directory so each can run alone."""

from pathlib import Path

import logfire
import typer
from pydantic import TypeAdapter

from ontology.models import Resource
from ontology_evals_pipeline import (
    evaluator,
    harness,
    hashing,
    prospectus_reader,
    rdf_reader,
    rdf_store,
)
from ontology_evals_pipeline.config import Config

app = typer.Typer(
    help="Evaluate LLM extraction of ontology instances from bond prospectuses."
)

_RESOURCES = TypeAdapter(list[Resource])
_EXTRACTED_FILENAME = "extracted.json"
_REPORT_FILENAME = "report.json"


@app.callback()
def main() -> None:
    """Telemetry: a no-op without LOGFIRE_TOKEN, full tracing with one."""
    logfire.configure(send_to_logfire="if-token-present")
    logfire.instrument_pydantic_ai()


@app.command()
def extract() -> None:
    """Read prospectuses and extract ontology resources with the LLM."""
    config = Config()
    prospectuses = prospectus_reader.read_prospectuses(
        config.prospectuses_dir, use_marker=config.use_marker
    )
    resources = [
        resource
        for prospectus in prospectuses
        for resource in harness.extract_resources(
            prospectus, model=config.llm_model, max_chars=config.max_prospectus_chars
        )
    ]
    config.output_dir.mkdir(parents=True, exist_ok=True)
    destination = config.output_dir / _EXTRACTED_FILENAME
    destination.write_bytes(
        _RESOURCES.dump_json(resources, by_alias=True, exclude_none=True, indent=2)
    )
    typer.echo(
        f"{len(resources)} resources from {len(prospectuses)} prospectuses"
        f" -> {destination}"
    )


@app.command()
def evaluate() -> None:
    """Compare extracted resources to RDF ground truth and write a report."""
    config = Config()
    context = rdf_reader.load_context(config.jsonld_context)
    extracted = [
        hashing.hash_resource(resource, num_perm=config.lsh_num_perm)
        for resource in _read_extracted(config.output_dir)
    ]
    ground_truth = [
        hashing.hash_resource(resource, num_perm=config.lsh_num_perm)
        for resource in rdf_reader.read_ground_truth(config.ground_truth_dir, context)
    ]
    report = evaluator.evaluate(
        extracted,
        ground_truth,
        threshold=config.lsh_threshold,
        num_perm=config.lsh_num_perm,
    )
    destination = config.output_dir / _REPORT_FILENAME
    destination.write_text(report.model_dump_json(indent=2), encoding="utf-8")
    typer.echo(report.model_dump_json(indent=2))
    typer.echo(f"report -> {destination}")


@app.command()
def store() -> None:
    """Load extracted resources into an RDF store and serialize the graph."""
    config = Config()
    context = rdf_reader.load_context(config.jsonld_context)
    resources = _read_extracted(config.output_dir)
    destination = rdf_store.store_resources(
        resources, context, config.output_dir, rdf_format=config.rdf_format
    )
    typer.echo(f"{len(resources)} resources -> {destination}")


@app.command()
def run() -> None:
    """Extract, evaluate, and store, end to end."""
    extract()
    evaluate()
    store()


def _read_extracted(output_dir: Path) -> list[Resource]:
    path = output_dir / _EXTRACTED_FILENAME
    if not path.is_file():
        raise typer.BadParameter(f"no extracted resources at {path}; run extract first")
    return _RESOURCES.validate_json(path.read_text(encoding="utf-8"))
