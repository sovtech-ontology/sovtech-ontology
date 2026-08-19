"""Deterministic IRI minting for extracted ontology instances.

Value nodes get a urn:uuid derived from their data, so identical values
merge. Everything else gets
{SVTO_DATA}{exchange}/{document-class}/{tbox-name}/[YYYY/MM/DD/]
[{cbox-name}/]{name}, where the date is the resource's primary date (or the
document's), cbox-name is the resource's primary classification, and a
missing name is guessed from both and written back onto the instance."""

import uuid
from datetime import date, datetime

from pydantic import AnyUrl

from ontology.models import SVTO_DATA, Resource, capital_case, named_individuals
from ontology_evals_pipeline.hashing import resource_tokens

_VALUE_TYPES = frozenset({"MonetaryAmount", "QuantitativeValue"})
_DATE_FIELDS = {
    "Agreement": "execution_date",
    "CreditRating": "date_published",
    "DebtInstrument": "issue_date",
    "DigitalDocument": "date_published",
    "Event": "start_date",
}
_FACET_FIELDS = {
    "Agreement": ("agreement_type",),
    "ContractProvision": ("provision_type",),
    "DebtInstrument": ("debt_instrument_type",),
    "DigitalDocument": ("document_class",),
    "Event": ("event_type",),
    "Organization": ("debtor_type", "creditor_type"),
    "OrganizationRole": ("role_name",),
    "PersonRole": ("role_name",),
    "TextObject": ("section_type",),
}


def mint(
    resource: Resource,
    *,
    exchange: str,
    document_class: str,
    document_date: date | None = None,
) -> Resource:
    """The resource with a deterministic @id (and a guessed name, if it had
    none)."""
    if resource.type_ in _VALUE_TYPES:
        return resource.model_copy(update={"id": AnyUrl(_value_urn(resource))})

    facet = _facet_key(resource)
    name = _name(resource, facet)
    segments = [
        _slug(exchange),
        _slug(document_class),
        _kebab(resource.type_),
        *_date_segments(resource, document_date),
        *([_kebab(facet)] if facet else []),
        _slug(name),
    ]
    update: dict[str, object] = {"id": AnyUrl(SVTO_DATA + "/".join(segments))}
    if (
        getattr(resource, "name", None) is None
        and "name" in type(resource).model_fields
    ):
        update["name"] = name
    return resource.model_copy(update=update)


def _value_urn(resource: Resource) -> str:
    payload = "|".join(sorted(resource_tokens(resource)))
    return f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, payload)}"


def _name(resource: Resource, facet: str | None) -> str:
    explicit = getattr(resource, "name", None) or getattr(resource, "pref_label", None)
    if explicit:
        return str(explicit)
    guess = capital_case(resource.type_)
    return f"{capital_case(facet)} {guess}" if facet else guess


def _facet_key(resource: Resource) -> str | None:
    """The registry key of the resource's primary CBox classification
    ("NegativePledge" from ...#NegativePledgeProvisionType)."""
    for field in _FACET_FIELDS.get(resource.type_, ()):
        value = getattr(resource, field, None)
        if value is None:
            continue
        local = str(value).rsplit("#", 1)[-1]
        for class_name, entries in named_individuals.items():
            key = local.removesuffix(class_name)
            if key != local and key in entries:
                return key
    return None


def _date_segments(resource: Resource, document_date: date | None) -> list[str]:
    field = _DATE_FIELDS.get(resource.type_)
    if field is None:
        return []
    value = getattr(resource, field, None) or document_date
    if isinstance(value, datetime):
        value = value.date()
    if not isinstance(value, date):
        return []
    return [f"{value.year:04d}", f"{value.month:02d}", f"{value.day:02d}"]


def _slug(name: str) -> str:
    return name.strip().lower().replace(" ", "-")


def _kebab(camel: str) -> str:
    return capital_case(camel).lower().replace(" ", "-")
