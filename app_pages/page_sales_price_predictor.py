import streamlit as st
import pandas as pd
import numpy as np
from src.preprocessing import drop_unwanted_columns
from src.data_management import load_house_market_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (predict_sales_price)

def page_sales_price_predictor_body():

    # load predict sales price files
    version = 'v1'
    pipeline_dc_fe = load_pkl_file(
        f'outputs/ml_pipelines/predict_SalePrice/{version}/pipeline_data_cleaning_feat_opt.pkl')
    pipeline_regressor = load_pkl_file(
        f"outputs/ml_pipelines/predict_SalePrice/{version}/pipeline_regressor.pkl")
    house_features = (pd.read_csv(f"outputs/ml_pipelines/predict_SalePrice/{version}/X_train.csv")
                      .columns
                      .to_list()
                      )

    st.write("### Sales Price Predictor")
    st.info(
        f"* The client is interested in receiving an predictive sales price, "
        f"based on his input parameter. "
    )
    st.write("---")

    # Generate User Input (live) Data
    X_live = DrawInputsWidgets()

    st.write('Enter the details of the property to predict the sales price.')

    # predict on User Input (live) Data
    if st.button("Run Predictive Analysis"):
        sales_price_prediction = predict_sales_price(
            X_live, house_features, pipeline_dc_fe, pipeline_regressor)
        sales_price_prediction = sales_price_prediction.item()
        st.success(f"Predicted sales price is: ${sales_price_prediction:,.2f}")

    st.write("---")

    # Define a dictionary of inherited houses
    inherited_houses = {
        "House 1": {
            'GrLivArea': 896,
            'GarageArea': 730.0,
            'MasVnrArea': 0,
            'YearBuilt': 1961,
            'OverallQual': 6
        },
        "House 2": {
            'GrLivArea': 1200,
            'GarageArea': 500.0,
            'MasVnrArea': 100,
            'YearBuilt': 1975,
            'OverallQual': 7
        },
        "House 3": {
            'GrLivArea': 1500,
            'GarageArea': 600.0,
            'MasVnrArea': 200,
            'YearBuilt': 1985,
            'OverallQual': 8
        },
        "House 4": {
            'GrLivArea': 1800,
            'GarageArea': 650.0,
            'MasVnrArea': 150,
            'YearBuilt': 1995,
            'OverallQual': 9
        }
    }

    # Iterate through each house and create a button + prediction
    for label, features in inherited_houses.items():
        if st.button(f"Predict sales price for {label}"):
            X_df = pd.DataFrame([features])
            st.write(X_df.head(1))
            
            prediction = predict_sales_price(X_df, house_features, pipeline_dc_fe, pipeline_regressor)

            if prediction is not None:
                predicted_value = prediction.item()
                st.success(f"Predicted sales price for {label}: ${predicted_value:,.2f}")

def DrawInputsWidgets():

    # load dataset
    df = load_house_market_data()
    percentageMin, percentageMax = 0.4, 2.0

# input widgets only for 5 house features
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)

    # We are using these features to feed the ML pipeline

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col3:
        feature = "MasVnrArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col4:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col5:
        feature = "OverallQual"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    st.write(X_live)

    return X_live
