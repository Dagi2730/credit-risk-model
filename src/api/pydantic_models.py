from pydantic import BaseModel, Field

class CustomerFeatures(BaseModel):
    CountryCode: int = Field(..., example=123)
    Amount: float = Field(..., example=2500.75)
    Value: float = Field(..., example=2500.75)
    PricingStrategy: int = Field(..., example=2)
    FraudResult: int = Field(..., example=0)

class RiskPredictionResponse(BaseModel):
    risk_probability: float = Field(..., ge=0.0, le=1.0, example=0.85)
