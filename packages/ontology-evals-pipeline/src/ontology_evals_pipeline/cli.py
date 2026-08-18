"""Typer CLI: the only module that reads Config. Stages hand off through
files in the output directory so each can run alone; run composes them
without re-reading what it already holds."""

from pathlib import Path

import logfire
import typer

from ontology.models import Resource, ResourceListAdapter, default_context
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

_EXTRACTED_FILENAME = "extracted.json"
_REPORT_FILENAME = "report.json"


@app.command()
def extract() -> None:
    """Read prospectuses and extract ontology resources with the LLM."""
    _extract(Config())


@app.command()
def evaluate() -> None:
    """Compare extracted resources to RDF ground truth and write a report."""
    config = Config()
    _evaluate(config, _read_extracted(config.output_dir))


@app.command()
def store() -> None:
    """Load extracted resources into an RDF store and serialize the graph."""
    config = Config()
    _store(config, _read_extracted(config.output_dir))


@app.command()
def run() -> None:
    """Extract, evaluate, and store, end to end."""
    config = Config()
    resources = _extract(config)
    _evaluate(config, resources)
    _store(config, resources)


def _extract(config: Config) -> list[Resource]:
    logfire.configure(send_to_logfire="if-token-present")
    logfire.instrument_pydantic_ai()
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
        ResourceListAdapter.dump_json(
            resources, by_alias=True, exclude_none=True, indent=2
        )
    )
    typer.echo(
        f"{len(resources)} resources from {len(prospectuses)} prospectuses"
        f" -> {destination}"
    )
    return resources


def _evaluate(config: Config, resources: list[Resource]) -> None:
    context = default_context()
    extracted = [
        hashing.hash_resource(resource, num_perm=config.lsh_num_perm)
        for resource in resources
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
    payload = report.model_dump_json(indent=2)
    destination = config.output_dir / _REPORT_FILENAME
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(payload, encoding="utf-8")
    typer.echo(payload)
    typer.echo(f"report -> {destination}")


def _store(config: Config, resources: list[Resource]) -> None:
    destination = rdf_store.store_resources(
        resources, default_context(), config.output_dir, rdf_format=config.rdf_format
    )
    typer.echo(f"{len(resources)} resources -> {destination}")


def _read_extracted(output_dir: Path) -> list[Resource]:
    path = output_dir / _EXTRACTED_FILENAME
    if not path.is_file():
        raise typer.BadParameter(f"no extracted resources at {path}; run extract first")
    return ResourceListAdapter.validate_json(path.read_text(encoding="utf-8"))
