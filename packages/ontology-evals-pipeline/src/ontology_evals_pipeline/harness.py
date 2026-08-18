"""Pydantic AI extraction harness: prospectus text in, ontology resources
out, with the ontology's Resource union as the structured output type."""

from functools import cache

from pydantic_ai import Agent

from ontology.models import SVTO_CBOX, SVTO_DATA, Resource
from ontology_evals_pipeline.prospectus import BondProspectus

_INSTRUCTIONS = (
    "You extract sovereign debt ontology instances from bond prospectus "
    "text. Return every organization, debt instrument, agreement, contract "
    "provision, defined term, event, role, and value object the text "
    f'supports. Mint "@id" IRIs under "{SVTO_DATA}" using short kebab-case '
    f'slugs. Use compact CURIEs in the "{SVTO_CBOX}" namespace for '
    "enumerated values (document classes, provision types, role names, "
    "countries). Only assert what the text states."
)


def extract_resources(
    prospectus: BondProspectus, *, model: str, max_chars: int
) -> list[Resource]:
    return _agent(model).run_sync(prospectus.text[:max_chars]).output


@cache
def _agent(model: str) -> Agent[None, list[Resource]]:
    """Built once per model string: agent construction derives the JSON
    schema for the whole Resource union and creates an HTTP client."""
    return Agent(model, output_type=list[Resource], instructions=_INSTRUCTIONS)
