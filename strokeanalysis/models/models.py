from strokeanalysis.types.models import ModelKind, StrokeClassifier
from sklearn.svm import SVC
from strokeanalysis.types.hparams import SVMHParams, LogisticHParams
from sklearn.linear_model import LogisticRegression

class ModelProxy:

    model_table = {
        ModelKind.SVM: [SVC, SVMHParams],
        ModelKind.LOGISTIC: [LogisticRegression, LogisticHParams]
    }

    def __init__(self) -> None:
        self.model_kind = ModelKind.SVM
        self.hparams = SVMHParams()

    def add_model_kind(self, model_kind: ModelKind) -> "ModelProxy":
        self.model_kind = model_kind
        return self
    
    def add_hparams(self, *args, **kwargs) -> "ModelProxy":
        self.hparams = self.model_table[self.model_kind][1](*args, **kwargs)
        return self
    

    def resolve(self) -> StrokeClassifier:
        model_class, _ = self.model_table[self.model_kind]        
        model = model_class(**self.hparams.dict(exclude_none=True)) 
        return model
    
