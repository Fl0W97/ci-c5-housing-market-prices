import streamlit as st

def predict_sales_price(X_live, house_features, preprocessing, pipline_regressor):

    # from live data, subset features related to this pipeline
    X_live = X_live.filter(house_features)

    # apply data cleaning / feat engine pipeline to live data
    X_live_dc_fe = preprocessing.transform(X_live)

    # predict
    sales_price_prediction = pipline_regressor.predict(X_live_dc_fe)

    # Extract the scalar value from the array
    sales_price = sales_price_prediction.item()

    # display the result
    statement = (
        f'### The predicted sales price for this house based on the given parameters is ${sales_price:,.2f}.')

    st.write(statement)

    return sales_price_prediction
