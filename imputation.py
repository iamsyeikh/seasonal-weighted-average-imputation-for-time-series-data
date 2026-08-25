import numpy as np
import pandas as pd


def adaptive_weighted_seasonal_imputation(
    series,
    seasonal_period,
    current_weight=0.50
):
    """
    Adaptive Weighted Seasonal Imputation.

    Window otomatis = seasonal_period - 1.
    """

    result = series.copy()

    P = seasonal_period
    window = P - 1

    previous_weight = (
        (1 - current_weight) / window
    )

    missing_positions = np.where(
        series.isna()
    )[0]

    for pos in missing_positions:

        predictions = []

        center = pos - P

        while center >= 0:

            values = []
            weights = []

            if not pd.isna(series.iloc[center]):

                values.append(
                    series.iloc[center]
                )

                weights.append(
                    current_weight
                )

            for i in range(1, P):

                idx = center - i

                if idx >= 0:

                    value = series.iloc[idx]

                    if not pd.isna(value):

                        values.append(value)

                        weights.append(
                            previous_weight
                        )

            if values:

                values = np.array(values)
                weights = np.array(weights)

                weights /= weights.sum()

                prediction = np.sum(
                    values * weights
                )

                predictions.append(
                    prediction
                )

            center -= P

        if predictions:

            result.iloc[pos] = np.mean(
                predictions
            )

    return result