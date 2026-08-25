import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)


def evaluate_imputation(
    actual,
    imputed,
    missing_index
):

    y_true = actual.loc[missing_index]
    y_pred = imputed.loc[missing_index]

    valid = (
        y_true.notna() &
        y_pred.notna()
    )

    y_true = y_true[valid]
    y_pred = y_pred[valid]

    mae = mean_absolute_error(
        y_true,
        y_pred
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_true,
            y_pred
        )
    )

    return mae, rmse