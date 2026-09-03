import pandas as pd


def mean_imputation(series: pd.Series) -> pd.Series:
    """
    Mengisi missing value menggunakan nilai mean.
    """
    result = series.copy()

    mean_value = result.mean()

    result = result.fillna(mean_value)

    return result
