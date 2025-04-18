import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file

def page_pipeline_performance_body():
     st.write("### Pipeline performance")

     version = 'v1'
     # load needed files
     pipeline_dc_fe_opt = load_pkl_file(
          f'outputs/ml_pipelines/predict_SalePrice/{version}/pipeline_data_cleaning_feat_eng.pkl')
     pipeline_regressor = load_pkl_file(
          f"outputs/ml_pipelines/predict_SalePrice/{version}/pipeline_regressor.pkl")
     X_train_opt = pd.read_csv(
          f"outputs/ml_pipelines/predict_SalePrice/{version}/X_train.csv")
     X_test_opt = pd.read_csv(
          f"outputs/ml_pipelines/predict_SalePrice/{version}/X_test.csv")
     y_train_opt = pd.read_csv(
          f"outputs/ml_pipelines/predict_SalePrice/{version}/y_train.csv").values
     y_test_opt = pd.read_csv(
          f"outputs/ml_pipelines/predict_SalePrice/{version}/y_test.csv").values

     st.write("### ML Pipeline: Predict Sales Price")
     # display pipeline training summary conclusions
     st.info(
          f"* The pipeline predicts a sales price with xx% of accurancy, "
          f"since we are interested in this project in determining a sales price. \n"
          f"* The pipeline performance on train and test set is xx xxx , respectively."
     )

     # show pipelines
     st.write("---")
     st.write("#### There are 2 ML Pipelines arranged in series.")

     st.write(" * The first is responsible for data cleaning and feature engineering.")
     st.write(pipeline_dc_fe_opt)

     st.write("* The second is for feature scaling and modelling.")
     st.write(pipeline_regressor)

     # show feature importance plot

     # Apply the data cleaning & feature engineering pipeline
     X_test_opt = pipeline_dc_fe_opt.transform(X_test_opt)

     # Make predictions
     y_pred = pipeline_regressor.predict(X_test_opt)

     # Evaluate metrics
     mae = mean_absolute_error(y_test_opt, y_pred)
     mse = mean_squared_error(y_test_opt, y_pred)
     rmse = mean_squared_error(y_test_opt, y_pred, squared=False)
     r2 = r2_score(y_test_opt, y_pred)

     # Display results
     st.write(f"**Mean Absolute Error (MAE):** {mae:.2f}")
     st.write(f"**Mean Squared Error (MSE):** {mse:.2f}")
     st.write(f"**Root Mean Squared Error (RMSE):** {rmse:.2f}")
     st.write(f"**R² Score:** {r2:.2f}")