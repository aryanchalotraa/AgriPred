🌱 AgriPred

A simple machine-learning based agriculture prediction system

AgriPred is a lightweight application that helps farmers and students predict the most suitable crop based on soil and weather parameters and detect whether a plant leaf is healthy or diseased using image analysis. The project is designed to be easy to run locally with minimal setup.

🔹 Features

Crop recommendation using a machine learning model

Plant disease detection from leaf images

Simple web interface built with Streamlit

No external APIs or cloud services required

🔹 Project Structure
AgriPred/
│
├── app.py
├── crop_predict.py
├── disease_predict.py
├── train_crop_model.py
├── crop_data.csv
├── requirements.txt
└── README.md

🔹 How to Run

git clone https://github.com/aryanchalotraa/AgriPred.git

Install required libraries

pip install -r requirements.txt

Train the crop prediction model (run once)

python train_crop_model.py

Start the application

streamlit run app.py

Use the browser interface to predict crops or detect plant disease

Press CTRL + C in terminal to stop the app

