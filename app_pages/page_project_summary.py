import streamlit as st


def page_project_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* The dataset represents a **house market study of Ames, Iowa** "
        f"containing individual house sales prices and further parameter such "
        f"as first & second floor square meters, kitchen quality, garage area "
        f", overall Condition, etc. \n"
        f"* Equally to the term parameter also the term features is used. \n\n"
        f" The most relevant parameter are: \n"
        f" * SalePrice - represents the value of the house \n"
        f" * GrLivArea - Above grade (ground) living area square feet \n"
        f" * OverallQual - Rates overall material and finish of the house "
        f"(10 = highest value)\n"
        f" * YearBuilt - Original construction date \n"
        f" * OpenPorchSF - Masonry veneer area in square feet \n"
        )

    # Link to README file
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Fl0W97/ci-c5-housing-market-prices)."
    )

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how the house "
        f"attributes correlate with the sale price. "
        f"Therefore, the client expects data visualisations of the "
        f"correlated variables against the sale price to show that. \n"
        f"* 2 - The client is interested in predicting the house sale price "
        f"from her four inherited houses and any other house in Ames, Iowa "
        )
