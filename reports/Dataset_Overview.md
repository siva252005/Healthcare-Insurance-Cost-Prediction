# Phase 03.1 – Dataset Overview Report

## Objective

The objective of this phase is to perform an initial exploration of the dataset before conducting detailed exploratory data analysis (EDA).

---

# Dataset Summary

| Property | Value |
|-----------|-------|
| Total Records | 100,000 |
| Total Features | 54 |
| Missing Values | 0 |
| Duplicate Records | 0 |
| Target Variable | annual_medical_cost |
| Machine Learning Problem | Regression |

---

# Key Observations

## Dataset Size

- Large dataset containing 100,000 records.
- Suitable for Machine Learning.

---

## Missing Values

No missing values are present.

Result:

0 Missing Values

---

## Duplicate Records

No duplicate records were found.

Duplicate Rows = 0

---

## Numerical Features

The dataset contains several numerical healthcare attributes including:

- Age
- BMI
- Income
- Blood Pressure
- LDL
- HbA1c
- Risk Score
- Claims Information
- Medical Cost

---

## Categorical Features

The dataset contains categorical healthcare attributes including:

- Gender
- Region
- Smoking Status
- Education
- Employment Status
- Plan Type
- Network Tier

---

## Target Variable

annual_medical_cost

The objective of the project is to predict annual medical expenses.

---

# Initial Insights

- person_id is an identifier and will be removed before model training.
- The dataset contains a mix of continuous, categorical, binary, and count-based variables.
- No preprocessing is required for missing values or duplicate records.
- Several medical variables such as Risk Score, Claims Count, Chronic Diseases, and Blood Pressure are expected to have a significant impact on medical costs.

---

# Next Phase

Phase 03.2

Univariate Analysis

The next phase focuses on understanding the distribution of each feature individually and identifying possible outliers.