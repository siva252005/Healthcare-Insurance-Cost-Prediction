# Phase 04.2 – Feature and Target Separation

## Objective

Separate the dataset into input features (X) and target variable (y) before applying preprocessing and machine learning algorithms.

---

# Target Variable

annual_medical_cost

This is the variable the machine learning model will predict.

---

# Feature Variables

All remaining columns except annual_medical_cost are used as input features.

---

# Dataset Shape

| Dataset | Shape |
|----------|-------|
| Features (X) | (100000, 52) |
| Target (y) | (100000,) |

---

# Conclusion

The dataset has been successfully divided into input features and the target variable, making it ready for preprocessing and train-test splitting.