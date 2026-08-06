from datetime import date, datetime
from typing import Annotated

from pydantic import BeforeValidator

Timestamp = Annotated[
    date | datetime,
    BeforeValidator(
        lambda value: value if isinstance(value, str | date | datetime) else None
    ),
]
