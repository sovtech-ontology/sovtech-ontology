# SovTech Ontology

An open domain model and tooling for SovTech: the intersection of sovereign debt, macroeconomics, international law, economics, and public policy. Built by [Teal Insights](https://tealinsights.com/) and [NatureFinance](https://www.naturefinance.net/).

The SovTech Ontology (SVTO) describes sovereign debt instruments, the agreements that govern them, their contract provisions, the parties that hold roles on them, and the documents that disclose them. It expresses them as linked data built on [RDF](https://www.w3.org/TR/rdf11-concepts/), [SKOS](https://www.w3.org/TR/skos-reference/), and [schema.org](https://schema.org).

The SVTO interchange format and its data model follow the pattern of [`@wpg/model`](https://github.com/DataEcosystems/WickedProblemGovernance/tree/main/packages/model) from the [WickedProblemGovernance](https://github.com/DataEcosystems/WickedProblemGovernance) repository.

## Structure of this repository

- [`packages/ontology`](./packages/ontology) — domain model: pydantic models with JSON-LD semantics and the shared JSON-LD context
- [`packages/ontology-evals-pipeline`](./packages/ontology-evals-pipeline) — evaluation pipeline that extracts the model from source documents and scores the results

## Development

### Prerequisites

* [Python 3.13](https://www.python.org/)
* [uv](https://docs.astral.sh/uv/)

### Install dependencies

    script/bootstrap

### Test

    script/test

## License

Licensed under the [MIT License](./LICENSE).
