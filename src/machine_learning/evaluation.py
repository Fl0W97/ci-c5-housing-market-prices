import numpy as np
import pandas as pd
import streamlit as st
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def regression_performance(y_test_opt_log, y_pred_opt_log, log_base=10):
    """
    Inverse transforms predictions and actuals from log scale
    and displays common regression metrics for a single model.

    Arguments:
        y_true_log: Ground truth (actual) values in log scale.
        y_pred_log: Predicted values in log scale.
        log_base: The logarithmic base (default is 10).

    """
    # Inverse transformation: from log scale back to original SalePrice
    y_test_actual = np.power(log_base, y_test_opt_log)
    y_pred_actual = np.power(log_base, y_pred_opt_log)

    # Calculate metrics
    mae = mean_absolute_error(y_test_actual, y_pred_actual)
    mse = mean_squared_error(y_test_actual, y_pred_actual)
    rmse = mean_squared_error(y_test_actual, y_pred_actual, squared=False)
    r2 = r2_score(y_test_actual, y_pred_actual)

    # Display metrics
    st.write("### Model Performance")
    st.write(f"**Mean Absolute Error (MAE):** ${mae:,.0f}")
    st.write(f"**Mean Squared Error (MSE):** ${mse:,.0f}")
    st.write(f"**Root Mean Squared Error (RMSE):** ${rmse:,.0f}")
    st.write(f"**R² Score:** {r2:.4f}")

    # Display sample predictions vs actuals — both in ORIGINAL scale
    results_df = pd.DataFrame({
        'Actual SalePrice': y_test_actual[:5],
        'Predicted SalePrice': y_pred_actual[:5]
    })

    st.write("### Sample Predictions")
    st.dataframe(results_df.style.format("${:,.0f}"))
