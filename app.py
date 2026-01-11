import streamlit as st
from crop_predict import recommend_crop
from disease_predict import detect_disease

st.title("AgriPred")

menu = st.selectbox("Select Service", ["Crop Recommendation", "Plant Disease Detection"])

if menu == "Crop Recommendation":
    N = st.number_input("Nitrogen")
    P = st.number_input("Phosphorus")
    K = st.number_input("Potassium")
    T = st.number_input("Temperature")
    H = st.number_input("Humidity")
    PH = st.number_input("pH")
    R = st.number_input("Rainfall")

    if st.button("Predict Crop"):
        crop = recommend_crop([N,P,K,T,H,PH,R])
        st.success(f"Recommended Crop: {crop}")

else:
    img = st.file_uploader("Upload leaf image")

    if img:
        with open("leaf.jpg", "wb") as f:
            f.write(img.getbuffer())

        result = detect_disease("leaf.jpg")
        st.image("leaf.jpg")
        st.success(f"Disease: {result}")
