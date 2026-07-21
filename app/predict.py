"""
predict.py

Loads the trained Machine Learning model and preprocessing pipeline.
"""

import os
import joblib
import streamlit as st

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "random_forest_model.pkl"
)

PREPROCESSOR_PATH = os.path.join(
    BASE_DIR,
    "models",
    "preprocessor.pkl"
)

# =====================================================
# Load Model & Preprocessor
# =====================================================

@st.cache_resource
def load_model():
    """
    Load the trained Random Forest model and preprocessing pipeline.

    Returns
    -------
    tuple
        (model, preprocessor)
    """

    try:
        model = joblib.load(MODEL_PATH)
        preprocessor = joblib.load(PREPROCESSOR_PATH)

        return model, preprocessor

    except FileNotFoundError as e:
        raise FileNotFoundError(
            "Model or preprocessor file not found. "
            "Please check the models folder."
        ) from e

    except Exception as e:
        raise RuntimeError(
            f"Error loading model: {e}"
        ) from e