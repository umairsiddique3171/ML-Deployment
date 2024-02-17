import pickle
import numpy as np


def classify(input,model):

    input = np.array(input)
    input = input.reshape(1,-1)
    prediction = model.predict(input)[0]
    confidence_score_array = model.predict_proba(input)[0]
    if prediction is not None : 
        if prediction == 0:
            classification = 'Not Diabetic'
            score = confidence_score_array[0]
        else : 
            classification = 'Diabetic'
            score = confidence_score_array[1]
    results = {}
    results['classification'] = classification
    results['score'] = score

    return results


def load_model(model_path): 
    model = pickle.load(open(model_path, "rb"))
    return model