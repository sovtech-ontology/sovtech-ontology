import ontology


def test_package_imports() -> None:
    assert ontology is not None


def test_provision_types_are_the_taxonomy_buckets() -> None:
    from ontology.models.named_individuals import named_individuals

    types = named_individuals["ProvisionType"]
    assert len(types) == 115
    assert "AntiCorruptionAMLRepresentationsAndWarranties" in types
    assert "AntiCorruptionAMLBorrowerCovenantsUndertakings" in types
    assert types["NonPaymentFailureToPay"]["name"] == "Non-payment/Failure to Pay"
    assert types["NonPaymentFailureToPay"]["description"].startswith(
        "Events of Default and Consequences:"
    )
    assert "PaymentTerms" not in types


def test_document_section_types_include_table_of_contents() -> None:
    from ontology.models.named_individuals import named_individuals

    assert "TableOfContents" in named_individuals["DocumentSectionType"]
