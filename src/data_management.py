import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_data
def load_house_market_data():
    df = pd.read_csv("outputs/data_collected/house_pricing_data.csv")
    return df
