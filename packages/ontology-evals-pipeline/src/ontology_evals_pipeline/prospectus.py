from pathlib import Path

from pydantic import BaseModel


class BondProspectus(BaseModel):
    """A bond prospectus in structured form."""

    identifier: str
    path: Path
    page_count: int
    text: str
