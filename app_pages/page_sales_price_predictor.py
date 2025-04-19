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

    # Initial value
    sales_price_prediction_h1 = None

    st.write('Enter the details of the property to predict the sales price.')

    # predict on User Input (live) Data
    if st.button("Run Predictive Analysis"):
        sales_price_prediction = predict_sales_price(
            X_live, house_features, pipeline_dc_fe, pipeline_regressor)

    st.write("---")
             
    # predict sales price inherent house 1
    if st.button("Predict sales price for inherent house 1"):

        X_house1 = {
            'GrLivArea': 896,
            'GarageArea': 730.0,
            'MasVnrArea': 0,
            'YearBuilt': 1961,
            'OverallQual': 6
        }

        # Convert X_house1 to a DataFrame
        X_house1_df = pd.DataFrame([X_house1])

        # Show input data (now it's a DataFrame so .head() works)
        st.write(X_house1_df.head(1))

         # Predict the sales price using the DataFrame
        sales_price_prediction_h1 = predict_sales_price(
            X_house1_df, house_features, pipeline_dc_fe, pipeline_regressor)

    # Only show prediction if it exists
    if sales_price_prediction_h1 is not None:
        # Safely extract and format the prediction
        predicted_value = sales_price_prediction_h1.item()  # works for 1-element arrays

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
