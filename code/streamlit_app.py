import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

# Load the dataset into a DataFrame (modify as per your actual dataset file path)
df = pd.read_csv('./data/data.csv')

# Define features excluding crime-related features
features = [
    'state', 'year', 'total_pop', 'white_pop', 'black_pop', 'hispanic_pop', 'asian_pop',
    'native_pop', 'islander_pop', 'multi_race_pop', 'median_income', 'poverty_rate',
    'unemployment_rate', 'unemployed_15_weeks', 'labor_force_participation_rate',
    'hs_grad_rate', 'bachelors_grad_rate', 'zhvi', 'crude_rate_suicide',
    'crude_rate_od', 'youth_not_in_school', 'youth_in_foster_care',
    'youth_living_in_poverty', 'youth_school_poverty_interaction'
]
target = 'log_total_crime_count'

X = df[features]
y = df[target]

# Preprocessing: Encode year, one-hot encode state, and standardize numeric features
preprocessor = ColumnTransformer(
    transformers=[
        ('onehot', OneHotEncoder(), ['state']),
        ('ordinal', OrdinalEncoder(), ['year']),
        ('num', StandardScaler(), [
            'total_pop', 'white_pop', 'black_pop', 'hispanic_pop', 'asian_pop', 'native_pop', 
            'islander_pop', 'multi_race_pop', 'median_income', 'poverty_rate', 
            'unemployment_rate', 'unemployed_15_weeks', 'labor_force_participation_rate', 
            'hs_grad_rate', 'bachelors_grad_rate', 'zhvi', 'crude_rate_suicide', 
            'crude_rate_od', 'youth_not_in_school', 'youth_in_foster_care', 
            'youth_living_in_poverty', 'youth_school_poverty_interaction'
        ])
    ]
)

# Create Linear Regression model
model = Pipeline([
    ('preprocessor', preprocessor),
    ('linear', LinearRegression())
])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Calculate R² scores
r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)

# Streamlit App
st.title("Crime Rate Prediction using Linear Regression")

# Data Overview
st.subheader("Dataset Overview")
st.write(df.head())

# Feature Selection
st.subheader("Feature Selection")
st.write("We have excluded crime-related features from the model to avoid data leakage.")

# Model Training
st.subheader("Model Training")
st.write("The model is trained using Linear Regression with the following features:")
st.write(features)

# R² Scores
st.subheader("Model Performance")
st.write(f"R² Score (Training): {r2_train:.2f}")
st.write(f"R² Score (Testing): {r2_test:.2f}")

# User Interaction - Predict New Data
st.subheader("Make Predictions")

# Inputs for Prediction
def get_user_input():
    state = st.selectbox('Select State', df['state'].unique())
    year = st.slider('Select Year', int(df['year'].min()), int(df['year'].max()), step=1)
    total_pop = st.number_input('Total Population', min_value=0, value=int(df['total_pop'].mean()))
    white_pop = st.number_input('White Population (%)', min_value=0.0, max_value=1.0, value=df['white_pop'].mean())
    black_pop = st.number_input('Black Population (%)', min_value=0.0, max_value=1.0, value=df['black_pop'].mean())
    hispanic_pop = st.number_input('Hispanic Population (%)', min_value=0.0, max_value=1.0, value=df['hispanic_pop'].mean())
    asian_pop = st.number_input('Asian Population (%)', min_value=0.0, max_value=1.0, value=df['asian_pop'].mean())
    native_pop = st.number_input('Native Population (%)', min_value=0.0, max_value=1.0, value=df['native_pop'].mean())
    islander_pop = st.number_input('Islander Population (%)', min_value=0.0, max_value=1.0, value=df['islander_pop'].mean())
    multi_race_pop = st.number_input('Multi-Race Population (%)', min_value=0.0, max_value=1.0, value=df['multi_race_pop'].mean())
    median_income = st.number_input('Median Income', min_value=0, value=int(df['median_income'].mean()))
    poverty_rate = st.number_input('Poverty Rate (%)', min_value=0.0, max_value=1.0, value=df['poverty_rate'].mean())
    unemployment_rate = st.number_input('Unemployment Rate (%)', min_value=0.0, max_value=1.0, value=df['unemployment_rate'].mean())
    unemployed_15_weeks = st.number_input('Unemployed 15 Weeks or Longer', min_value=0, value=int(df['unemployed_15_weeks'].mean()))
    labor_force_participation_rate = st.number_input('Labor Force Participation Rate (%)', min_value=0.0, max_value=1.0, value=df['labor_force_participation_rate'].mean())
    hs_grad_rate = st.number_input('High School Graduation Rate (%)', min_value=0.0, max_value=1.0, value=df['hs_grad_rate'].mean())
    bachelors_grad_rate = st.number_input('Bachelors Graduation Rate (%)', min_value=0.0, max_value=1.0, value=df['bachelors_grad_rate'].mean())
    zhvi = st.number_input('Zillow Home Value Index (ZHVI)', min_value=0, value=int(df['zhvi'].mean()))
    crude_rate_suicide = st.number_input('Crude Rate of Suicide', min_value=0, value=int(df['crude_rate_suicide'].mean()))
    crude_rate_od = st.number_input('Crude Rate of Overdose', min_value=0, value=int(df['crude_rate_od'].mean()))
    youth_not_in_school = st.number_input('Youth Not in School', min_value=0, value=int(df['youth_not_in_school'].mean()))
    youth_in_foster_care = st.number_input('Youth in Foster Care', min_value=0, value=int(df['youth_in_foster_care'].mean()))
    youth_living_in_poverty = st.number_input('Youth Living in Poverty', min_value=0, value=int(df['youth_living_in_poverty'].mean()))
    youth_school_poverty_interaction = st.number_input('Youth School Poverty Interaction', min_value=0, value=int(df['youth_school_poverty_interaction'].mean()))

    data = {
        'state': [state], 'year': [year], 'total_pop': [total_pop], 'white_pop': [white_pop], 'black_pop': [black_pop],
        'hispanic_pop': [hispanic_pop], 'asian_pop': [asian_pop], 'native_pop': [native_pop],
        'islander_pop': [islander_pop], 'multi_race_pop': [multi_race_pop], 'median_income': [median_income],
        'poverty_rate': [poverty_rate], 'unemployment_rate': [unemployment_rate], 'unemployed_15_weeks': [unemployed_15_weeks],
        'labor_force_participation_rate': [labor_force_participation_rate], 'hs_grad_rate': [hs_grad_rate],
        'bachelors_grad_rate': [bachelors_grad_rate], 'zhvi': [zhvi], 'crude_rate_suicide': [crude_rate_suicide],
        'crude_rate_od': [crude_rate_od], 'youth_not_in_school': [youth_not_in_school],
        'youth_in_foster_care': [youth_in_foster_care], 'youth_living_in_poverty': [youth_living_in_poverty],
        'youth_school_poverty_interaction': [youth_school_poverty_interaction]
    }
    return pd.DataFrame(data)

# Get user input data for prediction
user_input = get_user_input()

# Make prediction using the trained model
user_prediction = model.predict(user_input)

# Display prediction
st.write("Predicted Log Total Crime Count:", user_prediction[0])
