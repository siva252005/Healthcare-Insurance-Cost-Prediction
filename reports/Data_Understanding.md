# Phase 02 – Data Understanding Report

## Objective

The objective of this phase is to understand the dataset before performing any preprocessing or machine learning tasks.

A detailed analysis was carried out to identify the dataset structure, target variable, feature types, missing values, duplicate records, and the type of machine learning problem.

---

# Dataset Information

| Property | Value |
|----------|-------|
| Dataset Name | Medical Insurance Cost Prediction |
| Total Records | 100,000 |
| Total Features | 54 |
| Dataset Type | Structured Tabular Dataset |

---

# Target Variable

Target Variable:

annual_medical_cost

The objective of this project is to predict the annual medical cost of an individual using demographic, medical, lifestyle, and insurance-related features.

---

# Feature Classification

## Numerical Features

- person_id
- age
- income
- household_size
- dependents
- bmi
- visits_last_year
- hospitalizations_last_3yrs
- days_hospitalized_last_3yrs
- medication_count
- systolic_bp
- diastolic_bp
- ldl
- hba1c
- deductible
- copay
- policy_term_years
- policy_changes_last_2yrs
- provider_quality
- risk_score
- annual_medical_cost
- annual_premium
- monthly_premium
- claims_count
- avg_claim_amount
- total_claims_paid
- chronic_count
- hypertension
- diabetes
- asthma
- copd
- cardiovascular_disease
- cancer_history
- kidney_disease
- liver_disease
- arthritis
- mental_health
- proc_imaging_count
- proc_surgery_count
- proc_physio_count
- proc_consult_count
- proc_lab_count
- is_high_risk
- had_major_procedure

---

## Categorical Features

- sex
- region
- urban_rural
- education
- marital_status
- employment_status
- smoker
- alcohol_freq
- plan_type
- network_tier

---

# Missing Value Analysis

Result:

No missing values were found in the dataset.

Missing Values = 0

---

# Duplicate Analysis

Result:

No duplicate records were found.

Duplicate Records = 0

---

# Initial Observations

- Dataset contains a large number of records (100,000).
- Dataset is suitable for Machine Learning.
- No missing values.
- No duplicate records.
- Target variable is continuous.
- person_id is an identifier and will not be used for training.
- Dataset contains both numerical and categorical features.
- Multiple healthcare and insurance-related variables are available for prediction.

---

# Machine Learning Problem

Problem Type:

Regression

Reason:

The target variable (annual_medical_cost) is a continuous numerical value.

---

# Next Phase

Phase 03

Exploratory Data Analysis (EDA)

This phase focuses on understanding feature distributions, identifying outliers, and discovering relationships between variables before data preprocessing.