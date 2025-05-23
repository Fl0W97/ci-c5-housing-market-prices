import streamlit as st
import pandas as pd
import numpy as np
from src.preprocessing import drop_unwanted_columns
from src.data_management import load_house_market_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (predict_sales_price)


def page_sales_price_evaluation_body():

    # load predict sales price files
    version = 'v1'
    pipeline_dc_fe = load_pkl_file(
        f"outputs/ml_pipelines/predict_SalePrice/{version}/"
        f"pipeline_data_cleaning_feat_opt.pkl"
    )
    pipeline_regressor = load_pkl_file(
        f"outputs/ml_pipelines/predict_SalePrice/{version}/"
        f"pipeline_regressor.pkl"
    )
    house_features = (
        pd.read_csv(
            f"outputs/ml_pipelines/predict_SalePrice/{version}/X_train.csv"
        ).columns.to_list()
    )

    st.write("### Sales Price Evaluator")
    st.info(
        f"This tool estimates whether the entered sales price is "
        f"appropriate based on current market conditions. Please enter "
        f"the property details in the five sections below, then click "
        f"the button to evaluate."
    )
    st.write("---")

    # Generate User Input (live) Data
    X_live = DrawInputsWidgets()

    # Input field for actual sales price
    input_sales_price = st.number_input(
        "Enter the property's actual/listed sales price ($):",
        min_value=10000,
        max_value=1000000,
        step=5000
    )

    # predict on User Input (live) Data
    if st.button("Run Price Check"):
        # Apply log10 transformation
        X_live["GrLivArea"] = np.log10(X_live["GrLivArea"])

        sales_price_prediction = predict_sales_price(
            X_live, house_features, pipeline_dc_fe, pipeline_regressor)

        if sales_price_prediction is not None:
            predicted_value = sales_price_prediction.item()
            st.success(f"Predicted Market Value: ${predicted_value:,.2f}")
            st.info(f"Input Sales Price: ${input_sales_price:,.2f}")

            # Comparison logic
            price_difference = input_sales_price - predicted_value

            if input_sales_price < predicted_value:
                st.success(
                    "Good Deal! The property is listed **below** market value."
                )
            elif input_sales_price > predicted_value:
                st.warning(
                    "Bad Deal! The property is listed **above** market value."
                )
            else:
                st.info(
                    "Fair Deal. The property price matches the market "
                    "estimate."
                )

    st.write("---")


def DrawInputsWidgets():

    # load dataset
    df = load_house_market_data()
    percentageMin, percentageMax = 0.4, 2.0

# input widgets only for 4 house features
    col1, col2, col3, col4 = st.columns(4)

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type
    # and set initial values
    with col1:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median(),
            step=100.0
        )
    X_live[feature] = st_widget

    with col2:
        feature = "OpenPorchSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median(),
            step=10.0
        )
    X_live[feature] = st_widget

    with col3:
        feature = "OverallQual"
        st_widget = st.selectbox(
            label=feature,
            options=sorted(df[feature].unique())
        )
    X_live[feature] = st_widget

    with col4:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step=1
        )
    X_live[feature] = st_widget

    st.write(X_live)

    return X_live
