import streamlit as st
import cv2
import pickle
import json
import numpy as np
from utils import classify, load_model , set_background

import warnings
warnings.filterwarnings("ignore")

# set background
set_background('background_img.jpg')

# set title
st.title("Diabetes Prediction Web App")

# set header
st.header("Please fill in the required fields")

# getting input form user
pregnancies = st.text_input('Number of Pregnancies')
glucose = st.text_input('Glucose Level')
blood_pressure = st.text_input('Blood Pressure Value')
skin_thickness = st.text_input('Skin Thickness Value')
insulin = st.text_input('Insulin Value')
bmi = st.text_input('BMI Value')
dpf = st.text_input('DPF')
age = st.text_input('Age')

# load classifier
model_path = r"C:\Users\US593\OneDrive\Desktop\ml_model_deployement_as_web_app_using_streamlit_on_heroku\diabetes_classifier\logistic_regression_model.p"
model = load_model(model_path)

# classification
if st.button('Results'):
    results = classify([int(pregnancies),int(glucose),int(blood_pressure),int(skin_thickness),int(insulin),float(bmi),float(dpf),int(age)],model)
    classification = results['classification']
    score = results['score']


# show results
    st.write("## Result")
    st.write(f"### Classification : {classification}")
    st.write(f"#### Confidence Score : {score}")