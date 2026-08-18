"""Pydantic AI extraction harness: prospectus text in, ontology resources
out, with the ontology's Resource union as the structured output type."""

from pydantic_ai import Agent

from ontology.models import Resource
from ontology_evals_pipeline.prospectus import BondProspectus

_INSTRUCTIONS = (
    "You extract sovereign debt ontology instances from bond prospectus "
    "text. Return every organization, debt instrument, agreement, contract "
    "provision, defined term, event, role, and value object the text "
    'supports. Mint "@id" IRIs under "https://purl.org/svto/data/" using '
    'short kebab-case slugs. Use compact "svto-cbox:" CURIEs for enumerated '
    "values (document classes, provision types, role names, countries). "
    "Only assert what the text states."
)


def extract_resources(
    prospectus: BondProspectus, *, model: str, max_chars: int
) -> list[Resource]:
    agent: Agent[None, list[Resource]] = Agent(
        model, output_type=list[Resource], instructions=_INSTRUCTIONS
    )
    return agent.run_sync(prospectus.text[:max_chars]).output
