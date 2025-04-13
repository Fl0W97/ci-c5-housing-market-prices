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
        f"The client is interested in understanding the house market and the relevant attributes "
        f"so that the client can learn the most relevant variables correlated "
        f"to sales price.")

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
        sns.histplot(df['SalePrice'], kde=True, bins=40, color='skyblue', ax=ax)
        ax.axvline(average_sales_price, color='red', linestyle='--', label=f'Mean: ${average_sales_price:,.0f}')
        ax.axvline(median_sales_price, color='green', linestyle='--', label=f'Median: ${median_sales_price:,.0f}')
        ax.set_title('Distribution of Sale Prices')
        ax.set_xlabel('Sale Price')
        ax.set_ylabel('Frequency')
        ax.legend()
        st.pyplot(fig_dist)

    st.write("---")

    # Correlation Study Summary
    st.info(
        f"A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to SalePrice. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # inspect data
    if st.checkbox("Inspect Correlation Heatmap"):
        st.write(
            f"* Find below the correlation matrix")

        correlation_matrix = df.corr()
        fig_all, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, ax=ax)
        ax.set_title("Correlation Matrix")
        st.pyplot(fig_all)

        # inspect data
    if st.checkbox("Focus only on SalePrice correlations"):
        st.write(
            f"* Find below the top 10 correlations")

        top_corr = df.corr()['SalePrice'].sort_values(ascending=False)
        top_vars = top_corr[0:10].index  # Top 10 (excluding SalePrice itself)
        filtered_corr = df[top_vars].corr()

        # Plot just this smaller matrix
        correlation_matrix = df.corr()
        fig_top, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(filtered_corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        ax.set_title("Top Correlated Features with SalePrice")
        st.pyplot(fig_top)


    # Text based on "02 - Data Collection" notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlation indications and plots below interpretation converge. "
        f"It is indicated that: \n"
        f"* A property with a high sales price typically has huge ground living area (> xSF). \n"
        f"* A property with a high sales price typically has a big garage (> xSF). \n"
        f"* A property with a high sales price typically has a high kitchen quality. \n"
        f"* A property with a high sales price typically has a high overall quality. \n"
    )
