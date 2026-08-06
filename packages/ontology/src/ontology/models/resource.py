from typing import Annotated

from pydantic import Field, TypeAdapter

from ontology.models.administrative_area import AdministrativeArea
from ontology.models.agreement import Agreement
from ontology.models.cbox.agreement_type import AgreementType
from ontology.models.cbox.collective_action_clause_type import (
    CollectiveActionClauseType,
)
from ontology.models.cbox.debt_instrument_type import DebtInstrumentType
from ontology.models.cbox.document_class import DocumentClass
from ontology.models.cbox.document_section_type import DocumentSectionType
from ontology.models.cbox.event_type import EventType
from ontology.models.cbox.governing_law import GoverningLaw
from ontology.models.cbox.interest_rate_type import InterestRateType
from ontology.models.cbox.issuer_type import IssuerType
from ontology.models.cbox.organization_role_category import OrganizationRoleCategory
from ontology.models.cbox.organization_role_name import OrganizationRoleName
from ontology.models.cbox.pari_passu_type import PariPassuType
from ontology.models.cbox.payment_frequency import PaymentFrequency
from ontology.models.cbox.person_role_category import PersonRoleCategory
from ontology.models.cbox.person_role_name import PersonRoleName
from ontology.models.cbox.provision_type import ProvisionType
from ontology.models.cbox.seniority import Seniority
from ontology.models.cbox.sovereign_immunity_waiver_type import (
    SovereignImmunityWaiverType,
)
from ontology.models.cbox.voting_aggregation_method import VotingAggregationMethod
from ontology.models.contract_provision import ContractProvision
from ontology.models.country import Country
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
    | IssuerType
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
