import pandas as pd

def forward_fill_imputation(series: pd.Series) -> pd.Series:
    """
    Mengisi missing value dengan aturan:
    1. Jika missing berada di awal series, isi dengan nilai valid pertama setelahnya.
    2. Missing lainnya diisi menggunakan nilai sebelumnya (Forward Fill).
    """
    result = series.copy()

    # Cari indeks nilai valid pertama
    first_valid = result.first_valid_index()

    # Jika ada nilai valid dan terdapat NaN di awal
    if first_valid is not None:
        result.loc[:first_valid] = result.loc[:first_valid].fillna(result.loc[first_valid])

    # Forward fill untuk missing value lainnya
    result = result.ffill()

    return result