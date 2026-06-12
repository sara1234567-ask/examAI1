import pickle
import numpy as np

model = pickle.load(open("sentiment_model.pkl", "rb"))

def predict(text):
    proba = model.predict_proba([text])[0]
    classes = model.classes_

    index = np.argmax(proba)
    return classes[index], float(proba[index])