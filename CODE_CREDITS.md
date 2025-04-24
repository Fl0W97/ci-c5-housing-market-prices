# Code Creadits

I (re)used mainly the code provided in the Code Institute trianing section in the different training chapters and in the Walkthrough projects. In the following not all but main code I resused and adjsuted it for my project.

***Walkthrough Project 02 - Data collection***

<details>
    <summary>Change working directory</summary>

    import os
    current_dir = os.getcwd()
    current_dir

    os.chdir(os.path.dirname(current_dir))
    print("You set a new current directory")

    current_dir = os.getcwd()
    current_dir

</details>

<details>
    <summary>Load Kaggle data</summary>

    import os
    os.environ['KAGGLE_CONFIG_DIR'] = os.getcwd()
    ! chmod 600 kaggle.json

    KaggleDatasetPath = "codeinstitute/telecom-churn-dataset"
    DestinationFolder = "inputs/datasets/raw"   
    ! kaggle datasets download -d {KaggleDatasetPath} -p {DestinationFolder}

    ! unzip {DestinationFolder}/*.zip -d {DestinationFolder} \
    && rm {DestinationFolder}/*.zip \
    && rm kaggle.json

    import pandas as pd
    df = pd.read_csv(f"inputs/datasets/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    df.head()

</details>

<details>
    <summary>Push files to Repo</summary>

    import os
    try:
      os.makedirs(name='outputs/datasets/collection') # create outputs/datasets/collection folder
    except Exception as e:
      print(e)

    df.to_csv(f"outputs/datasets/collection/TelcoCustomerChurn.csv",index=False)

</details>

***Walkthrough Project 02 - Churned Customer Study***

<details>
    <summary>Walkthrough Project 02</summary>

      from ydata_profiling import ProfileReport
      pandas_report = ProfileReport(df=df, minimal=True)
      pandas_report.to_notebook_iframe()

      from feature_engine.encoding import OneHotEncoder
      encoder = OneHotEncoder(variables=df.columns[df.dtypes=='object'].to_list(), drop_last=False)
      df_ohe = encoder.fit_transform(df)
      print(df_ohe.shape)
      df_ohe.head(3)

</details>

***Walkthrough Project 02 - Data Cleaning***

<details>
    <summary>Walkthrough Project 02</summary>

      missing_data_absolute = df.isnull().sum()

      from sklearn.model_selection import train_test_split
      TrainSet, TestSet, _, __ = train_test_split(
                                        df,
                                        df['Churn'],
                                        test_size=0.2,
                                        random_state=0) 

      TrainSet.to_csv("outputs/datasets/cleaned/TrainSetCleaned.csv", index=False)

      TestSet.to_csv("outputs/datasets/cleaned/TestSetCleaned.csv", index=False)

</details>

***Walkthrough Project 02 - featureEngineering***

Function has been customized, however, a lot code is reused from here.

<details>
    <summary>Walkthrough Project 02</summary>

      import scipy.stats as stats
      import matplotlib.pyplot as plt
      import seaborn as sns
      import pandas as pd
      import warnings
      from feature_engine import transformation as vt
      from feature_engine.outliers import Winsorizer
      from feature_engine.encoding import OrdinalEncoder
      sns.set(style="whitegrid")
      warnings.filterwarnings('ignore')


      def FeatureEngineeringAnalysis(df, analysis_type=None):
          """
          - used for quick feature engineering on numerical and categorical variables
          to decide which transformation can better transform the distribution shape
          - Once transformed, use a reporting tool, like ydata-profiling, to evaluate distributions
          """
          check_missing_values(df)
          allowed_types = ['numerical', 'ordinal_encoder', 'outlier_winsorizer']
          check_user_entry_on_analysis_type(analysis_type, allowed_types)
          list_column_transformers = define_list_column_transformers(analysis_type)

          # Loop in each variable and engineer the data according to the analysis type
          df_feat_eng = pd.DataFrame([])
          for column in df.columns:
              # create additional columns (column_method) to apply the methods
              df_feat_eng = pd.concat([df_feat_eng, df[column]], axis=1)
              for method in list_column_transformers:
                  df_feat_eng[f"{column}_{method}"] = df[column]

              # Apply transformers in respective column_transformers
              df_feat_eng, list_applied_transformers = apply_transformers(
                  analysis_type, df_feat_eng, column)

              # For each variable, assess how the transformations perform
              transformer_evaluation(
                  column, list_applied_transformers, analysis_type, df_feat_eng)

          return df_feat_eng


      def check_user_entry_on_analysis_type(analysis_type, allowed_types):
          """ Check analysis type """
          if analysis_type is None:
              raise SystemExit(
                  f"You should pass analysis_type parameter as one of the following options: {allowed_types}")
          if analysis_type not in allowed_types:
              raise SystemExit(
                  f"analysis_type argument should be one of these options: {allowed_types}")


      def check_missing_values(df):
          if df.isna().sum().sum() != 0:
              raise SystemExit(
                  f"There is a missing value in your dataset. Please handle that before getting into feature engineering.")


      def define_list_column_transformers(analysis_type):
          """ Set suffix columns according to analysis_type"""
          if analysis_type == 'numerical':
              list_column_transformers = [
                  "log_e", "log_10", "reciprocal", "power", "box_cox", "yeo_johnson"]

          elif analysis_type == 'ordinal_encoder':
              list_column_transformers = ["ordinal_encoder"]

          elif analysis_type == 'outlier_winsorizer':
              list_column_transformers = ['iqr']

          return list_column_transformers


      def apply_transformers(analysis_type, df_feat_eng, column):
          for col in df_feat_eng.select_dtypes(include='category').columns:
              df_feat_eng[col] = df_feat_eng[col].astype('object')

          if analysis_type == 'numerical':
              df_feat_eng, list_applied_transformers = FeatEngineering_Numerical(
                  df_feat_eng, column)

          elif analysis_type == 'outlier_winsorizer':
              df_feat_eng, list_applied_transformers = FeatEngineering_OutlierWinsorizer(
                  df_feat_eng, column)

          elif analysis_type == 'ordinal_encoder':
              df_feat_eng, list_applied_transformers = FeatEngineering_CategoricalEncoder(
                  df_feat_eng, column)

          return df_feat_eng, list_applied_transformers


      def transformer_evaluation(column, list_applied_transformers, analysis_type, df_feat_eng):
          # For each variable, assess how the transformations perform
          print(f"* Variable Analyzed: {column}")
          print(f"* Applied transformation: {list_applied_transformers} \n")
          for col in [column] + list_applied_transformers:

              if analysis_type != 'ordinal_encoder':
                  DiagnosticPlots_Numerical(df_feat_eng, col)

              else:
                  if col == column:
                      DiagnosticPlots_Categories(df_feat_eng, col)
                  else:
                      DiagnosticPlots_Numerical(df_feat_eng, col)

              print("\n")


      def DiagnosticPlots_Categories(df_feat_eng, col):
          plt.figure(figsize=(4, 3))
          sns.countplot(data=df_feat_eng, x=col, palette=[
                        '#432371'], order=df_feat_eng[col].value_counts().index)
          plt.xticks(rotation=90)
          plt.suptitle(f"{col}", fontsize=30, y=1.05)
          plt.show()
          print("\n")


      def DiagnosticPlots_Numerical(df, variable):
          fig, axes = plt.subplots(1, 3, figsize=(12, 4))
          sns.histplot(data=df, x=variable, kde=True, element="step", ax=axes[0])
          stats.probplot(df[variable], dist="norm", plot=axes[1])
          sns.boxplot(x=df[variable], ax=axes[2])

          axes[0].set_title('Histogram')
          axes[1].set_title('QQ Plot')
          axes[2].set_title('Boxplot')
          fig.suptitle(f"{variable}", fontsize=30, y=1.05)
          plt.tight_layout()
          plt.show()


      def FeatEngineering_CategoricalEncoder(df_feat_eng, column):
          list_methods_worked = []
          try:
              encoder = OrdinalEncoder(encoding_method='arbitrary', variables=[
                                      f"{column}_ordinal_encoder"])
              df_feat_eng = encoder.fit_transform(df_feat_eng)
              list_methods_worked.append(f"{column}_ordinal_encoder")

          except Exception:
              df_feat_eng.drop([f"{column}_ordinal_encoder"], axis=1, inplace=True)

          return df_feat_eng, list_methods_worked


      def FeatEngineering_OutlierWinsorizer(df_feat_eng, column):
          list_methods_worked = []

          # Winsorizer iqr
          try:
              disc = Winsorizer(
                  capping_method='iqr', tail='both', fold=1.5, variables=[f"{column}_iqr"])
              df_feat_eng = disc.fit_transform(df_feat_eng)
              list_methods_worked.append(f"{column}_iqr")
          except Exception:
              df_feat_eng.drop([f"{column}_iqr"], axis=1, inplace=True)

          return df_feat_eng, list_methods_worked


      def FeatEngineering_Numerical(df_feat_eng, column):
          list_methods_worked = []

          # LogTransformer base e
          try:
              lt = vt.LogTransformer(variables=[f"{column}_log_e"])
              df_feat_eng = lt.fit_transform(df_feat_eng)
              list_methods_worked.append(f"{column}_log_e")
          except Exception:
              df_feat_eng.drop([f"{column}_log_e"], axis=1, inplace=True)

          # LogTransformer base 10
          try:
              lt = vt.LogTransformer(variables=[f"{column}_log_10"], base='10')
              df_feat_eng = lt.fit_transform(df_feat_eng)
              list_methods_worked.append(f"{column}_log_10")
          except Exception:
              df_feat_eng.drop([f"{column}_log_10"], axis=1, inplace=True)

          # ReciprocalTransformer
          try:
              rt = vt.ReciprocalTransformer(variables=[f"{column}_reciprocal"])
              df_feat_eng = rt.fit_transform(df_feat_eng)
              list_methods_worked.append(f"{column}_reciprocal")
          except Exception:
              df_feat_eng.drop([f"{column}_reciprocal"], axis=1, inplace=True)

          # PowerTransformer
          try:
              pt = vt.PowerTransformer(variables=[f"{column}_power"])
              df_feat_eng = pt.fit_transform(df_feat_eng)
              list_methods_worked.append(f"{column}_power")
          except Exception:
              df_feat_eng.drop([f"{column}_power"], axis=1, inplace=True)

          # BoxCoxTransformer
          try:
              bct = vt.BoxCoxTransformer(variables=[f"{column}_box_cox"])
              df_feat_eng = bct.fit_transform(df_feat_eng)
              list_methods_worked.append(f"{column}_box_cox")
          except Exception:
              df_feat_eng.drop([f"{column}_box_cox"], axis=1, inplace=True)

          # YeoJohnsonTransformer
          try:
              yjt = vt.YeoJohnsonTransformer(variables=[f"{column}_yeo_johnson"])
              df_feat_eng = yjt.fit_transform(df_feat_eng)
              list_methods_worked.append(f"{column}_yeo_johnson")
          except Exception:
              df_feat_eng.drop([f"{column}_yeo_johnson"], axis=1, inplace=True)

          return df_feat_eng, list_methods_worked



      from feature_engine.selection import SmartCorrelatedSelection
      corr_sel = SmartCorrelatedSelection(variables=None, method="spearman", threshold=0.6, selection_method="variance")

      corr_sel.fit_transform(df_engineering)
      corr_sel.correlated_feature_sets_
      
      corr_sel.features_to_drop_

</details>

***Walkthrough Project 02 - Modeling and Evaluation - Predict Churn***

<details>
    <summary>Walkthrough Project 02 - feature egineering pipeline, partly customized</summary>

      from sklearn.pipeline import Pipeline

      # Feature Engineering
      from feature_engine.selection import SmartCorrelatedSelection
      from feature_engine.encoding import OrdinalEncoder


      def PipelineDataCleaningAndFeatureEngineering():
          pipeline_base = Pipeline([
              ("OrdinalCategoricalEncoder", OrdinalEncoder(encoding_method='arbitrary',
                                                          variables=['gender', 'Partner', 'Dependents', 'PhoneService',
                                                                      'MultipleLines', 'InternetService', 'OnlineSecurity',
                                                                      'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                                                      'StreamingTV', 'StreamingMovies', 'Contract',
                                                                      'PaperlessBilling', 'PaymentMethod'])),

              ("SmartCorrelatedSelection", SmartCorrelatedSelection(variables=None,
              method="spearman", threshold=0.6, selection_method="variance")),

          ])

          return pipeline_base


      PipelineDataCleaningAndFeatureEngineering()

</details>

<details>
    <summary>Walkthrough Project 02 - Custom Class for Hyperparameter Optimisation</summary>

      from sklearn.model_selection import GridSearchCV

class HyperparameterOptimizationSearch:

    def __init__(self, models, params):
        self.models = models
        self.params = params
        self.keys = models.keys()
        self.grid_searches = {}

    def fit(self, X, y, cv, n_jobs, verbose=1, scoring=None, refit=False):
        for key in self.keys:
            print(f"\nRunning GridSearchCV for {key} \n")

            model = PipelineClf(self.models[key])
            params = self.params[key]
            gs = GridSearchCV(model, params, cv=cv, n_jobs=n_jobs,
                              verbose=verbose, scoring=scoring, )
            gs.fit(X, y)
            self.grid_searches[key] = gs

    def score_summary(self, sort_by='mean_score'):
        def row(key, scores, params):
            d = {
                'estimator': key,
                'min_score': min(scores),
                'max_score': max(scores),
                'mean_score': np.mean(scores),
                'std_score': np.std(scores),
            }
            return pd.Series({**params, **d})

        rows = []
        for k in self.grid_searches:
            params = self.grid_searches[k].cv_results_['params']
            scores = []
            for i in range(self.grid_searches[k].cv):
                key = "split{}_test_score".format(i)
                r = self.grid_searches[k].cv_results_[key]
                scores.append(r.reshape(len(params), 1))

            all_scores = np.hstack(scores)
            for p, s in zip(params, all_scores):
                rows.append((row(k, s, p)))

        df = pd.concat(rows, axis=1).T.sort_values([sort_by], ascending=False)
        columns = ['estimator', 'min_score',
                   'mean_score', 'max_score', 'std_score']
        columns = columns + [c for c in df.columns if c not in columns]
        return df[columns], self.grid_searches

</details>

<details>
    <summary>Walkthrough Project 02 - fit model to train data</summary>

      pipeline_data_cleaning_feat_eng = PipelineDataCleaningAndFeatureEngineering()
      X_train = pipeline_data_cleaning_feat_eng.fit_transform(X_train)
      X_test = pipeline_data_cleaning_feat_eng.transform(X_test)
      print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

</details>

<details>
    <summary>Walkthrough Project 02 - split test data</summary>

      from sklearn.model_selection import train_test_split
      X_train, X_test, y_train, y_test = train_test_split(
          df.drop(['Churn'], axis=1),
          df['Churn'],
          test_size=0.2,
          random_state=0,
      )

      print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

    X_train = X_train.filter(best_features)
    X_test = X_test.filter(best_features)

    print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)
    X_train.head(3)

</details>

<details>
    <summary>Walkthrough Project 02 - Finding best hyperparameter</summary>

      models_search = {
          "XGBClassifier":XGBClassifier(random_state=0),
      }

      params_search = {
          "XGBClassifier":{
              'model__learning_rate': [1e-1,1e-2,1e-3], 
              'model__max_depth': [3,10,None],
          }
      }

</details>

<details>
    <summary>Walkthrough Project 02 - feature importance check</summary>

        # create DataFrame to display feature importance
        df_feature_importance = (pd.DataFrame(data={
            'Feature': X_train.columns[pipeline_clf['feat_selection'].get_support()],
            'Importance': pipeline_clf['model'].feature_importances_})
            .sort_values(by='Importance', ascending=False)
        )

        # re-assign best_features order
        best_features = df_feature_importance['Feature'].to_list()

        # Most important features statement and plot
        print(f"* These are the {len(best_features)} most important features in descending order. "
            f"The model was trained on them: \n{df_feature_importance['Feature'].to_list()}")

        df_feature_importance.plot(kind='bar', x='Feature', y='Importance')
        plt.show()

</details>

***Walkthrough Project 02 - Streamlit pages and preparation***

<details>
    <summary>Walkthrough Project 02 - reuse structure of app.py </summary>

      import streamlit as st
      from app_pages.multipage import MultiPage

      # load pages scripts
      from app_pages.page_summary import page_summary_body
      from app_pages.page_churned_customer_study import page_churned_customer_study_body
      from app_pages.page_prospect import page_prospect_body
      from app_pages.page_project_hypothesis import page_project_hypothesis_body
      from app_pages.page_predict_churn import page_predict_churn_body
      from app_pages.page_predict_tenure import page_predict_tenure_body
      from app_pages.page_cluster import page_cluster_body

      app = MultiPage(app_name= "Churnometer") # Create an instance of the app 

      # Add your app pages here using .add_page()
      app.add_page("Quick Project Summary", page_summary_body)
      app.add_page("Customer Base Churn Study", page_churned_customer_study_body)
      app.add_page("Prospect Churnometer", page_prospect_body)
      app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
      app.add_page("ML: Prospect Churn", page_predict_churn_body)
      app.add_page("ML: Prospect Tenure", page_predict_tenure_body)
      app.add_page("ML: Cluster Analysis", page_cluster_body)

      app.run() # Run the  app
</details>

<details>
    <summary>Walkthrough Project 02 - reuse structure of src/predictive_analysis_ui </summary>

      import streamlit as st


      def predict_churn(X_live, churn_features, churn_pipeline_dc_fe, churn_pipeline_model):

          # from live data, subset features related to this pipeline
          X_live_churn = X_live.filter(churn_features)

          # apply data cleaning / feat engine pipeline to live data
          X_live_churn_dc_fe = churn_pipeline_dc_fe.transform(X_live_churn)

          # predict
          churn_prediction = churn_pipeline_model.predict(X_live_churn_dc_fe)
          churn_prediction_proba = churn_pipeline_model.predict_proba(
              X_live_churn_dc_fe)
          # st.write(churn_prediction_proba)

          # Create a logic to display the results
          churn_prob = churn_prediction_proba[0, churn_prediction][0]*100
          if churn_prediction == 1:
              churn_result = 'will'
          else:
              churn_result = 'will not'

          statement = (
              f'### There is {churn_prob.round(1)}% probability '
              f'that this prospect **{churn_result} churn**.')

          st.write(statement)

          return churn_prediction

</details>

<details>
    <summary>Walkthrough Project 02 - reuse structure of src/data_management </summary>

      import streamlit as st
      import pandas as pd
      import numpy as np
      import joblib

      @st.cache_data
      def load_telco_data():
          df = pd.read_csv("outputs/datasets/collection/TelcoCustomerChurn.csv")
          return df


      def load_pkl_file(file_path):
          return joblib.load(filename=file_path)

</details>
