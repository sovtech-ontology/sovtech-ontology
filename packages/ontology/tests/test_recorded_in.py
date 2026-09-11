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


@pytest.mark.parametrize(
    ("model", "node"),
    [(ContractProvision, _PROVISION), (DefinedTerm, _TERM)],
    ids=["provision", "term"],
)
def test_resource_records_one_triple_per_text_anchor(
    model: type[ContractProvision | DefinedTerm], node: dict[str, str]
) -> None:
    resource = model.model_validate(
        {"@id": f"{_DOC}/{node['@type'].lower()}/x", "recordedIn": _ANCHORS, **node}
    )
    assert resource.recorded_in is not None
    assert [str(anchor) for anchor in resource.recorded_in] == _ANCHORS
    assert resource.to_rdf(default_context()).count(_RECORDED_IN) == len(_ANCHORS)


def test_event_records_a_single_text_anchor() -> None:
    event = Event.model_validate(
        {
            "@id": f"{_DOC}/event/default/2016-09-13",
            "@type": "Event",
            "eventType": "svto-cbox:DefaultEventType",
            "recordedIn": _ANCHORS[0],
        }
    )
    assert str(event.recorded_in) == _ANCHORS[0]
    assert event.to_rdf(default_context()).count(_RECORDED_IN) == 1
