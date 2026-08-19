from datetime import date

from ontology.models import ContractProvision, Resource, ResourceAdapter
from ontology_evals_pipeline.iri_minter import mint


def _resource(node: dict[str, object]) -> Resource:
    return ResourceAdapter.validate_python(node)


def test_value_nodes_get_deterministic_urns() -> None:
    node = {
        "@id": "https://x.org/a",
        "@type": "MonetaryAmount",
        "currency": "EUR",
        "value": 11232223.82,
    }
    first = mint(_resource(node), exchange="PDIP", document_class="loan documentation")
    second = mint(
        _resource({**node, "@id": "https://x.org/b"}),
        exchange="PDIP",
        document_class="loan documentation",
    )
    assert str(first.id).startswith("urn:uuid:")
    assert first.id == second.id
    other = mint(
        _resource({**node, "value": 1.0}),
        exchange="PDIP",
        document_class="loan documentation",
    )
    assert other.id != first.id


def test_timestamped_resource_uses_its_own_date_and_facet() -> None:
    minted = mint(
        _resource(
            {
                "@id": "https://x.org/i",
                "@type": "DebtInstrument",
                "name": "Republic of Cameroon Loan",
                "debtInstrumentType": "svto-cbox:LoanFacilityDebtInstrumentType",
                "issueDate": "2016-09-13",
            }
        ),
        exchange="PDIP",
        document_class="loan documentation",
    )
    assert str(minted.id) == (
        "https://purl.org/svto/data/pdip/loan-documentation/debt-instrument/"
        "2016/09/13/loan-facility/republic-of-cameroon-loan"
    )


def test_missing_date_falls_back_to_the_document_date_then_undated() -> None:
    node: dict[str, object] = {
        "@id": "https://x.org/a",
        "@type": "Agreement",
        "name": "Facility Agreement",
        "agreementType": "svto-cbox:LoanAgreementAgreementType",
    }
    with_fallback = mint(
        _resource(node),
        exchange="pdip",
        document_class="loan documentation",
        document_date=date(2016, 9, 13),
    )
    assert "/2016/09/13/" in str(with_fallback.id)
    undated = mint(
        _resource(node), exchange="pdip", document_class="loan documentation"
    )
    assert str(undated.id) == (
        "https://purl.org/svto/data/pdip/loan-documentation/agreement/"
        "loan-agreement/facility-agreement"
    )


def test_missing_name_is_guessed_and_written_back() -> None:
    minted = mint(
        _resource(
            {
                "@id": "https://x.org/p",
                "@type": "ContractProvision",
                "provisionType": "svto-cbox:NegativePledgeProvisionType",
            }
        ),
        exchange="pdip",
        document_class="bond contract",
    )
    assert isinstance(minted, ContractProvision)
    assert minted.name == "Negative Pledge Contract Provision"
    assert str(minted.id) == (
        "https://purl.org/svto/data/pdip/bond-contract/contract-provision/"
        "negative-pledge/negative-pledge-contract-provision"
    )


def test_facetless_type_omits_the_cbox_segment() -> None:
    minted = mint(
        _resource(
            {
                "@id": "https://x.org/t",
                "@type": "DefinedTerm",
                "prefLabel": "External Indebtedness",
                "definedIn": "https://x.org/agreement",
            }
        ),
        exchange="pdip",
        document_class="bond contract",
    )
    assert str(minted.id) == (
        "https://purl.org/svto/data/pdip/bond-contract/defined-term/"
        "external-indebtedness"
    )
