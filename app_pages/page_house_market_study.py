import streamlit as st
import plotly.express as px
import numpy as np
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
        f"The client is interested in understanding the house market and the "
        f"relevant attributes so that the client can learn the most relevant "
        f"variables correlated to sales price.")

    # inspect dataset
    if st.checkbox("Inspect House market dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 5 rows.")

        st.write(df.head(5))

    st.write("---")

    # Display SalePrice distribution
    if st.checkbox("Show SalePrice Distribution"):
        st.write("### Distribution of Sale Prices")

        average_sales_price = df['SalePrice'].mean()
        median_sales_price = df['SalePrice'].median()

        fig_dist, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(
            df['SalePrice'],
            kde=True,
            bins=40,
            color='skyblue',
            ax=ax
        )
        ax.axvline(
            average_sales_price,
            color='red',
            linestyle='--',
            label=f'Mean: ${average_sales_price:,.0f}'
        )
        ax.axvline(
            median_sales_price,
            color='green',
            linestyle='--',
            label=f'Median: ${median_sales_price:,.0f}'
            )
        ax.set_title('Distribution of Sale Prices')
        ax.set_xlabel('Sale Price')
        ax.set_ylabel('Frequency')
        ax.legend()
        st.pyplot(fig_dist)

    st.write("---")

    # Correlation Study Summary
    st.info(
        f"A correlation study was conducted in the notebook to better "
        f"understand how the variables are correlated to SalePrice. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # inspect data
    if st.checkbox("Inspect Correlation Heatmap"):
        st.write(
            f"* Find below the correlation matrix")

        correlation_matrix = df.corr()
        fig_all, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(
            correlation_matrix,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            cbar=True,
            ax=ax
        )
        ax.set_title("Correlation Matrix")
        st.pyplot(fig_all)

    # Text based on "02 - Data Collection" notebook
    st.info(
        f"The correlation indications and plots below interpretation "
        f"converge. It is indicated that: \n"
        f"* A property with a high sales price typically has huge ground "
        f"living area. \n"
        f"* A property with a high sales price typically has a high "
        f"kitchen quality. \n"
        f"* A property with a high sales price typically has a high overall "
        f"quality. \n"
        f"* The sales price has a low correlation with basement exposure, "
        f"number of bedrooms or the overall condition. \n"
    )
