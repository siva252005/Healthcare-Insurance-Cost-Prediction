# Phase 03.4 – Multivariate Analysis Report

## Objective

The objective of this phase is to analyze the combined effect of multiple features on the target variable (annual_medical_cost). This helps identify interactions between variables that may improve machine learning model performance.

---

# Key Findings

## Age and Smoking Status

- Older individuals who are current smokers incur the highest medical costs.
- Age and smoking together have a stronger influence than age alone.

Observation:
Combining these features may improve prediction accuracy.

---

## BMI and Smoking Status

- Individuals with higher BMI who are current smokers tend to have significantly higher medical costs.
- Smoking amplifies the effect of BMI on healthcare expenses.

Observation:
BMI and smoking together form an important feature combination.

---

## Risk Score by Smoking Status

- Current smokers generally have higher risk scores than non-smokers.
- Higher risk scores correspond to increased medical costs.

Observation:
Risk Score and Smoking Status are strong predictors when used together.

---

## Region and Smoking Status

- Current smokers consistently show higher medical costs in every region.
- Regional differences are smaller than the impact of smoking.

Observation:
Smoking status has a greater influence than geographical region.

---

## Correlation Analysis

Strongly correlated features include:

- Annual Premium
- Monthly Premium
- Total Claims Paid
- Risk Score

Observation:
These variables are likely to contribute significantly to prediction accuracy.

---

## Pair Plot Analysis

- Positive relationships are visible among important numerical variables.
- Risk Score has the strongest relationship with Annual Medical Cost.

Observation:
The selected features are suitable for machine learning.

---

# Conclusion

Multivariate analysis confirms that combinations of Age, BMI, Smoking Status, Risk Score, Premium, and Claims Information provide valuable predictive information.

These interactions will be useful during feature engineering and machine learning model development.