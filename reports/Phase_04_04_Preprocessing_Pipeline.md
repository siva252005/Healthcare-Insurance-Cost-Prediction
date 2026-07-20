# Phase 04.4 – Build the Preprocessing Pipeline

## Objective

The objective of this phase is to build a preprocessing pipeline that automatically prepares numerical and categorical features for machine learning.

---

# Components Used

## Numerical Pipeline

- StandardScaler

Purpose:
- Standardizes numerical features to improve model performance.

---

## Categorical Pipeline

- OneHotEncoder

Purpose:
- Converts categorical variables into numerical format.
- Handles unseen categories during prediction.

---

## ColumnTransformer

The numerical and categorical pipelines are combined using `ColumnTransformer`, allowing different preprocessing techniques to be applied to different feature types.

---

# Processing Steps

1. Imported preprocessing libraries.
2. Created a numerical pipeline using `StandardScaler`.
3. Created a categorical pipeline using `OneHotEncoder`.
4. Combined both pipelines with `ColumnTransformer`.
5. Applied the pipeline to the feature dataset using `fit_transform()`.

---

# Output

| Property | Value |
|----------|-------|
| Original Features | 52 |
| Processed Features | *(Output from X_processed.shape)* |

---

# Benefits

- Ensures consistent preprocessing.
- Prevents data leakage.
- Simplifies model training and prediction.
- Creates a reusable preprocessing workflow.

---

# Conclusion

A reusable preprocessing pipeline has been successfully created. The transformed dataset is now ready for train-test splitting and machine learning model training.