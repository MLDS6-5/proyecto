from abc import ABC, abstractmethod
from numpy import ndarray as Array
from pandas import DataFrame
from typing import Tuple
from strokeanalysis.types.data_fields import DataFields
import pandas as pd
from sklearn.preprocessing import StandardScaler

class AbstractPreprocessing(ABC):
    data: DataFrame    
    fields: DataFields
    x: Array
    y: Array

    def add_data(self, data: DataFrame) -> "AbstractPreprocessing":
        self.data = data
        return self

    def add_fields(self, fields: DataFields) -> "AbstractPreprocessing":
        self.fields = fields
        return self

    @abstractmethod
    def clean_data(self) -> "AbstractPreprocessing":
        ...
    
    @abstractmethod
    def manage_categorical(self) -> "AbstractPreprocessing":
        ...

    def get_final_data(self) -> Tuple[Array, Array]:
        if self.fields.label not in self.data:
            self.y = None
            self.x = self.data.to_numpy()
        else:
            self.y = self.data[self.fields.label].to_numpy()        
            self.x = self.data.drop(self.fields.label, axis=1).to_numpy()
            
        scaler = StandardScaler().fit(self.x)
        self.x = scaler.transform(self.x)
        return self.x, self.y


class StrokePreprocessing(AbstractPreprocessing):

    def clean_data(self) -> "AbstractPreprocessing":
        self.data = self.data.dropna()
        return self
    
    def manage_categorical(self) -> "AbstractPreprocessing":

        self.data = pd.get_dummies(self.data, columns=self.fields.categorical)
        return self

