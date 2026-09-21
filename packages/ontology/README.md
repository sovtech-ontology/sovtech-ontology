# ontology

Data model for the SovTech Ontology (SVTO) interchange format. Defines resource types, their properties, and named individuals as [pydantic](https://docs.pydantic.dev) models with [JSON-LD](https://json-ld.org) semantics, following the pattern of [`@wpg/model`](https://github.com/DataEcosystems/WickedProblemGovernance/tree/main/packages/model) in the [WickedProblemGovernance](https://github.com/DataEcosystems/WickedProblemGovernance) repository.

It builds on semantic web technology: resources are [RDF](https://www.w3.org/TR/rdf11-concepts/) nodes identified by IRIs, defined terms are [SKOS](https://www.w3.org/TR/skos-reference/) concepts, and the shared JSON-LD context resolves every term to a [schema.org](https://schema.org), SKOS, or SVTO IRI.

## Building/Installation

See the [root README](../../README.md).

## Usage

### Example

```python
from ontology.models import DebtInstrument, default_context

# Validates the node object and returns a typed DebtInstrument instance
instrument = DebtInstrument.model_validate(
    {
        "@id": "https://example.com/instrument/1",
        "@type": "DebtInstrument",
        "name": "My Instrument",
        # ...
    }
)

# Converts the resource to RDF (N-Quads)
nquads = instrument.to_rdf(default_context())
```

## Encoding

SVTO interchange resources can be encoded as a stream of JSON-LD resources in [JSONL](https://jsonlines.org).

Each resource has:

* `@id`: an IRI identifying the resource
* `@type`: a type name resolved by the JSON-LD context

The JSON-LD `@context` is not embedded in the data. It is supplied externally when the data is passed to a JSON-LD processor.
