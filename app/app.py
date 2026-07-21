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
    page_title="Healthcare Insurance Cost Predictor",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
<div style="
    background: linear-gradient(90deg, #2563eb, #1d4ed8);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
">
    <h1 style="margin:0;">🏥 Healthcare Insurance Cost Predictor</h1>
    <p style="font-size:18px; margin-top:10px;">
        Predict medical insurance costs instantly using Machine Learning
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Sidebar
# =========================

st.sidebar.title("🏥 About")

st.sidebar.markdown("""
### Healthcare Insurance Cost Predictor

This application predicts **medical insurance costs**
using a trained **Random Forest Regression Model**.

---

### 📊 Model Information

- 🤖 Model : Random Forest
- 📈 R² Score : **0.9984**
- ⚙️ Framework : Streamlit

---

### 👨‍💻 Developer

**Siva**

AI & Data Science Student
""")

st.sidebar.markdown("---")

st.sidebar.markdown(
    "[🌐 GitHub Repository](https://github.com/siva252005/Healthcare-Insurance-Cost-Prediction)"
)

# ---------------------------------
# Load Model
# ---------------------------------
try:
    model, preprocessor = load_model()
    st.toast("✅ Machine Learning Model Loaded Successfully")
except Exception as e:
    st.error(f"Error Loading Model: {e}")
    st.stop()

# ---------------------------------
# Customer Details
# ---------------------------------

st.markdown("## 📝 Enter Customer Details")

st.write(
    "Fill in all the details below to estimate the annual healthcare insurance cost."
)

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

if st.button("🚀 Predict Insurance Cost", use_container_width=True):

    try:

        with st.spinner("🤖 Predicting Insurance Cost..."):

            processed_data = preprocessor.transform(input_df)

            prediction = model.predict(processed_data)

        predicted_cost = prediction[0]

        st.success("✅ Prediction Generated Successfully!")

        st.markdown("## 🎯 Prediction Result")

        # Risk Level
        if predicted_cost < 20000:
            risk = "🟢 Low Risk"
            risk_color = "#16a34a"
        elif predicted_cost < 50000:
            risk = "🟡 Medium Risk"
            risk_color = "#ca8a04"
        else:
            risk = "🔴 High Risk"
            risk_color = "#dc2626"

        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            color: white;
            margin-top: 15px;
            margin-bottom: 15px;
        ">
            <p style="font-size:18px; margin:0; opacity:0.9;">💰 Estimated Annual Cost</p>
            <h1 style="margin:10px 0; font-size:42px;">₹ {predicted_cost:,.2f}</h1>
            <p style="
                display:inline-block;
                background-color:{risk_color};
                padding:6px 18px;
                border-radius:20px;
                font-size:16px;
                margin-top:10px;
            ">{risk}</p>
        </div>
        """, unsafe_allow_html=True)

        st.caption(
            "⚠️ This prediction is generated using a machine learning model trained on historical insurance data. It is intended for educational purposes and should not be treated as an actual insurance quote."
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")

# ---------------------------------
# Footer
# ---------------------------------
st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; color:gray;'>
        Developed with ❤️ by <b>Siva</b><br>
        Healthcare Insurance Cost Prediction using Machine Learning
    </div>
    """,
    unsafe_allow_html=True,
)