# Housing Market Prices

Welcome to my fith project [market house pricing](https://analyse-predict-house-market-5a00f7807683.herokuapp.com/). This dashboard contains a house market study and a prediction function for sales prices depending on house features. According to the project requriements and the introduction this dashboard is used by a friend who needs market insights since she is about to sell her four inherited houses in Iowa, Ames.

<img src="images/amiresponsive.PNG" alt="see dashboard on multiple screens" width="700">

## Dashboard overview / features

### Menu / Navigation

This menu is located on the right side and contains 6 links. It can be hidden. The linked pages are the following ones:

<img src="images/overview_menu.PNG" alt="see menu" width="300">

### Quick Project Summary, Page 1

[page_project_summary](page_project_summary.py)

This site contains info blocks and a redirection to the README.me file.

<img src="images/overview_project_summary.PNG" alt="see project summary page" width="700">

### House Market Study, Page 2

[page_house_market_study](page_house_market_study.py)

This site contains 3 buttons (checkboxes) and graphics and three information blocks.

<img src="images/overview_house_market_study.PNG" alt="see house market study page" width="700">

### Project Hypothesis and Validation, Page 3

[page_hypothesis_and_validation](page_hypothesis_and_validation.py)

This site contains 5 hypothesis with text/info blocks and for each hypothesis there is a graphic to back up the result.
By using the functions ".success" or ".warning" each hypothesis is visually highlighted if it's correct the box appears green, if it's wrong the box appears yellow. This page solves business requirement 1.

<img src="images/overview_hypothesis_and_validation.PNG" alt="see project hypothesis and validation page" width="700">

### Sales Price Predictor, Page 4

[page_sales_price_predictor](page_sales_price_predictor.py)

This site contains info text, a table, 5 widgets/input forms and 5 buttons to predict the sales prices. The button "Run Predictive Analysis" deals with the manual input of the user. The other 4 buttons represent the parameters of the provided 4 inherited houses. This page solves business requirement 2.

<img src="images/overview_sales_price_predictor.PNG" alt="see sales price predictor page" width="700">

### Sales Price Evaluator, Page 5

[page_sales_price_evaluation](page_sales_price_evaluation.py)

This site contains info text, a table, 6 widgets/ input forms and 1 button to check if the provided sales price meets the predicted sales price. THis feature helps to validated if the deal is a good one or not.

<img src="images/overview_sales_price_evaluator.PNG" alt="see sales price predictor page" width="700">

### ML: Pipeline Perfoormance, Page 6

[page_pipeline_performance](page_pipeline_performance.py)

This site provides more detailed information about the two pipelines used within this project. The results of the evalaution are also mentioned (MAE, R² score).

<img src="images/overview_ml_pipeline_performance.PNG" alt="see pipeline performance page" width="700">

## Project Kanban Board and User Stories

The project scope is defined as an MVP. The main functionalities for adding comments and methods, as well as browsing through the different methods, have been set up. The "must-have"-User Stories have been labeld in the GitHub project and all relevant tickets for the projec have the milestone: MVP. Further User Stories have been added along the (MVP) project. The user stories have been defined, and all relevant ones for MVP have been closed. In the column 'MVP2', there are user stories defined for further improvements and extensions after the project submission. Milestone MVP is created andd linked with the relevant stories.

***[Project Kanban Board](https://github.com/users/Fl0W97/projects/4/views/1)***

<img src="images/project_kanban_board.PNG" alt="see project kanban board" width="700">

### User Stories

#### Data Practitioners

|Story No.|Titel|User Story|
|---|---|---|
|[#2](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/2)|MVP: Data collection (Create Jupyter Notebook)|As Data Practitioner I can access and upload the client's dataset to prepare for next analysis steps.|
|[#3](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/3)|MVP: Data Cleaning (Create Jupyter Notebook)|As Data Practitioner I preprocess the dataset so that I can continue with the analysis|
|[#4](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/4)|MVP: House Market Study (Jupyter Notebook)|As Data Practioner I can get an overview about the house market so that I can prepare my next steps for feature Engineering and Modeling|
|[#5](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/5)|MVP: Feature Engineering (Create Jupyter Notebook)|As a Data Practitioner I get an deep understanding of the dataset and using feature engineering tools so that I can prepare a data pipeline in the next work step.|
|[#6](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/6)|MVP: Modeling and Evaluation (Create a Jupyter Notebook)|As Data Practitioner I create one or more pipeline models so that I can evaluate and also use the pipelines to meet the business requirement|
|[#8](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/8)|MVP: Documentation (README.md)|As a Data Practitioner and Business Stakeholder I can read through a detailed project description so that I understand what the project is about and what might be adjusted.|
|[#11](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/11)|MVP: Create Page Pipeline Performance (Streamlit)|As Data Practitioner I can see information (and evaluations) about the used pipelines and their performance so that I understand the process and what happens to get the final predictions.|

#### User / friend

|Story No.|Titel|User Story|
|---|---|---|
|[#1](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/1)|MVP: Project Deployment|As a Site User I can *have live access to the dashboard so that I see the information and use functions of the dashboard|
|[#7](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/7)|MVP: Testing Streamlit Dashboard |As a User I want a properly working app so that I can understand the analysis of the house market properly, use the prediction feature and are not stop from error messages or failing functions.|
|[#9](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/9)|MVP: Create Page House Market Study (Streamlit)|As User I can see a house market study so that I get an understanding of the house market.|
|[#10](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/10)|MVP: Create Page Hypothesis and Validation (Streamlist)|As User I can read hypothesis and validation approaches so that I understand if the hypothesis are correct or wrong.|
|[#12](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/12)|MVP: Create Page Project Summary (Streamlit)|As User I get an overview of the project so that I can decide if it makes sense to deep dive.|
|[#13](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/13)|MVP: Create Page Sales Price Predictor (Streamlit)|As User I can predict the sale price when I enter certain attributes so that I can define a sales price for my houses.|
|[#14](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/14)|MVP: Create Page Sales Price Evaluator (Streamlit)|As User I can evaluate if the provided sale price is a good deal when I enter certain attributes and a sales price as offer so that I can define a sales price for my houses.|

## (ML) Business case - Step by step

This project closely follows the CRISP-DM (Cross-Industry Standard Process for Data Mining) workflow — a widely adopted framework for structuring data science and machine learning projects. It consists of six iterative phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment.

Throughout this project, each step maps to the CRISP-DM process. Below, the workflow is broken down into chapters, with examples of how each phase has been addressed. It's important to note that the process is not strictly linear — as shown in the diagram below, the project involved moving back and forth between phases. For example, some decisions made during data cleaning or feature engineering were later revisited and adjusted based on new insights gained in later stages of the workflow.

<img src="images/crisp-dm_workflow.PNG" alt="crisp-dm_workflow" width="700">

The primary objective of this project is to develop a machine learning model that can accurately predict the sales price of residential houses based on key property attributes. The main goal is to provide a solution to a friend. However, the tool enables better pricing strategies for sellers, informed purchasing decisions for buyers, and value estimation for real estate platforms or financial institutions.

In the real estate industry, accurate price prediction is critical for:

* Buyers: Making informed decisions on offers.
* Sellers/Agents: Setting competitive and fair prices.
* Lenders: Assessing property value for mortgage approvals.
* Real Estate Portals: Enhancing user experience with price estimations.

### Business Understanding

The first step in the project focuses on developing a solid understanding of the business context and objectives. This includes an initial review of the dataset, which contains 1460 entries and 24 columns with clear and descriptive variable names. While a few columns are missing, the overall structure and content of the data are well-defined. In addition to exploring the data, the business requirements are outlined to ensure alignment with the project's goals. Finally, a set of initial hypotheses was formulated, each accompanied by a brief explanation of how it could be validated through data analysis.

#### Dataset Content

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

#### Business Requirements

My friend received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although my friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.

* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

### Data collection

Jupyter nootebook: [01_data_collection](jupyter_notebooks/01_data_collection.ipynb)

The original dataset is downloaded from kaggle.com and provided by Code Institute, [Link details](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data). It is unzipped and loaded into the project folder 'input'. There are three data files: One dataset contains the four inherited houses where the sales price should be defined, one file contains the metadata explanation and the last one "house_prices_records.csv" is the main dataset which is handled within this project, it contains variables.
By using pandas a DataFrame is defined and an initial inspection is performed to understand its structure, dimensions, and content (Load and inspect the Kaggle dataset).There are 1460 entries, 0 to 1459, and 24 data columns. Data types of all columns are reviewed to distinguish between numerical and non-numerical features, which is essential for preprocessing and model selection.

**The following parameter do not have a numeric type:**

[BsmtExposure', 'BsmtFinType1', 'GarageFinish', 'KitchenQual'], dtype='object'.

In addition, the dataset is analyzed to detect columns with missing values. The number of missing entries per column is calculated and presented in descending order to highlight areas requiring attention. 

**The following columns have missing Values:**

['EnclosedPorch', 'WoodDeckSF', 'LotFrontage ', 'GarageFinish', 'BsmtFinType1', 'BedroomAbvGr', '2ndFlrSF', 'GarageYrBlt', 'BsmtExposure', 'MasVnrArea']

Last but not least, columns containing zero values are identified and evaluated. The total number of zero values in the dataset is reported, along with a breakdown per column, to assess if zeros may represent missing or invalid data. What is suprising is the fact that the columns 'EnclosedPorch' and 'WoodDeckSF' have a hughe number of missing values, therefore, those variables are not considered for the further analysis.

**The following columns have the value zero:**

['MasVnrArea', '2ndFlrSF', 'openPorchSF', 'BsmtFinSF1', 'BsmtUnfSF', 'EnclosedPorch', 'GarageArea', 'WoodDeckSF', 'TotalBsmtSF', 'BedroomAbvGr']

All values should remain, since it is an indication that the relevant attribute is not available.

With regards to the used code, here a few exampes of the mostly used code snippets that has been (re)used:

|Code snippet|library|Explanation|Comment|
|---|---|---|---|
| `df.info()` | pandas | Provides dataset df information | |
| `df.isnull()` | pandas | identifies missing values in the dataset df | |
| `os.makedirs(name='outputs/data_collected')` | os | creates a folder in repo | |

### Data cleaning

Jupyter notebook: [02_data_cleaning](jupyter_notebooks/02_data_cleaning.ipynb)

The data cleaning phase focus on preparing the dataset for analysis and modeling by improving its quality and consistency. This included handling missing values and correcting incorrect data types. Outliers that could distort model performance haven't been identified. A correlation matrix was created to better understand relationships between features and identify potential issues such as multicollinearity. After cleaning, the dataset was split into training and test sets to support proper model validation. All cleaned and prepared data, along with relevant scripts and notebooks, was versioned and pushed to the repository 'outputs/data_cleaned/...'.

#### Handling missing values

a. Dropping Columns:
Columns with a high proportion of missing data — such as EnclosedPorch, WoodDeckSF, and LotFrontage (with 259 missing values) — are better dropped entirely due to limited usability.

b. Imputing Missing Values:
For columns with a moderate number of missing entries, imputation is a suitable approach, and the method used depends on the type of data:

    Numeric columns: For '2ndFlrSF', 'BedroomAbvGr', 'LotFrontage', 'GarageYrBlt' the mean, median, or mode is used, depending on data distribution.

    Categorical columns: For 'BsmtExposure', 'BsmtFinType1', 'GarageFinish' missing values are filled in using the mode (most frequent value).

    The Column with minimal missing values (MasVnrArea, only 8 missing) is imputed with the mean mode.

    Special case – GarageYrBlt (81 missing): Simple imputation (mean/mode) isn't ideal here. A better strategy might involve group-based imputation or predictive modeling. However, since this column will be removed later, no imputation is performed.

c. Filling with Specific Values:
For certain categorical fields, missing values can be replaced with a placeholder like 'None' or 'Unknown', especially when that makes logical sense in the dataset context.

|Code snippet|library|Comment|
|---|---|---|
| `df.drop(columns=['column_name', 'column_name'])` | pandas | Is used to drop columns |
| `df['column_name'].fillna(df['column_name'].median())` | pandas | Is used to impute values by using the median value |
| `df['column_name'].fillna(df['column_name'].mean())` | pandas | Is used to impute values by using the mean value |

#### Correcting incorrect data types

In the provided dataset there are the following four variables which don't have numeric values.

* `BsmtExposure`
* `BsmtFinType1`
* `GarageFinish`
* `KitchenQual`

For further analysing steps and for the pipeline processing it is mandatory to transfrom those to numeric values. That is done with 'astype(str)'.

1. Convert the columns to string type (it will handle NaN as 'nan' string)
2. Strip any leading/trailing whitespace from the column values
3. Replace string representation of 'NaN' with 'Unknown'
4. Map categorical values to numeric
5. Check the unique values to confirm that the columns contain only valid values
6. Apply numeric conversion safely (handle non-numeric values)

|Code snippet|library|Comment|
|---|---|---|
| `df.info() | pandas | Provides information about range index, Non-Null Count, Dtypes |
| `df['column_name'].asype(str)` | pandas | Converts a column to string data type.|
| `df['column_name'].str.strip()` | pandas | Removes leading and trailing whitespace from string values in a column. |
| `df['column_name'].replace("nan", "Unknown")` | pandas | Replace string representation and map categorical values to numeric.|
| `pd.to_numeric(df['column_name'], errors='coerce')` | pandas | Converts column values to numeric (int or float). Invalid parsing will raise an error unless you pass errors='coerce'.|

#### Handling zeros in the dataset

Columns with Missing Values and Their Counts:
EnclosedPorch    1324
WoodDeckSF       1305
LotFrontage       259
GarageFinish      235
BsmtFinType1      145
BedroomAbvGr       99
2ndFlrSF           86
GarageYrBlt        81
BsmtExposure       38
MasVnrArea          8
dtype: int64

The analysis shows that there are zeros in the dataset. Total Missing Values in the Dataset: 3580. Whether those should be transformed depends on:

* The nature of the feature (binary, categorical, or continuous).
* The interpretation of zeros (absence vs. a true zero value).
* The impact of zeros on the target variable (do they have predictive power?).

The zeros represent absence of a feature (e.g., 2ndFlBsmt is a binary flag indicating the presence of a second-floor basement). There are two opitons: A - creating additional features (like a binary indicator for zero values) or B - leave them as-is. I decided to leave them as-is since the zeros show that a certain feature is not available. Currently a categorical approach by identifiying yes or no of a feature is not part of the analysis.

#### Correlation matrix

<img src="02_correlation_matrix_salesprice" alt="correlation matrix" width="700">

The correlation gives an early insight into data quality, structure, and relationships, helping to clean and shape the data more effectively for modeling. It becomes clear that the highes correlations with 'SalePrice' are 'OverallQual' and 'GrLivArea'.
In addition, it shows that there are 13 columns that contains varibales with a medium correlation between 0.3 and 0.7 and there are 6 columns with a correlation lower than 03.

***High Correlation: Correlation coefficient >0.7***

* OverallQual      0.790982
* GrLivArea        0.708624

***Medium Correlation: Correlation coefficient [0.3,0.7]***

* KitchenQual      0.659600
* GarageArea       0.623431
* TotalBsmtSF      0.613581
* 1stFlrSF         0.605852
* YearBuilt        0.522897
* YearRemodAdd     0.507101
* MasVnrArea       0.477493
* GarageYrBlt      0.466754
* GarageFinish     0.465039
* BsmtFinSF1       0.386420
* LotFrontage      0.334771
* OpenPorchSF      0.315856
* 2ndFlrSF         0.312479

***Low Correlation: Correlation coefficient <0.3***

* LotArea          0.263843
* BsmtFinType1     0.261373
* BsmtExposure     0.229632
* BsmtUnfSF        0.214479
* BedroomAbvGr     0.155784
* OverallCond     -0.077856

|Code snippet|library|Comment|
|---|---|---|
| `correlation_matrix = df.corr()`| pandas | create a correlation matrix |
| `correlation_matrix['SalePrice'].sort_values(ascending=False)` | pandas | focusing on SalesPrice correlations and sort |
| `plt.figure(), plt.title(), plt.show() | matplotlib.pyplot` | create a graphic |
| `sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)` | seaborn | create a graphic/heatmap |

#### Split into training and test sets

The split into trianing and test data is processed a few times wihtin this project. Both datasets are mandatory to apply a ML pipleline. It is a preparation for the next chapters.

|Code snippet|library|Comment|
|---|---|---|
| `os.makedirs(name='...')` | os | Create a directory (e.g., for saving train/test sets); exist_ok=True avoids errors if the folder already exists. |
| `TrainSet, TestSet = train_test_split(df, test_size=0.3, random_state=42)` | sklearn.model_selection | Split the DataFrame into training and testing sets using a 70/30 ratio. |
| `TestSet.to_csv("outputs/data_cleaned/TestSet.csv", index=False)` | pandas | 	Save the test set as a CSV file without the index column. |
| `TrainSet.to_csv("outputs/data_cleaned/TestSet.csv", index=False)` | pandas | Save the train set as a CSV file without the index column. |

### House Market Study

This study explores the key drivers of house prices within the dataset by validating five initial hypotheses using statistical correlation, visual inspection, and distributional comparisons. The dataset includes homes with sale prices ranging from $34,900 to $755,000, with a median sale price of $163,000 and a mean of $180,921. This indicates a slightly right-skewed distribution, with a few high-end properties pulling the average upward.

* The housing market appears to reward size (GrLivArea) more consistently than other features.
* High-end properties, while fewer in number, significantly impact the mean price, suggesting a right-skewed market.
* Features like bedroom count or overall condition alone are not strong indicators of price — buyers seem more influenced by total living space and renovation status.
* Renovation and newer construction positively affect sale price, though with moderate strength.
* Applying log transformation to SalePrice was effective in reducing the influence of outliers and improving model performance.
* Focus on GrLivArea, YearBuilt for modeling or predictive pricing.

#### Hypothesis and how to validate

Jupyter notebook: [02b_house_market_study](jupyter_notebooks/02b_house_market_study.ipynb)

There are five hpothesis generated at the beginning of the project. In the following you see each hypothesis, the result and how it has been validated.

##### Hypothesis (H1): Larger square footage often correlates with higher sales prices. (Correct.)

The first hypothesis suggests that houses with larger living areas tend to have higher sales prices. To validate this, we examined the correlation between square footage and sale price. The results confirmed a strong positive correlation, with larger homes generally commanding higher prices.

* Analyse the dataset and provide a correlation analysis about sales price.
* Plot a distribution of price vs square_footage. To separate both of these variables.

Validation:
See correlation analysis. The Correlation value GrLivArea/SalePrice is high (0.71)
[02_data_cleaning: Correlation analysis](jupyter_notebooks/02b_house_market_study.ipynb)

<img src="images/02_correlation_matrix_salesprice.PNG" alt="correlation matrix" width="700">

[02b_house_market_study: Distribution of GrLivArea by SalePrice](jupyter_notebooks/02b_house_market_study.ipynb)

<img src="images/02b_distribution_of_grlivarea_by_saleprice.PNG" alt="see distribution_of_grlivarea_by_saleprice" width="700">

##### Hypothesis (H2): More bedrooms, higher sales price. (Wrong.)

This hypothesis posits that houses with more bedrooms should fetch higher prices. Upon further analysis, however, the correlation between the number of bedrooms and sale price was weak, suggesting that the number of bedrooms alone is not a significant predictor of price in this market.

* Analyse the dataset and provide a correlation analysis about sales price.
* Use boxplots or plot of price vs number of bedrooms to compare average prices across different numbers of bedrooms.

Validation:
See correlation analysis above. The Correlation value BedroomAbvGr/SalePrice is very low (0.16)

[02b_house_market_study: Distribution of Bedroomabvgr by SalePrice](jupyter_notebooks/02b_house_market_study.ipynb)

<img src="images/02b_distribution_of_bedroomabvgr_by_saleprice.PNG" alt="see distribution_of_bedroomabvgr_by_saleprice" width="700">

##### Hypothesis (H3): Better OverallCond, higher sales price. (Wrong.)

The third hypothesis proposed that homes in better overall condition would be sold at higher prices. However, the analysis showed a very weak negative correlation, indicating that overall condition had little to no effect on the sales price in this dataset.

* Analyse the dataset and provide a correlation analysis about sales price.
* Use boxplots or plot of price vs overall condition to compare average prices across categories of overall condition.

Validation:
See correlation analysis above. The Correlation value OverallCond/SalePrice is very low (-0.078)

[02b_house_market_study: Distribution of OverallCond by SalePrice](jupyter_notebooks/02b_house_market_study.ipynb)

<img src="images/02b_distribution_of_overallcond_by_saleprice.PNG" alt="see distribution_of_bedroomabvgr_by_saleprice" width="700">

##### Hypothesis (H4): Renovated houses sell for more (Partly correct.)

Here, we hypothesized that houses that have been recently renovated would sell for a higher price. The results revealed a moderate correlation, with renovated houses tending to have higher prices, though the effect was not as strong as initially expected.

* Compare average prices of renovated vs not renovated homes.
* Check if the year of renovation is recent, and see if it correlates with price increase.
* Apply statistical test: t-test.

Validation:
See correlation analysis above. The Correlation value YearRemodadd/SalePrice is medium (0.51)

[02b_house_market_study: Comparison_of_old_houses_renovated_vs_not_renovated](jupyter_notebooks/02b_house_market_study.ipynb)

<img src="images/02b_comparison_of_old_houses_renovated_vs_not_renovated.PNG" alt="comparison_of_old_houses_renovated_vs_not_renovated" width="700">

##### Hypothesis (H5): Newer houses are more expensive (Partly correct.)

The final hypothesis suggests that newer houses are more expensive than older ones. Our findings supported this hypothesis to some extent, with a moderate correlation observed between the year of construction and sale price, though other factors also played a significant role in determining the price.

* Compare average prices of new vs old houses.
* Run correlation and scatterplots, or use regression analysis.
* Apply control for confounding. Compare houses of similar characteristics (e.g., same GrLivArea, OverallQual, etc.), only differing in YearBuilt.
* Apply statistical test: t-test.

Validation:
See correlation analysis above. The Correlation value year_built/SalePrice is medium (0.52)

[02b_house_market_study: Comparison_of_sale_price_new_vs_old_houses](jupyter_notebooks/02b_house_market_study.ipynb)

<img src="images/02b_comparison_of_sale_price_new_vs_old_houses.PNG" alt="comparison_of_old_houses_renovated_vs_not_renovated" width="700">

#### The rationale to map the business requirements to the Data Visualisations and ML tasks

List of business requirements and a rationale to map them to the Data Visualisations and ML tasks.

|Business requierement|relevant section of visualisations and ML task|
|---|---|
| 1 | See [02b_data_cleaning](jupyter_notebooks/02b_house_market_study.ipynb)|
| 2 | See [04_modeling and evaluation](jupyter_notebooks/04_modeling_and_evaluation.ipynb)|

### Feature Engineering

Jupyter notebook: [03_featureEngineering](jupyter_notebooks/featureEngineering.ipynb)

Durign the feature Engineering process different tools has been used such as ydata profiling reports, different transformers (categroical encoding, numerical Transformation and SmartCorrelation).

#### YData Profiling Report

The report enables to have a closer look at each variable. The following insighs are noticeable:

|Variable|Comment|
|--|--|
| 2stFlrSF | ~59% zeros, only 41% of the houses have a 2st floor |
| BsmtFinSF1 | 32% of the houses don't have a basement |
| GarageArea | 94% of the houses have a garage, it seems a garage is not a convenient, but mandatory attribute in the market. If a garage is finished or unfinished is not correlating with sales price. |
| TotalBsmtSF | THere are only 2,5% of the houses which don't have a basement. It seems a basement is a mandatory attribute. |
| YearBuilt | A big amount of houses in the dataset has been built around 2000. It seems there are a lot new houses in the market. |
| YearRemodAdd | A noticable amount of houses has been renovated around 2000. |

<img src="images/ydata_profiling_example1.PNG" alt="see ydata profiling report" width="350">
<img src="images/ydata_profiling_example2.PNG" alt="see ydata profiling report" width="350">

|Code snippet|library|Comment|
|---|---|---|
| `from ydata_profiling import ProfileReport`<br>`pandas_report = ProfileReport(df=TrainSet, minimal=True)`<br>`pandas_report.to_notebook_iframe()`| ydata_profiling, pandas | This code imports the ProfileReport class from the ydata_profiling library, which is used to generate an interactive data profiling report for the given dataset (TrainSet). The minimal=True argument generates a simplified version of the report. Finally, to_notebook_iframe() renders the report in a Jupyter Notebook as an iframe, making it interactive within the notebook. |

#### 1. Categorical Encoding

Categorical variables represent discrete categories. Machine learning models generally require numeric inputs, so categorical variables must be encoded into a numerical form. For the convertion the Label Encoding has been applied. It assigns each category a unique integer.

In the jupyter notebook '02_data cleaning'. The following parameters has been transformed (for correlation analysis): 'BsmtExposure', 'BsmtFinType1' and 'GarageFinish'.
In jupyter notebook '04_modeling_and_evaluation'. The following parameters has been transformed (for pipeline model): (...).

|Code snippet|library|Comment|
|---|---|---|
| `from feature_engine.encoding import OrdinalEncoder`<br>`def FeatEngineering_CategoricalEncoder(df_feat_eng, column):`<br>`list_methods_worked = []`<br>`try:`<br>`encoder = OrdinalEncoder(encoding_method='arbitrary', variables=[`<br>`f"{column}_ordinal_encoder"])`<br>`df_feat_eng = encoder.fit_transform(df_feat_eng)`<br>`list_methods_worked.append(f"{column}_ordinal_encoder")`<br>`except Exception:`<br>`df_feat_eng.drop([f"{column}_ordinal_encoder"], axis=1, inplace=True)`<br>`return df_feat_eng, list_methods_worked` | feature_engine | This code defines a function to perform ordinal encoding on a specified categorical column of a DataFrame (`df_feat_eng`). It uses the `OrdinalEncoder` from the `feature_engine` library to convert categories into numeric values based on an arbitrary encoding method. If the encoding is successful, the column is added to the DataFrame, and the method is logged. If an error occurs, the new column is dropped. The function returns the modified DataFrame and a list of methods applied. |

#### 2. Numerical Transformation

Numerical features often need to be transformed to improve model performance, especially if their distribution is skewed.
Common Transformation Techniques:

* Normalization: Scaling the values to a range, typically between 0 and 1.
* Standardization: Scaling the values to have a mean of 0 and a standard deviation of 1.
* Log Transformation: Helps with highly skewed data by compressing the range.

Within this project the log transformation is done for 'SalePrice' and 'GarageArea' since their distribution is skewed.

The graphics show the improvement of the distribution by using log10:
<img src="images/03_feature_engineering_saleprice_log10.PNG" alt="see saleprice_log10_transformation" width="350">
<img src="images/03_feature_engineering_saleprice_w_o_log10.PNG" alt="see saleprice_w_o_log10_transformation" width="350">

<img src="images/03_feature_engineering_grlivarea_log10.PNG" alt="see grlivarea_log10_transformation" width="350">
<img src="images/03_feature_engineering_grlivarea_w_o_log10.PNG" alt="see grlivarea_w_o_log10_transformation" width="350">

| **Code snippet** | **Library** | **Comment** |
|------------------|-------------|------------|
| `from feature_engine import transformation as vt`<br>`def FeatEngineering_Numerical(df_feat_eng, column):`<br>`list_methods_worked = []`<br>`# LogTransformer base 10`<br>`try:`<br>`lt = vt.LogTransformer(variables=[f"{column}_log_10"], base='10')`<br>`df_feat_eng = lt.fit_transform(df_feat_eng)`<br>`list_methods_worked.append(f"{column}_log_10")`<br>`except Exception:`<br>`df_feat_eng.drop([f"{column}_log_10"], axis=1, inplace=True)`<br>`...` | feature_engine | This code defines a function to apply a base-10 log transformation on a specified numerical column of a DataFrame (`df_feat_eng`). The `LogTransformer` from the `feature_engine` library is used to perform the transformation, which can help in normalizing skewed data by compressing high values. If the transformation is successful, the log-transformed column is added to the DataFrame, and the method is logged. If an error occurs, the new column is dropped. |
| `TrainSet['column_name'] = np.log10(TrainSet['column_name'])`<br>`TestSet['column_name'] = np.log10(TestSet['column_name'])` | numpy, pandas | This code applies a log transformation with base 10 to the relevant column of both the training set (`TrainSet`) and the test set (`TestSet`). The transformation helps compress the high values, making the distribution more symmetric and reducing the impact of extreme values. The result is that both datasets now have log-transformed values, which can improve model performance by handling skewed data. |

Similar like the code above further transformer are applied and tested: LogTransformer base e, ReciprocalTransformer, PowerTransformer, BoxCoxTransformer, YeoJohnsonTransformer.

#### 3. Smart Correlation Selection

In a dataset, some features may be highly correlated with others. Keeping highly correlated features in a model can lead to multicollinearity, which can negatively impact model performance.
Method to Select Features Based on Correlation:

* Correlation Matrix: You can compute the correlation matrix to find highly correlated pairs.
* Threshold-based Feature Removal: Remove features that have a correlation higher than a certain threshold, e.g., 0.8 or -0.8.

Within this project, based on the correlation analysis for salePrice and further interpretation of the context the following parameters will be ignored:
'TotalBsmtSF', '1stFlrSF', 'YearRemodAdd', 'GarageYrBlt', 'MasVnrArea', 'BsmtFinSF1', '2ndFlrSF'

***1stFlrSF***:

This feature represents the area of the first floor. It is likely correlated with other features like GrLivArea (the total above-ground living area) or TotalBsmtSF (the total basement area). Including both could introduce redundancy in the model.

Action: Drop this feature to avoid multicollinearity. Keep GrLivArea as it represents the total above-ground living space, which is likely more informative.

***GrLivArea***:

This feature is related to some variables related to the total above-ground living area, which is a strong indicator of house size and price. It’s already closely related to 1stFlrSF, TotalBsmtSF, TotalArea and might also have a relationship with 2ndFlrSF.

Action: This feature is kept. However, feature 2ndFlrSF is being dropped to simplify the model and reduce multicollinearity.

***SalePrice***:

This is the log-transformed version of the target variable, SalePrice. It's highly correlated with GarageArea as well, as shown in the earlier analysis. Since SalePrice is the target variable (the dependent variable you are trying to predict), it should not be used as an independent variable in the model. Hence, it’s correct to drop this feature from the set of predictors, but still necessary for the train and test set.

Action:  'Saleprice' is kept for test and train set. 'GarageArea' is dropped.

***OverallQual***:

This feature represents the overall quality of the house and is highly correlated with KitchenQual and YearBuilt. Since OverallQual is a general measure of the house’s quality, it may be more valuable for predicting SalePrice than other more specific quality features like KitchenQual. In addition, OverallQual does have the highest correlation to SalePrice in the correlation anylsis (02_data_cleaning).

Action: OverallQual is kept, YearBuilt is kept.

***KitchenQual***:

This feature represents the quality of the kitchen, which may be closely related to the overall quality of the house (OverallQual). Dropping one of these two features will reduce redundancy in your dataset.

Action: Drop KitchenQual because OverallQual might already capture the overall quality of the house, including the kitchen.

| **Code snippet** | **Library** | **Comment** |
|------------------|-------------|------------|
| `from feature_engine.selection import SmartCorrelatedSelection`<br>`corr_sel = SmartCorrelatedSelection(variables=None, method="spearman", threshold=0.6, selection_method="variance")`<br>`corr_sel.fit_transform(df_engineering)`<br>`corr_sel.correlated_feature_sets_` | feature_engine | This code imports the `SmartCorrelatedSelection` class from the `feature_engine` library. It initializes an object `corr_sel` with specific parameters to select correlated features from a DataFrame. The method uses the Spearman correlation and a threshold of 0.6 to identify features that are highly correlated. The `fit_transform()` function fits the model to the data and transforms the input DataFrame by removing correlated features based on the specified threshold. The `correlated_feature_sets_` attribute holds the sets of correlated features identified by the method. |
| `corr_sel.features_to_drop_` | feature_engine | This line retrieves the list of features that should be dropped based on the correlation analysis. The `features_to_drop_` attribute of the `SmartCorrelatedSelection` object contains the names of features that have been identified as highly correlated with others and are removed from the dataset. This helps reduce multicollinearity and improves model performance by removing redundant information. |

#### 4. Discretization (Binning) - not applied

Discretization (or binning) is the process of transforming continuous variables into categorical ones. This is useful if you want to reduce the impact of outliers or make certain trends more interpretable. This method could have been used for the house market study. For the new category old/new houses. However, for the pipeline binning is not relevant, as a consequence it hasn't been used during the Feature Engineering process.

#### 5. Outlier Detection and Treatment - not applied

Outliers can negatively impact model performance by skewing results and leading to inaccurate predictions. A common technique for detecting outliers is the Interquartile Range (IQR) method, which identifies outliers as data points falling outside of 1.5 times the IQR from the first or third quartile.

Although this method is effective, in this case, the outliers in the SalePrice column represent genuine, high-value property sales. These data points are not errors but valid examples of high-end properties. Removing them would limit the model’s ability to generalize across the full range of property values, especially for future predictions involving expensive homes (e.g., properties priced at $1,000,000 or more).

To address the skewness introduced by these extreme values, a log transformation was applied to the SalePrice variable. This transformation compresses the range of high values, resulting in a more symmetric distribution and reducing the influence of outliers. As a result, after the transformation, the data no longer contains extreme values that exceed the IQR threshold, and no additional outlier treatment is necessary.

#### Feature Engineering Spreadsheet summary (IN PROGRESS, final features still has to be clarified!

|Variables|Comment| Correlation with SalePrice|Potential Feature Engineering Transformers|
|---------|-------|---------------------------|------------------------------------------|
| SalePrice| Target variable; log-transformed to normalize skewness| 1.00| Numerical Transformation (log)|
| EnclosedPorch| Dropped during data cleaning process due to low correlation and high amount of missing values| 0.13| Dropped|
| WoodDeckSF| Dropped during data cleaning process due to low correlation and high amount of missing values| 0.32| Dropped|
| OpenPorchSF| Dropped during data cleaning process, after house market study, due to low correlation| 0.32| Dropped|
| BsmtFinType1| Dropped during data cleaning process due to low correlation| 0.26| Dropped|
| LotArea| Dropped during data cleaning process due to low correlation| 0.26| Dropped|
| BsmtFinSF1| Dropped during data cleaning process due to low correlation| 0.39| Dropped|
| BsmtUnfSF| Dropped during data cleaning process due to low correlation| 0.21| Dropped|
| LotFrontage| Dropped during data cleaning process due to low correlation| 0.35| Dropped|
| BsmtExposure| Categorical values, Dropped during data cleaning process, after house market study, due to low correlation| 0.12| Dropped|
| BedroomAbvGr| Dropped during data cleaning process, after house market study, due to low correlation, analysis for BedroomAbvGr done| 0.17| Dropped|
| OverallCond| Dropped during data cleaning process, after house market study, due to low correlation, analysis for CverallCond done| 0.08| Dropped|
| 1stFlrSF| Highly correlated with TotalBsmtSF; dropped during Smart Correlated Selection| 0.61| Dropped|
| 2ndFlrSF| Missing values filled using median(), dropped during Smart Correlated Selection| 0.32| Dropped|
| GarageYrBlt| Highly correlated with YearBuilt dropped during Smart Correlated Selection| 0.49| Dropped|
| KitchenQual| Categorical; encoded using OrdinalEncoder; removed during Smart Correlated Selection| 0.51| Dropped|
| YearRemodAdd| Closely related to YearBuilt, removed during Smart Correlated Selection | 0.51| Dropped|
| TotalBsmtSF| Highly correlated with 1stFlrSF; removed during Smart Correlated Selection| 0.61| Dropped|
| GarageArea| Highly correlated with GrLivArea; removed during Smart Correlated Selection| 0.62| None|
| GarageFinish| Categorical; imputed with most frequent value; encoded using OrdinalEncoder, removed during Smart Correlated Selection | 0.55| CategoricalImputer, OrdinalEncoder|
| **YearBuilt**| closely related to YearRemodAdd, retained in final features| 0.52| None|
| **OverallQual**| Strongly correlated with target; retained in final features| 0.79| None|
| ***MasVnrArea***| Imputed with mean values; retained in final model| 0.48| MeanMedianImputer|
| **GrLivArea**| Log-transformed due to skewness; retained in final features| 0.71| Numerical Transformation (log)|

Special thoughts: Keeping GrargeArea or GarageFinished.
* GarageArea has a high  correlation with Sales price
* GarageFinish has no real correlation with any attribute... it seems just not important.. and additional effort is needed for data cleaning, also imputation due to missing values is needed in the pipeline. 

### Modeling

Jupyter notebook: [04_modeling_and_evaluation_regression](04_modeling_and_evaluation_regression.ipynb)

A regression model was used in this project because the target variable—house sale price—is a continuous numerical value, not a category or group. It scales the data, selects features using model's feature importance and fits the model on the selected, scaled features.

Classification models are designed for predicting discrete classes (e.g., “high” vs. “low” price range), while clustering models group similar data points without using a labeled target. Since the goal is to predict the exact sale price based on property features, regression is the appropriate and most effective approach.

#### Data Cleaning and Feature Engineering pipeline (Data Preprocessing Pipeline)

A comprehensive data cleaning and transformation pipeline was implemented using the **scikit-learn** and **feature-engine** libraries. The process begins by loading the data from the "collected_data" folder.

**Step 1: Data Cleaning and Feature Engineering**

The first machine learning pipeline focuses on preprocessing the data and includes the following transformers:

- **DropUnwantedFeatures**: Removes unnecessary columns (defined separately in preprocessing.py)
- **ImputeMasVnrArea**: Fills missing values in the `MasVnrArea` column.
- **ImputeGarageFinish**: Fills missing values in the `GarageFinish` column.
- **OrdinalCategoricalEncoder**: Encodes ordinal categorical features.
- **SmartCorrelatedSelection**: Selects relevant features based on correlation analysis.
- **LogTransformation**: Applies a log10 transformation to the `GrLivArea` feature.

This pipeline is applied to the dataset, resulting in a transformed DataFrame (`df_transformed`).

**Step 2: Train-Test Split and Target Transformation**

After preprocessing, the target variable, `SalePrice`, is transformed using the log10 scale to ensure consistency across both the training and test datasets. The transformed target variable is then split into training and testing sets:

- **X_train** and **y_train** are used for model training.
- **X_test** and **y_test** are reserved for model evaluation.

The feature set (`X`) excludes the target variable `SalePrice`. Following the transformation, the target variable’s distribution is checked for imbalance. As the `SalePrice` variable was log-transformed, no further adjustments are necessary, as the distribution is well-balanced.

| **Code snippet** | **Library** | **Comment** |
|------------------|-------------|-------------|
| `from feature_engine.selection import SmartCorrelatedSelection` | feature_engine | Imports class to detect and remove highly correlated features to reduce multicollinearity. |
| `from feature_engine.encoding import OrdinalEncoder` | feature_engine | Encodes categorical variables using arbitrary integers. Useful for tree-based models. |
| `from feature_engine.transformation import LogTransformer` | feature_engine | Applies logarithmic transformation to reduce skewness in numeric features. |
| `from feature_engine.imputation import MeanMedianImputer, CategoricalImputer` | feature_engine | Imputes missing values using mean/median for numeric and mode for categorical variables. |
| `from src.preprocessing import drop_unwanted_columns` | custom module | Imports user-defined function to remove low-value or irrelevant columns from the dataset. |
| `class HyperparameterOptimizationSearch:` | custom code | Custom class to perform hyperparameter tuning and model evaluation across multiple algorithms. |
| `y_log = np.log10(df['SalePrice'])` | numpy, pandas | Log-transforms target variable to stabilize variance and handle outliers. |
| `X_train, X_test, y_train, y_test = train_test_split(X, y_log, test_size=0.2, random_state=0)` | sklearn | Splits the dataset into training and testing sets, using the transformed target. |
| `pipeline = PipelineDataCleaningAndFeatureEngineering()`<br>`X_train = pipeline.fit_transform(X_train)`<br>`X_test = pipeline.transform(X_test)` | sklearn (custom pipeline) | Applies preprocessing pipeline to both training and test data, ensuring consistent transformations. |
| `plt.figure(figsize=(10, 6))`<br>`sns.histplot(y_train, bins=40, kde=True, color='skyblue')`<br>`plt.axvline(y_train.mean(), color='red', linestyle='--', label=f'Mean: ${y_train.mean():,.0f}')`<br>`plt.axvline(y_train.median(), color='green', linestyle='--', label=f'Median: ${y_train.median():,.0f}')`<br>`plt.title("Distribution of Sale Prices in Training Set")`<br>`plt.xlabel("SalePrice")`<br>`plt.ylabel("Frequency")`<br>`plt.legend()`<br>`plt.show()` | matplotlib, seaborn | Visualizes the distribution of the `SalePrice` in the training set, highlighting mean and median. |

#### Regression pipeline

The second pipeline focuses on regression modeling and sales price prediction. The key steps are as follows:

- **Hyperparameter Optimization**: A search for the best model and hyperparameters is conducted. Multiple regression algorithms, including ExtraTreesRegressor, GradientBoostingRegressor, and others, are evaluated. Among the algorithms tested, ExtraTreesRegressor provided the best performance.

- **Multiple Regression Models**: Several regression models were trained and evaluated with hyperparameter optimization using GridSearchCV. The models tested included:

    - **ExtraTreesRegressor**: Mean score around -0.056811 (best performance).
    - **GradientBoostingRegressor**: Mean score around -0.066239.
    - **XGBRegressor**: Mean score around -0.069641.
    - **RandomForestRegressor**: Mean score around -0.072316.
    - **AdaBoostRegressor**: Mean score around -0.076377.
    - **DecisionTreeRegressor**: Mean score around -0.083047 (lowest performance).

- **Hyperparameter Tuning for ExtraTreesRegressor**: Several hyperparameters for the ExtraTreesRegressor were tested to identify the optimal configuration. The hyperparameters were defined using the `params_quick_search` method.

- **Model Selection**: After the optimization process, the best-performing model and corresponding hyperparameters were selected based on the evaluation results.

- **Model Evaluation**: Predictions were made using the trained model, and performance was evaluated using various metrics. A visual comparison of the actual vs. predicted sales prices was generated. Different scoring methods, such as `neg_mean_absolute_error` and `r2`, were used to assess the pipeline's overall effectiveness.

- **Feature Importance**: The most important features contributing to the model's predictions were identified. The top features in terms of importance were:
    - `OverallQual`
    - `GrLivArea`
    - `YearBuilt`

| **Code snippet** | **Library** | **Comment** |
|------------------|-------------|-------------|
| `models_quick_search = { ... }`<br>`params_quick_search = { ... }` | sklearn, xgboost | Defines multiple regression models (e.g., `XGBRegressor`, `RandomForestRegressor`) with default or empty hyperparameters for later comparison and tuning. Useful for quick model testing. |
| `search = HyperparameterOptimizationSearch(models=models_quick_search, params=params_quick_search)`<br>`search.fit(X_train, y_train, scoring='neg_mean_absolute_error', n_jobs=-1, cv=5)`<br>`search.score_summary(sort_by='mean_score')` | custom/extended sklearn (possibly from `mlxtend` or a custom wrapper) | Runs a hyperparameter optimization search over defined models using cross-validation and a scoring metric (negative MAE). Summarizes performance for comparison. |
| `model = ExtraTreesRegressor(n_estimators=100, random_state=42)`<br>`model.fit(X_train, y_train)` | sklearn | Initializes and fits an `ExtraTreesRegressor` on the training data. A fast and accurate ensemble method useful for feature importance and prediction. |
| `models_quick_search = {"ExtraTreesRegressor": ExtraTreesRegressor(random_state=0)}`<br>`params_quick_search = { "ExtraTreesRegressor": { "model__n_estimators": [100, 200], "model__max_depth": [None, 20], "model__min_samples_split": [2, 5] }}` | sklearn | Sets up model and grid of hyperparameters for `ExtraTreesRegressor` to be used in grid search or tuning, allowing exploration of different configurations. |
| `df_feature_importance = (pd.DataFrame(data={ 'Feature': X_train.columns[feat_selector.get_support()], 'Importance': model.feature_importances_})`<br>`    .sort_values(by='Importance', ascending=False)` | pandas, sklearn | Creates a DataFrame to display feature importance values from the trained model. |
| `best_features = df_feature_importance['Feature'].to_list()` | pandas | Extracts the list of important features based on their importance scores. |
| `df_feature_importance.plot(kind='bar', x='Feature', y='Importance')` | pandas, matplotlib | Plots a bar chart of feature importance for visual analysis. |

#### Feature Refinement

In this step, the pipeline is refined by evaluating additional features. The primary objective is to determine whether the three most important features (`OverallQual`, `GrLivArea`, and `YearBuilt`) alone provide the best results, or if adding one or two more features can enhance the model's performance.

- **Feature Evaluation**: Several feature combinations were tested to identify the optimal feature set for the model. The focus was on whether adding features beyond the top three most important ones would result in better predictive performance.

- **Outcome**: Adding the `MasVnrArea` feature led to a slight improvement in the model's performance. This feature was incorporated into the existing pipeline without requiring additional encoding steps. Unlike the `GarageFinish` feature, which would have required an encoder transformer for categorical data, the `MasVnrArea` feature could be seamlessly integrated into the pipeline. This streamlined integration ensured that the model retained its performance without significant changes to the preprocessing pipeline.

| **Code snippet** | **Library** | **Comment** |
|------------------|-------------|-------------|
| `X_train_refined = X_train[['OverallQual', 'GrLivArea', 'YearBuilt', 'MasVnrArea']]` | pandas | Creates a refined training set by selecting important features (`OverallQual`, `GrLivArea`, `YearBuilt`, `MasVnrArea`) for model training. |
| `model.fit(X_train_refined, y_train)` | sklearn | Fits the regression model using the refined feature set. |

#### Final Model Training and Evaluation

The final training and evaluation process includes:

* Splitting the data into training and test sets.
* Applying the Data Cleaning and Feature Engineering pipeline to both the training and testing data.
* Applying the Regressor Pipeline, which includes the best model, hyperparameters, and features, to the training set.
* Evaluating the model’s performance, with results visualized through graphics comparing actual vs. predicted sales prices.


|Metric | Value | What It Means|
|-------|-------|--------------|
|MAE | $19,473 | On average, your model's predictions are off by less than $20K. For house prices, that’s very acceptable, especially for mid-to-upper priced homes.|
|RMSE | $33,867 | This gives an idea of the “typical” error. It’s only slightly higher than MAE, which suggests that large outliers are not dominating the error.|
|R² Score | 0.83 | Your model explains 83% of the variance in sale prices — this is very good for a regression problem in real estate, where 70–85% is typically strong.|

| **Code snippet** | **Library** | **Comment** |
|------------------|-------------|-------------|
| `from sklearn.metrics import mean_absolute_error, r2_score` | sklearn | Imports evaluation metrics for measuring model performance. |
| `y_pred_log = pipeline_regressor.predict(X_test)` | sklearn | Predicts target values using the trained model; outputs are in log scale. |
| `y_pred = np.power(10, y_pred_log)`<br>`y_test_actual = np.power(10, y_test)` | numpy | Converts log-scale predictions and true values back to their original scale. |
| `mae = mean_absolute_error(y_test_actual, y_pred)` | sklearn | Calculates the average absolute error between predicted and actual prices. |
| `mse = mean_squared_error(y_test_actual, y_pred)`<br>`rmse = mean_squared_error(y_test_actual, y_pred, squared=False)` | sklearn | Computes squared error and its root, capturing average and large prediction errors. |
| `r2 = r2_score(y_test_actual, y_pred)` | sklearn | Measures how well the model explains the variance in actual house prices. |

#### Model and Data Storage

Once the final model has been trained and evaluated, the training data, test data, and pipeline (in .pkl format) are stored in the repository for future use.

#### Integration of Pipelines (in progress)

The final step involves merging the two separate pipelines (data cleaning and feature engineering, and regressor pipeline) into a unified pipeline. This consolidated pipeline streamlines the entire process, from data preprocessing to prediction, ensuring consistency across training, testing, and deployment.

### Suggestions for Future Improvements:

* Setting up one complete pipeline that combines the data cleaning and feature engineering pipeline and teh regressor pipeine.
* Model Monitoring: After deployment, consider adding monitoring tools to track the model's performance on new, unseen data.
* Cross-Validation: To ensure robustness, consider using cross-validation techniques for model evaluation.

### Outcome / Business impact

The final machine learning model achieved a strong level of predictive accuracy while relying on just five key features, making it both efficient and easy to interpret. By carefully balancing data preprocessing, feature selection, and algorithm tuning, the solution is optimized for performance and scalability. The streamlined pipeline is well-suited for integration into real-world applications where reliable, fast, and accurate house price estimation is essential.

This predictive model delivers tangible value to the requestor (a friend) by significantly improving pricing accuracy, thereby reducing the risks associated with underpricing or overpricing properties. It enables more efficient operations by automating the valuation process and supports better decision-making through data-driven insights. This tool could be used by further stakeholders such as end users—buyers, sellers, and financial institutions—it enhances trust in pricing information, contributing to more transparent and confident transactions across the housing market.

## Deployment

For detailed deployment information, see the content related to testing in [DEPLOYMENT.md](DEPLOYMENT.md).

## Testing

For detailed testing information, see the content related to testing in [TESTING.md](TESTING.md).

## Tools & Technologies used

### Main Data Analysis and Machine Learning Libraries

| Library / Package         | Purpose / Description                                                                 | Comment |
|---------------------------|----------------------------------------------------------------------------------------|--------| 
| numpy==1.26.1             | Numerical operations and array handling                                                ||
| pandas==2.1.1             | Data manipulation and analysis                                                         ||
| matplotlib==3.8.0         | Static data visualization                                                              ||
| seaborn==0.13.2           | Statistical data visualization built on top of matplotlib                             ||
| ydata-profiling==4.12.0   | Automated EDA (exploratory data analysis) – removed before deployment                  |# removed from requirements before deployment|
| plotly==5.17.0            | Interactive visualizations for exploratory analysis and dashboards                     ||
| ppscore==1.1.0            | Predictive Power Score for evaluating feature-target relationships    |# removed from requirements before deployment|
| streamlit==1.40.2         | Web application framework for deploying ML models and data apps                       ||
| feature-engine==1.6.1     | Feature engineering and preprocessing tools for machine learning pipelines             ||
| imbalanced-learn==0.11.0  | Handling class imbalance in datasets (TBC – usage may be limited in regression context)||
| scikit-learn==1.3.1       | Core ML library used for modeling, pipelines, and evaluation                          ||
| xgboost==1.7.6            | Gradient boosting algorithm used for high-performance regression                ||

### Languages

*Python 3.12.1: The primary programming language used for developing the backend of the website.

### Other tools

* [Jupyter Notebook](https://jupyter.org/): used to built jupyter nootebooks, structure code and tests
* [Git](https://git-scm.com/): The version control system that tracks changes in the code and enables collaboration among developers.
* [Gitpod](https://www.gitpod.io/): A cloud-based IDE used for local development and coding.
* [Pip3](https://pypi.org/): The Python package manager used to install and manage project dependencies.
* [GitHub](https://github.com/): A platform that hosts the website’s source code and facilitates project management through features like the Kanban board.
* [Chrome DevTools](https://developer.chrome.com/docs/devtools): The developer tools in Google Chrome used to debug and inspect the website’s frontend.
* [Firefox DevTools](https://firefox-source-docs.mozilla.org/devtools-user/): The developer tools in Firefox used to debug and inspect the website’s frontend.
* [Font Awesome](https://fontawesome.com/): A library used to incorporate scalable vector icons into the website.
* [W3C Validator](https://validator.w3.org/): A tool used to validate the HTML5 code to ensure it follows best practices and standards.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): A tool used to validate the CSS code, ensuring it conforms to web standards.
* [PEP8](https://pep8ci.herokuapp.com/): A tool used to check the Python code against the PEP8 coding standards for readability and consistency.
* [Heroku](https://www.heroku.com): A cloud platform used to deploy and host the website in a production environment.
* [Tinypng](https://tinypng.com/): Used for reducing image size
* [Languagetool](https://languagetool.org/): Free grammar checker for checking my project documentation

## Credits

### Content

* [Specific YouTube Tutorial](https://www.youtube.com/) Ideas and supprot of plot analysis was taken from (to be added)
* [Project Methods Library](https://github.com/Fl0W97/ci-p4-methods-library)The structure of the documentation has been reused from my project 4
* [Code_Institute](https://codeinstitute.net) - The code and text for project and Dashboard was taken partly from Code Institute Walkthorugh 02 and 01
* [Code Institute](https://codeinstitute.net) - Tutorial: Data Analytics Packages ML: feature-engine, Data Analytics Packages ML: Scikit-learn ... 
* [Code_Institute](https://codeinstitute.net) - The template for this project was provided by Code Institute
* [Code_Institute](https://codeinstitute.net) - Mentor Rohit: Providing guidance and tips for my project
* [Youtube](https://www.youtube.com/): for access to a huge community of developers who facing similar challenges like me
* [SessionLab](https://www.sessionlab.com/): for access to various free Methods to fill the database and insiration for functionalities
* [Stackoverflow](https://stackoverflow.com/): for access to a huge community of developers who facing similar challenges like me
* [Scikit-learn](https://scikit-learn.org/stable/): for accessing to documentation and code
* [Scilkt-learn ML algorithms](https://scikit-learn.org/stable/api/sklearn.ensemble.html): for various ML algorithms
* [Matplot](https://matplotlib.org/): for accessing to documentation and code

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from the Code Institute Course 'Delivering Data Science Projects Data Culture and CRISP-DM Workflow CRISP-DM Workflow'
* The images used for the dashboard page XY were taken from (to be added)

### Code

For detailed Code Credit information, see the content related to testing in [CODE_CREDITS.md](CODE_CREDITS.md).

### Templates

*For this project I reused the provided [Code Institute Template](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues)
