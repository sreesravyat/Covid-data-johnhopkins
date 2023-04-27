import pandas as pd

# Load COVID-19 data
covid_data = pd.read_csv('time-series-19-covid-combined.csv')

# Load climate data
climate_data = pd.read_json('climate.json')

# Merge COVID-19 and climate data
merged_data = pd.merge(covid_data, climate_data, how='inner', left_on=['Country/Region', 'Date'], right_on=['country', 'date'])
