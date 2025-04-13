import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_data
def load_house_market_data():
    df = pd.read_csv("outputs/data_cleaned/house_market_data_complete_cleaned.csv")
    return df

def load_pkl_file():
    return joblib.load("outputs/ml_pipeline/predict_SalePrice/v3/full_pipeline.pkl")
