# enable import from 04.ipynb to Page_sales_price_predictor.py
def drop_unwanted_columns(X):
    # Columns to drop from the dataframe
    columns_to_drop = [
        'LotFrontage', '2ndFlrSF', 'GarageYrBlt',
        'EnclosedPorch', 'WoodDeckSF', 'BsmtFinType1', 'LotArea',
        'BsmtUnfSF', 'BedroomAbvGr', 'BsmtExposure', 'OverallCond'
    ]

    # Drop columns that exist in the dataframe
    columns_to_drop = [col for col in columns_to_drop if col in X.columns]

    return X.drop(columns=columns_to_drop)
