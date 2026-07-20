import streamlit as st
import pandas as pd
from predict import predict_cost

st.set_page_config(
    page_title="Healthcare Insurance Cost Prediction",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Healthcare Insurance Cost Prediction")

st.header("Enter Patient Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
    smoker = st.selectbox("Smoker", ["Yes", "No"])

with col2:
    children = st.number_input("Children", 0, 10, 0)
    region = st.selectbox(
        "Region",
        ["Northeast", "Northwest", "Southeast", "Southwest"]
    )
    income = st.number_input("Annual Income", 0, 5000000, 500000)

if st.button("Predict Insurance Cost"):

    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "bmi": [bmi],
        "smoker": [smoker],
        "children": [children],
        "region": [region],
        "income": [income]
    })

    prediction = predict_cost(input_data)

    st.success(f"Predicted Annual Medical Cost: ₹ {prediction:,.2f}")