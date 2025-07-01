# 📄 Feature Engineering Overview (Task 3)

In this phase, we developed a robust data processing pipeline using **scikit-learn** to transform raw transaction data into a clean, model-ready format. This was a critical step in preparing high-quality inputs for credit scoring.

---

## 🔧 Key Steps Implemented:

### Custom Feature Extraction
- Extracted temporal features from `TransactionStartTime`:
  - `TransactionHour`, `TransactionDay`, `TransactionMonth`, `TransactionYear`
- Aggregated transaction metrics per customer:
  - `TotalTransactionAmount`, `AverageTransactionAmount`, `TransactionCount`, `TransactionAmountStd`

### Preprocessing Pipeline
- Used `SimpleImputer` for missing value imputation (median for numerics, mode for categoricals)
- Applied `StandardScaler` for numeric feature standardization
- Applied `OneHotEncoder` for low-cardinality categorical features (excluded high-cardinality like `TransactionId`, `ProductId`)

### Memory Optimization
- Categorical columns with high cardinality (e.g., `TransactionId`, `ProductId`) were excluded from OneHotEncoding to avoid memory explosion.

### Final Output
- The final dataset includes **48 engineered features**, ready for training
- The pipeline was tested interactively in `2.0-feature-engineering.ipynb`
- Saved outputs:
  - `data/processed/processed_features.csv`
  - `data/processed/target.csv` (created using `FraudResult` as proxy)

---

## 📁 Source Code:
- All pipeline logic implemented in: `src/feature_engineering.py`
