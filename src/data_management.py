import streamlit as st
import pandas as pd
import numpy as np
import joblib


@st.cache_data
def load_house_market_data():
    df = pd.read_csv(
        "outputs/data_cleaned/house_market_data_complete_cleaned.csv"
    )
    return df


def load_house_market_study_data():
    df_study = pd.read_csv(
        "outputs/data_cleaned/house_market_study.csv"
    )
    return df_study


def load_house_market_study_data_filtered():
    df_filtered = pd.read_csv(
        "outputs/data_cleaned/house_market_study_filtered.csv"
    )
    return df_filtered


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)
