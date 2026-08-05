"""The Timestamp annotated type: an ISO 8601 date or datetime.

Parsed into date/datetime objects, which serialize back to ISO 8601 strings
in JSON mode (model_dump(mode="json")).

The BeforeValidator keeps a string-only contract for JSON input: pydantic
would otherwise also accept epoch numbers as datetimes. Anything that is not
a string (or already a date/datetime, for construction from Python code) is
mapped to None, which the date | datetime validation then rejects.
"""

from datetime import date, datetime
from typing import Annotated

from pydantic import BeforeValidator

Timestamp = Annotated[
    date | datetime,
    BeforeValidator(
        lambda value: value if isinstance(value, str | date | datetime) else None
    ),
]
