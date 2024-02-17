from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
from utils import classify,load_model

app = FastAPI()

class model_input(BaseModel):

    pregnancies : int
    glucose : int
    blood_pressure : int
    skin_thickness : int
    insulin : int
    bmi : float
    dpf : float
    age : int

# loading_trained_model
model_path = r"C:\Users\US593\OneDrive\Desktop\ml_model_deployment_as_an_api_using_fastapi\diabetes_classifier\logistic_regression_model.p"
model = load_model(model_path)

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):

    input_data = input_parameters.json()  # retrieve json data from input_parameters and assign it to the variable input_data.
    input_dict = json.loads(input_data)   # convert json string to python dictionary.

    pregnancies = input_dict["pregnancies"]
    glucose = input_dict["glucose"]
    blood_pressure = input_dict["blood_pressure"]
    skin_thickness = input_dict["skin_thickness"]
    insulin = input_dict["insulin"]
    bmi = input_dict["bmi"]
    dpf = input_dict["dpf"]
    age = input_dict["age"]

    user_input = [pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,dpf,age]

    results = classify(user_input,model)
    
    if results is not None: 
        return f"Result : {results['classification']}, Confidence_Score : {results['score']}"
    return "Error!"


# to get local-host api url, run in cmd : uvicorn main:app