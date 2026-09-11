from ontology.models import DigitalDocument, OrganizationRole, PersonRole, default_context


def test_digital_document_identifier_round_trips() -> None:
    doc = DigitalDocument.model_validate(
        {
            "@id": "https://purl.org/svto/data/v1/document/pdip__AGO1",
            "@type": "DigitalDocument",
            "identifier": ["nsm__5502302", "ago1"],
        }
    )
    assert doc.identifier == ("nsm__5502302", "ago1")
    assert '<https://schema.org/identifier> "ago1"' in doc.to_rdf(default_context())


def test_roles_accept_member() -> None:
    role = OrganizationRole.model_validate(
        {
            "@id": "urn:tmp:role-1",
            "@type": "OrganizationRole",
            "member": "urn:tmp:org-1",
            "roleName": "svto-cbox:IssuerOrganizationRoleName",
        }
    )
    assert str(role.member) == "urn:tmp:org-1"
    person_role = PersonRole.model_validate(
        {"@id": "urn:tmp:prole-1", "@type": "PersonRole", "member": "urn:tmp:p-1"}
    )
    assert "<https://schema.org/member> <urn:tmp:p-1>" in person_role.to_rdf(
        default_context()
    )
