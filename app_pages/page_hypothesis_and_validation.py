import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
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
        f"Variables such as 'GrLivArea' (corr. 0.708624), 'TotalBsmtSF' (corr. 0.613581), 'GarageArea' (corr. 0.623431) and '1stFlrSF' (corr. 0.605852) have high correlations with the 'SalePrice'."
        f"In addition, The distribution of GrLivArea by SalePrice show it clearly: \n\n")

    if st.checkbox("Focus only on SalePrice correlations"):
        st.write(f"* Find below the top 10 correlations")

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

    # * Use boxplots or plot of price vs number of bedrooms to compare average prices across different numbers of bedrooms.
    # <img src="images/02b_distribution_of_bedroomabvgr_by_saleprice.PNG" alt="see distribution_of_bedroomabvgr_by_saleprice" width="700">
    st.write("---")

    st.warning(
        f"* H3: Better OverallCond, higher sales price: Wrong \n\n"
        f"The correlation study and the distribution plot don't support the "
        f"hypothesis (corr. -0.077856). The variable 'OverallCond' indicates the number of "
        F"bedrooms which are not related to the sales price or saquare feets. "
        f"In addition, below the distribution of OverallCond by SalePrice\n\n")

    # * Use boxplots or plot of price vs overall condition to compare average prices across categories of overall condition.
    # <img src="" alt="see distribution_of_bedroomabvgr_by_saleprice" width="700">
    st.write("---")

    st.success(
        f"* H4: Renovated houses sell for more: Partly correct \n\n"
        f"The correlation study and the distribution plot don't support the "
        f"hypothesis (corr. -0.077856). The variable 'OverallCond' indicates the number of "
        F"bedrooms which are not related to the sales price or saquare feets. "
        f"In addition, below the distribution of OverallCond by SalePrice\n\n")

    # * Use boxplots or plot of price vs overall condition to compare average prices across categories of overall condition.
    # <img src="" alt="see distribution_of_bedroomabvgr_by_saleprice" width="700">
    st.write("---")

    st.success(
        f"* H5: Renovated houses sell for more: Partly correct \n\n"
        f"Compare average prices of renovated vs not renovated homes."
        f"The correlation study and the distribution plot don't support the "
        f"hypothesis (corr. xxx). The variable 'OverallCond' indicates the number of "
        F"bedrooms which are not related to the sales price or saquare feets. "
        f"In addition, below the distribution of OverallCond by SalePrice\n\n")

    # Check if the year of renovation is recent, and see if it correlates with price increase.
    # <img src="images/02b_distribution_of_yearremodadd_by_saleprice" alt="distribution_of_yearremodadd_by_saleprice" width="700">
    # Correlation value YearRemodadd/SalePrice: 0.507101
    st.write("---")

    st.success(
        f"* H6: Newer houses are more expensive: Partly correct \n\n"
        f"Compare average prices of renovated vs not renovated homes."
        f"The correlation study and the distribution plot don't support the "
        f"hypothesis (corr. xxx). The variable 'OverallCond' indicates the number of "
        F"bedrooms which are not related to the sales price or saquare feets. "
        f"In addition, below the distribution of OverallCond by SalePrice\n\n")

    # * Analyze the relationship between year_built and price.
    # * Convert year to age of house (current_year - year_built) if needed.
    # * Run correlation and scatterplots, or use regression analysis.
    # <img src="images/02b_distribution_of_yearbuilt_by_saleprice.PNG" alt="see distribution_of_yearbuilt_by_saleprice" width="700">
    # Correlation value YearBuilt/SalePrice: 0.522897
    st.write("---")

    #    f"* A house market study showed the sales price correlates with \n "
    #    f"A house with a value between $100.000 - $150.000 typically has GrLivArea = , OverallQual = , as demonstrated by a house maket study.\n "
    #    f"A house with a value between $150.000 - $300.000 typically has GrLivArea = , OverallQual = , as demonstrated by a house maket study.\n "
    #    f"A house with a value min. $300.000 typically has GrLivArea = , OverallQual = , as demonstrated by a house maket study.\n "
    #    f"This insight will be used by the survey team for further discussions and investigations."
