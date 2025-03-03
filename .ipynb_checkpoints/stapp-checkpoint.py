import streamlit as st
import pickle
import numpy as np

# Load trained Random Forest model
with open("rf_model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("🏡 House Price Prediction App")

# User inputs
sqft_living = st.number_input("🏠 Living Area (sqft)", min_value=200, max_value=10000, value=1500)
bathrooms = st.number_input("🚿 Number of Bathrooms", min_value=1, max_value=10, value=2)
bedrooms = st.number_input("🛏️ Number of Bedrooms", min_value=1, max_value=10, value=3)
grade = st.number_input("🏆 House Grade", min_value=1, max_value=13, value=7)
sqft_lot = st.number_input("🏆 House Grade", min_value=1, max_value=1651359, value=1001)
floors = st.number_input("🏆 House Grade", min_value=1, max_value=10, value=7)
house_age = st.number_input("🏆 House Grade", min_value=1, max_value=130, value=10)
sqft_living15 = st.number_input("🏆 House Grade", min_value=1, max_value=14000, value=7)

# Predict button
if st.button("💰 Predict Price"):
    input_features = np.array([[sqft_living, bathrooms, bedrooms, grade,sqft_lot,floors,house_age,sqft_living15]])
    prediction = model.predict(input_features)
    st.success(f"🏡 Estimated House Price: **${prediction[0]:,.2f}**")
