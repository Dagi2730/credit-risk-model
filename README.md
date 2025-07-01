## 📌 Task 4 - Proxy Target Variable Engineering

Since the dataset did not contain a direct "credit risk" label, we engineered a proxy target variable named `is_high_risk` to identify potentially risky customers. This was done by programmatically labeling disengaged customers who are more likely to default on their loans.

### Approach:

1. **RFM Metric Calculation**  
   We computed Recency, Frequency, and Monetary (RFM) values for each customer based on their transaction history.  
   - **Recency** measures how recently a customer made a transaction relative to a fixed snapshot date.  
   - **Frequency** counts the total number of transactions per customer.  
   - **Monetary** sums the total transaction amounts per customer.

2. **Clustering Customers**  
   We used K-Means clustering to segment customers into 3 groups based on scaled RFM features. A fixed `random_state` was set for reproducibility.

3. **High-Risk Group Identification**  
   By analyzing cluster characteristics, the cluster with the lowest frequency and monetary values was assigned as the high-risk group.

4. **Label Creation and Integration**  
   A binary target column `is_high_risk` was created, where customers in the high-risk cluster were labeled 1 and others 0. This label was merged back into the main processed dataset for use in model training.

### Outcome:

- The `is_high_risk` target variable serves as a proxy for credit risk, enabling supervised modeling despite the absence of explicit default labels.
- This approach facilitates the identification of customers who are likely to default, based on behavioral transaction patterns.

### Files updated:

- `data/processed/raw_with_high_risk_label.csv` — processed dataset including the `is_high_risk` target column.
- Relevant code for RFM calculation, clustering, and labeling is implemented in the Task 4 notebook and/or scripts.
