# Phase 06 – Hyperparameter Tuning

## Objective

The objective of this phase was to improve the performance of the selected Random Forest Regressor by optimizing its hyperparameters using **RandomizedSearchCV**. Hyperparameter tuning helps identify the best combination of model parameters to achieve better predictive performance.

---

## Hyperparameter Tuning Method

The Random Forest Regressor was optimized using **RandomizedSearchCV** with 5-fold cross-validation. Multiple combinations of hyperparameters were evaluated, and the model with the highest cross-validation score was selected.

### Hyperparameters Tuned

- Number of Trees (`n_estimators`)
- Maximum Depth (`max_depth`)
- Minimum Samples Split (`min_samples_split`)
- Minimum Samples Leaf (`min_samples_leaf`)
- Maximum Features (`max_features`)

---

## Best Hyperparameters

| Hyperparameter | Best Value |
|---------------|------------|
| n_estimators | 100 |
| max_depth | 30 |
| min_samples_split | 5 |
| min_samples_leaf | 1 |
| max_features | sqrt |

---

## Model Performance Comparison

| Model | MAE | RMSE | R² Score |
|--------|----:|------:|---------:|
| Random Forest | **7.67** | **126.63** | **0.9984** |
| Tuned Random Forest | **218.67** | **643.19** | **0.9580** |

---

## Analysis

### Original Random Forest

- Achieved excellent prediction accuracy.
- Produced a very low Mean Absolute Error (MAE) of **7.67**.
- Achieved a low Root Mean Squared Error (RMSE) of **126.63**.
- Obtained an outstanding R² Score of **0.9984**, explaining approximately **99.84%** of the variation in annual medical costs.

### Tuned Random Forest

- The tuning process selected a different combination of hyperparameters using RandomizedSearchCV.
- However, the tuned model showed lower performance on the unseen test dataset.
- MAE increased significantly from **7.67** to **218.67**.
- RMSE increased from **126.63** to **643.19**.
- R² Score decreased from **0.9984** to **0.9580**.

Although the tuned model achieved the highest score during cross-validation, it did not generalize better on the test dataset.

---

## Conclusion

Hyperparameter tuning was successfully performed using RandomizedSearchCV. However, the optimized model did not outperform the original Random Forest model on the test dataset.

Therefore, the **original Random Forest Regressor** was selected as the final model for this project because it achieved:

- Lowest prediction error (MAE)
- Lowest RMSE
- Highest R² Score
- Better overall generalization performance

The original Random Forest model was retained for deployment and future predictions.

---

## Final Model Selected

**Model:** Random Forest Regressor

### Final Performance

| Metric | Value |
|---------|------:|
| MAE | **7.67** |
| RMSE | **126.63** |
| R² Score | **0.9984** |

---

## Saved Model Files

```
models/
├── preprocessor.pkl
├── random_forest_model.pkl      ✅ Final Model
└── random_forest_tuned.pkl      (For experimental comparison)
```

---

## Key Takeaways

- Hyperparameter tuning does not always guarantee better performance.
- The default Random Forest model provided superior predictive accuracy for this dataset.
- Model selection should always be based on evaluation using an unseen test dataset rather than only cross-validation results.
- The original Random Forest Regressor was chosen as the final production model due to its excellent predictive performance.