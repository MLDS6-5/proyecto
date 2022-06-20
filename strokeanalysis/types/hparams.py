from typing import Optional
from pydantic import BaseModel

class SVMHParams(BaseModel):
    C: float = 1.0
    kernel: str = "linear"
    gamma: Optional[float] = None

class LogisticHParams(BaseModel):
    C: float = 1.0