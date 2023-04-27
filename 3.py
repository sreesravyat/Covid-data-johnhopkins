import pandas as pd
import json

# read the CSV file into a pandas dataframe
df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv')

# filter the dataframe to include only the latest date for each country
latest_date = df['Date'].max()
df_latest = df[df['Date'] == latest_date]

# group the data by country and calculate the total number of confirmed cases
grouped = df_latest.groupby('Country/Region')[['Confirmed']].sum()

# read the population data from the JSON file
with open('worldpopulation.json') as f:
    pop_data = json.load(f)

# create a dictionary to map country names between different datasets
name_map = {
    'US': 'United States',
    'Czechia': 'Czech Republic',
    'S. Korea': 'South Korea',
    'Taiwan*': 'Taiwan',
    'Congo (Kinshasa)': 'Democratic Republic of the Congo',
    'Congo (Brazzaville)': 'Republic of the Congo',
    'Burma': 'Myanmar',
}

# compute the confirmed cases per capita for each country
per_capita = {}
for country, cases in grouped['Confirmed'].items():
    # check if the country name needs to be mapped
    if country in name_map:
        country = name_map[country]
    # find the population of the country
    pop = None
    for data in pop_data:
        if data['Country Name'] == country:
            pop = data['2019']
            break
    # skip countries with no population data
    if pop is None:
        continue
    # compute the confirmed cases per capita
    per_capita[country] = cases / pop * 100000

# sort the data by confirmed cases per capita in descending order and select the top 10 countries
top10 = pd.Series(per_capita).sort_values(ascending=False).head(10)

# print the top 10 countries with the highest number of confirmed COVID-19 cases per capita
print
