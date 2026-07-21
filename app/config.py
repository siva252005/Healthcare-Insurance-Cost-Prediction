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
    "Bachelor",
    "Master",
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
# Binary options
YES_NO = [0, 1]

def yes_no_label(value):
    return "Yes" if value == 1 else "No"