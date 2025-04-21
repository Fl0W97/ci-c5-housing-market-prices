# Deployment

## Heroku

* The [App live link](https://analyse-predict-house-market-5a00f7807683.herokuapp.com/)
* The project was deployed to Heroku using the following steps.

## Preparation

Make sure that the following files are created in the project environment before connect it with Heroku:

* setup.sh
    mkdir -p ~/.streamlit/
    echo "\
    [server]\n\
    headless = true\n\
    port = $PORT\n\
    enableCORS = false\n\
    \n\
    " > ~/.streamlit/config.toml """

* Procfile
    web: sh setup.sh && streamlit run app.py

* runtime.txt
    python-3.12.8

* requirements.txt
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
    yellowbrick==1.5 (can be removed from requirements before deployment)
    Pillow==10.0.1 (can be removed from requirements before deployment)

* Using .slugignore for reducing slug size

## Deployment steps

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Cloud IDE Reminders (???)

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In your Cloud IDE, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with *Regenerate API Key*.