import streamlit as st


def predict_sales_price(X_live, sales_price_features, preprocessing, pipline_regressor):

    # from live data, subset features related to this pipeline
    X_live_churn = X_live.filter(churn_features)

    # apply data cleaning / feat engine pipeline to live data
    X_live_churn_dc_fe = preprocessing.transform(X_live_churn)

    # predict
    sales_price_prediction = pipline_regressor.predict(X_live_churn_dc_fe)
    # churn_prediction_proba = pipline_regressor.predict_proba(
    #    X_live_churn_dc_fe)
    # st.write(churn_prediction_proba)

    # Create a logic to display the results
    sales_price_prediction = 

    statement = (
        f'### The predicted sales price for this house based on the given parameters is {sales_price_prediction}.')

    st.write(statement)

    return sales_price_prediction
