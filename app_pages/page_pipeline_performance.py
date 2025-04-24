import streamlit as st
import pandas as pd
import numpy as np
from src.data_management import load_pkl_file
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.machine_learning.evaluation import regression_performance
import matplotlib.pyplot as plt


def page_pipeline_performance_body():
    st.write("### ML Pipeline performance of Predict Sales Price")

    version = 'v1'
    # load needed files
    pipeline_dc_fe_opt = load_pkl_file(
        f"outputs/ml_pipelines/predict_SalePrice/{version}/"
        f"pipeline_data_cleaning_feat_opt.pkl"
    )
    pipeline_regressor = load_pkl_file(
        f"outputs/ml_pipelines/predict_SalePrice/{version}/"
        f"pipeline_regressor.pkl"
    )
    X_train_opt = pd.read_csv(
        f"outputs/ml_pipelines/predict_SalePrice/{version}/"
        f"X_train_opt.csv" #X_train_opt
    )
    X_test_opt = pd.read_csv(
        f"outputs/ml_pipelines/predict_SalePrice/{version}/"
        f"X_test_opt.csv" #X_test_opt
    )
    y_train_opt = pd.read_csv(
        f"outputs/ml_pipelines/predict_SalePrice/{version}/"
        f"y_train_opt.csv"
    ).values.squeeze()
    y_test_opt = pd.read_csv(
        f"outputs/ml_pipelines/predict_SalePrice/{version}/"
        f"y_test_opt.csv"
    ).values.squeeze()

    # display pipeline training summary conclusions
    st.info(
        f"The model explains approximately 80% of the variance in sale prices. "
        f"On average, its predictions deviate by less than 22,000 USD, which is "
        f"considered highly acceptable—particularly for mid- to upper-range "
        f"properties. Nonetheless, a small number of significant outliers "
        f"persist, indicating potential areas for further model refinement."
    )

    # Make predictions with the final regression model
    y_pred_opt = pipeline_regressor.predict(X_test_opt)

    # Show performance metrics
    regression_performance(y_test_opt, y_pred_opt, log_base=10)

    # Add plot: Predicted vs Actual (Original Scale)
    import matplotlib.pyplot as plt

    y_test_actual = np.power(10, y_test_opt)
    y_pred_actual = np.power(10, y_pred_opt)

    # Define the range to plot
    min_val = min(y_test_actual.min(), y_pred_actual.min())
    max_val = max(y_test_actual.max(), y_pred_actual.max())

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(y_test_actual, y_pred_actual, alpha=0.5, color='blue')

    ax.plot([min_val, max_val],
            [min_val, max_val],
            color='red', lw=2, linestyle='--')

    ax.set_title("Predicted vs Actual Sale Prices")
    ax.set_xlabel("Actual Sale Price ($)")
    ax.set_ylabel("Predicted Sale Price ($)")
    ax.grid(True)

    st.write("### Predicted vs Actual Sale Prices")
    st.pyplot(fig)
