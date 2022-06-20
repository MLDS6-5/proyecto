from typing import Protocol, Optional
from numpy import ndarray as Array
from enum import Enum, auto

class StrokeClassifier(Protocol):

    def fit(self, X: Array, y: Optional[Array]) -> "StrokeClassifier":
        ...
    
    def predict(self, X: Array) -> Array:
        ...

class ModelKind(Enum):
    SVM = auto()
    LOGISTIC = auto()    
