import pytest

from ontology.models import Resource, ResourceAdapter, default_context

_NODES = (
    {
        "@id": "https://purl.org/svto/data/orgs/jamaica",
        "@type": "Organization",
        "name": "Jamaica",
        "debtorType": "svto-cbox:CentralGovernmentDebtorType",
        "location": "svto-cbox:JAMCountry",
    },
    {
        "@id": "https://purl.org/svto/data/instruments/jam-bond",
        "@type": "DebtInstrument",
        "name": "Jamaica Global Bond",
        "currency": "USD",
        "seniority": "svto-cbox:SeniorUnsecuredSeniority",
        "maturityDate": "2039-06-15",
    },
    {
        "@id": "https://purl.org/svto/data/provisions/jam-cac",
        "@type": "ContractProvision",
        "provisionType": "svto-cbox:CollectiveActionClauseProvisionType",
        "cacType": "svto-cbox:SecondGenerationCollectiveActionClauseType",
    },
)


@pytest.fixture(scope="session")
def context() -> dict[str, object]:
    return default_context()


@pytest.fixture()
def sample_resources() -> list[Resource]:
    return [ResourceAdapter.validate_python(node) for node in _NODES]
