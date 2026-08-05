import re

from ontology.models.namespaces import SCHEMA, SKOS, SVTO, SVTO_CBOX

PREFIXES: dict[str, str] = {
    "schema": SCHEMA,
    "skos": SKOS,
    "svto": SVTO,
    "svto-cbox": SVTO_CBOX,
}


def expand_curie(value: str) -> str | None:
    # Already an absolute IRI (http:, https:, urn:, etc.)? Pass through.
    if re.compile(r"^[a-z][a-z0-9+.-]*://", re.IGNORECASE).match(
        value
    ) or value.startswith("urn:"):
        return value

    match = re.compile(r"^([A-Za-z_][\w.-]*):(.+)$").match(value)

    if not match:
        return None
    prefix, reference = match.group(1), match.group(2)
    base = PREFIXES.get(prefix)
    return base + reference if base else None
