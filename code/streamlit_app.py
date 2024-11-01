import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load the trained model
with open('linear_regression_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit App
st.title("Crime Rate Predictor")

# Display Data Dictionary
st.subheader("Data Dictionary")
data_dictionary = {
    'state': 'The state for which the data is provided',
    'year': 'The year of the data record',
    'total_pop': 'Total population of the state',
    'median_income': 'Median income of the population',
    'poverty_rate': 'Percentage of the population living in poverty',
    'unemployment_rate': 'Unemployment rate in the state',
    'unemployed_15_weeks': 'Number of people unemployed for 15 weeks or longer',
    'labor_force_participation_rate': 'Labor force participation rate (%)',
    'hs_grad_rate': 'High school graduation rate (%)',
    'bachelors_grad_rate': 'Bachelors degree graduation rate (%)',
    'zhvi': 'Zillow Home Value Index (ZHVI)',
    'crude_rate_suicide': 'Crude rate of suicide per 100,000 population',
    'crude_rate_od': 'Crude rate of overdose per 100,000 population',
    'youth_not_in_school': 'Number of youth not in school',
    'youth_in_foster_care': 'Number of youth in foster care',
    'youth_living_in_poverty': 'Number of youth living in poverty',
    'youth_school_poverty_interaction': 'Interaction term representing youth not in school and poverty levels'
}
st.write(pd.DataFrame(list(data_dictionary.items()), columns=['Feature', 'Description']))

# Display Dataset
st.subheader("Dataset Overview")
dataset = pd.read_csv('../data/data.csv')
st.dataframe(dataset)

# Input Form for Prediction
st.sidebar.header("User Input")

def user_input_features():
    state = st.sidebar.selectbox('Select State', ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'])
    total_pop = st.sidebar.number_input('Total Population', min_value=0, value=5000000)
    median_income = st.sidebar.number_input('Median Income', min_value=0, value=60000)
    poverty_rate = st.sidebar.number_input('Poverty Rate (%)', min_value=0.0, max_value=1.0, value=0.15)
    unemployment_rate = st.sidebar.number_input('Unemployment Rate (%)', min_value=0.0, max_value=1.0, value=0.05)
    unemployed_15_weeks = st.sidebar.number_input('Unemployed 15 Weeks or Longer', min_value=0, value=1000)
    labor_force_participation_rate = st.sidebar.number_input('Labor Force Participation Rate (%)', min_value=0.0, max_value=1.0, value=0.65)
    hs_grad_rate = st.sidebar.number_input('High School Graduation Rate (%)', min_value=0.0, max_value=1.0, value=0.85)
    bachelors_grad_rate = st.sidebar.number_input('Bachelors Graduation Rate (%)', min_value=0.0, max_value=1.0, value=0.30)
    zhvi = st.sidebar.number_input('Zillow Home Value Index (ZHVI)', min_value=0, value=250000)
    crude_rate_suicide = st.sidebar.number_input('Crude Rate of Suicide', min_value=0, value=10)
    crude_rate_od = st.sidebar.number_input('Crude Rate of Overdose', min_value=0, value=15)
    youth_not_in_school = st.sidebar.number_input('Youth Not in School', min_value=0, value=10000)
    youth_in_foster_care = st.sidebar.number_input('Youth in Foster Care', min_value=0, value=500)
    youth_living_in_poverty = st.sidebar.number_input('Youth Living in Poverty', min_value=0, value=20000)
    youth_school_poverty_interaction = st.sidebar.number_input('Youth School Poverty Interaction', min_value=0, value=3000000)

    data = {
        'state': [str(state)], 'year': [2022], 'total_pop': [total_pop], 'median_income': [median_income],
        'poverty_rate': [poverty_rate], 'unemployment_rate': [unemployment_rate], 'unemployed_15_weeks': [unemployed_15_weeks],
        'labor_force_participation_rate': [labor_force_participation_rate], 'hs_grad_rate': [hs_grad_rate],
        'bachelors_grad_rate': [bachelors_grad_rate], 'zhvi': [zhvi], 'crude_rate_suicide': [crude_rate_suicide],
        'crude_rate_od': [crude_rate_od], 'youth_not_in_school': [youth_not_in_school],
        'youth_in_foster_care': [youth_in_foster_care], 'youth_living_in_poverty': [youth_living_in_poverty],
        'youth_school_poverty_interaction': [youth_school_poverty_interaction]
    }
    return pd.DataFrame(data)

# Get user input
input_df = user_input_features()

# Make prediction
prediction = model.predict(input_df)

# Display prediction
st.subheader("Prediction")
st.write(f"Predicted Log Total Crime Rate: {prediction[0]:.2f}")

# Calculate total crime count from the log prediction
total_crime_count = 10 ** prediction[0]
st.write(f"Predicted Total Crime Count: {total_crime_count:.0f}")