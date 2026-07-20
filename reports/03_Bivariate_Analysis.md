# Phase 03.3 – Bivariate Analysis Report

## Objective

The objective of this phase is to analyze the relationship between independent variables and the target variable (annual_medical_cost). This helps identify the most influential features for prediction and provides business insights.

---

# Key Findings

## Age vs Medical Cost

- Medical cost generally increases with age.
- Older individuals tend to have higher healthcare expenses.

Observation:
Age is a useful predictor of medical cost.

---

## BMI vs Medical Cost

- Individuals with higher BMI generally incur higher medical costs.
- A positive relationship exists between BMI and medical expenses.

Observation:
BMI is an important feature for model training.

---

## Income vs Medical Cost

- Income shows only a weak relationship with medical cost.
- High-income individuals do not necessarily have higher medical expenses.

Observation:
Income alone is not a strong predictor.

---

## Smoking Status vs Medical Cost

- Current smokers have the highest medical costs.
- Non-smokers generally incur lower medical expenses.

Observation:
Smoking status is a significant predictor and should be encoded during preprocessing.

---

## Gender vs Medical Cost

- Medical costs are similar across Male and Female groups.
- Gender has minimal influence on healthcare expenses.

Observation:
Gender contributes limited predictive value.

---

## Region vs Medical Cost

- The South region has a slightly higher median medical cost.
- Differences among regions are relatively small.

Observation:
Region may provide moderate predictive information after encoding.

---

## Risk Score vs Medical Cost

- Medical cost increases as the risk score increases.
- A strong positive relationship exists.

Observation:
Risk Score is one of the most influential predictors.

---

## Correlation Analysis

Top correlated features with annual_medical_cost:

- Monthly Premium
- Annual Premium
- Risk Score
- Total Claims Paid

Observation:
These features are expected to contribute significantly to model performance.

---

# Conclusion

The analysis indicates that Age, BMI, Smoking Status, Risk Score, Annual Premium, Monthly Premium, and Total Claims Paid have the strongest influence on annual medical cost.

These findings will guide feature selection, preprocessing, and machine learning model development in the next phases.