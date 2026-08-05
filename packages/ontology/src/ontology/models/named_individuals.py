"""The CBox registry.

An entry's "name" is only given where it differs from the capital-cased key.
"""

named_individuals: dict[str, dict[str, dict[str, str]]] = {
    "AgreementType": {
        "TrustIndenture": {
            "description": (
                "An independent trustee acts on behalf of bondholders and "
                "protects their interests."
            ),
        },
        "FiscalAgencyAgreement": {
            "description": (
                "A fiscal agent appointed by the issuer provides "
                "administrative services; no bondholder representation."
            ),
        },
        "TrustDeed": {
            "description": "English-law analogue of the trust indenture.",
        },
        "LoanAgreement": {
            "description": "A loan, credit, facility, or financing agreement.",
        },
        "Guarantee": {
            "description": "A third party guarantees the obligations.",
        },
        "UnderwritingAgreement": {
            "description": (
                "Underwriting or subscription arrangements for a distribution."
            ),
        },
        "Other": {
            "description": "An agreement not covered by the other categories.",
        },
    },
    "CollectiveActionClauseType": {
        "No": {
            "name": "No CACs",
            "description": "Unanimity required for payment-term changes.",
        },
        "FirstGeneration": {
            "name": "1st Generation CACs",
            "description": "Series-by-series majority modification only.",
        },
        "SecondGeneration": {
            "name": "2nd Generation CACs",
            "description": (
                "Aggregated voting across series with a per-series "
                "requirement (two-limb)."
            ),
        },
        "ThirdGeneration": {
            "name": "3rd Generation Enhanced CACs",
            "description": (
                "Post-2014 ICMA model: adds single-limb aggregated voting "
                "with uniformly applicable treatment."
            ),
        },
    },
    "DebtInstrumentType": {
        "Bond": {
            "description": "A long-term marketable debt security.",
        },
        "Note": {
            "description": "A medium-term marketable debt security.",
        },
        "Bill": {
            "description": "A short-term discount security.",
        },
        "Sukuk": {
            "description": "A sharia-compliant certificate of investment.",
        },
        "LoanFacility": {
            "description": "A bilateral or syndicated loan or credit facility.",
        },
        "Other": {
            "description": "An instrument not covered by the other categories.",
        },
    },
    "DocumentClass": {
        "Prospectus": {
            "description": (
                "Standalone disclosure document for a specific offer or "
                "listing; readable on its own."
            ),
        },
        "BaseProspectus": {
            "description": (
                "Programme-level disclosure under which individual tranches "
                "are issued later; no tranche pricing."
            ),
        },
        "Supplement": {
            "description": (
                "Amends or updates an existing prospectus or base prospectus."
            ),
        },
        "FinalTerms": {
            "description": (
                "Completes a base prospectus for one tranche; carries the "
                "tranche economics."
            ),
        },
        "FreeWritingProspectus": {
            "description": (
                "SEC Rule 433 offering communications, mostly final pricing "
                "term sheets."
            ),
        },
        "AnnualReport": {
            "description": (
                "Periodic or standing issuer disclosure not tied to a specific offer."
            ),
        },
        "Notice": {
            "description": (
                "Exchange or regulatory announcements about issuers or instruments."
            ),
        },
        "LoanDocumentation": {
            "description": (
                "Loan contracts and related official-lender documentation."
            ),
        },
        "BondContract": {
            "description": "Contracts of bond issuance and administration.",
        },
        "RestructuringDocument": {
            "description": (
                "Documents proposing, executing, or contracting liability management."
            ),
        },
        "Other": {
            "description": "Reviewed and does not fit any class.",
        },
    },
    "DocumentSectionType": {
        "RiskFactors": {
            "description": "Disclosure of risks to investors.",
        },
        "Definitions": {
            "description": "The defined-terms section.",
        },
        "DescriptionOfSecurities": {
            "name": "Description of Securities",
            "description": "Terms and conditions of the securities.",
        },
        "UseOfProceeds": {
            "name": "Use of Proceeds",
            "description": "How the issuer will use the money raised.",
        },
        "Taxation": {
            "description": "Tax treatment disclosure.",
        },
        "PlanOfDistribution": {
            "name": "Plan of Distribution",
            "description": "Underwriting and distribution arrangements.",
        },
        "Other": {
            "description": "A section not covered by the other categories.",
        },
    },
    "EventType": {
        "Issuance": {
            "description": "The instrument is issued.",
        },
        "Settlement": {
            "description": "The issue settles; money and securities move.",
        },
        "EffectiveDate": {
            "description": "An agreement or amendment takes effect.",
        },
        "InterestPayment": {
            "description": "A scheduled coupon payment.",
        },
        "Maturity": {
            "description": "Scheduled final repayment of principal.",
        },
        "Default": {
            "description": (
                "An event of default occurs (non-payment, breach, misrepresentation)."
            ),
        },
        "Moratorium": {
            "description": "The sovereign declares a moratorium on payments.",
        },
        "Acceleration": {
            "description": ("Principal is declared immediately due following default."),
        },
        "Restructuring": {
            "description": (
                "A liability management transaction (exchange, amendment, buyback) is executed or settles."
            ),
        },
        "Other": {
            "description": "An occurrence not covered by the other categories.",
        },
    },
    "GoverningLaw": {
        "NewYork": {
            "name": "New York Law",
            "description": "The law of the State of New York.",
        },
        "English": {
            "name": "English Law",
            "description": "The law of England and Wales.",
        },
        "Local": {
            "name": "Local Law",
            "description": "The issuer's own domestic law.",
        },
        "Other": {
            "description": "A governing law not covered by the other categories.",
        },
    },
    "InterestRateType": {
        "Fixed": {
            "description": "Constant coupon over the instrument's life.",
        },
        "Floating": {
            "description": "Coupon resets off a reference rate plus a margin.",
        },
        "ZeroCoupon": {
            "description": "No periodic interest; issued at a discount.",
        },
        "StepUp": {
            "name": "Step-Up",
            "description": "Coupon changes on a predefined schedule.",
        },
        "Other": {
            "description": ("A rate structure not covered by the other categories."),
        },
    },
    "IssuerType": {
        "CentralGovernment": {
            "description": (
                "The sovereign state itself, including ministries and "
                "treasuries acting for it."
            ),
        },
        "SubSovereign": {
            "name": "Sub-Sovereign",
            "description": (
                "A sub-national government or territory issuing in its own "
                "name (Emirate of Abu Dhabi, Hong Kong SAR)."
            ),
        },
        "CentralBank": {
            "description": "The monetary authority as a distinct legal entity.",
        },
        "StateOwnedEnterprise": {
            "name": "State-Owned Enterprise",
            "description": ("A public corporation owned or controlled by the state."),
        },
        "IssuanceVehicle": {
            "description": (
                "An SPV established to issue on behalf of a public-sector "
                "obligor (Oman Sovereign Sukuk S.A.O.C.)."
            ),
        },
        "Supranational": {
            "description": (
                "A multilateral institution owned by member states (Asian "
                "Development Bank)."
            ),
        },
        "MultiIssuer": {
            "name": "Multi-Issuer",
            "description": (
                "A composite of several issuers filing jointly; constituents "
                "carried as members."
            ),
        },
    },
    "OrganizationRoleCategory": {
        "Obligor": {
            "description": "A party that owes the debt or stands behind it.",
        },
        "Creditor": {
            "description": "A party with a claim to be paid.",
        },
        "Agent": {
            "name": "Agent / Intermediary",
            "description": (
                "A third party administering the issuance or the relationship."
            ),
        },
        "DistributionAndAdvisory": {
            "name": "Distribution and Advisory",
            "description": (
                "A party distributing the securities or advising on the deal."
            ),
        },
    },
    "OrganizationRoleName": {
        "Issuer": {
            "description": "The entity issuing the instrument.",
        },
        "Borrower": {
            "description": "The entity drawing under a loan facility.",
        },
        "Guarantor": {
            "description": "An entity guaranteeing the obligations.",
        },
        "Bondholder": {
            "description": "A holder of the securities.",
        },
        "Lender": {
            "description": "A lender under a facility.",
        },
        "Trustee": {
            "description": (
                "Independent entity acting on behalf of bondholders and "
                "protecting their interests."
            ),
        },
        "FiscalAgent": {
            "description": (
                "Issuer-appointed provider of administrative services for the issue."
            ),
        },
        "PayingAgent": {
            "description": "Makes payments to holders on the issuer's behalf.",
        },
        "Registrar": {
            "description": "Maintains the register of holders.",
        },
        "TransferAgent": {
            "description": ("Processes transfers and exchanges of the securities."),
        },
        "CalculationAgent": {
            "description": ("Determines rates and amounts for variable terms."),
        },
        "ClearingSystem": {
            "description": (
                "Clears and settles the securities (DTC, Euroclear, Clearstream)."
            ),
        },
        "ProcessAgent": {
            "description": (
                "Accepts service of process in the chosen jurisdiction for "
                "the sovereign."
            ),
        },
        "Underwriter": {
            "description": "Purchases and distributes the securities.",
        },
        "LeadManager": {
            "description": "Leads the syndicate for the offering.",
        },
        "ListingAgent": {
            "description": "Handles the exchange listing.",
        },
        "LegalCounsel": {
            "description": ("Law firm advising a party or delivering opinions."),
        },
    },
    "PariPassuType": {
        "Old": {
            "description": (
                "Pre-2014 wording exposed to the ratable-payment "
                "interpretation litigated in the 1990s-2010s."
            ),
        },
        "Enhanced": {
            "description": (
                "Post-2014 wording clarifying equal ranking only, with no "
                "ratable-payment obligation."
            ),
        },
    },
    "PaymentFrequency": {
        "Annual": {
            "description": "Paid once a year.",
        },
        "SemiAnnual": {
            "name": "Semi-Annual",
            "description": "Paid twice a year.",
        },
        "Quarterly": {
            "description": "Paid four times a year.",
        },
        "Monthly": {
            "description": "Paid monthly.",
        },
        "AtMaturity": {
            "description": "Paid once, at maturity.",
        },
        "Other": {
            "description": "A frequency not covered by the other categories.",
        },
    },
    "PersonRoleCategory": {
        "Execution": {
            "description": "A person executing documents.",
        },
        "Representation": {
            "description": ("A person representing or acting for an organization."),
        },
    },
    "PersonRoleName": {
        "Signatory": {
            "description": ("A person signing an agreement on behalf of a party."),
        },
        "AuthorizedRepresentative": {
            "description": "A person authorized to act for a party.",
        },
        "ContactOfficer": {
            "description": ("A named contact for notices or investor communications."),
        },
    },
    "ProvisionType": {
        "Definitions": {
            "description": (
                "Defines terms used in the agreement; the anchor for DefinedTerms."
            ),
        },
        "GoverningLaw": {
            "description": (
                "Selects the legal framework governing interpretation and enforcement."
            ),
        },
        "Jurisdiction": {
            "description": (
                "Specifies which courts hear disputes; often includes "
                "process-agent appointment."
            ),
        },
        "PaymentTerms": {
            "description": (
                "Amount, timing, and mechanics of interest and principal payments."
            ),
        },
        "FacilityCommitment": {
            "name": "Facility / Commitment",
            "description": ("Size and financial terms of a promise to lend."),
        },
        "Drawdown": {
            "name": "Drawdown / Utilization",
            "description": ("When and how a commitment to lend turns into debt."),
        },
        "ConditionsPrecedent": {
            "description": (
                "What must happen before money moves: authority, approvals, "
                "opinions, information."
            ),
        },
        "RepresentationsAndWarranties": {
            "name": "Representations and Warranties",
            "description": (
                "The borrower testifies to key facts and is liable for lies."
            ),
        },
        "Covenant": {
            "description": (
                "A promise by the issuer on financial management, "
                "information, or conduct."
            ),
        },
        "NegativePledge": {
            "description": (
                "Prohibits securing other creditors without securing this "
                "one proportionately."
            ),
        },
        "PariPassu": {
            "description": (
                "Ranking of this claim relative to the issuer's other "
                "comparable obligations."
            ),
        },
        "InformationUndertaking": {
            "description": ("Reporting and disclosure obligations to creditors."),
        },
        "EventsOfDefault": {
            "name": "Events of Default",
            "description": (
                "Tripwires — non-payment, breach, misrepresentation, "
                "moratorium — giving rise to remedies."
            ),
        },
        "CrossDefault": {
            "name": "Cross-Default",
            "description": (
                "A default under other indebtedness constitutes a default here."
            ),
        },
        "Acceleration": {
            "description": (
                "On default, principal can be declared due immediately; "
                "voting rules apply."
            ),
        },
        "CollectiveActionClause": {
            "description": (
                "Binds all holders to a modification approved by a qualified majority."
            ),
        },
        "NonReservedMatterModification": {
            "name": "Non-Reserved Matter Modification",
            "description": "Rules for modifying non-reserved matters.",
        },
        "ReservedMatterModification": {
            "description": (
                "Rules for modifying reserved matters (payment terms and "
                "other protected matters)."
            ),
        },
        "SovereignImmunityWaiver": {
            "description": (
                "The extent to which the sovereign waives immunity from suit "
                "and execution."
            ),
        },
        "Other": {
            "description": "A provision not covered by the other categories.",
        },
    },
    "Seniority": {
        "SeniorUnsecured": {
            "description": "Senior claim with no collateral.",
        },
        "SeniorSecured": {
            "description": "Senior claim backed by collateral.",
        },
        "Subordinated": {
            "description": "Claim ranking behind senior obligations.",
        },
    },
    "SovereignImmunityWaiverType": {
        "Full": {
            "description": "Immunity waived for suit and execution.",
        },
        "No": {
            "name": "None",
            "description": "No waiver of sovereign immunity.",
        },
        "Selective": {
            "description": (
                "Waived only for specified proceedings, forums, or assets."
            ),
        },
    },
    "VotingAggregationMethod": {
        "SingleSeries": {
            "description": "Votes counted within one series only.",
        },
        "CrossSeriesSingleAggregated": {
            "name": "Cross-Series, Single Aggregated",
            "description": (
                "One aggregate vote across all affected series; typically "
                "conditioned on uniformly applicable treatment."
            ),
        },
        "CrossSeriesTwoTier": {
            "name": "Cross-Series, Two-Tier",
            "description": (
                "An aggregate threshold across all affected series plus a "
                "separate threshold in each series."
            ),
        },
    },
}
