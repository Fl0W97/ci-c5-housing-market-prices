# Deployment

## Heroku
The site was deployed to a Heroku page using a GitHub repository for data storage.

* The [App live link](https://analyse-predict-house-market-5a00f7807683.herokuapp.com/)
* The project is stored on [GitHub](https://github.com/Fl0W97/ci-c5-housing-market-prices)

## Preparation

Make sure that the following files are created in the project environment before connect it with Heroku:

### setup.sh
    mkdir -p ~/.streamlit/
    echo "\
    [server]\n\
    headless = true\n\
    port = $PORT\n\
    enableCORS = false\n\
    \n\
    " > ~/.streamlit/config.toml """

### Procfile
    web: sh setup.sh && streamlit run app.py

### runtime.txt
    python-3.12.8

### requirements.txt
    numpy==1.26.1
    pandas==2.1.1
    matplotlib==3.8.0
    seaborn==0.13.2
    ydata-profiling==4.12.0 (can be removed from requirements before deployment)
    plotly==5.17.0
    ppscore==1.1.0 (can be removed from requirements before deployment)
    streamlit==1.40.2
    feature-engine==1.6.1
    imbalanced-learn==0.11.0
    scikit-learn==1.3.1
    xgboost==1.7.6
    scipy==1.11.3 (can be removed from requirements before deployment)


### Using .slugignore for reducing slug size

## Deployment steps

### 1. Create a Heroku account

If you haven't already, sign up for a [Heroku](https://www.heroku.com) account.

### 2. Create a new app on Heroku

1. Log in to Heroku
2. Navigate to the [Heroku dashboard](https://dashboard.heroku.com/apps)
3. Click on the "New" button.
4. Select "Create new app."
5. Choose a name for your app.
6. Select a region.
7. Click the "Create app" button.

### 3. Add your GitHub repository to the Heroku app

1. At the Deploy tab, select GitHub as the deployment method.
2. Select your repository name and click Search. Once it is found, click Connect.
3. Select the branch you want to deploy, then click Deploy Branch.
4. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
5. If the slug size is too large then add large files not required for the app to the .slugignore file.
