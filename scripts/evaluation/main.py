from argparse import ArgumentParser
from os import path
import pandas as pd
import joblib

from strokeanalysis.database.database import StrokeDataLoader
from strokeanalysis.preprocessing.preprocessing import StrokePreprocessing
from strokeanalysis.types.data_fields import DataFields

def make_parser() -> ArgumentParser:
    parser = ArgumentParser()

    subparsers = parser.add_subparsers(dest="subcommand", help="Método de ingreso de la información")
    subparsers.required = True

    parser_svm = subparsers.add_parser("file")  

    parser_svm.add_argument("--path", help="Path del archivo csv", type=str, required=True)
    
    parser_log = subparsers.add_parser("line")  
    
    parser_log.add_argument("--gender", type=str,  choices=["Male", "Female"], help="Genero de la persona")
    parser_log.add_argument("--age", type=float,  help="Edad de la persona")
    parser_log.add_argument("--hypertension", type=int,  choices=[0, 1], help="¿Tiene hipertensión?")
    parser_log.add_argument("--heart_disease", type=int,  choices=[0, 1], help="¿Alguna enfermedad del corazón?")
    parser_log.add_argument("--ever_married", type=str,  choices=["Yes", "No"], help="¿Alguna se ha casado?")
    parser_log.add_argument("--work_type", type=str,  choices=["children", "Govt_job", "Never_worked", "Self-employed"])
    parser_log.add_argument("--Residence_type", type=str,  choices=["Rural", "Urban"])
    parser_log.add_argument("--avg_glucose_level", type=float,  help="Nivel de glucosa en la sangre")
    parser_log.add_argument("--bmi", type=float,  help="Indice de masa corporal")
    parser_log.add_argument("--smoking_status", type=str,  choices=["formerly smoked", "never smoked", "smokes", "Unknown"])    

    return parser

def main():
    parser = make_parser()
    args = parser.parse_args()

    if path.exists("logistic.joblib"):
        model = joblib.load("logistic.joblib")
    elif path.exists("svm.joblib"):
        model = joblib.load("svm.joblib")
    else:
        print("No existe un modelo valido para hacer la predicción")
        exit()
    
    if args.subcommand == "file":

        dataset = StrokeDataLoader().add_path(args.path).load()
        data = dataset.get_data()    
    
    else:

        d = vars(args)        
        del d["subcommand"]        
        data = pd.DataFrame(d, index=[0])

    cleaned_data = (
        StrokePreprocessing()
            .add_data(data)
            .add_fields(
                DataFields(label="stroke", categorical=["gender", "hypertension", "heart_disease", "ever_married", "work_type", "Residence_type", "smoking_status"])
                )
            .clean_data()
            .manage_categorical()            
        )   
    

    X, _ = cleaned_data.get_final_data()

    y_pred = model.predict(X)

    print(y_pred)

if __name__ == "__main__":
    main()


    