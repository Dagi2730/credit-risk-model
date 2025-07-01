def calculate_revenue(df):
    """
    Calculates total revenue for each customer in the dataframe.

    Args:
        df (pd.DataFrame): Data with 'CustomerId' and 'Amount' columns.

    Returns:
        pd.Series: Total revenue per CustomerId.
    """
    return df.groupby('CustomerId')['Amount'].sum()
