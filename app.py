import streamlit as st
import sys
import os

# Assuming 'src' folder is at the root level
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_house_market_study import page_house_market_study_body
from app_pages.page_hypothesis_and_validation import page_project_hypothesis_and_validation_body
from app_pages.page_sales_price_predictor import page_sales_price_predictor_body
from app_pages.page_pipeline_performance import page_pipeline_performance_body
from app_pages.page_sales_price_evaluation import page_sales_price_evaluation_body

app = MultiPage(app_name= "House Market Analysis (Project 5)") # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_project_summary_body)
app.add_page("House Market Study", page_house_market_study_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_and_validation_body)
app.add_page("Sales Price Predictor", page_sales_price_predictor_body)
app.add_page("ML: Pipeline Performance", page_pipeline_performance_body)
app.add_page("Sales Price Evaluator", page_sales_price_evaluation_body)

app.run() # Run the  app
