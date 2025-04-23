# Testing

* Testing was conducted regularly in small intervals throughout the development process as well as at the end of the project to ensure functionality and identify any potential issues early on.
* Bugs that were encountered during testing have been thoroughly documented in the Bug section, detailing the nature of the issue and the steps taken to resolve it.
* Validators were used to ensure that the code meets all necessary standards and specifications. More details can be found in the Validators chapter.
* Logic checks were performed to verify that the program's operations and algorithms were working as intended. This included testing different scenarios and edge cases to ensure robustness.
* Manual input tests were carried out to simulate real-world usage of the application. This involved entering data manually into the system to ensure that all inputs were handled correctly and that the user interface responded appropriately.

## Manual Testing Plan
|Test Area|Objective|Test Steps|Test Cases|Test Completed|Comments|
|---|---|---|---|---|---|
|Navigation Functionality|Ensure that the website navigation is intuitive and functional.| 1. Open the homepage. <br> 2. Click on various menu items or links. <br> 3. Verify correct redirection. <br> 4. Verify active menu item highlight. <br> 5. Test the menu hide feature.|- **Responsive Navigation**: Test navigation across different screen sizes. <br> - **Menu Items**: Ensure the menu items lead to correct pages.|[ y ]|---|
|Project Summary|Ensure that the summary page content is understandable, describes the project and has a structured format and the available functions work| 1. Read through project overview and terminology sections. <br> 2. Check the functionality of the README.md link. |- Project is clearly described. <br> - Key terms and business context are explained. <br> - External links work correctly.|[ y ]|---|
|House Market Study|Ensure that the page content is clear and the interactive elements work as expected.| 1. Test Checkbox 'Inspect House market data' <br> 2. Test Checkbox 'Show SalePrice Distribution' <br> 3. Test Checkbox 'Inspect Correlation Heatmap'|- Visualizations render correctly. <br> - Information is clearly presented. <br> - All checkboxes trigger the correct outputs.|[ y ]|---|
|Tool: Hypothesis and Validation|Ensure that the hypothesis testing visualizations and conclusions are understandable.|1. View correlation heatmap. <br> 2. View distribution plots for 'GrLivArea', 'BedroomAbvGr', 'OverallCond'. <br> 3. Compare graphics about prices between Renovated/Non-renovated and New/Old houses.|- Charts load and update correctly. <br> - Price comparisons are visible and logical. <br> - Hypotheses are supported with clear visual evidence.|[ y ]|---|
|Tool: Sales Price Predictor|Ensure that the model correctly predicts prices based on input or predefined data.| 1. Fill out 5 input widgets. <br> 2. Click 'Predictive Analysis'. <br> 3. Use buttons to predict prices for predefined houses (House 1–4). | - Input is accepted and processed. <br> - Predictions are displayed for both custom and predefined inputs.|[ y ]|---|
|Tool: Sales Price Evaluator|Ensure that the evaluator can determine if a price is a good deal compared to market prediction.| 1. Fill out 5 feature input widgets. <br> 2. Enter a sales price. <br> 3. Click 'Run Price Check'.|- Market value is predicted. <br> - User's input price is compared to predicted value. <br> - App states whether it’s a good, bad, or fair deal.|[ y ]|---|
|ML: Pipeline Performance|Ensure that machine learning pipeline steps and performance metrics are correctly displayed. |  1. Review pipeline visualizations (data cleaning, feature engineering, regression). <br> 2. Check model evaluation values (e.g., MAE, R²). |- Pipeline structure is explained. <br> - Performance metrics are clearly visible and accurate. <br> - Models are logically compared if applicable.|[ y ]|---|

## Additional Testing Considerations

These are additional tests to ensure the overall quality, performance, security, and compatibility of the website across different platforms.

| **Test Area** | **Objective** | **Test Steps**| **Test Cases** | **Test Completed** | **Comments** |
|---------------|-------------- |---------------|----------------|--------------------|--------------|
| **1. Cross-browser Testing** | Ensure the website works correctly across different web browsers.                                                | 1. Open the website in Chrome. <br> 2. Open the website in Firefox. <br> 3. Open the website in Edge. <br> 4. Open the website in Safari. <br> 5. Test basic functionality (navigation, login, forms) in each browser. | - **Browser Compatibility**: Ensure that features are functional across Chrome, Firefox, Edge, and Safari. <br> - **CSS and Layout**: Verify the website layout and styles appear correctly in all browsers. <br> - **JavaScript**: Ensure JavaScript runs properly across all browsers. <br> - **Responsive Layout**: Test that the website is responsive and adapts to different screen sizes in each browser. |[ y ]||
| **2. Mobile Testing**        | Ensure that the website is fully responsive and works on different mobile devices.                               | 1. Open the website on a mobile device (or simulate using browser dev tools). <br> 2. Test website navigation. <br> 3. Test form submissions and interactive elements (login, comment forms, etc.) on mobile. <br> 4. Test responsiveness on different screen sizes. | - **Mobile Compatibility**: Ensure the website is usable on mobile browsers (Chrome, Safari, Firefox). <br> - **Touch Interaction**: Test touch interactions, such as tapping and swiping. <br> - **Mobile Layout**: Verify proper layout on small screens and large mobile devices. <br> - **Performance on Mobile**: Ensure the website loads and interacts on mobile devices. |[ y ]||

## Testing User Stories

### User Stories for Data Practitioner

**No.** | **User Story** | **Requirement met (y/n)** |
| ------|--------------- |---------------------------|
|#2|As Data Practitioner I can access and upload the client's dataset to prepare for next analysis steps.| y |
|#3|As Data Practitioner I preprocess the dataset so that I can continue with the analysis| y |
|[#4](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/4)|As Data Practioner I can get an overview about the house market so that I can prepare my next steps for feature Engineering and Modeling| y |
|[#5](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/5)|As a Data Practitioner I get an deep understanding of the dataset and using feature engineering tools so that I can prepare a data pipeline in the next work step.| y |
|[#6](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/6)|As Data Practitioner I create one or more pipeline models so that I can evaluate and also use the pipelines to meet the business requirement| y |
|#8|As a Data Practitioner and Business Stakeholder I can read through a detailed project description so that I understand what the project is about and what might be adjusted.| y |
|#11|As Data Practitioner I can see information (and evaluations) about the used pipelines and their performance so that I understand the process and what happens to get the final predictions.| y |

### User Stories for User

**No.** | **User Story** | **Requirement met (y/n)** |
| ------|--------------- |---------------------------|
|[#1](https://github.com/Fl0W97/ci-c5-housing-market-prices/issues/1)|As a Site User I can *have live access to the dashboard so that I see the information and use functions of the dashboard| y |
|#7|As a User I want a properly working app so that I can understand the analysis of the house market properly, use the prediction feature and are not stop from error messages or failing functions.| y |
|#9|As User I can see a house market study so that I get an understanding of the house market.| y |
|#10|As User I can read hypothesis and validation approaches so that I understand if the hypothesis are correct or wrong.| y |
|#12|As User I get an overview of the project so that I can decide if it makes sense to deep dive.| y |
|#13|As User I can predict the sale price when I enter certain attributes so that I can define a sales price for my houses.| y |

## Unfixed Bugs

There are no unfixed bugs.

## Fixed Bugs & Errors messages

<details><summary>***NameError: name 'PipelineClf' is not defined***</summary>

Image (Error):

<img src="images/fixed_bugs_run_multiple_algorithms_error.PNG" width="800"/>

Image (Code):

<img src="images/fixed_bugs_run_multiple_algorithms_code2.PNG" width="800"/>

Comment:
The name PipelineClf was used by mistake due to copy-paste from an earlier classification project. It does not exist in this context.

Fix:
Updated to use the correct pipeline name for regression.

</details>

<details><summary>***ValueError: could not convert str to float: 'No' ***</summary>

Image (Error):

<img src="images/fixed_bugs_scale_data_error.PNG" width="800"/>

Image (Code):

<img src="images/fixed_bugs_scale_data_code.PNG" width="800"/>

Comment:
Data scaling failed due to unexpected input types or missing values.

Fix:
Ensured that input features are correctly preprocessed and numeric before scaling.

</details>

<details><summary>***KeyError: "[SalePRice"] not in index"***</summary>

Error: Target Imbalance (Visualization)

Image (Error):

<img src="images/fixed_bugs_target_imbalance_error.PNG" width="800"/>

Image (Code):

<img src="images/fixed_bugs_target_imbalance_code1.PNG" width="800"/> 

<img src="images/fixed_bugs_target_imbalance_code2.PNG" width= "800"/>

Fix:
<img src="images/fixed_bugs_target_imbalance_fix.PNG" width="800"/>

Comment:
Initial suspicion of imbalance in target distribution was resolved after applying a log10 transformation.

</details>

<details><summary>***KeyError: "['LotFrontage','GarageFinish', '2ndFlrSF' (...)] not found in axis" (1)***</summary>

Widget dashboard columns are not dropped

Image (Error): 

<img src="images/fixed_bugs_widget_dashboard_columns_are_not_dropped_error.PNG" width="800"/>

Image (Code): 

<img src="images/fixed_bugs_widget_dashboard_columns_are_not_dropped_code.PNG" width="800"/>

Comment:
Drop functionality in the dashboard did not execute correctly due to notebook environment limitations.

Fix:
Moved the drop logic into a dedicated Python file: src.preprocessing.py.

</details>

<details><summary>***Error: KeyError: "['TotalArea'] not found in axis"***</summary>

Image (Error):
No image provided

Code:

`df_engineering = df_engineering.drop(columns=['TotalBsmtSF', '1stFlrSF', 'GarageArea', '2ndFlrSF', 'KitchenQual', 'YearBuilt', 'TotalArea'])`

Comment:
The variable TotalArea does not exist anymore. It was originally introduced to combine variables like GrLivArea, 1stFlr, and 2ndFlr, but later removed due to low value.

Fix:
The variable TotalArea was removed from the drop list.

</details>

<details><summary>***KeyError: "['LotFrontage','GarageFinish', '2ndFlrSF' (...)] not found in axis" (2)***</summary>

Widget dashboard column mismatch

Image (Error): 

<img src="images/fixed_bugs_widget_dashboard_columns_drop_error.PNG" width="800"/>

Image (Code): 

<img src="images/fixed_bugs_widget_dashboard_columns_drop_code.PNG" width="800"/>

Fix:

<img src="images/fixed_bugs_widget_dashboard_columns_drop_fix.PNG" width="800"/>

Comment:
Test set had a mismatch in columns due to inconsistencies in feature dropping.

</details>

<details><summary>***KeyError: OverallQual ***</summary>

Error: Typo in widget name OverallQual

Image (Error):

<img src="images/fixed_bugs_widget_dashboard_overallqual_error.PNG" width="800"/>

Image (Code):

<img src="images/fixed_bugs_widget_dashboard_overallqual_code.PNG" width="800"/>

Fix:

<img src="images/fixed_bugs_widget_dashboard_overallqual_fix.PNG" width="800"/>

Comment:
Typo in the widget name caused the dashboard to break.

</details>

<details><summary>***NameError: name 'y_test_opt_log' is not defined.***</summary>

Page Pipeline performance is not displayed when streamlit is started.

Image (Error):

<img src="images/fixed_bugs_show testdata_pipeline_performance_error.PNG" width="800"/>

Image (Code):

<img src="images/fixed_bugs_show testdata_pipeline_performance_code.PNG" width="800"/>

Fix:

<img src="images/fixed_bugs_show testdata_pipeline_performance_fix.PNG" width="800"/>

Comment:
Model pipeline was not loaded or passed properly, resulting in evaluation failure.

</details>

<details><summary>***AttributeError: 'dict' object has no attribute 'filter'***</summary>

Page_sales_price_predictor.py was not loaded via Streamlit.
Missing df in predictor.

Image (Error):

<img src="images/fixed_bugs_page_sales_price_predictor_missing_df_error.PNG" width="800"/>

Image (Code):

<img src="images/fixed_bugs_page_sales_price_predictor_missing_df_code.PNG" width="800"/>

Fix:

<img src="images/fixed_bugs_page_sales_price_predictor_missing_df_fix.PNG" width="800"/>

Comment:
df was not correctly loaded or defined in the prediction function scope.

</details>

<details><summary>***NameError: name 'mean_absolute_error' is not defined***</summary>

Streamlit page is not running.

Image (Error):

<img src="images/fixed_bugs_missing_import_pipeline_performance_error.PNG" width="800"/>

Image (Code):

<img src="images/fixed_bugs_missing_import_pipeline_performance_code.PNG" width="800"/>

Fix:

<br> <img src="images/fixed_bugs_missing_import_pipeline_performance_fix.PNG" width="800"/>

Comment:
Forgot to import a required pipeline function 'mean_absolute_error' in the evaluation script.

</details>

<details><summary>***FileNotFoundError***</summary>

Error was displayed during Heroku Deployment.

Image (Error):

<img src="images/fixed_bugs_heroku_deployment_error.PNG" width="800"/>

Comment:
Errors occurred due to missing files or incorrect file paths during Heroku deployment.

Fix:
Added proper working directory setup using os.chdir() and ensured file availability.

</details>

## Validator Testing
Validator testing has been done on:

### [CI Python validator](https://pep8ci.herokuapp.com/)
No errors were returned.

<details>
    <summary>see details about CI Python validator</summary>

#### app.py

<img src="images/ci_python_validator_app.PNG" alt="shows result of validation of app.py" width="650">

#### app_pages/multipage.py

<img src="images/ci_python_validator_multipage.PNG" alt="shows result of validation of multipage" width="650">

#### app_pages/page_project_summary.py

<img src="images/ci_python_validator_page_project_summary.PNG" alt="shows result of validation of page_project_summary" width="650">

#### app_pages/page_house_market_study.py

<img src="images/ci_python_validator_page_hose_market_price.PNG" alt="shows result of validation of page_house_market_price" width="650">

#### app_pages/page_hypothesis_and_validation.py

<img src="images/ci_python_validator_hypothesis_and_validation.PNG" alt="shows result of validation of validator_hypothesis_and_validation" width="650">

#### app_pages/page_sales_price_predictor.py

<img src="images/ci_python_validator_page_sale_price_predictor.PNG" alt="shows result of validation of page_sale_price_predictor" width="650">

#### app_pages/page_sales_price_evaluation.py

<img src="images/ci_python_validator_page_sale_price_evaluation.PNG" alt="shows result of validation of page_sale_price_evaluation" width="650">

#### app_pages/page_pipeline_performance.py

<img src="images/ci_python_validator_page_pipeline_performance.PNG" alt="shows result of validation of page_pipeline_performance" width="650">

#### src/data_management.py

<img src="images/ci_python_validator_data_management.PNG" alt="shows result of validation of data_management py" width="650">

#### src/preprocessing.py

<img src="images/ci_python_validator_preprocessing.PNG" alt="shows result of validation of preprocessing py" width="650">

#### src/machine_learning/predictive_analysis_ui

<img src="images/ci_python_validator_predictive_analysis_ui.PNG" alt="shows result of validation of predictive_analysis_ui py" width="650">

#### src/machine_learning/evaluation

<img src="images/ci_python_validator_evaluation.PNG" alt="shows result of validation of evaluation py" width="650">

</details>

### [HTML validator](https://validator.w3.org/)
No errors were returned. However, a few warnings. They will be not fixed. HTML is not focus of this porject and is be provided from streamlit standard.

<details>
<summary>see details about HTML validator</summary>

<img src="images/html_validator_results.PNG" alt="shows result of HTML validation" width="650">

</details>

### [CSS validator](https://jigsaw.w3.org/css-validator/)
A few errors has been returned. However, the errors do not seem to interfere with the use of the dashboard I ignore them. CSS is not focus of this project and is be provided from streamlit standard.

<details>
<summary>see details about CSS validator</summary>

<img src="images/css_validator_results.PNG" alt="shows result of CSS validation" width="650">

</details>

### Validation functions for Dashboard
In Streamlit a few validation funtions are applied as standard i.e. by using a widget input data is only accepted when they are correct.

## Lighthouse Reports
LightHouse is a web performance testing tool used to assess a website's performance. The report is generated through Google Chrome.
The scoring for SEO, Accessibility and Best PRactices is high. Room for improvement is the Performance. This might be happen due to the project's size of around 450MB. The soft limit of the maximal slug size from Heroku is reached. By ignoring certain data already via .slugignore the Performance has been already improved.

<img src="readme.images/lighthouse_validation_report"shows Lighthouse report generated by GoogleChrome" width="700">

## Responsivness
The responsiveness was manually tested using Chrome's devtools throughout the entire development process.

<img src="images/amiresponsive.PNG" alt="shows usage of DevTool by GoogleChrome" width="700">

## Accessability
I confirm that the selected colors and fonts are easy to read and accessible by using Lighthouse in devtools (Chrome), see chapter "Lighthouse reports".
