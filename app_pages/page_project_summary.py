import streamlit as st

def page_project_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* The dataset represents a **house market study of Ames, Iowa** "
        f"containing individual house sales prices and further parameter such as first & second floor square meters, kitchen quality, garage area, overall Condition, etc. "
        f" The most relevant parameter are: \n" 
        f" * GarageArea - Size of garage in square feet \n"
        f" * YearBuilt - Original construction date \n"
        f" * OverallQual - Rates the overall material and finish of the house \n"
        f" * MasVnrArea - Masonry veneer area in square feet \n"
        f" * GrLivArea - Above grade (ground) living area square feet \n"
        f" * SalePrice - represents the value of the house \n"
        )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Fl0W97/ci-c5-housing-market-prices).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how the house attributes correlate with the sale price. "
        f" Therefore, the client expects data visualisations of the correlated variables against the sale price to show that. \n"
        f"* 2 - The client is interested in predicting the house sale price from her four inherited houses "
        f"and any other house in Ames, Iowa "
        )
