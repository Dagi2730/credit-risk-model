from fastapi import FastAPI, HTTPException
from src.api.pydantic_models import CustomerFeatures, RiskPredictionResponse
import mlflow.pyfunc
from mlflow.exceptions import MlflowException

app = FastAPI(title="Credit Risk Prediction API")

MODEL_NAME = "CreditRiskRandomForestModel"  # your MLflow registered model name
STAGE = "Production"  # model stage to load

try:
    model = mlflow.pyfunc.load_model(f"models:/{MODEL_NAME}/{STAGE}")
except MlflowException as e:
    # Model or stage not found in MLflow registry
    raise RuntimeError(f"Failed to load model from MLflow registry: {e}")

@app.get("/")
async def root():
    return {"message": "Credit Risk Prediction API is live!"}

@app.post("/predict", response_model=RiskPredictionResponse)
async def predict_risk(customer: CustomerFeatures):
    # Prepare input data as a DataFrame (MLflow pyfunc models expect DataFrame)
    import pandas as pd

    input_df = pd.DataFrame([customer.dict()])

    # Predict risk probability (assuming model.predict returns probabilities or scores)
    # If your model.predict returns class labels, you need to adapt this accordingly.
    try:
        risk_prob = model.predict(input_df)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model prediction error: {e}")

    # Ensure the risk probability is between 0 and 1
    if not (0.0 <= risk_prob <= 1.0):
        risk_prob = max(0.0, min(1.0, risk_prob))

    return RiskPredictionResponse(risk_probability=risk_prob)
