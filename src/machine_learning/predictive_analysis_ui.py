import streamlit as st
import numpy as np

def predict_sales_price(X_live, house_features, preprocessing, pipline_regressor):

    # from live data, subset features related to this pipeline
    X_live = X_live.filter(house_features)

    # apply data cleaning / feat engine pipeline to live data
    X_live_dc_fe = preprocessing.transform(X_live)

    # Predict (in log scale)
    sales_price_log = pipline_regressor.predict(X_live_dc_fe)

    # Inverse transform to get actual price
    sales_price_prediction = np.power(10, sales_price_log)

    # predict
    # sales_price_prediction = pipline_regressor.predict(X_live_dc_fe)

    return sales_price_prediction
