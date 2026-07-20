# Phase 05.4 – Gradient Boosting Regressor

## Objective

Train a Gradient Boosting Regressor to predict annual medical cost and compare its performance with previously trained regression models.

---

## Model

- Algorithm: Gradient Boosting Regressor
- Problem Type: Regression
- Number of Estimators: 100
- Learning Rate: 0.1
- Maximum Tree Depth: 3
- Random State: 42

---

## Training Steps

1. Imported the GradientBoostingRegressor from Scikit-learn.
2. Configured the model with 100 estimators.
3. Trained the model using the processed training dataset.
4. Generated predictions on the testing dataset.
5. Evaluated the model using regression metrics.

---

## Evaluation Metrics

| Metric | Value |
|---------|-------:|
| MAE | 54.31 |
| MSE | 16,173.82 |
| RMSE | 127.18 |
| R² Score | 0.9984 |

---

## Interpretation

- The model achieved an R² Score of **99.84%**, indicating excellent predictive performance.
- The low RMSE shows that prediction errors are small.
- The model produces predictions that closely match the actual annual medical costs.
- Compared with previous models, Gradient Boosting performs very well, although Random Forest achieves slightly lower prediction errors.

---

## Conclusion

The Gradient Boosting Regressor is a high-performing regression model for predicting annual medical costs. It achieved excellent accuracy and will be included in the final comparison with all regression models before selecting the best model for deployment.