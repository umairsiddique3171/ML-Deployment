import json
import requests


url = "/diabetes_prediction"

input_data = {
    # values are taken from sample data which link is also given in markdown.
    'pregnancies' : 1,
    'glucose' : 85,
    'blood_pressure' : 66,
    'skin_thickness' : 29,
    'insulin' : 0,
    'bmi' : 26.6,
    'dpf' : 0.351,
    'age' : 31
    # outcome should be "Not Diabetic"
}

input_json = json.dumps(input_data)
response = requests.post(url,data=input_json)
print(response.text)