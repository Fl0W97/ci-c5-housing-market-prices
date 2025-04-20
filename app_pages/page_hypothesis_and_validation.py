import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from src.data_management import load_house_market_data


def page_project_hypothesis_and_validation_body():

    # load data
    df = load_house_market_data()

    st.write("### Project Hypothesis and Validation")
    st.write("Find here the validated hypothesis H1-H5:")

    # conclusions taken from "02 - Data Collection" notebook
    st.success(
        f"* H1: Larger square footage often correlates with higher sales prices: Correct \n\n"
        f"The correlation with focus on 'SalePrice' supports the hypothesis. "
        f"Variables such as 'GrLivArea' (corr. 0.708624), 'TotalBsmtSF' (corr. 0.613581), 'GarageArea' (corr. 0.623431) and '1stFlrSF' (corr. 0.605852) have high correlations with the 'SalePrice' ."
        f"In addition, The distribution of GrLivArea by SalePrice show it clearly: \n\n")

    if st.checkbox("Find below the distribution"):

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x='SalePrice', y='GrLivArea', data=df, ax=ax)
        ax.set_title('GrLivArea vs SalePrice')
        st.pyplot(fig)

    if st.checkbox("Focus only on SalePrice correlations"):
        st.write(f"*See here the top 10 correlations")

        top_corr = df.corr()['SalePrice'].sort_values(ascending=False)
        top_vars = top_corr[0:10].index  # Top 10 (excluding SalePrice itself)
        filtered_corr = df[top_vars].corr()

        fig_top, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(filtered_corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        ax.set_title("Top Correlated Features with SalePrice")
        st.pyplot(fig_top)

    st.write("---")

    st.warning(
        f"* H2: More bedrooms, higher sales price: Wrong \n\n"
        f"The correlation study and the distribution plot don't support the "
        f"hypothesis (corr. 0.161901). The variable 'BedroomAbvGr' indicates the number of "
        F"bedrooms which are not related to the sales price or saquare feets. "
        f"In addition, below the distribution of BedroomAbvGr by SalePrice\n\n")

    if st.checkbox("See here the distribution 'BedroomAbvGr vs SalePrice'"):

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x='SalePrice', y='BedroomAbvGr', data=df, ax=ax)
        ax.set_title('BedroomAbvGr vs SalePrice')
        st.pyplot(fig)

    st.write("---")

    st.warning(
        f"* H3: Better OverallCond, higher sales price: Wrong \n\n"
        f"The correlation study and the distribution plot don't support the "
        f"hypothesis (corr. -0.077856). The variable 'OverallCond' indicates the number of "
        F"bedrooms which are not related to the sales price or saquare feets. "
        f"In addition, below the distribution of OverallCond by SalePrice\n\n")

    if st.checkbox("See here the distribution 'OverallCond vs SalePrice'"):

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x='SalePrice', y='OverallCond', data=df, ax=ax)
        ax.set_title('OverallCond vs SalePrice')
        st.pyplot(fig)

    st.write("---")

    st.warning(
        f"* H4: Renovated old houses sell for more than non-renovated old "
        f"houses: Wrong. \n\n"
        f"It was tested by comparing SalePrice for old houses, grouped by "
        f"whether they were renovated or not. \n"
        f"The statistical tests shows that there is no statistically "
        f"significant difference in SalePrice between old houses that were "
        f"renovated and those that were not.\n "
        f"t-statistic = 0.27. 0.27 is very close to zero, so the difference in "
        f"average SalePrice between groups is tiny compared to the variability.\n\n"
        f"p-value = 0.7842. This means the difference is not statistically significant. \n\n "
        f"In addtion, the correlation value YearRemodadd/SalePrice is 0.51, not strong. "
        )

    if st.checkbox("See here the Sale Price Comparison: Renovated vs. Not Renovated"):
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x="IsRenovated", y="SalePrice", data=df, ax=ax)
        ax.set_title("Sale Price Comparison: Renovated vs. Not Renovated")
        ax.set_xticklabels(["Not Renovated", "Renovated"])
        st.pyplot(fig)

    st.write("---")

    st.success(
        f"* H5: Newer houses are more expensive: Partly correct \n\n"
        f"Here average prices of old (< 2000 (YearBuilt)) vs newer homes. > 2000 (YearBuilt) has been analyzed. "
        f"To control for confounding variables houses of similar characteristics (same GrLivArea, OverallQual) has been compared, only differing in YearBuilt "
        f"The result of a t-test shows (p =  0.0123), newer houses tend to be more expensive controlling for other features. "
        f"The visualization below support the statement. "
        )

    if st.checkbox("See here the Sale Price Comparison: New vs. Old Houses"):
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=df_filtered, x='House_Age_Group', y='SalePrice')
        ax.set_title("Sale Price Comparison: New vs. Old Houses")
        st.pyplot(fig)

    st.write("---")
