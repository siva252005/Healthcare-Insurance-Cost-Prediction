import streamlit as st
import pandas as pd

from predict import load_model
from forms import (
    personal_information,
    medical_information,
    insurance_information,
    procedure_information
)

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Healthcare Insurance Cost Prediction",
    page_icon="🏥",
    layout="wide"
)

# ---------------------------------
# Title
# ---------------------------------
st.title("🏥 Healthcare Insurance Cost Prediction")
st.write(
    "Estimate the annual medical insurance cost based on personal, medical, insurance, and health information."
)

# ---------------------------------
# Sidebar
# ---------------------------------
st.sidebar.title("ℹ️ About")

st.sidebar.info(
    """
    **Healthcare Insurance Cost Prediction**

    **Machine Learning Model:** Random Forest Regressor

    **Preprocessing:** ColumnTransformer
    - StandardScaler
    - OneHotEncoder

    **Framework:** Streamlit
    """
)

# ---------------------------------
# Load Model
# ---------------------------------
try:
    model, preprocessor = load_model()
    st.success("✅ Model Loaded Successfully")
except Exception as e:
    st.error(f"Error Loading Model: {e}")
    st.stop()

# ---------------------------------
# User Input
# ---------------------------------
user_data = personal_information()
medical_data = medical_information()
insurance_data = insurance_information()
procedure_data = procedure_information()

# ---------------------------------
# Combine Inputs
# ---------------------------------
input_data = {}

input_data.update(user_data)
input_data.update(medical_data)
input_data.update(insurance_data)
input_data.update(procedure_data)

input_df = pd.DataFrame([input_data])

# ---------------------------------
# Preview Input (Optional)
# ---------------------------------
with st.expander("📄 View Entered Information"):
    st.dataframe(input_df)

# ---------------------------------
# Prediction
# ---------------------------------
st.markdown("---")

if st.button("💰 Predict Annual Medical Cost", use_container_width=True):

    try:

        # Preprocess
        processed_data = preprocessor.transform(input_df)

        # Predict
        prediction = model.predict(processed_data)

        predicted_cost = prediction[0]

        st.markdown("## 🎯 Prediction Result")

        st.metric(
            label="Predicted Annual Medical Cost",
            value=f"₹ {predicted_cost:,.2f}"
        )

        # Risk Level
        if predicted_cost < 20000:
            risk = "🟢 Low Cost"
        elif predicted_cost < 50000:
            risk = "🟡 Medium Cost"
        else:
            risk = "🔴 High Cost"

        st.info(f"**Risk Level:** {risk}")

        st.caption(
            "⚠️ This prediction is generated using a machine learning model trained on historical insurance data. It is intended for educational purposes and should not be treated as an actual insurance quote."
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")