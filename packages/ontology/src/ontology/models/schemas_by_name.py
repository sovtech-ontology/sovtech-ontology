from ontology.models.base_resource import BaseResource
from ontology.models.schemas import schemas

schemas_by_name: dict[str, type[BaseResource]] = {
    schema.__name__: schema for schema in schemas
}
