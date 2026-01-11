import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("crop_data.csv")

X = data.drop("label", axis=1)
y = data["label"]

model = RandomForestClassifier()
model.fit(X, y)

with open("crop_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Crop model trained and saved")
