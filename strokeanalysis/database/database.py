from abc import ABC, abstractmethod
from pandas import DataFrame
import pandas as pd

class AbstractDataLoader(ABC):
    data: DataFrame
    path: str
    name: str
    
    def add_path(self, path: str) -> "AbstractDataLoader":
        self.path = path
        return self
    
    def get_data(self) -> DataFrame:
        return self.data
    

    @abstractmethod
    def export(self, path: str) -> "AbstractDataLoader":
        ...    

    @abstractmethod
    def load(self) -> DataFrame:
        ...
    
    def __repr__(self) -> str:
        return f"{self.name}(\npath={self.path}\ndata=\n{self.data})"
    
    def __str__(self) -> str:
        return self.__repr__()


class StrokeDataLoader(AbstractDataLoader):

    name = "StrokeDataLoader"

    def __init__(self) -> None:
        self.data = DataFrame([])
        self.path = ""
    
    def export(self, path: str) -> "StrokeDataLoader":
        self.data.to_csv(path)
        return self
    
    def load(self) -> "StrokeDataLoader":
        self.data = DataFrame(pd.read_csv(self.path, index_col=0))
        return self