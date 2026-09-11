import pytest

from ontology.models import ContractProvision, DefinedTerm, Event, default_context

_DOC = "https://purl.org/svto/data/document/pdip__CMR7"
_ANCHORS = [f"{_DOC}/quote/1", f"{_DOC}/tag/NegativePledge_Covenants"]
_RECORDED_IN = "<https://schema.org/recordedIn>"

_PROVISION = {
    "@type": "ContractProvision",
    "provisionType": "svto-cbox:NegativePledgeProvisionType",
}
_TERM = {
    "@type": "DefinedTerm",
    "prefLabel": "External Indebtedness",
    "definedIn": _DOC,
}
_EVENT = {"@type": "Event", "eventType": "svto-cbox:DefaultEventType"}


@pytest.mark.parametrize(
    ("model", "node"),
    [(ContractProvision, _PROVISION), (DefinedTerm, _TERM), (Event, _EVENT)],
    ids=["provision", "term", "event"],
)
def test_resource_records_one_triple_per_text_anchor(
    model: type[ContractProvision | DefinedTerm | Event], node: dict[str, str]
) -> None:
    resource = model.model_validate(
        {"@id": f"{_DOC}/{node['@type'].lower()}/x", "recordedIn": _ANCHORS, **node}
    )
    assert resource.recorded_in is not None
    assert [str(anchor) for anchor in resource.recorded_in] == _ANCHORS
    assert resource.to_rdf(default_context()).count(_RECORDED_IN) == len(_ANCHORS)
