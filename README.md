## 📌 Task 5 - Model Training and Tracking

In this task, we developed a structured model training pipeline that includes experiment tracking, hyperparameter tuning, model versioning, and performance evaluation.

### Approach:

1. **Data Splitting**  
   The processed dataset was split into training and testing sets with stratification on the `is_high_risk` label to preserve class distribution.

2. **Model Selection**  
   We trained and compared at least two classification models:  
   - Logistic Regression (with class balancing)  
   - Random Forest Classifier (with class balancing)

3. **Hyperparameter Tuning**  
   Hyperparameter optimization was performed using Grid Search with 5-fold cross-validation to identify the best parameter sets for each model.

4. **Model Evaluation**  
   Models were assessed on the test set using multiple metrics:  
   - Accuracy  
   - Precision  
   - Recall  
   - F1 Score  
   - ROC-AUC (Area Under the Receiver Operating Characteristic Curve)

5. **Experiment Tracking and Model Registry**  
   All training runs and metrics were logged to MLflow for experiment tracking. The best-performing Random Forest model was registered in the MLflow Model Registry for production deployment.

### Outcome:

- Logistic Regression showed high recall but poor precision, indicating many false positives.
- Random Forest achieved a better balance between precision and recall, with higher overall ROC-AUC.
- The registered model can be loaded for inference and further evaluation.

### Files updated:

- `src/train.py` — model training pipeline with hyperparameter tuning, evaluation, MLflow logging, and model registration.
- MLflow UI for visualizing experiments and metrics.
