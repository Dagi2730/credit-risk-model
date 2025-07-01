import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import mlflow
import mlflow.sklearn
import numpy as np
from mlflow.tracking import MlflowClient

def load_data():
    df = pd.read_csv('data/processed/raw_with_high_risk_label.csv')
    return df

def preprocess_data(df):
    # Drop ID and target columns
    X = df.drop(['CustomerId', 'is_high_risk'], axis=1)
    # Keep only numeric features (drop non-numeric)
    X = X.select_dtypes(include=['number'])
    y = df['is_high_risk']
    return X, y

def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

def evaluate_model(y_true, y_pred, y_prob):
    print(f"Accuracy:  {accuracy_score(y_true, y_pred):.4f}")
    print(f"Precision: {precision_score(y_true, y_pred, zero_division=0):.4f}")
    print(f"Recall:    {recall_score(y_true, y_pred, zero_division=0):.4f}")
    print(f"F1 Score:  {f1_score(y_true, y_pred, zero_division=0):.4f}")
    print(f"ROC-AUC:   {roc_auc_score(y_true, y_prob):.4f}")

def register_best_model(run_id, model_name="CreditRiskRandomForestModel"):
    client = MlflowClient()
    model_uri = f"runs:/{run_id}/RandomForest"
    print(f"Registering model {model_name} from {model_uri}")
    # Create registered model only if it does not exist (handle exception)
    try:
        client.create_registered_model(model_name)
        print(f"Registered model name: {model_name}")
    except Exception as e:
        print(f"Model {model_name} probably already exists: {str(e)}")
    # Create model version
    client.create_model_version(name=model_name, source=model_uri, run_id=run_id)
    print(f"Model version created for run {run_id}")

def train_and_evaluate():
    df = load_data()
    X, y = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_data(X, y)

    print("Class distribution in training set:")
    print(y_train.value_counts(normalize=True))

    mlflow.set_experiment("Credit Risk Modeling")

    models = {
        "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced'),
        "RandomForest": RandomForestClassifier(random_state=42, class_weight='balanced')
    }

    param_distributions = {
        "LogisticRegression": {
            "C": np.logspace(-4, 4, 20),
            "penalty": ["l2"],
            "solver": ["lbfgs"],
            "class_weight": ["balanced"]
        },
        "RandomForest": {
            "n_estimators": [100, 200, 300],
            "max_depth": [None, 10, 20, 30],
            "min_samples_split": [2, 5, 10],
            "class_weight": ["balanced"]
        }
    }

    for name, model in models.items():
        print(f"\nStarting hyperparameter tuning for {name}...")

        search = RandomizedSearchCV(
            estimator=model,
            param_distributions=param_distributions[name],
            n_iter=10,
            scoring='roc_auc',
            cv=5,
            verbose=1,
            random_state=42,
            n_jobs=-1
        )

        with mlflow.start_run(run_name=name) as run:
            search.fit(X_train, y_train)
            best_model = search.best_estimator_
            print(f"Best params for {name}: {search.best_params_}")

            y_pred = best_model.predict(X_test)
            y_prob = best_model.predict_proba(X_test)[:, 1]

            print(f"\nModel evaluation for {name} with best hyperparameters:")
            evaluate_model(y_test, y_pred, y_prob)

            mlflow.sklearn.log_model(best_model, name)
            mlflow.log_params(search.best_params_)
            mlflow.log_metrics({
                "accuracy": accuracy_score(y_test, y_pred),
                "precision": precision_score(y_test, y_pred, zero_division=0),
                "recall": recall_score(y_test, y_pred, zero_division=0),
                "f1_score": f1_score(y_test, y_pred, zero_division=0),
                "roc_auc": roc_auc_score(y_test, y_prob),
            })

            # Register best RandomForest model in MLflow Model Registry
            if name == "RandomForest":
                register_best_model(run.info.run_id)

if __name__ == "__main__":
    train_and_evaluate()
