# Phase 04.3 – Identify Numerical and Categorical Features

## Objective

The objective of this phase is to classify the input features into numerical and categorical variables. This classification helps apply appropriate preprocessing techniques before training machine learning models.

---

# Numerical Features

Numerical features consist of integer and floating-point variables.

These features will later be scaled using StandardScaler.

Example:

- age
- bmi
- income
- annual_premium
- monthly_premium
- claims_count
- risk_score

---

# Categorical Features

Categorical features contain text-based or category values.

These features will later be converted into numerical format using OneHotEncoder.

Example:

- gender
- smoking_status
- region
- plan_type
- network_tier

---

# Processing Steps

1. Loaded the feature dataset (X).
2. Identified numerical columns using `select_dtypes()`.
3. Identified categorical columns using `select_dtypes()`.
4. Verified that all features were classified correctly.

---

# Summary

| Category | Count |
|----------|------:|
| Numerical Features | *(your output)* |
| Categorical Features | *(your output)* |
| Total Features | 52 |

---

# Python Code

```python
numerical_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

categorical_features = X.select_dtypes(include=["object", "category"]).columns.tolist()
```

---

# Conclusion

The feature set has been successfully divided into numerical and categorical variables. This prepares the dataset for building a preprocessing pipeline using StandardScaler and OneHotEncoder.