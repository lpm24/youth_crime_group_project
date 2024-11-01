# Identifying Key Drivers of Youth Crime

## Problem Statement
The goal of this project is to understand the factors that influence crime rates across different regions and times.

## Research Question
This analysis aims to answer the following question:  
> "What socioeconomic, educational, and demographic factors are most strongly associated with variations in youth crime rates among young adults (ages 16 to 24) across U.S. states?"

## Table of Contents
1. [Identifying Key Drivers of Youth Crime](#identifying-key-drivers-of-youth-crime)
2. [Problem Statement](#problem-statement)
3. [Research Question](#research-question)
4. [Analysis](#analysis)
    - [Notebook 1: Data Cleaning and Preparation](code/01_EDA_and_Data_Cleaning.ipynb)
    - [Notebook 2: Model Benchmarks](code/02_Model_Benchmarks.ipynb)
    - [Notebook 3: Model Tuning](code/03_Model_Tuning.ipynb)
    - [Notebook 4: Production Model and Insights](code/04_Production_Model_and_Insights.ipynb)
5. [Executive Summary](#executive-summary)
    - [Introduction](#introduction)
    - [Data Collection](#data-collection)
    - [Data Dictionary](#data-dictionary)
    - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
    - [Model Performance and Evaluation](#model-performance-and-evaluation)
    - [Conclusion](#conclusion)
    - [Key Takeaways](#key-takeaways)
    - [Next Steps](#next-steps)
6. [Setup Instructions and Software Requirements](#setup-instructions-and-software-requirements)

### Introduction
Youth crime poses significant challenges to communities, affecting social cohesion, economic stability, and public safety. Understanding the underlying causes is essential for developing effective prevention and intervention strategies. Research indicates that factors such as poverty, unemployment, lack of education, and certain demographic characteristics can contribute to higher crime rates among young adults. By analyzing data over a decade, this project seeks to uncover patterns and correlations that can inform targeted approaches to mitigate youth crime.

### Data Collection
This project uses the following key datasets:

* **[`CPS March 2024 Documentation`](https://www2.census.gov/programs-surveys/cps/techdocs/cpsmar24.pdf)**: Provides labor force statistics, including median income, poverty rate, unemployment rate, high school graduation rate, and bachelor’s degree graduation rate.
* **[`FRED Economic Data Series`](https://fred.stlouisfed.org/)**: A comprehensive range of economic indicators, including employment and unemployment data, state-specific economic insights, and housing and construction metrics.
* **[`CDC WONDER MCD Expanded Data`](https://wonder.cdc.gov/wonder/help/mcd-expanded.html)**: Mortality and morbidity statistics, including crude rates for suicide and overdose per 100,000 population.
* **[`Kids Count Data Center`](https://datacenter.kidscount.org/)**: Youth-related metrics essential for understanding factors impacting young populations within communities.
* **[`Bureau of Justice Statistics (BJS)`](https://www.bjs.gov/)**: Supplies crime data critical for examining patterns in criminal activity and understanding community safety.

During data preparation, key cleaning steps included removing null values, handling missing data through imputation, and transforming certain variables (e.g., log-transforming crime rates) to reduce skewness. 
### Data Dictionary

| Feature                              | Type     | Dataset                        | Description                                                                                           |
|--------------------------------------|----------|--------------------------------|-------------------------------------------------------------------------------------------------------|
| **state**                            | *object* | Census/FRED Dataset            | The U.S. state where the data was collected.                                                          |
| **year**                             | *integer*| Census/FRED Dataset            | The year in which the data was recorded.                                                              |
| **median_income**                    | *integer*| CPS March 2024                 | Median income in the state in USD.                                                                    |
| **poverty_rate**                     | *float*  | CPS March 2024                 | Percentage of the population living below the poverty line.                                           |
| **unemployment_rate**                | *float*  | FRED/CPS Dataset               | Overall unemployment rate in the state.                                                               |
| **unemployed_15_weeks**              | *float*  | FRED Dataset                   | Percentage of the labor force unemployed for 15 weeks or more.                                        |
| **labor_force_participation_rate**   | *float*  | FRED Dataset                   | Labor force participation rate among the working-age population.                                      |
| **hs_grad_rate**                     | *float*  | CPS March 2024                 | High school graduation rate in the state.                                                             |
| **bachelors_grad_rate**              | *float*  | CPS March 2024                 | Bachelor's degree graduation rate in the state.                                                       |
| **zhvi**                             | *float*  | FRED Dataset                   | Zillow Home Value Index, representing the median home value.                                          |
| **crude_rate_suicide**               | *float*  | CDC WONDER MCD                 | Crude suicide rate per 100,000 population.                                                            |
| **crude_rate_od**                    | *float*  | CDC WONDER MCD                 | Crude overdose rate per 100,000 population.                                                           |
| **rate:__crimes_against_society**    | *float*  | BJS Dataset                    | Rate of crimes against society per 100,000 population.                                                |
| **rate:__fraud_and_other_financial_crimes** | *float* | BJS Dataset           | Rate of fraud and other financial crimes per 100,000 population.                                      |
| **rate:__property_crime**            | *float*  | BJS Dataset                    | Rate of property crimes per 100,000 population.                                                       |
| **rate:__violent_crime**             | *float*  | BJS Dataset                    | Rate of violent crimes per 100,000 population.                                                        |
| **youth_not_in_school**              | *float*  | Kids Count Data Center         | Number of youths (ages 16-19) not enrolled in school.                                                 |
| **youth_in_foster_care**             | *float*  | Kids Count Data Center         | Number of youths in foster care.                                                                      |
| **youth_living_in_poverty**          | *float*  | Kids Count Data Center         | Number of youths living below the poverty line.                                                       |
| **total_crime_count**                | *float*  | BJS Dataset                    | Aggregate count of all crime categories.                                                              |
| **total_crime_rate**                 | *float*  | BJS Dataset                    | Aggregate crime rate per 100,000 population.                                                          |

### Exploratory Data Analysis (EDA)


 Below are some of the visualizations generated during the EDA process.

#### Distribution of Total Crime Rate
The log-transformation was applied to the total crime rate to normalize its distribution. This transformation helps in visualizing and analyzing crime rates with less skewness.

![Distribution of Total Crime Rate](./img/distribution_log_transformed_total_crime_rate.jpg)

#### Trends of Different Types of Crime Over the Years
This visualization shows the trends of various types of crime over the years, allowing us to observe patterns or changes in crime rates across different categories over time.

![Trends of Different Types of Crime Over the Years](./img/trends_different_types_crime_over_years.jpg)


### Model Performance and Evaluation

We tested several regression models to analyze and predict target variables based on key features in our dataset. The goal was to compare the performance of each model using key metrics, including R² Score, Mean Squared Error (MSE), and Mean Absolute Error (MAE).

#### Models Evaluated:
1. **Linear Regression**
2. **Ridge Regression**
3. **Decision Tree**
4. **Random Forest**
5. **Gradient Descent**
6. **XGBoost**
7. **Support Vector Machine (SVM)**
8. **Stacking Model**
9. **Bagging XGBoost Model**

#### Summary of Model Performance

| **Model**                        | **R² Score (Train)** | **R² Score (Test)** | **Mean Squared Error (Train)** | **Mean Squared Error (Test)** | **Mean Absolute Error (Train)** | **Mean Absolute Error (Test)** |
|----------------------------------|----------------------|---------------------|--------------------------------|-------------------------------|---------------------------------|--------------------------------|
| **Linear Regression**            | 0.3001              | 0.3514             | 0.8777                         | 0.6599                        | 0.6902                          | 0.6135                          |
| **Decision Tree**                | 0.5698              | 0.2556             | 0.5220                         | 1.0520                        | 0.4906                          | 0.6988                          |
| **Grid Search Decision Tree**    | 0.1548              | 0.1824             | 1.0255                         | 1.1554                        | 0.7031                          | 0.7793                          |
| **Random Forest**                | 0.6915              | 0.3192             | 0.3743                         | 0.9621                        | 0.3930                          | 0.6991                          |
| **Grid Search Random Forest**    | 0.6702              | 0.3623             | 0.4002                         | 0.9012                        | 0.4164                          | 0.6908                          |
| **Gradient Boosting**            | 1.0000              | 0.5669             | 1.703e-15                      | 0.6121                        | 3.263e-08                       | 0.5273                          |
| **Grid Search Gradient Boosting**| 1.0000              | 0.3965             | 4.280e-06                      | 0.8528                        | 0.0018                          | 0.6218                          |
| **XGBoost**                      | 0.9873              | 0.4906             | 0.0154                         | 0.7199                        | 0.0881                          | 0.5682                          |
| **Grid Search XGBoost**          | 1.0000              | 0.5564             | 5.874e-07                      | 0.6269                        | 0.0005                          | 0.5392                          |
| **Grid Search SVM**              | 0.7450              | 0.2080             | 0.3095                         | 1.1192                        | 0.1541                          | 0.6434                          |
| **Stacking Model**               | 0.8967              | 0.5237             | 0.1253                         | 0.6732                        | 0.2341                          | 0.5671                          |
| **Bagging XGBoost Model**        | 0.8967              | 0.5237             | 0.1253                         | 0.6732                        | 0.2341                          | 0.5671                          |

The Gradient Boosting Model (without Grid Search) performed best, with a test R² score of 0.5669, explaining 56.69% of the variance. It also achieved a lower test MSE of 0.6121 and an MAE of 0.5273, indicating strong predictive accuracy overall.


### Conclusion
The Gradient Boosting Model provided the most accurate predictions for identifying the factors associated with youth crime rates. Key drivers such as lack of school enrollment, foster care status, housing value index, and labor force participation emerged as significant predictors. These insights suggest that socioeconomic and educational factors play a critical role in influencing youth crime rates across U.S. states, highlighting areas where policy intervention may be beneficial.

### Key Takeaways
- Educational Engagement: The feature importance analysis underscores the impact of school enrollment, with "youth_not_in_school" as the top predictor of youth crime rates.
- Support Systems: The strong influence of "youth_in_foster_care" suggests that targeted support for youths in foster care could be pivotal in crime prevention strategies.
- Economic Stability: Features like zhvi (Zillow Home Value Index) and labor_force_participation_rate highlight the role of economic factors in youth crime, indicating that job creation and housing affordability might indirectly reduce crime rates.
- Health and Well-being: Variables related to mental health and poverty (e.g., crude suicide rate, poverty rate) also emerged as important, suggesting that improving access to mental health services could be beneficial.
### Next Steps
- Data Expansion: Integrate additional demographic data or policy-related variables to capture broader influences on youth crime rates, including potential time-series analysis for temporal effects.
- Actionable Reporting: Develop focused reports for policymakers, emphasizing the significance of educational and economic stability, and recommending interventions that support youths in vulnerable conditions, such as foster care or poverty.
## Setup Instructions and Software Requirements

To run this project, clone the repository and install the required Python packages.

### Required Packages
The following packages are required for the analysis:

Pandas - For data manipulation and cleaning.<br>
NumPy - For numerical computations.<br>
Scikit-learn - For model building, evaluation, and preprocessing.<br>
Matplotlib & Seaborn - For data visualization and exploratory data analysis.<br>

