# Phase 05.5 – Extra Trees Regressor

## Objective

Train an Extra Trees Regressor to predict annual medical cost and compare its performance with the previously trained regression models.

---

## Model

- **Algorithm:** Extra Trees Regressor
- **Problem Type:** Regression
- **Number of Trees:** 100
- **Random State:** 42

---

## Training Steps

1. Imported the `ExtraTreesRegressor` from Scikit-learn.
2. Created the model with 100 decision trees.
3. Trained the model using the processed training dataset.
4. Generated predictions on the testing dataset.
5. Evaluated the model using regression metrics.

---

## Evaluation Metrics

| Metric | Value |
|---------|-------:|
| MAE | **6.33** |
| MSE | **22,619.44** |
| RMSE | **150.40** |
| R² Score | **0.9977** |

---

## Actual vs Predicted (Sample)

| Actual | Predicted |
|---------:|----------:|
| 1640.86 | 1640.98 |
| 2306.61 | 2306.95 |
| 1015.03 | 1014.87 |
| 1136.82 | 1136.67 |
| 3990.84 | 3991.13 |

---

## Residual Analysis

Residual = Actual − Predicted

| Actual | Predicted | Residual |
|---------:|----------:|---------:|
| 1640.86 | 1640.98 | -0.12 |
| 2306.61 | 2306.95 | -0.34 |
| 1015.03 | 1014.87 | 0.16 |
| 1136.82 | 1136.67 | 0.15 |
| 3990.84 | 3991.13 | -0.29 |

---

## Interpretation

- The **Extra Trees Regressor** achieved an **R² Score of 0.9977**, indicating that it explains **99.77%** of the variation in annual medical costs.
- The **MAE of 6.33** is the **lowest among all the models**, showing that the average prediction error is extremely small.
- The **RMSE of 150.40** is slightly higher than Random Forest and Gradient Boosting, indicating that although the average error is very low, a few larger prediction errors increase the RMSE.
- The predicted values closely match the actual values, and the residuals are very close to zero for most observations.
- Overall, the model demonstrates excellent predictive performance and is highly suitable for this regression task.

---

## Model Comparison

| Model | MAE | RMSE | R² Score |
|--------|----:|------:|---------:|
| Linear Regression | 319.91 | 574.87 | 0.9664 |
| Decision Tree | 8.48 | 144.26 | 0.9979 |
| Random Forest | 7.67 | **126.63** | **0.9984** |
| Gradient Boosting | 54.31 | 127.18 | **0.9984** |
| **Extra Trees** | **6.33** | 150.40 | 0.9977 |

---

## Conclusion

The Extra Trees Regressor achieved outstanding predictive performance with the **lowest Mean Absolute Error (MAE)** among all the evaluated models. Although its RMSE is slightly higher than Random Forest, its predictions remain highly accurate, and the model explains **99.77%** of the variance in annual medical costs. Extra Trees is one of the strongest models in this project and will be included in the final comparison before selecting the best model for deployment.