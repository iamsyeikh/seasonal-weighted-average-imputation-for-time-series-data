import pandas as pd


def linear_interpolation(series):
    """
    Linear Interpolation

    Mengisi missing value berdasarkan interpolasi linear
    antara nilai sebelum dan sesudah missing value.

    Parameters
    ----------
    series : pandas Series
        Time series yang memiliki missing value.

    Returns
    -------
    pandas Series
        Series setelah missing value diimputasi.
    """

    result = series.copy()

    result = result.interpolate(
        method="linear",
        limit_direction="both"
    )

    return result