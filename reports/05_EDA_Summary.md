# Phase 03.5 – Exploratory Data Analysis Summary

## Objective

The objective of this phase is to summarize the insights obtained from Exploratory Data Analysis (EDA) and identify the preprocessing steps required before building machine learning models.

---

# Dataset Overview

| Property | Value |
|----------|-------|
| Total Records | 100,000 |
| Total Features | 54 |
| Missing Values | 0 |
| Duplicate Records | 0 |
| Target Variable | annual_medical_cost |
| Machine Learning Problem | Regression |

---

# Key Findings

## Dataset Quality

- No missing values were found.
- No duplicate records were identified.
- Dataset is clean and suitable for machine learning.

---

## Target Variable

- annual_medical_cost is positively skewed.
- Several high-cost outliers are present.
- Outliers represent genuine medical cases and should not be removed without investigation.

---

## Important Numerical Features

The following numerical features showed a strong relationship with annual medical cost:

- Risk Score
- Annual Premium
- Monthly Premium
- Total Claims Paid
- BMI
- Age

---

## Important Categorical Features

The following categorical features significantly influence medical cost:

- Smoking Status
- Region
- Gender
- Plan Type
- Network Tier

---

## Feature Relationships

- Medical cost increases with age.
- Higher BMI is associated with higher medical expenses.
- Current smokers incur significantly higher medical costs.
- Higher Risk Score strongly increases medical cost.
- Premium and Claims variables are highly correlated with medical cost.

---

# Recommended Preprocessing Steps

- Remove identifier column (person_id).
- Encode categorical variables.
- Scale numerical variables where required.
- Split features and target variable.
- Perform train-test split.
- Build a preprocessing pipeline.

---

# Expected Important Features

- Risk Score
- Annual Premium
- Monthly Premium
- Total Claims Paid
- Age
- BMI
- Smoking Status
- Claims Count

---

# Conclusion

EDA confirms that the dataset is clean, well-structured, and suitable for regression modeling.

The identified relationships and feature importance will guide preprocessing, feature engineering, and machine learning model development.