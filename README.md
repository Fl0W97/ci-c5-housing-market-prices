# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Template Instructions

Welcome,

this is my project 5 - hose market pricing...


## How to use this repo

1. Use this template to create your GitHub project repo

2. Log into the cloud-based IDE with your GitHub account.

3. On your Dashboard, click on the Create button

4. Paste in the URL you copied from GitHub earlier

5. Click Create

6. Wait for the workspace to open. This can take a few minutes.

7. Open a new terminal and `pip3 install -r requirements.txt`

11. Open the jupyter_notebooks directory and click on the notebook you want to open.

12. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.12.2 as it inherits from the workspace so it will be Python-3.12.2 as installed by our template. To confirm this you can use `! python --version` in a notebook code cell.


## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In your Cloud IDE, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with *Regenerate API Key*.


## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). A fictitious user story is applied where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (i.e. Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|


## Business Requirements

My friend received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although my friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.


## Hypothesis and how to validate

### Hypothesis: Larger square footage often correlates with higher prices.
I suspect the sales price correlates with a high amount of ground living area.

How to validate: 
    - Analyse the dataset and provide a correlation analysis about sales price. See [02_data_cleaning](jupyter_notebooks/02b_mouse_market_study.ipynb)
    - Plot a scatter plot of price vs square_footage. See [02_data_cleaning](jupyter_notebooks/02b_mouse_market_study.ipynb)

### Hypothesis: More bedrooms, higher value.

How to validate:

    - Use boxplots or groupby().mean() to compare average prices across different numbers of bedrooms.

### Hypothesis: Renovated houses sell for more

How to validate: 
    - Compare average prices of renovated vs not renovated homes.
    - Check if the year of renovation is recent, and see if it correlates with price increase.

### Hypothesis: Newer houses are more expensive

How to validate:
    - Analyze the relationship between year_built and price.
    - Convert year to age of house (current_year - year_built) if needed.
    - Run correlation and scatterplots, or use regression analysis.

### Hypothesis: Luxury or convenience features often raise prices
* A house market study showed the sales price correlates with \n "
* A house with a value between $100.000 - $150.000 typically has GrLivArea = , OverallQual = , as demonstrated by a house maket study.\n "
* A house with a value between $150.000 - $300.000 typically has GrLivArea = , OverallQual = , as demonstrated by a house maket study.\n "
* A house with a value min. $300.000 typically has GrLivArea = , OverallQual = , as demonstrated by a house maket study.\n "


How to validate:
  - Analyze certain attributes such as 'OverallQual', 'GarageSF', 'EnclosedPorch' and ceate the clusters low-, mid- and high_price


This insight will be used by the survey team for further discussions and investigations.


## The rationale to map the business requirements to the Data Visualisations and ML tasks

List of business requirements and a rationale to map them to the Data Visualisations and ML tasks.

|  Business requierement | relevant section of visualisations and ML task |
| --- | --- |
| 1 | See [02b_data_cleaning](jupyter_notebooks/02b_house_market_study.ipynb) |
| 2 | See [04_modeling and evaluation](jupyter_notebooks/04_modeling_and_evaluation.ipynb) |


## Decision during Feature engineering

### Zeros in the dataset

The analysis shows that there are zeros in the dataset. Whether those should be transformed depends on:

- The nature of the feature (binary, categorical, or continuous).
- The interpretation of zeros (absence vs. a true zero value).
- The impact of zeros on the target variable (do they have predictive power?).

The zeros represent absence of a feature (e.g., 2ndFlBsmt is a binary flag indicating the presence of a second-floor basement). I don't need to transform them. There are two opitons: A - creating additional features (like a binary indicator for zero values) or B - leave them as-is. (!!add decision!!)

### 1. Categorical Encoding

Categorical variables represent discrete categories. Machine learning models generally require numeric inputs, so categorical variables must be encoded into a numerical form. For the convertion the Label Encoding has been applied. It assigns each category a unique integer.

In the jupyter notebook '02_data cleaning'. The following parameters has been transformed (for correlation analysis): 'BsmtExposure', 'BsmtFinType1' and 'GarageFinish'.
In jupyter notebook '04_modeling_and_evaluation'. The following parameters has been transformed (for pipeline model): (...).

### 2. Numerical Transformation

Numerical features often need to be transformed to improve model performance, especially if their distribution is skewed.
Common Transformation Techniques:

- Normalization: Scaling the values to a range, typically between 0 and 1.
- Standardization: Scaling the values to have a mean of 0 and a standard deviation of 1.
- Log Transformation: Helps with highly skewed data by compressing the range.

Within this project the log transformation is done for 'SalePrice' and 'GarageArea' since thir distribution is skewed.


### 3. Smart Correlation Selection

In a dataset, some features may be highly correlated with others. Keeping highly correlated features in a model can lead to multicollinearity, which can negatively impact model performance.
Method to Select Features Based on Correlation:

- Correlation Matrix: You can compute the correlation matrix to find highly correlated pairs.
- Threshold-based Feature Removal: Remove features that have a correlation higher than a certain threshold, e.g., 0.8 or -0.8.

Within this project, based on the correlation analysis for salePrice and further interpretation of the context the following parameters will be ignored:
'TotalBsmtSF', '1stFlrSF', 'YearRemodAdd', 'GarageYrBlt', 'MasVnrArea', 'BsmtFinSF1', '2ndFlrSF'

### 4. Discretization (Binning)

Discretization (or binning) is the process of transforming continuous variables into categorical ones. This is useful if you want to reduce the impact of outliers or make certain trends more interpretable.

Ideas: 
'EnlosedPorch': 1. Yes, 2. No
'MasVnrArea': 1. Yes, 2. No
(in progress)

### 5. Outlier Detection and Treatment

Outliers can distort model performance and lead to incorrect predictions. Various methods can be used to detect and handle outliers.
Common Outlier Detection Methods:

- IQR (Interquartile Range) Method: Detect outliers based on the IQR, typically using a threshold of 1.5 * IQR.
- Z-score Method: Detect outliers based on the Z-score (values above a certain threshold).

Since the outliers for SalePrice represent real, valid data points, I keep them in the model. The dataset contains examples of extreme property prices, the model should be trained on those extreme values. This ensures the model can predict for higher prices in the future. Example: If you have properties worth $1,000,000 or more, and they are valid sales, it’s important to include them.

A log transformation to the target variable SalePrice is used for Numerical Transformation. This transformation will compress the high values, making the distribution more symmetric and reducing the effect of extreme values, but still allowing the model to learn the overall patterns.

Some machine learning models are more robust to outliers than others. For instance: Random Forest, Gradient Boosting (like XGBoost), and Decision Trees handle outliers relatively well. Linear regression models, however, are more sensitive to extreme outliers and might give distorted results when exposed to such values. Therefore, a more robust ML model is selected.

### Feature Engineering Spreadsheet summary:

- Categorical Encoding (already done in 02_data_cleaning)
- Numerical Transformation (log transformation): 'SalePrice', 'GrLivArea'
- Smart Correlated Selection (there are a various varables with can be dropped due to a high correlation match): ['TotalBsmtSF', '1stFlrSF', 'GarageArea', 'GrLivArea', '2ndFlrSF', 'SalePrice', 'KitchenQual', 'YearBuilt']


| variabels | comment | correlation with SalePrice | Potential Feature Engineering Transformers |
| --- | --- | --- | --- |
|Sale Price| | 1 | Numerical Transformation |
|1stFlrSF|  |  |  |
|2ndFlrSF|  |  |  |
|BedroomAbvGr|  |  |  |
|BsmtExposure|  |  |  |
|BsmtFinType1|  |  |  |
|BsmtFinSF1|  |  |  |
|BsmtUnfSF|  |  |  |
|TotalBsmtSF|  |  |  |
|GarageArea|  |  |  |
|GarageFinish|  |  |  |
|GarageYrBlt|  |  |  |
|GrLivArea|  |  |  |
|KitchenQual|  |  |  |
|LotArea|  |  |  |
|LotFrontage|  |  |  |
|MasVnrArea|  |  |  |
|EnclosedPorch|  |  |  |
|OpenPorchSF|  |  |  |
|OverallCond|  |  |  |
|OverallQual|  |  |  |
|WoodDeckSF|  |  |  |
|YearBuilt|  |  |  |
|YearRemodAdd|  |  |  |


## ML Business Case

* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

The ML task was done by following the CRISP-DM workflow.

<img src="images/crisp-dm_workflow.PNG" alt="crisp-dm_workflow" width="700">


## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.

| Dashboard page name | Screenshot | Content | Comment |
| --- | --- | --- | --- | --- |
| page_project summary |  |  |  |
| page_house_market_study |  |  |  |
| page_project_hypothesis_and_validation |  |  |  |
| page_sales_price_predictor |  |  |  |
| page_pipeline_performance |  |  |  |



## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the .python-version Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

- numpy==1.26.1
- pandas==2.1.1
- matplotlib==3.8.0
- seaborn==0.13.2
- ydata-profiling==4.12.0 # can be removed from requirements before deployment
- plotly==5.17.0
- ppscore==1.1.0 # can be removed from requirements before deployment (tbc)
- streamlit==1.40.2
- feature-engine==1.6.1
- imbalanced-learn==0.11.0 (tbc)
- scikit-learn==1.3.1
- xgboost==1.7.6 (tbc)
- yellowbrick==1.5 # can be removed from requirements before deployment (tbc)
- Pillow==10.0.1 # can be removed from requirements before deployment (tbc)

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Dahsboard was taken partly from Code Institute Walkthorugh 02
* 
* Ideas and supprot of plot analysis was taken from [Specific YouTube Tutorial](https://www.youtube.com/) (to be added)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/) (to be added)
* The template for this project was provided by Code Institute
* 

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from the Code Institute Course 'Delivering Data Science Projects Data Culture and CRISP-DM Workflow CRISP-DM Workflow'
* The images used for the dashboard page XY were taken from (to be added)

## Acknowledgements (optional)


* In case you would like to thank the people that provided support through this project.

