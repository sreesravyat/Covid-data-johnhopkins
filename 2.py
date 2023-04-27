import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file into a pandas dataframe
df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv')

# filter the dataframe to include only the latest date for each country
latest_date = df['Date'].max()
df_latest = df[df['Date'] == latest_date]

# group the data by country and calculate the number of confirmed cases and deaths
grouped = df_latest.groupby('Country/Region')[['Confirmed', 'Deaths']].sum()

# calculate the observed case-fatality ratio for each country
grouped['CFR'] = grouped['Deaths'] / grouped['Confirmed'] * 100

# sort the data by CFR in descending order and select the top 20 countries
top20 = grouped.sort_values('CFR', ascending=False).head(20)

# create a bar plot of the CFR for the top 20 countries
plt.bar(top20.index, top20['CFR'])
plt.xticks(rotation=90)
plt.ylabel('Deaths per 100 Confirmed Cases')
plt.title('Observed Case-Fatality Ratio for the 20 Most Affected Countries')
plt.show()
