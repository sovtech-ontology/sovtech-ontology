from typing import Annotated, Literal, override

from pydantic import AnyUrl, ConfigDict, Field

from ontology.models.base_resource import BaseResource
from ontology.models.cbox import (
    DebtInstrumentType,
    InterestRateType,
    PaymentFrequency,
    Seniority,
)
from ontology.models.iri import Iri
from ontology.models.monetary_amount import MonetaryAmount
from ontology.models.named_individual_iri_enum import named_individual_iri_enum
from ontology.models.named_individuals import named_individuals
from ontology.models.object_meta import ObjectMeta
from ontology.models.property_meta import PropertyMeta
from ontology.models.quantitative_value import QuantitativeValue
from ontology.models.thing import Thing
from ontology.models.timestamp import Timestamp


def _object_meta() -> ObjectMeta:
    return ObjectMeta(
        type_="DebtInstrument",
        description=(
            "A debt obligation: a bond series, note, bill, sukuk, or loan "
            "facility. The subject documents disclose, agreements govern, "
            "parties hold roles on, and events happen to."
        ),
        named_individuals=named_individuals,
    )


class DebtInstrument(BaseResource):
    """A debt obligation: a bond series, note, bill, sukuk, or loan
    facility. The subject documents disclose, agreements govern, parties
    hold roles on, and events happen to."""

    model_config = ConfigDict(
        title=_object_meta().title,
        json_schema_extra=_object_meta().json_schema_extra(),
    )

    type_: Literal["DebtInstrument"] = Field(alias="@type")
    amount_issued: Annotated[
        Iri | None,
        PropertyMeta(
            description="The principal amount issued.",
            range_=MonetaryAmount,
            title="Amount Issued",
        ).generate_meta(),
    ] = Field(default=None, alias="amountIssued")
    commitment_amount: Annotated[
        Iri | None,
        PropertyMeta(
            description="The committed facility size, for loan facilities.",
            range_=MonetaryAmount,
            title="Commitment Amount",
        ).generate_meta(),
    ] = Field(default=None, alias="commitmentAmount")
    currency: Annotated[
        str | None,
        PropertyMeta(
            description=("The ISO 4217 denomination currency of the instrument."),
            title="Currency",
        ).generate_meta(),
    ] = None
    debt_instrument_type: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("DebtInstrumentType"),
        PropertyMeta(
            description="Bond, note, bill, sukuk, or loan facility.",
            range_=DebtInstrumentType,
            title="Instrument Type",
        ).generate_meta(),
    ] = Field(default=None, alias="debtInstrumentType")
    description: Annotated[str | None, Thing.Fields.DESCRIPTION] = None
    governed_by: Annotated[
        tuple[Iri, ...] | None,
        PropertyMeta(
            description=(
                "The agreement(s) under which this instrument is issued and "
                "administered."
            ),
            range_="Agreement",
            title="Governed By",
        ).generate_meta(),
    ] = Field(default=None, alias="governedBy")
    identifier: Annotated[
        tuple[str, ...] | None,
        Thing.Fields.IDENTIFIER,
        PropertyMeta(
            description="Security identifiers (ISIN, CUSIP).",
            title="Identifier",
        ).generate_meta(),
    ] = None
    interest_payment_frequency: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("PaymentFrequency"),
        PropertyMeta(
            description="How often interest is paid.",
            range_=PaymentFrequency,
            title="Interest Payment Frequency",
        ).generate_meta(),
    ] = Field(default=None, alias="interestPaymentFrequency")
    interest_rate: Annotated[
        Iri | None,
        PropertyMeta(
            description="The coupon or margin, in percent per annum.",
            range_=QuantitativeValue,
            title="Interest Rate",
        ).generate_meta(),
    ] = Field(default=None, alias="interestRate")
    interest_rate_type: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("InterestRateType"),
        PropertyMeta(
            description="Fixed, floating, zero-coupon, or step-up.",
            range_=InterestRateType,
            title="Interest Rate Type",
        ).generate_meta(),
    ] = Field(default=None, alias="interestRateType")
    issue_date: Annotated[
        Timestamp | None,
        PropertyMeta(
            description=(
                "The date of issuance. Lifecycle occurrences beyond this are Events."
            ),
            title="Issue Date",
        ).generate_meta(),
    ] = Field(default=None, alias="issueDate")
    issue_price: Annotated[
        Iri | None,
        PropertyMeta(
            description="The issue price as percent of face.",
            range_=QuantitativeValue,
            title="Issue Price",
        ).generate_meta(),
    ] = Field(default=None, alias="issuePrice")
    maturity_date: Annotated[
        Timestamp | None,
        PropertyMeta(
            description="The scheduled final maturity.",
            title="Maturity Date",
        ).generate_meta(),
    ] = Field(default=None, alias="maturityDate")
    name: Annotated[str | None, Thing.Fields.NAME] = None
    seniority: Annotated[
        AnyUrl | None,
        named_individual_iri_enum("Seniority"),
        PropertyMeta(
            description="The ranking of the claim.",
            range_=Seniority,
            title="Seniority",
        ).generate_meta(),
    ] = None

    @classmethod
    @override
    def object_meta(cls) -> ObjectMeta:
        return _object_meta()

    @override
    def to_rdf(self, jsonld_context: dict) -> str:
        return super().to_rdf(jsonld_context)
