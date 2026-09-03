import pandas as pd


def median_imputation(series: pd.Series) -> pd.Series:
    """
    Mengisi missing value menggunakan nilai median.
    """
    result = series.copy()

    median_value = result.median()

    result = result.fillna(median_value)

    return result