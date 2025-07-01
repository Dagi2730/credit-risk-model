import pandas as pd
from src.data_processing import calculate_revenue

def test_calculate_revenue_basic():
    data = {
        'CustomerId': [1, 1, 2, 2, 3],
        'Amount': [100, 200, 300, -50, 0]
    }
    df = pd.DataFrame(data)
    result = calculate_revenue(df)
    # Make expected index a pd.Index with same name and dtype as result.index
    expected_index = pd.Index([1, 2, 3], name='CustomerId', dtype=result.index.dtype)
    expected = pd.Series([300, 250, 0], index=expected_index, name='Amount')
    pd.testing.assert_series_equal(result, expected)

def test_calculate_revenue_empty():
    df = pd.DataFrame({'CustomerId': [], 'Amount': []})
    result = calculate_revenue(df)
    expected_index = pd.Index([], name='CustomerId', dtype=result.index.dtype)
    expected = pd.Series(dtype='float64', index=expected_index, name="Amount")  # Set name here
    pd.testing.assert_series_equal(result, expected)

