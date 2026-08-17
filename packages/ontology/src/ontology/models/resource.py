from typing import Annotated

from pydantic import Field, TypeAdapter

from ontology.models.administrative_area import AdministrativeArea
from ontology.models.agreement import Agreement
from ontology.models.cbox import (
    AgreementType,
    CollectiveActionClauseType,
    Country,
    DebtInstrumentType,
    DebtorType,
    DocumentClass,
    DocumentSectionType,
    EventType,
    GoverningLaw,
    InterestRateType,
    OrganizationRoleCategory,
    OrganizationRoleName,
    PariPassuType,
    PaymentFrequency,
    PersonRoleCategory,
    PersonRoleName,
    ProvisionType,
    Seniority,
    SovereignImmunityWaiverType,
    VotingAggregationMethod,
)
from ontology.models.contract_provision import ContractProvision
from ontology.models.debt_instrument import DebtInstrument
from ontology.models.defined_term import DefinedTerm
from ontology.models.digital_document import DigitalDocument
from ontology.models.event import Event
from ontology.models.media_object import MediaObject
from ontology.models.monetary_amount import MonetaryAmount
from ontology.models.organization import Organization
from ontology.models.organization_role import OrganizationRole
from ontology.models.person import Person
from ontology.models.person_role import PersonRole
from ontology.models.place import Place
from ontology.models.quantitative_value import QuantitativeValue
from ontology.models.text_object import TextObject

Resource = Annotated[
    AdministrativeArea
    | Agreement
    | AgreementType
    | CollectiveActionClauseType
    | ContractProvision
    | Country
    | DebtInstrument
    | DebtInstrumentType
    | DefinedTerm
    | DigitalDocument
    | DocumentClass
    | DocumentSectionType
    | Event
    | EventType
    | GoverningLaw
    | InterestRateType
    | DebtorType
    | MediaObject
    | MonetaryAmount
    | Organization
    | OrganizationRole
    | OrganizationRoleCategory
    | OrganizationRoleName
    | PariPassuType
    | PaymentFrequency
    | Person
    | PersonRole
    | PersonRoleCategory
    | PersonRoleName
    | Place
    | ProvisionType
    | QuantitativeValue
    | Seniority
    | SovereignImmunityWaiverType
    | TextObject
    | VotingAggregationMethod,
    Field(discriminator="type_"),
]

ResourceAdapter: TypeAdapter[Resource] = TypeAdapter(Resource)
