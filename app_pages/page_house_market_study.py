import streamlit as st
import plotly.express as px
import numpy as np
st.pyplot()
from src.data_management import load_house_market_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_house_market_study_body():

    # load data
    df = load_house_market_data()

    # hard copied from jupyter notebook
    vars_to_study = [{'GrLivArea'}, {'OverallQual'}]

    st.write("### House Market Study")
    st.info(
        f"* The client is interested in understanding the house market and the relevant attributes "
        f"so that the client can learn the most relevant variables correlated "
        f"to sales price.")

    # inspect data
    if st.checkbox("Inspect House market"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 5 rows.")

        st.write(df.head(5))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to SalePrice. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Graphic of correlation study with 
    st.write("### Correlation Heatmap")
    correlation_matrix = df.corr()
    fig, ax = plt.subplots(figsize=(12, 8))

    # Add focus only on SalePrice correlations and top 10
    top_corr = df.corr()['SalePrice'].sort_values(ascending=False)
    top_vars = top_corr[1:11].index  # Top 10 (excluding SalePrice itself)
    filtered_corr = df[top_vars].corr()

    # Plot just this smaller matrix
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(filtered_corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title("10 Top Correlated Features with SalePrice")
    st.pyplot(fig)
    

    # Text based on "02 - Data Collection" notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlation indications and plots below interpretation converge. "
        f"It is indicated that: \n"
        f"* A property with a high sales price typically has huge ground living area (> xSF). \n"
        f"* A property with a high sales price typically has a big garage (> xSF). \n"
        f"* A property with a high sales price typically has a high kitchen quality. \n"
        f"* A property with a high sales price typically has a high overall quality. \n"
    )
