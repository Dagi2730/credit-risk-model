## 📌 Task 6 - Model Deployment and Continuous Integration

In this task, we packaged the trained credit risk prediction model into a containerized REST API service and set up a CI/CD pipeline to automate code quality checks and testing. This enables easy deployment, scalability, and continuous integration to maintain high code standards.

---

### Objective:

- Serve the trained model via a FastAPI REST API.
- Containerize the API for consistent deployment environments.
- Automate testing and linting through GitHub Actions CI workflow.

---

### Approach:

1. **API Development:**
   - Built a REST API using FastAPI in `src/api/main.py`.
   - The API loads the best trained model directly from the MLflow Model Registry.
   - Created a `/predict` POST endpoint that accepts new customer data (validated with Pydantic models) and returns the predicted risk probability.
   - Defined request and response schemas in `src/api/pydantic_models.py` for strict input validation and clear API documentation.

2. **Containerization:**
   - Wrote a `Dockerfile` that sets up the environment, installs dependencies, and runs the FastAPI app using Uvicorn.
   - Created a `docker-compose.yml` file to easily build and run the API service with a single command.
   - This ensures the service runs consistently across different environments (local, staging, production).

3. **Continuous Integration (CI):**
   - Configured a GitHub Actions workflow in `.github/workflows/ci.yml`.
   - The workflow triggers on every push to the `main` branch.
   - It runs two key steps:
     - A **code linter** (`flake8`) to enforce code style and prevent style issues.
     - **Unit tests** execution with `pytest` to verify code correctness.
   - The build fails if any linting errors or failing tests are detected, ensuring code quality before merging.

---

### Outcome:

- The model is now accessible as a scalable API endpoint, facilitating integration with client applications or other services.
- Containerization guarantees environment reproducibility and ease of deployment.
- CI pipeline automates quality control, reducing bugs and improving maintainability.

---

### Files updated / created:

- `src/api/main.py` — FastAPI application serving the model.
- `src/api/pydantic_models.py` — Pydantic schemas for request/response validation.
- `Dockerfile` — Docker configuration for containerizing the API.
- `docker-compose.yml` — Compose file for local container orchestration.
- `.github/workflows/ci.yml` — GitHub Actions CI pipeline configuration.
- `requirements.txt` — Added `fastapi`, `uvicorn`, and `flake8` dependencies.

---

### How to run locally:

1. **Start the FastAPI app:**

   ```bash
   uvicorn src.api.main:app --reload
Access the API docs:

Open http://127.0.0.1:8000/docs in your browser to interact with the API.