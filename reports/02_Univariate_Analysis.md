# Phase 03.2 – Univariate Analysis Report

## Objective

The objective of this phase is to analyze each feature individually to understand its distribution, identify outliers, and detect any issues before preprocessing and model building.

---

# Summary of Findings

## Annual Medical Cost

- The target variable is right-skewed.
- Most individuals have relatively low medical costs.
- A small number of individuals have very high medical expenses.

Observation:
A log transformation may be considered if skewness affects model performance.

---

## Medical Cost Outliers

- Several high-cost outliers were identified.
- These likely represent genuine high-expense medical cases.

Observation:
Outliers should be retained unless further analysis suggests they are data errors.

---

## Age

- Age follows an approximately normal distribution.
- Most individuals are between 35 and 60 years old.

Observation:
No transformation is currently required.

---

## BMI

- BMI values are centered around 27.
- Most individuals fall within a healthy to overweight BMI range.

Observation:
Only extreme BMI values should be reviewed.

---

## Income

- Income distribution is positively skewed.
- Most individuals have moderate incomes.

Observation:
Feature scaling or transformation may be useful.

---

## Smoking Status

- Non-smokers form the majority of the dataset.
- Current smokers represent the smallest group.

Observation:
Categorical encoding will be required.

---

## Gender

- Male and Female categories are well balanced.
- Very few records belong to the Other category.

Observation:
Encoding will be applied during preprocessing.

---

## Region

- Regional distribution is reasonably balanced.
- South contains the largest number of observations.

Observation:
One-Hot Encoding can be used.

---

## Correlation Heatmap

- Most numerical features show weak correlation.
- Some medical variables appear moderately correlated.

Observation:
A detailed correlation analysis with the target variable will be performed during bivariate analysis.

---

# Conclusion

The dataset is clean and suitable for machine learning.

Key observations:

- No missing values
- No duplicate records
- Presence of target outliers
- Right-skewed numerical variables
- Multiple categorical variables requiring encoding

The dataset is now ready for Bivariate Analysis.