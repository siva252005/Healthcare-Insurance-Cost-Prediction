# Phase 04.5 – Train-Test Split & Apply Preprocessing

## Objective

The objective of this phase is to split the dataset into training and testing sets and apply the preprocessing pipeline before machine learning model training.

---

## Train-Test Split

The dataset was divided into:

- Training Data: 80%
- Testing Data: 20%

Random State: 42

---

## Processing Steps

1. Split the dataset into training and testing sets.
2. Fitted the preprocessing pipeline using the training dataset.
3. Applied the same preprocessing to the testing dataset.
4. Verified the shapes of the processed datasets.

---

## Dataset Shapes

| Dataset | Shape |
|---------|-------|
| X Train | *(your output)* |
| X Test | *(your output)* |
| y Train | *(your output)* |
| y Test | *(your output)* |
| Processed X Train | *(your output)* |
| Processed X Test | *(your output)* |

---

## Why Fit Only on Training Data?

The preprocessing pipeline is fitted only on the training data to prevent data leakage. The testing data is transformed using the same learned parameters, ensuring a fair evaluation of the machine learning model.

---

## Conclusion

The dataset has been successfully split and preprocessed. It is now ready for training and evaluating machine learning regression models.