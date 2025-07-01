# Credit Risk Modeling Project

## Overview

You are an Analytics Engineer at Bati Bank, a leading financial service provider with over 10 years of experience. Bati Bank is partnering with an upcoming successful eCommerce company to enable a buy-now-pay-later service, providing customers with the ability to buy products by credit if they qualify.

This project focuses on building a Credit Scoring Model using transactional data to predict the likelihood of a customer defaulting on their loan.

---

## Business Understanding

Credit scoring assigns a quantitative measure estimating the risk of default by potential borrowers. This model will help Bati Bank make informed decisions about loan approvals.

### Basel II Accord

The Basel II Capital Accord emphasizes risk measurement and management, requiring financial institutions to use interpretable and well-documented models for credit risk to ensure regulatory compliance and capital adequacy.

### Proxy Target Variable

Because the dataset lacks a direct "default" label, we engineered a proxy variable `is_high_risk` to categorize users as high risk (likely to default) or low risk. This proxy carries potential business risks if the assumptions behind it do not perfectly map to actual defaults, but it enables supervised learning in the absence of explicit labels.

### Model Complexity Trade-offs

- **Simple Models (Logistic Regression with WoE):** Highly interpretable, easier to audit and explain, favored in regulated environments.
- **Complex Models (Gradient Boosting, Random Forest):** Often more accurate but can be opaque ("black-box"), posing challenges for interpretability and compliance.

---

## Data and Features

- **TransactionId:** Unique transaction identifier.
- **BatchId:** Batch number for transaction processing.
- **AccountId:** Customer account number.
- **SubscriptionId:** Customer subscription ID.
- **CustomerId:** Unique customer identifier.
- **CurrencyCode, CountryCode:** Currency and country info.
- **ProviderId, ProductId, ProductCategory:** Source and type of purchase.
- **ChannelId:** Channel used for transaction (web, Android, etc.).
- **Amount, Value:** Transaction amounts.
- **TransactionStartTime:** Timestamp.
- **PricingStrategy:** Merchant pricing category.
- **FraudResult:** Fraud status indicator.

---

## Project Structure

credit-risk-model/

├── .github/workflows/ci.yml # GitHub Actions CI/CD pipeline

├── data/ # Data (add to .gitignore)

│ ├── raw/ # Raw data

│ └── processed/ # Processed data

├── notebooks/

│ └── 1.0-eda.ipynb # Exploratory Data Analysis notebook

├── src/

│ ├── init.py

│ ├── data_processing.py # Feature engineering script

│ ├── train.py # Model training script

│ ├── predict.py # Inference script

│ └── api/

│ ├── main.py # FastAPI app

│ └── pydantic_models.py # Pydantic models for request/response validation

├── tests/

│ └── test_data_processing.py # Unit tests for helper functions

├── Dockerfile # Container setup

├── docker-compose.yml # Docker Compose file

├── requirements.txt # Python dependencies

├── .gitignore

└── README.md # Project documentation (this file)

---

## Task Breakdown

### Task 1 - Understanding Credit Risk

- Read key references on credit risk and Basel II.
- Document business understanding, proxy target rationale, and model trade-offs.

### Task 2 - Exploratory Data Analysis (EDA)

- Explore dataset structure, summary statistics, distributions.
- Identify missing values and outliers.
- Summarize top 3-5 insights.

### Task 3 - Feature Engineering

- Automate data processing using sklearn pipelines.
- Create aggregate features (e.g., total transaction amount).
- Extract temporal features.
- Encode categorical variables.
- Handle missing values.
- Normalize and standardize features.

### Task 4 - Proxy Target Variable Engineering

- Calculate Recency, Frequency, Monetary (RFM) metrics per customer.
- Use K-Means clustering to segment customers.
- Identify and label the high-risk cluster (`is_high_risk`).
- Merge the label into the processed dataset.

### Task 5 - Model Training and Tracking

- Split data into train/test sets.
- Train and tune at least two models (e.g., Logistic Regression, Random Forest).
- Evaluate with metrics: Accuracy, Precision, Recall, F1, ROC-AUC.
- Track experiments and models using MLflow.
- Register the best model in the MLflow Model Registry.
- Write unit tests for helper functions.

### Task 6 - Model Deployment and Continuous Integration

- Build a FastAPI REST API to serve the model.
- Use Pydantic models for input/output validation.
- Load the best model from MLflow registry.
- Create `/predict` endpoint accepting new customer data and returning risk probability.
- Containerize the API with Docker and Docker Compose.
- Set up GitHub Actions for CI/CD:
  - Run linter (flake8).
  - Run unit tests (pytest).
  - Fail build on errors.

---

## Usage

### Clone the Repository

```bash
git clone https://github.com/Dagi2730/credit-risk-model.git
cd credit-risk-model
Setup Environment and Install Dependencies
```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
Run the API Locally

uvicorn src.api.main:app --reload
Access the API Documentation
Open your browser and navigate to:

http://127.0.0.1:8000/docs#/default/predict_risk_predict_post

This interactive Swagger UI lets you test the /predict endpoint by sending JSON requests matching the expected input schema.

Example input JSON:

{
  "CountryCode": 123,
  "Amount": 2500.75,
  "Value": 2500.75,
  "PricingStrategy": 2,
  "FraudResult": 0
}
Example successful response:

{
  "risk_probability": 0.85
}
Docker Deployment

Build and run the Docker container:

docker-compose build

docker-compose up

The API will be available at http://localhost:8000 with the same Swagger UI for testing.

Testing and CI/CD

Run unit tests with:

pytest

Run code linting with:

flake8 src tests

GitHub Actions automates these checks on every push to the main branch using .github/workflows/ci.yml.

References

Basel II Capital Accord and Credit Risk:

Basel II Summary

Credit Scoring Approaches

Credit Risk Tutorial
