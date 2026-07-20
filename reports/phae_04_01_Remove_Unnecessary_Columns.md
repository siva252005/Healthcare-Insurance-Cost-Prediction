# Phase 04.1 – Remove Unnecessary Columns

## Objective

The objective of this phase is to remove columns that do not contribute to the machine learning model. These columns contain identification information rather than meaningful patterns, so removing them helps improve model quality and reduces unnecessary complexity.

---

# Removed Column

## person_id

### Reason for Removal

The `person_id` column is a unique identifier assigned to each individual in the dataset. Since every value is unique, it does not provide any useful information for predicting the target variable (`annual_medical_cost`).

Including this column may introduce unnecessary noise into the model and negatively affect its learning process.

---

# Dataset Summary

| Property | Before | After |
|----------|-------:|------:|
| Total Rows | 100,000 | 100,000 |
| Total Columns | 54 | 53 |
| Removed Columns | 0 | 1 |

---

# Processing Steps

1. Loaded the processed healthcare insurance dataset.
2. Identified the non-predictive identifier column (`person_id`).
3. Removed the `person_id` column using Pandas.
4. Verified that the dataset now contains 53 columns.
5. Saved the updated dataset as:

```
data/processed/medical_insurance_processed.csv
```

---

# Python Code

```python
df = df.drop(columns=["person_id"])

df.to_csv(
    "../data/processed/medical_insurance_processed.csv",
    index=False
)
```

---

# Output

```
Original Shape : (100000, 54)

Updated Shape : (100000, 53)
```

---

# Key Observation

- `person_id` is a unique identifier and has no predictive value.
- Removing it reduces unnecessary information without affecting the target variable.
- All remaining columns are relevant for further preprocessing and model development.

---

# Conclusion

The dataset has been successfully cleaned by removing the non-predictive `person_id` column. The processed dataset now contains **53 useful features** and is ready for feature-target separation and further preprocessing.

---

# Next Phase

**Phase 04.2 – Feature and Target Separation**

In the next phase, the dataset will be divided into:

- **Features (X):** Independent variables used for prediction.
- **Target (y):** `annual_medical_cost`, the variable to be predicted.

This prepares the dataset for preprocessing, train-test splitting, and machine learning model development.