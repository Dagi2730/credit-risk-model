import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# Step 1: Custom Transformers
class DateTimeFeatureExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, datetime_col='TransactionStartTime'):
        self.datetime_col = datetime_col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X[self.datetime_col] = pd.to_datetime(X[self.datetime_col], errors='coerce')
        X['TransactionHour'] = X[self.datetime_col].dt.hour
        X['TransactionDay'] = X[self.datetime_col].dt.day
        X['TransactionMonth'] = X[self.datetime_col].dt.month
        X['TransactionYear'] = X[self.datetime_col].dt.year
        return X

class AggregateTransactionFeatures(BaseEstimator, TransformerMixin):
    def __init__(self, customer_id_col='CustomerId', amount_col='Amount'):
        self.customer_id_col = customer_id_col
        self.amount_col = amount_col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        agg = X.groupby(self.customer_id_col)[self.amount_col].agg(['sum', 'mean', 'count', 'std']).reset_index()
        agg.columns = [self.customer_id_col, 'TotalTransactionAmount', 'AverageTransactionAmount', 'TransactionCount', 'TransactionAmountStd']
        X = pd.merge(X, agg, on=self.customer_id_col, how='left')
        return X

# Step 2: Helper to get column types with filtering for high cardinality
def get_column_types(df, threshold=50):
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    # Filter out high-cardinality categorical columns
    low_cardinality_cats = [col for col in categorical_cols if df[col].nunique() <= threshold]
    return numerical_cols, low_cardinality_cats

# Step 3: Build preprocessing pipeline
def build_preprocessing_pipeline(df):
    numerical_cols, categorical_cols = get_column_types(df)

    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    full_pipeline = ColumnTransformer([
        ('num', num_pipeline, numerical_cols),
        ('cat', cat_pipeline, categorical_cols)
    ])

    return full_pipeline

# Step 4: Combine all transformations
def build_feature_engineering_pipeline(df):
    preprocessing_pipeline = build_preprocessing_pipeline(df)

    full_pipeline = Pipeline([
        ('datetime_features', DateTimeFeatureExtractor()),
        ('aggregate_features', AggregateTransactionFeatures()),
        ('preprocessing', preprocessing_pipeline)
    ])

    return full_pipeline

# Entry point for testing
if __name__ == "__main__":
    df = pd.read_csv('data/raw/data.csv')

    # Optional: print cardinality report
    print("\n[INFO] Cardinality of categorical features:")
    for col in df.select_dtypes(include=['object']).columns:
        print(f"{col}: {df[col].nunique()} unique values")

    pipeline = build_feature_engineering_pipeline(df)
    processed_data = pipeline.fit_transform(df)

    print(f"\n✅ Processed data shape: {processed_data.shape}")
