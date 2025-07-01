from mlflow.tracking import MlflowClient

client = MlflowClient()
model_name = "CreditRiskRandomForestModel"
version = 1  # Replace with your actual model version number

client.transition_model_version_stage(
    name=model_name,
    version=version,
    stage="Production",
    archive_existing_versions=True
)

print(f"Model {model_name} version {version} set to Production stage.")
