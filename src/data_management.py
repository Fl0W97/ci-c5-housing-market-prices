import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_data
def load_house_market_data():
    df = pd.read_csv("outputs/data_cleaned/house_market_data_complete_cleaned.csv")
    return df
