import streamlit as st
import numpy as np
import pickle
import base64
import matplotlib.pyplot as plt

# Load trained model
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

# Function to make predictions
def predict_price(features):
    prediction = model.predict([features])
    return prediction[0]

image_path= r"C:\Users\user\Downloads\istockphoto-2017790676-612x612.jpg"

# Set up background image
def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

background_image_base64 = get_base64_of_image(r"C:\Users\user\Downloads\istockphoto-2017790676-612x612.jpg")



background_css = f"""
<style>
    .stApp {{
        background: url("data:image/jpeg;base64,{background_image_base64}") no-repeat center center fixed;
        background-size: cover;
    }}
</style>
"""
st.markdown(background_css, unsafe_allow_html=True)

# App title
st.markdown("""
    <h1 style='text-align: center; color: white;'>🏡 Real Estate Price Prediction</h1>
    <h3 style='text-align: center; color: lightgreen;'>Enter the details below to estimate the property value</h3>
""", unsafe_allow_html=True)

# Arrange inputs in two columns
col1, col2 = st.columns(2)

with col1:
    sqft_living = st.number_input("🏠 Living Area (sqft)", min_value=200, max_value=10000, value=1500)
    bedrooms = st.number_input("🛏️ Bedrooms", min_value=1, max_value=10, value=3)
    grade = st.number_input("🏆 House Grade", min_value=1, max_value=13, value=7)
    floors = st.number_input("🏠 Floors", min_value=1, max_value=10, value=1)
    lat = st.number_input("🌍 Latitude", min_value=47.0, max_value=48.0, value=47.5)


with col2:
    sqft_lot = st.number_input("🌲 Lot Size (sqft)", min_value=1, max_value=1651359, value=1001)
    bathrooms = st.number_input("🚿 Bathrooms", min_value=1, max_value=10, value=2)
    house_age = st.number_input("📅 House Age (years)", min_value=1, max_value=130, value=10)
    sqft_living15 = st.number_input("🏘️ Living Area of Neighbors (sqft)", min_value=1, max_value=14000, value=1500)
    long = st.number_input("🌍 Longitude", min_value=-122.5, max_value=-121.5, value=-122.0)

# Predict price dynamically
features = [sqft_living, bedrooms, grade, floors, sqft_lot, bathrooms, house_age, sqft_living15,lat, long]
predicted_price = predict_price(features)

st.markdown(f"""
    <h2 style='text-align: center; color: yellow;'>Estimated Price: <span style='color: lightgreen;'>${predicted_price:,.2f}</span></h2>
""", unsafe_allow_html=True)

# Add interactive chart for feature impact
fig, ax = plt.subplots()
feature_names = ["Living Area", "Bedrooms", "Grade", "Floors", "Lot Size", "Bathrooms", "Age", "Living Area (Neighbors)","lat", "long"]
ax.barh(feature_names, features, color='lightblue')
ax.set_xlabel("Value")
ax.set_title("Feature Values")
st.pyplot(fig)
