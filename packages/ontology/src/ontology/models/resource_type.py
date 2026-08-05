"""The valid "@type" discriminators: one per concrete model in
sovereign-prospectus-ontology-initial.md — the 17 TBox classes plus the 19
CBox enumeration classes.

The abstract shared shapes (CreativeWork, RoleBase) are deliberately absent:
they are never instantiated, so nothing carries them as a "@type".
"""

from typing import Literal

ResourceType = Literal[
    "AdministrativeArea",
    "Agreement",
    "AgreementType",
    "CollectiveActionClauseType",
    "ContractProvision",
    "Country",
    "DebtInstrument",
    "DebtInstrumentType",
    "DefinedTerm",
    "DigitalDocument",
    "DocumentClass",
    "DocumentSectionType",
    "Event",
    "EventType",
    "GoverningLaw",
    "InterestRateType",
    "IssuerType",
    "MediaObject",
    "MonetaryAmount",
    "Organization",
    "OrganizationRole",
    "OrganizationRoleCategory",
    "OrganizationRoleName",
    "PariPassuType",
    "PaymentFrequency",
    "Person",
    "PersonRole",
    "PersonRoleCategory",
    "PersonRoleName",
    "Place",
    "ProvisionType",
    "QuantitativeValue",
    "Seniority",
    "SovereignImmunityWaiverType",
    "TextObject",
    "VotingAggregationMethod",
]
