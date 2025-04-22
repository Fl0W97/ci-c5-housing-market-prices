import streamlit as st
import pandas as pd
import numpy as np
from src.data_management import load_pkl_file
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.machine_learning.evaluation import regression_performance
import matplotlib.pyplot as plt


def page_pipeline_performance_body():
    st.write("### Pipeline performance")

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
        f"X_train_opt.csv"
    )
    X_test_opt = pd.read_csv(
        f"outputs/ml_pipelines/predict_SalePrice/{version}/"
        f"X_test_opt.csv"
    )
    y_train_opt = pd.read_csv(
        f"outputs/ml_pipelines/predict_SalePrice/{version}/"
        f"y_train_opt.csv"
    ).values.squeeze()
    y_test_opt = pd.read_csv(
        f"outputs/ml_pipelines/predict_SalePrice/{version}/"
        f"y_test_opt.csv"
    ).values.squeeze()

    st.write("### ML Pipeline: Predict Sales Price")
    # display pipeline training summary conclusions
    st.info(
         f"* The model explains 83% of the variance in sale prices \n"
         f"* On average, the model's predictions are off by less than $20K. "
         f"For house prices, that’s very acceptable, especially for "
         f"mid-to-upper priced homes."
    )

    # Apply data cleaning & feature engineering pipeline to the test data
    # test_opt_transformed = pipeline_dc_fe_opt.transform(X_test_opt)

    # Make predictions with the final regression model
    y_pred_opt = pipeline_regressor.predict(X_test_opt)

    # Show performance metrics
    regression_performance(y_test_opt, y_pred_opt, log_base=10)

    # Add plot: Predicted vs Actual (Original Scale)
    import matplotlib.pyplot as plt

    y_test_actual = np.power(10, y_test_opt)
    y_pred_actual = np.power(10, y_pred_opt)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(y_test_actual, y_pred_actual, alpha=0.5, color='blue')
    ax.plot([y_test_actual.min(), y_test_actual.max()],
            [y_pred_actual.min(), y_pred_actual.max()],
            color='red', lw=2, linestyle='--')

    ax.set_title("Predicted vs Actual Sale Prices")
    ax.set_xlabel("Actual Sale Price ($)")
    ax.set_ylabel("Predicted Sale Price ($)")
    ax.grid(True)

    st.write("### Predicted vs Actual Sale Prices")
    st.pyplot(fig)
