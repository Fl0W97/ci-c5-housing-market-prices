import streamlit as st
import pandas as pd
import numpy as np
from src.data_management import load_pkl_file

def page_sales_price_predictor_body():
    # Streamlit UI for input
    st.title('Sales Price Prediction')
    st.info(
        f"The client is interested in predicting a sales price based on certain input attributes. "
    )
    st.write("---")

    st.write('Enter the details of the property to predict the sales price.')

    # Input form
    gr_liv_area = st.number_input('GrLivArea (Ground Living Area)', min_value=0)
    garage_finish = st.selectbox('GarageFinish', ['Fin', 'RFn', 'Unf', 'None'])
    masonery_area = st.number_input('MasVnrArea', min_value=0)
    basement_finish = st.number_input('BsmtFinSF1', min_value=0)
    open_porch = st.number_input('OpenPorchSF', min_value=0)
    overall_qual = st.selectbox('OverallQual', ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1'])
    year_remod_add = st.number_input('YearRemodAdd', min_value=0)

    # Legend for input form
    if st.checkbox("Open legend for input values"):
        if st.checkbox("GarageFinish options"):    
            st.write(f"*Fin: Finished "
                    f"*RFn: Rough Finished "
                    f"*Unf: Unfinished "
                    f"*None: No Garage "
                    )
        if st.checkbox("OverallQual options"):    
            st.write(f"*10: Very Excellent "
                    f"*9: Excellent "
                    f"*8: Very Good "
                    f"*7: Good "
                    f"*6: Above Average "
                    f"*5: Average "
                    f"*4: Below Average "
                    f"*3: Fair "
                    f"*2: Poor "
                    f"*1: Very Poor "              
                    )


    # Prepare the new input data
    new_data = pd.DataFrame({
        'GrLivArea': [gr_liv_area],
        'GarageFinish': [garage_finish],
        'MasVnrArea': [masonery_area],
        'BsmtFinSF1': [basement_finish],
        'OpenPorchSF': [open_porch],
        'OverallQual': [overall_qual],
        'YearRemodAdd': [year_remod_add]
    })