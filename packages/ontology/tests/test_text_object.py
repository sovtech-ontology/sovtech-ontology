from ontology.models import DigitalDocument, TextObject


def test_text_object_about_may_target_a_contract_provision() -> None:
    about = TextObject.model_json_schema()["properties"]["about"]
    assert "ContractProvision" in about["range"]


def test_document_about_range_is_unchanged() -> None:
    about = DigitalDocument.model_json_schema()["properties"]["about"]
    assert about["range"] == ["DebtInstrument", "Agreement", "Organization"]
