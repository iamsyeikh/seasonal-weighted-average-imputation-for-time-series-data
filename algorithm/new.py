import numpy as np
import pandas as pd


def new_adaptive_weighted_seasonal_imputation(
    series,
    seasonal_period,
    current_weight=0.50
):
    """
    Adaptive Weighted Seasonal Imputation

    Parameters
    ----------
    series : pandas Series
        Time series yang memiliki missing value.

    seasonal_period : int
        Panjang periode seasonal, misalnya 7, 12, 24, dst.

    current_weight : float, default=0.50
        Bobot untuk komponen seasonal.
        Default = 50%.

    Rules
    -----
    1. Seasonal component:
       Mengambil maksimal:
           t - 2P
           t - P
           t + P
           t + 2P

       Nilai seasonal yang NaN atau berada di luar data
       akan diabaikan.

    2. Local component:
       Mengambil:
           t - 1
           t + 1

       Nilai NaN atau di luar data akan diabaikan.

    3. Jika seasonal dan local tersedia:
           prediction = 0.5 * seasonal + 0.5 * local

    4. Jika hanya seasonal tersedia:
           prediction = seasonal

    5. Jika hanya local tersedia:
           prediction = local

    6. Jika keduanya tidak tersedia:
           prediction = mean seluruh data yang tersedia.
    """

    # Salin data agar data asli tidak berubah
    result = series.copy()

    P = seasonal_period
    n = len(series)

    # Validasi seasonal period
    if P <= 0:
        raise ValueError(
            "seasonal_period harus lebih besar dari 0."
        )

    # Bobot
    seasonal_weight = current_weight
    local_weight = 1 - current_weight

    # Rata-rata global sebagai fallback terakhir
    global_mean = series.mean()

    # Cari posisi missing
    missing_positions = np.where(
        series.isna()
    )[0]

    # =====================================================
    # PROSES SETIAP MISSING VALUE
    # =====================================================

    for pos in missing_positions:

        # =================================================
        # 1. SEASONAL COMPONENT
        # =================================================

        seasonal_values = []

        seasonal_positions = [
            pos - (2 * P),
            pos - P,
            pos + P,
            pos + (2 * P)
        ]

        for idx in seasonal_positions:

            # Pastikan index berada dalam data
            if 0 <= idx < n:

                value = series.iloc[idx]

                # Hanya gunakan nilai yang tidak NaN
                if not pd.isna(value):

                    seasonal_values.append(value)

        # Hitung rata-rata seasonal
        if len(seasonal_values) > 0:

            seasonal_prediction = np.mean(
                seasonal_values
            )

        else:

            seasonal_prediction = np.nan


        # =================================================
        # 2. LOCAL COMPONENT
        # =================================================

        local_values = []

        local_positions = [
            pos - 1,
            pos + 1
        ]

        for idx in local_positions:

            # Pastikan index berada dalam data
            if 0 <= idx < n:

                value = series.iloc[idx]

                # Hanya gunakan nilai yang tidak NaN
                if not pd.isna(value):

                    local_values.append(value)

        # Hitung rata-rata local
        if len(local_values) > 0:

            local_prediction = np.mean(
                local_values
            )

        else:

            local_prediction = np.nan


        # =================================================
        # 3. GABUNGKAN SEASONAL + LOCAL
        # =================================================

        if (
            not pd.isna(seasonal_prediction)
            and not pd.isna(local_prediction)
        ):

            # Kedua komponen tersedia
            prediction = (
                seasonal_weight * seasonal_prediction
                +
                local_weight * local_prediction
            )

        elif not pd.isna(seasonal_prediction):

            # Hanya seasonal tersedia
            prediction = seasonal_prediction

        elif not pd.isna(local_prediction):

            # Hanya local tersedia
            prediction = local_prediction

        else:

            # Tidak ada seasonal maupun local
            # Gunakan rata-rata seluruh data
            prediction = global_mean


        # =================================================
        # 4. MASUKKAN HASIL IMPUTASI
        # =================================================

        result.iloc[pos] = prediction


    # =====================================================
    # 5. PENGAMAN TERAKHIR
    # =====================================================

    # Jika masih ada NaN karena kondisi ekstrem,
    # isi dengan rata-rata data yang tersedia.
    if result.isna().any():

        result = result.fillna(global_mean)

    return result