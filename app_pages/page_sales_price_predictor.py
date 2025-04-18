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

    # Generate Live Data
    X_live = DrawInputsWidgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        sales_price_prediction = predict_sales_price(
            X_live, house_features, pipeline_dc_fe, pipeline_regressor)

    st.write("---")

    st.write('Enter the details of the property to predict the sales price.')

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

    # Input form
    # gr_liv_area = st.number_input('GrLivArea (Ground Living Area)', min_value=0)
    # garage_finish = st.selectbox('GarageFinish', ['Fin', 'RFn', 'Unf', 'None'])
    # masonery_area = st.number_input('MasVnrArea', min_value=0)
    # basement_finish = st.number_input('BsmtFinSF1', min_value=0)
    # open_porch = st.number_input('OpenPorchSF', min_value=0)
    # overall_qual = st.selectbox('OverallQual', ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1'])
    # year_remod_add = st.number_input('YearRemodAdd', min_value=0)

    # Legend for input form
    # if st.checkbox("Open legend for input values"):
    #    if st.checkbox("GarageFinish options"):    
    #        st.write(f"*Fin: Finished "
    #                f"*RFn: Rough Finished "
    #                f"*Unf: Unfinished "
    #                f"*None: No Garage "
    #                )
    #    if st.checkbox("OverallQual options"):    
    #        st.write(f"*10: Very Excellent "
    #                f"*9: Excellent "
    #                f"*8: Very Good "
    #                f"*7: Good "
    #                f"*6: Above Average "
    #                f"*5: Average "
    #                f"*4: Below Average "
    #                f"*3: Fair "
    #                f"*2: Poor "
    #                f"*1: Very Poor "              
    #                )


    # Prepare the new input data
    # new_data = pd.DataFrame({
    #    'GrLivArea': [gr_liv_area],
    #    'GarageFinish': [garage_finish],
    #    'MasVnrArea': [masonery_area],
    #    'BsmtFinSF1': [basement_finish],
    #    'OpenPorchSF': [open_porch],
    #    'OverallQual': [overall_qual],
    #    'YearRemodAdd': [year_remod_add]
    # })

    # st.write("f {new_data}")"""
