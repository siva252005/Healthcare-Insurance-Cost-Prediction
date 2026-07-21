"""
config.py

Stores all dropdown options and helper functions
used throughout the Healthcare Insurance Cost
Prediction application.
"""

# =====================================================
# PERSONAL INFORMATION
# =====================================================

GENDER = [
    "Male",
    "Female"
]

REGIONS = [
    "North",
    "South",
    "East",
    "West"
]

AREA = [
    "Urban",
    "Rural"
]

EDUCATION = [
    "High School",
    "Bachelor's Degree",
    "Master's Degree",
    "PhD"
]

MARITAL_STATUS = [
    "Single",
    "Married",
    "Divorced"
]

EMPLOYMENT = [
    "Employed",
    "Self-employed",
    "Unemployed",
    "Retired"
]

# =====================================================
# LIFESTYLE INFORMATION
# =====================================================

SMOKER = [
    "Yes",
    "No"
]

ALCOHOL = [
    "Never",
    "Occasionally",
    "Weekly",
    "Daily"
]

# =====================================================
# BINARY OPTIONS
# =====================================================

YES_NO = [0, 1]


def yes_no_label(value):
    """
    Convert binary values into readable labels.

    Parameters
    ----------
    value : int
        0 -> No
        1 -> Yes

    Returns
    -------
    str
        "Yes" or "No"
    """
    return "Yes" if value == 1 else "No"