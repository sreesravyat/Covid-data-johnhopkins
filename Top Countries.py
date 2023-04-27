import pandas as pd
import matplotlib.pyplot as plt

# Download data from GitHub
url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv'
df = pd.read_csv(url)

# Merge data for countries with multiple regions
df = df.groupby(['Country/Region', 'Date']).sum().reset_index()

# Print total number of confirmed cases and deaths in each country in the last reported day
latest_date = df['Date'].max()
latest_data = df[df['Date'] == latest_date]
total_confirmed = latest_data.groupby('Country/Region')['Confirmed'].sum()
total_deaths = latest_data.groupby('Country/Region')['Deaths'].sum()
print('Total confirmed cases by country on {}:'.format(latest_date))
print(total_confirmed)
print('\nTotal deaths by country on {}:'.format(latest_date))
print(total_deaths)

# Top 10 countries with highest number of confirmed cases
top_confirmed = total_confirmed.sort_values(ascending=False)[:10]
print('\nTop 10 countries with highest number of confirmed cases:')
print(top_confirmed)

# Top 10 countries with highest number of deaths
top_deaths = total_deaths.sort_values(ascending=False)[:10]
print('\nTop 10 countries with highest number of deaths:')
print(top_deaths)

# Plot number of confirmed cases over time for each country
for country, data in df.groupby('Country/Region'):
    plt.plot(data['Date'], data['Confirmed'], label=country)
plt.title('Number of confirmed COVID-19 cases over time by country')
plt.xlabel('Date')
plt.ylabel('Confirmed cases')
plt.legend()
plt.show()

# Countries with exponential growth in the number of cases
exp_growth = {}
for country, data in df.groupby('Country/Region'):
    # Calculate the average daily growth rate for the last 7 days
    last_week = data.tail(7)
    avg_growth_rate = (last_week['Confirmed'].iloc[-1] / last_week['Confirmed'].iloc[0])**(1/7) - 1
    if avg_growth_rate > 0.1:
        exp_growth[country] = avg_growth_rate
print('\nCountries with exponential growth in the number of cases:')
print(exp_growth)

# Countries that are leaving exponential growth
non_exp_growth = {}
for country, data in df.groupby('Country/Region'):
    # Calculate the average daily growth rate for the last 7 days
    last_week = data.tail(7)
    avg_growth_rate = (last_week['Confirmed'].iloc[-1] / last_week['Confirmed'].iloc[0])**(1/7) - 1
    if avg_growth_rate < 0.05:
        non_exp_growth[country] = avg_growth_rate
print('\nCountries that are leaving exponential growth:')
print(non_exp_growth)
