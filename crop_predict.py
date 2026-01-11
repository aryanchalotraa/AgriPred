import pickle
import numpy as np

with open("crop_model.pkl", "rb") as f:
    model = pickle.load(f)

def recommend_crop(data):
    data = np.array(data).reshape(1, -1)
    return model.predict(data)[0]
