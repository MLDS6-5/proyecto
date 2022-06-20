from argparse import ArgumentParser

import joblib
from strokeanalysis.database.database import StrokeDataLoader
from strokeanalysis.models.models import ModelProxy
from strokeanalysis.preprocessing.preprocessing import StrokePreprocessing
from strokeanalysis.types.data_fields import DataFields
from strokeanalysis.types.models import ModelKind
import joblib


def make_parser() -> ArgumentParser:
    parser = ArgumentParser()    

    parser.add_argument('file', help='Path del archivo con data en csv')

    subparsers = parser.add_subparsers(dest="subcommand", help="Modelo que desea entrenar")
    subparsers.required = True

    parser_svm = subparsers.add_parser("svm")  

    parser_svm.add_argument("--kernel", type=str, default="linear")
    parser_svm.add_argument("--C", type=float, default=1.0)
    parser_svm.add_argument("--gamma", type=float)

    parser_log = subparsers.add_parser("logistic")  
    
    parser_log.add_argument("--C", type=float, default=1.0)
    

    return parser

def main():
    parser = make_parser()
    args = parser.parse_args()

    path = args.file
    dataset = StrokeDataLoader().add_path(path).load()

    data = dataset.get_data()

    cleaned_data = (
        StrokePreprocessing()
            .add_data(data)
            .add_fields(
                DataFields(label="stroke", categorical=["gender", "hypertension", "heart_disease", "ever_married", "work_type", "Residence_type", "smoking_status"])
                )
            .clean_data()
            .manage_categorical()            
        )

    X, y = cleaned_data.get_final_data()

    dictt = {}

    if "kernel" in args:
        dictt["kernel"] = args.kernel
    
    if "C" in args:
        dictt["C"] = args.C

    if "gamma" in args and args.gamma != None:
        dictt["gamma"] = args.gamma   

    model_proxy = ModelProxy().add_model_kind(ModelKind[args.subcommand.upper()]).add_hparams(**dictt)    
    model = model_proxy.resolve()

    model.fit(X, y)

    joblib.dump(model, f"{args.subcommand}.joblib")


if __name__ == "__main__":
    main()
    