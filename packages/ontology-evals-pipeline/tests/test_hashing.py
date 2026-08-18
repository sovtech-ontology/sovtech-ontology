from ontology.models import Resource, ResourceAdapter
from ontology_evals_pipeline.hashing import hash_resource, resource_tokens


def _organization(id_: str, name: str = "Jamaica") -> Resource:
    return ResourceAdapter.validate_python(
        {
            "@id": id_,
            "@type": "Organization",
            "name": name,
            "debtorType": "svto-cbox:CentralGovernmentDebtorType",
            "parentOrganization": "https://purl.org/svto/data/orgs/parent",
        }
    )


def test_tokens_keep_data_and_drop_minted_iris() -> None:
    tokens = resource_tokens(_organization("https://purl.org/svto/data/orgs/jm"))
    assert "name=Jamaica" in tokens
    assert "@type=Organization" in tokens
    assert "debtorType=https://purl.org/svto/cbox#CentralGovernmentDebtorType" in tokens
    assert not any("@id" in token for token in tokens)
    assert not any("parentOrganization" in token for token in tokens)


def test_same_data_different_id_hash_alike() -> None:
    first = hash_resource(_organization("https://x.org/a"), num_perm=128)
    second = hash_resource(_organization("https://x.org/b"), num_perm=128)
    assert first["hash"].jaccard(second["hash"]) == 1.0


def test_different_data_hash_apart() -> None:
    first = hash_resource(_organization("https://x.org/a"), num_perm=128)
    second = hash_resource(
        _organization("https://x.org/a", name="Cameroon"), num_perm=128
    )
    assert first["hash"].jaccard(second["hash"]) < 1.0


def test_hashing_is_deterministic() -> None:
    resource = _organization("https://x.org/a")
    first = hash_resource(resource, num_perm=128)
    second = hash_resource(resource, num_perm=128)
    assert (first["hash"].digest() == second["hash"].digest()).all()
