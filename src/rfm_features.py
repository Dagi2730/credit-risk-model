import pandas as pd

# Load raw data
df = pd.read_csv('data/raw/data.csv')


# Convert TransactionStartTime to datetime
df['TransactionStartTime'] = pd.to_datetime(df['TransactionStartTime'])

# Define snapshot date: max date in data + 1 day
snapshot_date = df['TransactionStartTime'].max() + pd.Timedelta(days=1)

# Calculate RFM metrics per CustomerId
rfm = df.groupby('CustomerId').agg({
    'TransactionStartTime': lambda x: (snapshot_date - x.max()).days,  # Recency
    'TransactionId': 'count',                                         # Frequency
    'Amount': 'sum'                                                  # Monetary
}).rename(columns={
    'TransactionStartTime': 'Recency',
    'TransactionId': 'Frequency',
    'Amount': 'Monetary'
}).reset_index()

print(rfm.head())
