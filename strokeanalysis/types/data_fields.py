from pydantic import BaseModel
from typing import Optional

class DataFields(BaseModel):
    label: str
    categorical: Optional[list[str]]
    optionals: Optional[list[str]]