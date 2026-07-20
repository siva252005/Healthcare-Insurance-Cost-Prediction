# Phase 05.3 – Random Forest Regressor

## Objective

Train a Random Forest Regressor to predict annual medical cost and compare its performance with the previously trained Linear Regression and Decision Tree models.

---

## Model

- **Algorithm:** Random Forest Regressor
- **Problem Type:** Regression
- **Number of Trees:** 100
- **Random State:** 42

---

## Training Steps

1. Imported the `RandomForestRegressor` from Scikit-learn.
2. Created the model with 100 decision trees.
3. Trained the model using the processed training dataset.
4. Generated predictions on the testing dataset.
5. Evaluated the model using regression metrics.

---

## Evaluation Metrics

| Metric | Value |
|---------|-------:|
| MAE | **7.67** |
| MSE | **16,036.08** |
| RMSE | **126.63** |
| R² Score | **0.9984** |

---

## Actual vs Predicted (Sample)

| Actual | Predicted |
|---------:|----------:|
| 1640.86 | 1641.09 |
| 2306.61 | 2307.33 |
| 1015.03 | 1015.21 |
| 1136.82 | 1135.86 |
| 3990.84 | 4003.85 |

---

## Residual Analysis

Residual = Actual − Predicted

| Actual | Predicted | Residual |
|---------:|----------:|---------:|
| 1640.86 | 1641.09 | -0.23 |
| 2306.61 | 2307.33 | -0.72 |
| 1015.03 | 1015.21 | -0.18 |
| 1136.82 | 1135.86 | 0.96 |
| 3990.84 | 4003.85 | -13.01 |

---

## Interpretation

- The Random Forest Regressor achieved an **R² Score of 99.84%**, indicating that it explains almost all the variation in annual medical costs.
- The **MAE of 7.67** shows that the average prediction error is very small.
- The **RMSE of 126.63** indicates that prediction errors are low and the model makes highly accurate predictions.
- The predicted values are extremely close to the actual values, with only minor residuals for most observations.
- Compared to the previous models, Random Forest produced the lowest prediction errors and the highest accuracy.

---

## Model Comparison

| Model | MAE | RMSE | R² Score |
|--------|----:|------:|---------:|
| Linear Regression | 319.91 | 574.87 | 0.9664 |
| Decision Tree | 8.48 | 144.26 | 0.9979 |
| **Random Forest** | **7.67** | **126.63** | **0.9984** |

---

## Conclusion

The Random Forest Regressor outperformed both the Linear Regression and Decision Tree models. It achieved the lowest prediction error and the highest R² Score, making it the best-performing model so far for predicting annual medical costs. This model will be compared with Gradient Boosting and Extra Trees Regressor in the next phases before selecting the final model for hyperparameter tuning and deployment.